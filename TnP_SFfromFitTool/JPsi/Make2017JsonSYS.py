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
            #'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root',
            ##'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_eta.root',
            ##'TnP_MC_NUM_TightID_DEN_genTracks_PAR_eta.root',
            #'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root',
            ##'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt.root',
            ##'TnP_MC_NUM_TightID_DEN_genTracks_PAR_vtx.root',
            ##'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_vtx.root',
            ##'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_eta.root',
            ##'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt.root',
            #'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root',
            'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root',
            ##'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_vtx.root',
            ##'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt.root',
            ]

    #List of all the systematic variations 
    sysList = ['nominal', 'mass_up', 'mass_down', 'nbins_up', 'nbins_down', 'pdf']
    #sysList = ['nominal', 'mass_up']
    sysDic = {
            'nominal':'nominal',
            'mass_up':'MassRange/EfficiencyRun2017B_F_massRange_2p85_3p35',
            'mass_down':'MassRange/EfficiencyRun2017B_F_massRange_2p95_3p25',
            'nbins_up':'MassBin/EfficiencyRun2017B_F_binfit45',
            'nbins_down':'MassBin/EfficiencyRun2017B_F_binfit35',
            'pdf':'PDF/EfficiencyRun2017B_F_PDF_Gauss'
            
            }

    #

    path_in = []
    #################
    #Path where the main SF root files are stored (using the full statistics)
    path_in.append('/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/')
    #%s_%s/%s_%sid%s/%s'%(n,r,t.upper(),t,r,s)

    ##################
    #Main path where all the root files are stored
    #path_in.append('/afs/cern.ch/user/f/fernanpe/public/for_Gael/Systematics_2017')
    path_in.append('/afs/cern.ch/user/s/sfonseca/public/for_Gael/varied')

    Num = ['ID']
    Run = ['BCDEF']
    NumDic = {'ID':ID}
    Type = ['mc', 'data']

    NameDic = {'TnP_MC_NUM_SoftID_DEN_genTracks_PAR_pt_eta.root':'Soft',
        'TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root':'Tight',
        'TnP_MC_NUM_MediumID_DEN_genTracks_PAR_pt_eta.root':'Medium',
        'TnP_MC_NUM_LooseID_DEN_genTracks_PAR_pt_eta.root':'Loose'
            }

    #########
    #Provide DATA and MC JSON separetly for run BC, DE and F
    #########
    # this is loop over the selectors/ID
    for n in Num:
        #Used for SF
        SF_MapList = []
        MC_MapList = []
        DATA_MapList = []
        SFoutputJSONname ='Run%s_%s_%s'%('BCDEF','SF',n)
        jSF = JsonMaker(SFoutputJSONname)
        rSF = RootFileMaker(SFoutputJSONname)
        # Will now loop over the syslist. Need to store the the SF map for each variation
        sysSFMapList = {} 
        for sys in sysList:
            # for each sys variation, store data and mc maps
            sysSFMapList[sys] = {} 
            for t in Type:
                #All the rest will be within the json file
                #outputJSONname ='Run%s_%s_%s'%('BCDEF',t,n)
                MapList = []
                #j = JsonMaker(outputJSONname)
                #r_ = RootFileMaker(outputJSONname)
                for s in NumDic[n]:
                    IDname = NameDic[s]
                    if sys == 'nominal':
                        path = path_in[0]
                    else: path = path_in[1]
                        
                    if not sys == 'nominal':
                        file_ = '%s/%s/%s_%s_all/%s'%(path,sysDic[sys],t.upper(),t,s)
                    else: 
                        file_ = '%s/EfficiencyRun2017B_F/%s_%s_all/%s'%(path,t.upper(),t,s)
                    #file_ = '/afs/cern.ch/user/s/sfonseca/public/for_Gael/nominal/EfficiencyRun2017B_F/%s_%s_all/%s'%(t.upper(),t,s)
                    print 'file is', file_
                    hr = HistoReader('hr')
                    hr.readfile(file_)     
                    print 'done reading file'
                    #Set a custom range for the x parameter. e.g. SetNewRange(3, 20) will only keep the bins within 3-20 (used for pt distribution)
                    #if 'pt_eta.root' or 'pt.root' in s:
                    #    hr.SetNewRange(3, 21) 
                    hr.setInfo('dummy')         
                    ##If error is bigger than 0.01, will use error from neighbour bin average
                    #hr.CleanBigError(0.01)  
                    hr.setType(t)      
                    MapList.append(hr.eff2D)

                    ##For SF
                    #if t == 'mc':
                    #    MC_MapList.append(hr.eff2D)
                    #elif t == 'data':
                    #    DATA_MapList.append(hr.eff2D)
                    #del hr

                    # store 2D map in sys
                    sysSFMapList[sys][t] = hr.eff2D

        # done looping over all the sys
        # create SF map for all the sys
        for sys in sysSFMapList:
            SF_map = sysSFMapList[sys]['data'].divideMap(sysSFMapList[sys]['mc'])
            sysSFMapList[sys]['sf'] = SF_map

        # loop over all the sys and store corresponding jsons and root files
        for sys in sysSFMapList:
            for t in Type+['sf']:
                JSONname = 'Run%s_%s_%s_%s'%('BCDEF',t,sys,IDname)
                jSF = JsonMaker(JSONname)
                rSF = RootFileMaker(JSONname)
                jSF.makeJSON([sysSFMapList[sys][t]])
                rSF.makeROOT([sysSFMapList[sys][t]])

                # save nominal/sys ratio (to see change)
                sys_ratio_map = sysSFMapList['nominal'][t].divideMap(sysSFMapList[sys][t])
                JSONname = 'Run%s_%s_nominalRatio%s_%s'%('BCDEF',t,sys,IDname)
                rSF = RootFileMaker(JSONname)
                rSF.cutstomRange(0.95, 1.05)
                rSF.makeROOT([sys_ratio_map])

        # computing the sys uncertainties here
        # list of 2DMap. The first items is the nominal. Other items are all the sys variation (order not relevant)
        #sysVarList = []

        # first test on data
        # add nominal value
        # add rest of sys
        for t in Type+['sf']:
            sysVarList = []
            for sys in sysSFMapList:
                if sys == 'nominal': continue
                sysVarList.append(sysSFMapList[sys][t])

            sysMap = sysSFMapList['nominal'][t].evalSysUncertainties(sysVarList)
            JSONname = 'Run%s_%s_%s_%s'%('BCDEF',t,'SYS',IDname)
            jSF = JsonMaker(JSONname)
            rSF = RootFileMaker(JSONname)
            jSF.makeJSON([sysMap])
            rSF.makeROOT([sysMap])

            
                    


#                #For DATA, MC
#                print '=============='
#                print 'goind to make the root files for the data and mc'
#                j.makeJSON(MapList)
#                print 'MapList is', MapList
#                r_.makeROOT(MapList)
#                print '========='
#                print 'done'
#
#            #For SF
#            for mcm, datam in zip(MC_MapList,DATA_MapList):
#                SF_MapList.append(datam.divideMap(mcm))
#
#            jSF.makeJSON(SF_MapList)
#            rSF.makeROOT(SF_MapList)
#
