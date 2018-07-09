import ROOT
from myutils.HistoReader import HistoReader
from myutils.HistoPloter import HistoPloter
from myutils.Efficiency import Efficiency

#To run ROOT in batch mode
ROOT.gROOT.SetBatch(True)

if __name__ == "__main__":
    
    #input root file containing all the efficiencies
    #test_file = '/eos/cms/store/group/phys_muon/perrin/FitForTest/TnP_MC_NUM_hlt_Mu17_Mu8_OR_TkMu8_leg8_DEN_LooseIDnISO_PAR_pt_eta.root'
    #test_file = '/afs/cern.ch/work/s/sesanche/private/Muonico/CMSSW_9_2_4/src/MuonAnalysis/TagAndProbe/test/TnP_Muon_ID_Simple.root'

    #test_file  = '/afs/cern.ch/work/g/gaperrin/public/ForSergio/FitExample/Good/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
#    test_file  = '/afs/cern.ch/work/g/gaperrin/public/ForSergio/FitExample/Bad/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta_BIGSTAT.root'
    #test_file  = '/afs/cern.ch/work/g/gaperrin/public/ForSergio/FitExample/Bad/TnP_MC_NUM_TightID_DEN_genTracks_PAR_pt_eta.root'
    test_file  = 'output_20.root'

    #path where all the plots are going to be saved
    plot_path = 'TnP_SFfromFitTool'

    hr = HistoReader('Data test2')
    hr.readfile(test_file)

    effList = hr.EffList  

    hp = HistoPloter(plot_path)

    ##Plot add the fits
    hp.PlotFitList(effList)
    
    ## Make chi2 tests
    #hp.CheckFitList(effList)

    #Make all 1D efficiency plots
    hp.PlotEff1D([effList])

#    hKS = ROOT.TH1F('KS','',20, min(hp.KSs)*0.9, max(hp.KSs)*1.1)
#    for i in hp.KSs:
#        hKS.Fill(i)

#    c=ROOT.TCanvas()
#    hKS.Draw()
#    c.SaveAs('hKS.pdf')

    
    #Make 1D efficiency plots for multiple sample (not yet implemented)
    #hp.PlotEff1D([effList,effList])

    
