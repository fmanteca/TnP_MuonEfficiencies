#Creates all the jsons
#

import ROOT
from myutils.HistoReader import HistoReader
from myutils.HistoPloter import HistoPloter
from myutils.Efficiency import Efficiency
from myutils.JsonMaker import JsonMaker
from myutils.RootFileMaker import RootFileMaker
import sys

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":


    ##################


    ID = [  'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_HighPtID_DEN_genTracks_PAR_newpt_eta.root',
#            'TnP_MC_NUM_TrkHighPtID_DEN_genTracks_PAR_newpt_eta.root',
#            'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root',
#            'TnP_MC_NUM_MediumPromptID_DEN_genTracks_PAR_pt_eta.root'
            ]

    ISO = [ 'TnP_MC_NUM_TightRelIso_DEN_MediumID_PAR_pt_eta.root',
            'TnP_MC_NUM_LooseRelIso_DEN_MediumID_PAR_pt_eta.root',
            'TnP_MC_NUM_TightRelIso_DEN_TightIDandIPCut_PAR_pt_eta.root',
            'TnP_MC_NUM_LooseRelIso_DEN_LooseID_PAR_pt_eta.root',
#            'TnP_MC_NUM_TightRelTkIso_DEN_TrkHighPtID_PAR_newpt_eta.root',
#            'TnP_MC_NUM_LooseRelTkIso_DEN_TrkHighPtID_PAR_newpt_eta.root',
            'TnP_MC_NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_PAR_newpt_eta.root',
            'TnP_MC_NUM_LooseRelIso_DEN_TightIDandIPCut_PAR_pt_eta.root',
#            'TnP_MC_NUM_TightRelTkIso_DEN_HighPtIDandIPCut_PAR_newpt_eta.root']
            ]
    eta_region = ['part1', 'part2', 'part3']
    Type = ['mc', 'data']
    Num = ['ISO', 'ID']
            
    NumDic = {'ISO':ISO, 'ID':ID}
    LumiDic = {'BCDEF':36, 'GH':36}


    #########
    #Provide DATA and MC JSON separetly for run BC, DE and F
    #########
    for n in Num:
        for r in eta_region: 
            #Used for SF
            SF_MapList = []
            MC_MapList = []
            DATA_MapList = []
            SFoutputJSONname ='Run%s_%s_%s'%(NumDic[n],'SF',n)
            jSF = JsonMaker(SFoutputJSONname)
            rSF = RootFileMaker(SFoutputJSONname)
            for t in Type:
                #All the rest will be within the json file
                outputJSONname ='Run%s_%s_%s'%(r,t,n)
                MapList = []
                j = JsonMaker(outputJSONname)
                r_ = RootFileMaker(outputJSONname)
                for s in NumDic[n]:
                    file_ = '/eos/cms/store/group/phys_muon/fernanpe/Efficiencies_LegacyReReco2016_final/Efficiency%s_%s_%s/%s_%sid%s/%s'%(n,s,r,t.upper(),t,s)
                    hr = HistoReader('hr')
                    hr.readfile(file_)     
                    hr.SetNewRange(20, 120) 
                    hr.setInfo('dummy')         
                    hr.CleanBigError(0.01)  
                    hr.setType(t)      
                    MapList.append(hr.eff2D)
                    #print '==========='
                    #print hr.eff2D.name
                    #print s
                    #print r
                    #print t
                    #print '==========='
                    #hr.eff2D.Print('nominal')
                    #hr.eff2D.Print('up')
                    #hr.eff2D.Print('down')
                    #sys.exit()

                    #For SF
                    if t == 'mc':
                        MC_MapList.append(hr.eff2D)
                    elif t == 'data':
                        DATA_MapList.append(hr.eff2D)

                #For DATA, MC
                j.makeJSON(MapList)
                r_.makeROOT(MapList)

            #For SF
            for mcm, datam in zip(MC_MapList,DATA_MapList):
                datam.getTH2D()
                SF_MapList.append(datam.divideMap(mcm))

            jSF.makeJSON(SF_MapList)
            rSF.makeROOT(SF_MapList)

    #########
    #Will contain hr for run BC, DE and F to compute SF on BCDEF
    #########
    for n in Num:
        #Used for SF
        SF_MapList = []
        MC_MapList = []
        DATA_MapList = []
        SFoutputJSONname ='RunBCDEFGH_%s_%s'%('SF',n)
        jSF = JsonMaker(SFoutputJSONname)
        rSF = RootFileMaker(SFoutputJSONname)
        for t in Type:
            #All the rest will be within the json file
            outputJSONname ='RunBCDEFGH_%s_%s'%(t,n)
            j = JsonMaker(outputJSONname)
            r_ = RootFileMaker(outputJSONname)
            MapList = []
            for s in NumDic[n]:
                #Contains hr from Run BC, DE and F that will be summed up at the end
                hrList = []
                for r in eta_region: 
                    file_ = '/eos/cms/store/group/phys_muon/fernanpe/Efficiencies_LegacyReReco2016_final/Efficiency%s_%s_%s/%s_%sid%s/%s'%(n,s,r,t.upper(),t,s)
                    hr = HistoReader('hr')
                    hr.readfile(file_)     
                    hr.SetNewRange(20, 120) 
                    hr.setLumi(LumiDic[r])
                    hr.CleanBigError(0.05)  
                    hr.setInfo('dummy')         
                    hr.setType(t)      
                    hrList.append(hr)

                #lumi sum of all the hr
                hr0 = hrList[0]
                for hr in hrList[1:]:
                    hr0.Sum(hr)

                MapList.append(hr0.eff2D)

                #For SF
                if t == 'mc':
                    MC_MapList.append(hr0.eff2D)
                elif t == 'data':
                    DATA_MapList.append(hr0.eff2D)
            #For DATA, MC
            j.makeJSON(MapList)
            r_.makeROOT(MapList)

        #For SF
        for mcm, datam in zip(MC_MapList,DATA_MapList):
            SF_MapList.append(datam.divideMap(mcm))

        jSF.makeJSON(SF_MapList)
        rSF.makeROOT(SF_MapList)