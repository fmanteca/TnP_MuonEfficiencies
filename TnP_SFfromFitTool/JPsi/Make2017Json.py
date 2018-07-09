#Creates all the jsons
#

import ROOT
import sys
sys.path.append('../myutils')

from HistoReader import HistoReader
from HistoPloter import HistoPloter
from Efficiency import Efficiency
from JsonMaker import JsonMaker
from RootFileMaker import RootFileMaker

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":


    ##################
    ID = [  
            #'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_eta.root',
            #'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_vtx.root',
            #'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt.root',
            'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root',
            #'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_eta.root',
            #'TnP_MC_NUM_TightID_DEN_genTracks_PAR_eta.root',
            'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root',
            #'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt.root',
            #'TnP_MC_NUM_TightID_DEN_genTracks_PAR_vtx.root',
            #'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_vtx.root',
            #'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_eta.root',
            #'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt.root',
            'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root',
            #'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_vtx.root',
            #'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt.root',
            ]

    Num = ['ID']
    Run = ['BCDEF']
    NumDic = {'ID':ID}
    Type = ['mc', 'data']

    #########
    #Provide DATA and MC JSON separetly for run BC, DE and F
    #########
    for n in Num:
        #Used for SF
        SF_MapList = []
        MC_MapList = []
        DATA_MapList = []
        SFoutputJSONname ='Run%s_%s_%s'%('BCDEF','SF',n)
        jSF = JsonMaker(SFoutputJSONname)
        rSF = RootFileMaker(SFoutputJSONname)
        for t in Type:
            #All the rest will be within the json file
            outputJSONname ='Run%s_%s_%s'%('BCDEF',t,n)
            MapList = []
            j = JsonMaker(outputJSONname)
            r_ = RootFileMaker(outputJSONname)
            for s in NumDic[n]:
                file_ = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/%s_%s_all/%s'%(t.upper(),t,s)
                print 'file is', file_
                hr = HistoReader('hr')
                hr.readfile(file_)     
                print 'done reading file'
                #Set a custom range for the x parameter. e.g. SetNewRange(3, 20) will only keep the bins within 3-20 (used for pt distribution)
                #if 'pt_eta.root' or 'pt.root' in s:
                #    hr.SetNewRange(3, 21) 
                hr.setInfo('dummy')         
                #If error is bigger than 0.01, will use error from neighbour bin average
                hr.CleanBigError(0.01)  
                hr.setType(t)      
                MapList.append(hr.eff2D)

                #For SF
                if t == 'mc':
                    MC_MapList.append(hr.eff2D)
                elif t == 'data':
                    DATA_MapList.append(hr.eff2D)
                del hr


            #For DATA, MC
            print '=============='
            print 'goind to make the root files for the data and mc'
            j.makeJSON(MapList)
            print 'MapList is', MapList
            r_.makeROOT(MapList)
            print '========='
            print 'done'

        #For SF
        for mcm, datam in zip(MC_MapList,DATA_MapList):
            SF_MapList.append(datam.divideMap(mcm))

        jSF.makeJSON(SF_MapList)
        rSF.makeROOT(SF_MapList)

