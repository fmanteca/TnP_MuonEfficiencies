#Make all the plots
#

import ROOT
from myutils.HistoReader import HistoReader
from myutils.HistoPloter import HistoPloter
from myutils.Efficiency import Efficiency
from myutils.JsonMaker import JsonMaker
from  multiprocessing import Process
import time
#import sys as SYS

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":


    path_in = []
    #################
    #Path where the main SF root files are stored (using the full statistics)
    path_in.append('/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017')
    #%s_%s/%s_%sid%s/%s'%(n,r,t.upper(),t,r,s)

    ##################
    #Main path where all the root files are stored
    #path_in.append('/afs/cern.ch/user/f/fernanpe/public/for_Gael/Systematics_2017')
    path_in.append('/afs/cern.ch/user/f/fernanpe/public/for_Gael/Systematics_2017_Full')


    
    #List of all the systematic variations 
    #sysList = ['main']
    sysList = ['nominal', 'mass_up', 'mass_down', 'tag_up', 'tag_down', 'signalvar', 'nbins_up', 'nbins_down']

    #

    #ID = ['TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root']

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
            'TnP_MC_NUM_TightRelIso_DEN_MediumID_PAR_pt_eta.root',
            'TnP_MC_NUM_LooseRelIso_DEN_MediumID_PAR_pt_eta.root',
            'TnP_MC_NUM_TightRelIso_DEN_TightIDandIPCut_PAR_pt_eta.root',
            'TnP_MC_NUM_LooseRelIso_DEN_LooseID_PAR_pt_eta.root',
            'TnP_MC_NUM_TightRelTkIso_DEN_TrkHighPtID_PAR_newpt_eta.root',
            'TnP_MC_NUM_LooseRelTkIso_DEN_TrkHighPtID_PAR_newpt_eta.root',
            'TnP_MC_NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_PAR_newpt_eta.root',
            'TnP_MC_NUM_LooseRelIso_DEN_TightIDandIPCut_PAR_pt_eta.root',
            'TnP_MC_NUM_TightRelTkIso_DEN_HighPtIDandIPCut_PAR_newpt_eta.root'
    ]


    Run = ['BC', 'DE', 'F']
    #Run = ['DE']
    #Run = ['BC']
    Type = ['mc', 'data']
    #Type = ['mc']
    Num = ['ID', 'ISO']
    #Num = ['ID']

    NumDic = {'ISO':ISO, 'ID':ID}
    LumiDic = {'BC':14.432, 'DE':13.503, 'F':13.433}

    def makePlots(n, r, s, t):
        hrList = [] 
        for sys in sysList:
        #All the rest will be within the json file
            print t
            if sys != 'nominal':
                file_ = '%s/Efficiency%s_%s_%s/%s_%sid%s_%s/%s'%(path_in[1],n,r,sys,t.upper(),t,r,sys,s)
            else: 
                file_ = '%s/Efficiency%s_%s/%s_%sid%s/%s'%(path_in[0],n,r,t.upper(),t,r,s)
            print 'file_ is', file_
            hr = HistoReader('RUN%s_%s%s%s'%(r,n,t,sys))
            hr.readfile(file_)     
            hr.SetNewRange(20, 120) 
            hr.setInfo(sys)         
            hr.CleanBigError(0.01)  
            hr.setType(t)      
            hrList.append(hr)
        
        hp = HistoPloter('.')
        ##Uncomment next line to have only min, max variations
        hp.MinMax = True
        hp.setRatioRange(0.98, 1.02)#Set the ratio range. Default one is 0.85, 1.15
        hp.PlotEff1D(hrList)#making the 1D plot


    #########
    #Provide Plots for run BC, DE and F
    #########
    jobs = []
    for n in Num:
        for r in Run: 
            for s in NumDic[n]:
                for t in Type:
                    #print 'Will wait 5 sec to avoid crashes'
                    #time.sleep(5)
                    p = Process(target=makePlots, args=(n,r,s,t,))
                    jobs.append(p)
                    p.start()
