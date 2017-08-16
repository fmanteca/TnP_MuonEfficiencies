#!/usr/bin/env python
import sys
import os
import re
from ROOT import TFile, TIter, TKey, TH2F
import json
import pickle


# ----------------------------------------------------------------------------------------------
#
# -------------------------  DOCUMENTATION  ----------------------------------------------------
#
# ----------------------------------------------------------------------------------------------
#
#
# UPDATED 170721 by Pedro Fernandez Manteca: both 1D and 2D input histograms
# From now on it gets the efficiencies json, not only the SF json
#
#
# Usage: choose if you want to obtain efficiencies json or SF json
# (or both of them) by setting GetEffJSON / GetSFJSON to 1
#
# The output json format and keys are fixed following the 
# Dmytro Kovalskyi recommendation on CMSMUONS-5 jira tickect (170720)
#
#
#
# Note: Following Dima's recomendation, we would like to have one mother folder (for example TightID)
# and three subfolders inside the mother depending on the chosen kind of varible bins (pt, eta, vtx...).
# Make sure that when running extractPlotsAndComputeTheSFs.C you put the same name (first function parameter)
# for all the ID kind of variable bins.
#
# For example: TightID
#
# root -b -q -l 'extractPlotsAndComputeTheSFs.C("TightID","EfficiencyID/DATA_dataid/TnP_MC_NUM_TightID_DEN_genTracks_PAR_eta.root","EfficiencyID/MC_mcid/TnP_MC_NUM_TightID_DEN_genTracks_PAR_eta.root")'
#
# root -b -q -l 'extractPlotsAndComputeTheSFs.C("TightID","EfficiencyID/DATA_dataid/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt.root","EfficiencyID/MC_mcid/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt.root")'
#
# root -b -q -l 'extractPlotsAndComputeTheSFs.C("TightID","EfficiencyID/DATA_dataid/TnP_MC_NUM_TightID_DEN_genTracks_PAR_vtx.root","EfficiencyID/MC_mcid/TnP_MC_NUM_TightID_DEN_genTracks_PAR_vtx.root")'
#
# 
#
#------------------------------------------------------------------------------------------------


GetEffJSON_DATA = 1
GetEffJSON_MC = 0
GetSFJSON = 0

DEBUG = 0

#-------------------------------------------------------------------------------------


args = sys.argv[1:]
if len(args) > 0: inputTree = args[0]
print "input tree=", inputTree

if len(args) > 1: outputJson = args[1]
print "output json=", outputJson

#from array import *
#import math
#import pickle


def getValueError(value, error):
    binEntry={}
    binEntry["value"]=value
    binEntry["error"]=error
    return binEntry

def getHistoContentInJson(histo):
    xBins={}
    histoName=histo.GetName()
    null = None
    xaxisName = ""
    yaxisName = re.split("_",histoName)[1]
    if (histo.GetYaxis().GetNbins()==1):
        if DEBUG == 1: print "this is a 1D histo"
        for i in range(1,histo.GetXaxis().GetNbins()+1):
            xBinValue=str(histo.GetXaxis().GetBinLowEdge(i))+","+str(histo.GetXaxis().GetBinUpEdge(i))
            xBins[xBinValue]=getValueError(histo.GetBinContent(i), histo.GetBinError(i))
        if "pt" in histoName:
            if histo.GetBinLowEdge(1)!=2.0:
                xBinValue=str(2.0)+","+str(2.5)
                xBins[xBinValue]=getValueError(null,null)
            if histo.GetBinLowEdge(2)!=2.5:
                xBinValue=str(2.5)+","+str(2.75)
                xBins[xBinValue]=getValueError(null, null)
            if histo.GetBinLowEdge(3)!=2.75:
                xBinValue=str(2.75)+","+str(3.0)
                xBins[xBinValue]=getValueError(null, null)
            if histo.GetBinLowEdge(24)!=700:
                xBinValue=str(700)+","+str(1200)
                xBins[xBinValue]=getValueError(null, null)
            if histo.GetBinLowEdge(23)!=500:
                xBinValue=str(500)+","+str(700)
                xBins[xBinValue]=getValueError(null, null)

    else :
        for i in range(1,histo.GetXaxis().GetNbins()+1):
            yBins={}
            xBinValue=str(histo.GetXaxis().GetBinLowEdge(i))+","+str(histo.GetXaxis().GetBinUpEdge(i))
            for j in range(1,histo.GetYaxis().GetNbins()+1):
                yBinValue=str(histo.GetYaxis().GetBinLowEdge(j))+","+str(histo.GetYaxis().GetBinUpEdge(j))
                yBins[yBinValue]=getValueError(histo.GetBinContent(i,j), histo.GetBinError(i,j))
            if "pt" in histoName or "histo2D" in histoName:
                if histo.GetYaxis().GetBinLowEdge(1)!=2.0:
                    yBinValue=str(2.0)+","+str(2.5)
                    yBins[yBinValue]=getValueError(null, null)
                if histo.GetYaxis().GetBinLowEdge(2)!=2.5:
                    yBinValue=str(2.5)+","+str(2.75)
                    yBins[yBinValue]=getValueError(null, null)
                if histo.GetYaxis().GetBinLowEdge(3)!=2.75:
                    yBinValue=str(2.75)+","+str(3.0)
                    yBins[yBinValue]=getValueError(null, null)
                if histo.GetYaxis().GetBinLowEdge(24)!=700:
                    yBinValue=str(700)+","+str(1200)
                    yBins[yBinValue]=getValueError(null, null)
                if histo.GetYaxis().GetBinLowEdge(23)!=500:
                    yBinValue=str(500)+","+str(700)
                    yBins[yBinValue]=getValueError(null, null)

            xBins[xBinValue]=yBins

        #fixed for Gael's common format

    return xBins

