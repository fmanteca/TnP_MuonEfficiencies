import ROOT
from Efficiency import Efficiency
import os
import sys


class CheckFit:
    '''Check the quality of the fit for each bin. Return integer (0 = good, 1 = to be checked, 2 = bad) and plot depending on the method'''

    def __init__(self):
        pass

    def CheckFitDummy(self, eff):
        '''eff is a Efficiency, and contains all failing and passing probes distribution, as well as the fit function. Check PlotFit in HistoPloter.py for comparison'''
        #Creat folder that will contain info about quality of fits
        directory = self.CreateOutputFolder(self.FormatOutputPath('%s/%s/%s'%('Plots/QualityofFits',eff.type_,eff.name)))

        nbin = 0 
        nbinQual = []#List containing integer concerning quality of fit (0 = good, 1 = to be checked, 2 = bad)
        for hp, fp, hf, ff in zip(eff.hpassing, eff.funcpassing, eff.hfailing, eff.funcfailing):
            nbin += 1
            #this function is dummy. All the fits are considered as good by default
            nbinQual.append(0)

        #Output txt file that containing the efficiency and the corresponding quality of fit for all bin. Gives a quick overview to the user about the status of the fits
        output_file
