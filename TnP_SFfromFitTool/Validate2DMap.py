###########
#INFO
#RUN: python Validate2DMap.py 
#
#Use to validate 2D map implementation (i.e. make sure that the map is modified accordingly to the operations on the historeader
###########

import ROOT
from myutils.HistoReader import HistoReader
from myutils.HistoPloter import HistoPloter
from myutils.Efficiency import Efficiency
import sys

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":


    Id = 'TnP_MC_NUM_HighPtID_DEN_genTracks_PAR_newpt_eta.root'
    hr_data_List = []

    

    print 'Readind'
    print '================'
    print Id
    print '================'

    ########
    #Test 2D map
    ########
    fileBC = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_BC/DATA_dataidBC/'+Id
    hr_dataBC = HistoReader('DataBC')
    hr_dataBC.readfile(fileBC)

    print 'Initial map'
    print '----------------'
    eff2D = hr_dataBC.eff2D
    eff2D.Print()
    eff2D.Print('up')
    eff2D.Print('down')

    print 'After Changing Range'
    print '----------------'
    hr_dataBC.SetNewRange(20, 90)
    eff2D = hr_dataBC.eff2D
    eff2D.Print()
    eff2D.Print('up')
    eff2D.Print('down')

    print 'After removing errors below 1%'
    print '----------------'
    hr_dataBC.CleanBigError(0.01)
    eff2D = hr_dataBC.eff2D
    eff2D.Print()
    eff2D.Print('up')
    eff2D.Print('down')

    print 'Other run'
    print '----------------'
    fileDE = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_DE/DATA_dataidDE/'+Id
    hr_dataDE = HistoReader('DataDE')
    hr_dataDE.readfile(fileDE)
    hr_dataDE.SetNewRange(20, 90)
    hr_dataDE.CleanBigError(0.01)
    hr_dataDE.setLumi(10)
    hr_dataDE.setInfo('DE')
    hr_dataDE.setType('data')
    eff2D = hr_dataDE.eff2D
    eff2D.Print()
    eff2D.Print('up')
    eff2D.Print('down')

    print 'Afer added other run (lumi-rew)'
    print '----------------'
    hr_dataBC.setLumi(10)
    hr_dataBC.setInfo('BC')
    hr_dataBC.setType('data')
    hr_dataBC.Sum(hr_dataDE)
    eff2D = hr_dataBC.eff2D
    eff2D.Print()
    eff2D.Print('up')
    eff2D.Print('down')

    print 'To test the ratio'
    print '----------------'

    fileLoose = '/afs/cern.ch/user/f/fernanpe/public/for_Gael/Efficiencies_2017/EfficiencyID_DE/MC_mcidDE/'+Id
    hr_dataLoose = HistoReader('DataLoose')
    hr_dataLoose.readfile(fileLoose)
    hr_dataLoose.SetNewRange(20, 90)
    hr_dataLoose.setLumi(10)
    hr_dataLoose.setInfo('DE')
    hr_dataLoose.setType('data')
    hr_dataLoose.Sum(hr_dataDE)
    print 'Den (num is the previous map)'
    print '----------------'
    eff2Den = hr_dataLoose.eff2D
    eff2Den.Print()
    eff2Den.Print('up')
    eff2Den.Print('down')
    print 'SF (after division)'
    print '----------------'
    ratioMap = eff2D.divideMap(eff2Den)
    ratioMap.Print()
    ratioMap.Print('up')
    ratioMap.Print('down')


