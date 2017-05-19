void customAxis(TString filename,
		TString canvasname)
{
  // Create directory
  gSystem->mkdir("png/" + filename, kTRUE);

  // Open file
  TFile* file = new TFile("/afs/cern.ch/work/f/fernanpe/CMSSW_8_0_20/src/MuonAnalysis/TagAndProbe/test/170124/EfficiencyID/" + filename + ".root");
  
  // Get canvas
  TCanvas* canvas = (TCanvas*)file->Get(canvasname);

  // Get frame
  TH1F* frame = (TH1F*)canvas->GetPrimitive("frame");

  // Modify frame
  frame->SetMinimum(0.99);

  frame->GetYaxis()->CenterTitle();

  frame->GetYaxis()->SetTitle("efficiency");

  frame->GetYaxis()->SetTitleOffset(1.3);

  // Draw
  canvas->Draw();

  // Save
  canvas->SaveAs("png/" + filename + ".png");
}
