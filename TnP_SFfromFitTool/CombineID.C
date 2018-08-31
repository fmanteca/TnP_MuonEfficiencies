//root -l -q -b "CombineID.C(\"BCDEF\",\"ID\")"
#include "TCanvas.h"
#include "TTree.h"
#include "TH2D.h"
#include "TFile.h"
#include <iostream>
#include <fstream>




void CombineID(TString run, TString id_iso)

{

  
  TFile* file1 = new TFile("Run" + run + "_Eff_mc_" + id_iso + "_part1.root");
  TFile* file2 = new TFile("Run" + run + "_Eff_mc_" + id_iso + "_part2.root");
  TFile* file3 = new TFile("Run" + run + "_Eff_mc_" + id_iso + "_part3.root");


  if(id_iso == "ID"){
    TH2D* NUM_LooseID_DEN_genTracks_eta_pt_part1 = (TH2D*)file1->Get("NUM_LooseID_DEN_genTracks_eta_pt");
    TH2D* NUM_TightID_DEN_genTracks_eta_pt_part1 = (TH2D*)file1->Get("NUM_TightID_DEN_genTracks_eta_pt");
    TH2D* NUM_MediumID_DEN_genTracks_eta_pt_part1 = (TH2D*)file1->Get("NUM_MediumID_DEN_genTracks_eta_pt");
    TH2D* NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt_part1 = (TH2D*)file1->Get("NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt");
    
    TH2D* NUM_LooseID_DEN_genTracks_eta_pt_part2 = (TH2D*)file2->Get("NUM_LooseID_DEN_genTracks_eta_pt");
    TH2D* NUM_TightID_DEN_genTracks_eta_pt_part2 = (TH2D*)file2->Get("NUM_TightID_DEN_genTracks_eta_pt");
    TH2D* NUM_MediumID_DEN_genTracks_eta_pt_part2 = (TH2D*)file2->Get("NUM_MediumID_DEN_genTracks_eta_pt");
    TH2D* NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt_part2 = (TH2D*)file2->Get("NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt");
    
    TH2D* NUM_LooseID_DEN_genTracks_eta_pt_part3 = (TH2D*)file3->Get("NUM_LooseID_DEN_genTracks_eta_pt");
    TH2D* NUM_TightID_DEN_genTracks_eta_pt_part3 = (TH2D*)file3->Get("NUM_TightID_DEN_genTracks_eta_pt");
    TH2D* NUM_MediumID_DEN_genTracks_eta_pt_part3 = (TH2D*)file3->Get("NUM_MediumID_DEN_genTracks_eta_pt");
    TH2D* NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt_part3 = (TH2D*)file3->Get("NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt");
    
    TFile output("Run" +run+ "_Eff_mc_ID.root","RECREATE");
    NUM_LooseID_DEN_genTracks_eta_pt_part1->Write();
    NUM_TightID_DEN_genTracks_eta_pt_part1->Write();
    NUM_MediumID_DEN_genTracks_eta_pt_part1->Write();
    NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt_part1->Write();
    NUM_LooseID_DEN_genTracks_eta_pt_part2->Write();
    NUM_TightID_DEN_genTracks_eta_pt_part2->Write();
    NUM_MediumID_DEN_genTracks_eta_pt_part2->Write();
    NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt_part2->Write();
    NUM_LooseID_DEN_genTracks_eta_pt_part3->Write();
    NUM_TightID_DEN_genTracks_eta_pt_part3->Write();
    NUM_MediumID_DEN_genTracks_eta_pt_part3->Write();
    NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt_part3->Write();
    output.Close();




  }else if(id_iso == "ISO"){


    TH2D* NUM_TightRelIso_DEN_MediumID_eta_pt_part1 = (TH2D*)file1->Get("NUM_TightRelIso_DEN_MediumID_eta_pt");
    TH2D* NUM_LooseRelIso_DEN_MediumID_eta_pt_part1 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_MediumID_eta_pt");
    TH2D* NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_part1 = (TH2D*)file1->Get("NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt");
    TH2D* NUM_LooseRelIso_DEN_LooseID_eta_pt_part1 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_LooseID_eta_pt");
    TH2D* NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt_part1 = (TH2D*)file1->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt");
    TH2D* NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt_part1 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt");

    TH2D* NUM_TightRelIso_DEN_MediumID_eta_pt_part2 = (TH2D*)file1->Get("NUM_TightRelIso_DEN_MediumID_eta_pt");
    TH2D* NUM_LooseRelIso_DEN_MediumID_eta_pt_part2 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_MediumID_eta_pt");
    TH2D* NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_part2 = (TH2D*)file1->Get("NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt");
    TH2D* NUM_LooseRelIso_DEN_LooseID_eta_pt_part2 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_LooseID_eta_pt");
    TH2D* NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt_part2 = (TH2D*)file1->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt");
    TH2D* NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt_part2 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt");

    TH2D* NUM_TightRelIso_DEN_MediumID_eta_pt_part3 = (TH2D*)file1->Get("NUM_TightRelIso_DEN_MediumID_eta_pt");
    TH2D* NUM_LooseRelIso_DEN_MediumID_eta_pt_part3 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_MediumID_eta_pt");
    TH2D* NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_part3 = (TH2D*)file1->Get("NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt");
    TH2D* NUM_LooseRelIso_DEN_LooseID_eta_pt_part3 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_LooseID_eta_pt");
    TH2D* NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt_part3 = (TH2D*)file1->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt");
    TH2D* NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt_part3 = (TH2D*)file1->Get("NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt");

    
    


    TFile output("Run" +run+ "_Eff_mc_ISO.root","RECREATE");
    NUM_TightRelIso_DEN_MediumID_eta_pt_part1->Write();
    NUM_LooseRelIso_DEN_MediumID_eta_pt_part1->Write();
    NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_part1->Write();
    NUM_LooseRelIso_DEN_LooseID_eta_pt_part1->Write();
    NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt_part1->Write();
    NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt_part1->Write();

    NUM_TightRelIso_DEN_MediumID_eta_pt_part2->Write();
    NUM_LooseRelIso_DEN_MediumID_eta_pt_part2->Write();
    NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_part2->Write();
    NUM_LooseRelIso_DEN_LooseID_eta_pt_part2->Write();
    NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt_part2->Write();
    NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt_part2->Write();

    NUM_TightRelIso_DEN_MediumID_eta_pt_part3->Write();
    NUM_LooseRelIso_DEN_MediumID_eta_pt_part3->Write();
    NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_part3->Write();
    NUM_LooseRelIso_DEN_LooseID_eta_pt_part3->Write();
    NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt_part3->Write();
    NUM_LooseRelIso_DEN_TightIDandIPCut_eta_pt_part3->Write();
    output.Close();





  }


}
