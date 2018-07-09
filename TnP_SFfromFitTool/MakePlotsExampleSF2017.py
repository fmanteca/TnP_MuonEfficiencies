#Make all the plots
#

import ROOT
from myutils.HistoReader import HistoReader
from myutils.HistoPloter import HistoPloter
from myutils.Efficiency import Efficiency
from myutils.JsonMaker import JsonMaker
import sys

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":


    ##################


    ID = [  
            'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_HighPtID_DEN_genTracks_PAR_newpt_eta.root',
            'TnP_MC_NUM_TrkHighPtID_DEN_genTracks_PAR_newpt_eta.root',
            'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_MediumPromptID_DEN_genTracks_PAR_pt_eta.root'
            ]

    ISO = [ 
    #        'TnP_MC_NUM_TightRelIso_DEN_MediumID_PAR_pt_eta.root',
    #        'TnP_MC_NUM_LooseRelIso_DEN_MediumID_PAR_pt_eta.root',
    #        'TnP_MC_NUM_TightRelIso_DEN_TightIDandIPCut_PAR_pt_eta.root',
    #        'TnP_MC_NUM_LooseRelIso_DEN_LooseID_PAR_pt_eta.root',
    #        'TnP_MC_NUM_TightRelTkIso_DEN_TrkHighPtID_PAR_newpt_eta.root',
    #        'TnP_MC_NUM_LooseRelTkIso_DEN_TrkHighPtID_PAR_newpt_eta.root',
    #        'TnP_MC_NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_PAR_newpt_eta.root',
    #        'TnP_MC_NUM_LooseRelIso_DEN_TightIDandIPCut_PAR_pt_eta.root',
    #        'TnP_MC_NUM_TightRelTkIso_DEN_HighPtIDandIPCut_PAR_newpt_eta.root'
    ]

    Run = ['BC', 'DE', 'F']
    Type = ['mc', 'data']
    #Num = ['ISO', 'ID']
    Num = ['ID']
    #Num = ['ISO']

    #NumDic = {'ISO':ISO, 'ID':ID}
    NumDic = {'ID':ID}
    #NumDic = {'ISO':ISO}
    LumiDic = {'BC':14.432, 'DE':13.503, 'F':13.433}


    ##########
    ##Provide Plots for run BC, DE and F
    ##########
    #for n in Num:
    #    for r in Run: 
    #        for s in NumDic[n]:
    #            #All the rest will be within the json file
    #            DATA_hr = None
    #            MC_hr = None
    #            for t in Type:
    #                file_ = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/Efficiency%s_%s/%s_%sid%s/%s'%(n,r,t.upper(),t,r,s)
    #                hr = HistoReader('%s%s'%(t,r))
    #                hr.readfile(file_)     
    #                hr.SetNewRange(20, 120) 
    #                hr.setInfo(r)         
    #                hr.CleanBigError(0.01)  
    #                hr.setType(t)      
    #                #For SF
    #                if t == 'mc':
    #                    MC_hr = hr
    #                elif t == 'data':
    #                    DATA_hr = hr

    #            hp = HistoPloter('.')
    #            #print 'going to plot'
    #            hp.PlotEff1D([DATA_hr, MC_hr])
    #            #print 's is', s

    #########
    #Provide Plots separetly for run BCDEF
    #########
    for n in Num:
        for s in NumDic[n]:
            DATA_hrList = []
            MC_hrList = []
            for r in Run: 
                #All the rest will be within the json file
                for t in Type:
                    file_ = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/Efficiency%s_%s/%s_%sid%s/%s'%(n,r,t.upper(),t,r,s)
                    hr = HistoReader('%s%s'%(t,r))
                    hr.readfile(file_)     
                    hr.SetNewRange(20, 120) 
                    hr.setInfo(r)         
                    hr.CleanBigError(0.01)  
                    hr.setLumi(LumiDic[r])
                    hr.setType(t)      
                    #For SF
                    if t == 'mc':
                        MC_hrList.append(hr)
                    elif t == 'data':
                        DATA_hrList.append(hr)

            DATA_hr = DATA_hrList[0]
            MC_hr = MC_hrList[0]
            for d in DATA_hrList[1:]:
                DATA_hr.Sum(d)

            for d in MC_hrList[1:]:
                MC_hr.Sum(d)

            hp = HistoPloter('.')
            hp.PlotEff1D([DATA_hr, MC_hr])

#    #########
#    #Will contain hr for run BC, DE and F to compute SF on BCDEF
#    #########
#    for n in Num:
#        #Used for SF
#        SF_MapList = []
#        MC_MapList = []
#        DATA_MapList = []
#        SFoutputJSONname ='RunBCDEF_%s_%s'%('SF',n)
#        jSF = JsonMaker(SFoutputJSONname)
#        for t in Type:
#            #All the rest will be within the json file
#            outputJSONname ='RunBCDEF_%s_%s'%(t,n)
#            j = JsonMaker(outputJSONname)
#            MapList = []
#            for s in NumDic[n]:
#                #Contains hr from Run BC, DE and F that will be summed up at the end
#                hrList = []
#                for r in Run: 
#                    file_ = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/Efficiency%s_%s/%s_%sid%s/%s'%(n,r,t.upper(),t,r,s)
#                    hr = HistoReader('hr')
#                    hr.readfile(file_)     
#                    hr.SetNewRange(20, 120) 
#                    hr.setLumi(LumiDic[r])
#                    hr.CleanBigError(0.05)  
#                    hr.setInfo('dummy')         
#                    hr.setType(t)      
#                    hrList.append(hr)
#
#                #lumi sum of all the hr
#                hr0 = hrList[0]
#                for hr in hrList[1:]:
#                    hr0.Sum(hr)
#
#                MapList.append(hr0.eff2D)
#
#                #For SF
#                if t == 'mc':
#                    MC_MapList.append(hr0.eff2D)
#                elif t == 'data':
#                    DATA_MapList.append(hr0.eff2D)
#            #For DATA, MC
#            j.makeJSON(MapList)
#
#        #For SF
#        for mcm, datam in zip(MC_MapList,DATA_MapList):
#            SF_MapList.append(datam.divideMap(mcm))
#
#        jSF.makeJSON(SF_MapList)