data={}

rootoutput = TFile.Open(inputTree)

nextkey = TIter(rootoutput.GetListOfKeys())
key = nextkey.Next()
while (key): #loop
    if key.IsFolder() != 1:
        continue
    if DEBUG == 1: print "debug key ", key.GetTitle()
    directory = rootoutput.GetDirectory(key.GetTitle())
    keyInDir = TIter(directory.GetListOfKeys())
    subkey = keyInDir.Next()

    efficienciesForThisID = {}
    while (subkey):
        if "efficiencies" in subkey.GetName() and GetEffJSON_DATA == 1 and "DATA" in subkey.GetName():
            directory2 = rootoutput.GetDirectory(key.GetTitle()+"/"+subkey.GetName())
            keyInDir2 = TIter(directory2.GetListOfKeys())
            subsubkey = keyInDir2.Next()

            while (subsubkey):
                if "histo"  in subsubkey.GetName() or "abseta_pt_DATA" in subsubkey.GetName():
                    theHistoPlot = rootoutput.Get(key.GetTitle()+"/"+subkey.GetTitle()+"/"+subsubkey.GetName())
                    if "histo_pt_DATA" in subsubkey.GetName():
                        efficienciesForThisID["Pt"] = getHistoContentInJson(theHistoPlot)
                    if "histo_eta_DATA" in subsubkey.GetName():
                        efficienciesForThisID["Eta"] = getHistoContentInJson(theHistoPlot)
                    if "histo_tag_nVertices" in subsubkey.GetName():
                        efficienciesForThisID["Vtx"] = getHistoContentInJson(theHistoPlot)
                    if "abseta_pt" in subsubkey.GetName():
                        efficienciesForThisID["Pt_Eta"] = getHistoContentInJson(theHistoPlot)

                if DEBUG == 1: print "debug subsubkey ", subsubkey.GetTitle()
                subsubkey = keyInDir2.Next()


        if "efficiencies" in subkey.GetName() and GetEffJSON_MC == 1 and "MC" in subkey.GetName():
            directory2 = rootoutput.GetDirectory(key.GetTitle()+"/"+subkey.GetName())
            keyInDir2 = TIter(directory2.GetListOfKeys())
            subsubkey = keyInDir2.Next()

            while (subsubkey):
                if "histo" in subsubkey.GetName() or "abseta_pt_MC" in subsubkey.GetName():
                    theHistoPlot = rootoutput.Get(key.GetTitle()+"/"+subkey.GetTitle()+"/"+subsubkey.GetName())
                    if "histo_pt_MC" or "histo_ne_MC" in subsubkey.GetName():
                        efficienciesForThisID["Pt"] = getHistoContentInJson(theHistoPlot)
                    if "histo_eta_MC" in subsubkey.GetName():
                        efficienciesForThisID["Eta"] = getHistoContentInJson(theHistoPlot)
                    if "histo_tag_nVertices" in subsubkey.GetName():
                        efficienciesForThisID["Vtx"] = getHistoContentInJson(theHistoPlot)
                    if "abseta_pt" in subsubkey.GetName():
                        efficienciesForThisID["Pt_Eta"] = getHistoContentInJson(theHistoPlot)

                if DEBUG == 1: print "debug subsubkey ", subsubkey.GetTitle()
                subsubkey = keyInDir2.Next()

        if "ratio" in subkey.GetName() and GetSFJSON == 1:

            theHistoPlot = rootoutput.Get(key.GetTitle()+"/"+subkey.GetName())
            if  subkey.GetName()=='pt_ratio':
                efficienciesForThisID["Pt"] = getHistoContentInJson(theHistoPlot)
            if  subkey.GetName()=='eta_ratio':
                efficienciesForThisID["Eta"] = getHistoContentInJson(theHistoPlot)
            if "tag_nVertices" in subkey.GetName():
                efficienciesForThisID["Vtx"] = getHistoContentInJson(theHistoPlot)
            if  subkey.GetName()=='abseta_pt_ratio':
                efficienciesForThisID["Pt_Eta"] = getHistoContentInJson(theHistoPlot)
        if DEBUG == 1: print "debug subkey ", subkey.GetTitle()
        subkey = keyInDir.Next()
    data[key.GetTitle()]=efficienciesForThisID
    key = nextkey.Next()


with open(outputJson,"w") as f:
    json.dump(data, f, sort_keys = False, indent = 4)

outputPickle = outputJson.replace('json', 'pkl')

with open(outputPickle,"w") as f:
    pickle.dump(data, f)


