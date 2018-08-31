#Make all the plots
#

import ROOT
from myutils.HistoReader import HistoReader
from myutils.HistoPloter import HistoPloter
from myutils.Efficiency import Efficiency
from myutils.JsonMaker import JsonMaker
from  multiprocessing import Process
import sys as sys_
import time
#import sys as SYS

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":


    path_in = []
    #################
    #Path where the main SF root files are stored (using the full statistics)
    path_in.append('/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/')
    #%s_%s/%s_%sid%s/%s'%(n,r,t.upper(),t,r,s)

    ##################
    #Main path where all the root files are stored
    #path_in.append('/afs/cern.ch/user/f/fernanpe/public/for_Gael/Systematics_2017')
    path_in.append('/afs/cern.ch/user/s/sfonseca/public/for_Gael/varied')

    
    #List of all the systematic variations 
    #sysList = ['main']
    sysList = ['nominal', 'mass_up', 'mass_down', 'nbins_up', 'nbins_down', 'pdf']
    sysDic = {
            'nominal':'nominal',
            'mass_up':'MassRange/EfficiencyRun2017B_F_massRange_2p85_3p35',
            'mass_down':'MassRange/EfficiencyRun2017B_F_massRange_2p95_3p25',
            'nbins_up':'MassBin/EfficiencyRun2017B_F_binfit45',
            'nbins_down':'MassBin/EfficiencyRun2017B_F_binfit35',
            'pdf':'PDF/EfficiencyRun2017B_F_PDF_Gauss'
            
            }

    #

    #ID = ['TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root']

    ID = [  
            ##'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_eta.root',
            ##'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_vtx.root',
            ##'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt.root',
            'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root',
            ##'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_eta.root',
            ##'TnP_MC_NUM_TightID_DEN_genTracks_PAR_eta.root',
            #'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root',
            ##'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt.root',
            ##'TnP_MC_NUM_TightID_DEN_genTracks_PAR_vtx.root',
            ##'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_vtx.root',
            ##'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_eta.root',
            ##'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt.root',
            #'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root',
            #'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root',
            ##'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_vtx.root',
            ##'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt.root',
            ]

    Run = ['BCDEF']
    Type = ['mc', 'data']
    Num = ['ID']

    NumDic = {'ID':ID}
    LumiDic = {'BC':14.432, 'DE':13.503, 'F':13.433}

    def makePlots(n, r, s, t):
        hrList = [] 
        for sys in sysList:
        #All the rest will be within the json file
            print t
            path = ''
            if sys == 'nominal':
                path = path_in[0]
            else: path = path_in[1]
                
            if not sys == 'nominal':
                #file_ = '%s/Efficiency%s_%s_%s/%s_%sid%s_%s/%s'%(path_in[1],n,r,sys,t.upper(),t,r,sys,s)
                file_ = '%s/%s/%s_%s_all/%s'%(path,sysDic[sys],t.upper(),t,s)
            else: 
                #file_ = '%s/Efficiency%s_%s/%s_%sid%s/%s'%(path_in[0],n,r,t.upper(),t,r,s)
                file_ = '%s/EfficiencyRun2017B_F/%s_%s_all/%s'%(path,t.upper(),t,s)
            print 'file_ is', file_
            #sys_.exit()
            hr = HistoReader('RUN%s_%s%s%s'%(r,n,t,sys))
            hr.readfile(file_)     
            #hr.SetNewRange(20, 120) 
            hr.setInfo(sys)         
            hr.CleanBigError(0.01)  
            hr.setType(t)      
            hrList.append(hr)
        
        hp = HistoPloter('.')
        ##Uncomment next line to have only min, max variations
        hp.MinMax = True
        hp.setRatioRange(0.98, 1.02)#Set the ratio range. Default one is 0.85, 1.15
        print 'hrList is', hrList
        #print 'I WILL MAKE THE PLOTS'
        #hp.PlotEff1D(hrList)#making the 1D plot


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
