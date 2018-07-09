#Make all the plots
#

import ROOT
from myutils.HistoReader import HistoReader
from myutils.HistoPloter import HistoPloter
from myutils.Efficiency import Efficiency
from myutils.JsonMaker import JsonMaker
from  multiprocessing import Process
import time
import sys
#import sys as SYS

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":

    #####################
    #Some function you need
    #####################


    def Gethr(lumi, run, file, name, info):
        ''' retrieve historeader for a single efficiency'''
        hr = HistoReader(name)
        hr.setInfo(info)         
        hr.readfile(file)
        hr.setLumi(lumi)
        hr.setType(info)
        return hr

    def GetSumLumihr(lumiDic, runList, file, name, info):
        ''' retrieve historeader in case separated for multiple runs'''
        hr = HistoReader(name)
        for run in runList:
            file = file.replace('RUN', run)
            if run == runList[0]:
                hr = Gethr(lumiDic[run], run, file, name, info)
            else:
                hr_run = Gethr(lumiDic[run], run, file, name, info)
                hr.Sum(hr_run)

        return hr

    #######################
    ##Compare the efficiency
    #######################


    #############To make efficiency comparison
    ##This is a list of historeader. All the historeader in this list will be ploted simultaneously
    #hrList = []

    ##Histogram from DY
    #runList = ['BC', 'DE', 'F']
    #lumiDic = {'BC':14.432, 'DE':13.503, 'F':13.433}
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    ###MC
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    #name = 'DY'

    #hr = GetSumLumihr(lumiDic, runList, file, name, 'DY')
    #hr.SetNewRange(20, 40) 
    #hrList.append(hr)


    ##file for loose J/Psi: 
    ###DATA
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    ###MC
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    ##file = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    #hr = Gethr( '1', 'BCDEF', file, 'JPsi', 'Jpsi')
    #hrList.append(hr)
    #
    #hp = HistoPloter('.')
    #hp.PlotEff1D(hrList)#making the 1D plot


    ######################
    #Compare the SF 
    ######################

    #Histogram from DY
    runList = ['BC', 'DE', 'F']
    lumiDic = {'BC':14.432, 'DE':13.503, 'F':13.433}

    #Loose
    #file_data = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    #Tight
    file_data = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    #Medium
    #file_data = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    #Soft
    #file_data = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/DATA_dataidRUN/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    name = 'DY'
    hr_data = GetSumLumihr(lumiDic, runList, file_data, name, name)
    hr_data.SetNewRange(20, 40) 

    #Loose
    #file_mc = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    #Tight
    file_mc = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    #Medium
    #file_mc = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    #Soft
    #file_mc = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_RUN/MC_mcidRUN/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    hr_mc = GetSumLumihr(lumiDic, runList, file_mc, name, name)
    hr_mc.SetNewRange(20, 40) 

    print 'I am going to divide'
    hr_mc.Divide(hr_data)
    
    hr_DY_SF = hr_mc
    #hr_DY_SF.SetNewRange(20, 40) 
    #hr_DY_SF.setInfo('DY SF')         
    hr_data = None
    hr_mc = None

    #on J/Psi
    print '===================='
    print 'debug'
    print '===================='
    #Loose
    #file_data = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    #Tight
    file_data = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    #Medium
    #file_data = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    #Soft
    #file_data = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/DATA_data_all/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    
    hr_data = Gethr('1', 'BCDEF', file_data, 'JPsi', 'JPsi')
    print '===================='
    print 'set new range in data'
    print '===================='
    #hr_data.SetNewRange(20, 40) 
    #sys.exit()

    #Loose
    #file_mc = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root'
    #Tight
    file_mc = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    #Medium
    #file_mc = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root'
    #Soft
    #file_mc = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/MC_mc_all/TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root'
    hr_mc = Gethr('1', 'BCDEF', file_mc, 'JPsi', 'JPsi')
    #sys.exit()
    print '===================='
    print 'set new range in mc'
    print '===================='
    #hr_mc.SetNewRange(20, 40) 
    #sys.exit()
    hr_data.Divide(hr_mc)

    print 'I am going to divide'
    print 'debug this'


    #hr_data.Divide(hr_mc)
    hr_JPsi_SF = hr_data
    #hr_JPsi_SF.SetNewRange(20, 40) 
    #hr_DY_SF.setInfo('JPsi SF')         
    hr_data = None

    #plot and compare the SF
    hp = HistoPloter('.')
    hp.setEffRange(0.9, 1.2)
    hp.PlotEff1D([hr_DY_SF, hr_JPsi_SF])
    #hp.PlotEff1D([hr_SF_DY])


   




