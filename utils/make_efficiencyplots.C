#include "TString.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TGraphAsymmErrors.h"
#include "TAxis.h"
#include "TGaxis.h"
#include "TH1F.h"
#include "TROOT.h"
#include "TLegend.h"
#include "TGaxis.h"
#include "tdrstyle.C"
#include "CMS_lumi.C"
#include "TLegendEntry.h"

#include <iostream>

////!! To compute SF = MC/Data
//TH1F* DividTGraphs(TGraphAsymmErrors* gr1, TGraphAsymmErrors* gr2){
//
//    int nbins = gr1->GetN();
//    double xbins[nbins+1];
//
//    for(int i = 0;  i < nbins; ++i){
//
//        Double_t x = 999; 
//        Double_t x_hi = 999; 
//        Double_t x_low = 999; 
//        Double_t y = 999; 
//        gr1->GetPoint(i,x,y);
//        x_hi = gr1->GetErrorXhigh(i);
//        x_low = gr1->GetErrorXlow(i);
//        if(i == nbins-1){
//            xbins[i] = x-x_low;
//            xbins[i+1] = x+x_hi;
//        }else{
//            xbins[i] = x-x_low;
//        }
//    }
//
//    TH1F *h1 = new TH1F("h1","h1",nbins,xbins);
//    TH1F *h2 = new TH1F("h2","h2",nbins,xbins);
//
//    TGraphAsymmErrors* gr[2] = {gr1, gr2};
//    TH1F* h[2] = {h1, h2};
//
//    //Loop over bins to do ratio
//    //
//    for (int k = 0; k < 2; ++k){
//        for(int i = 0;  i < nbins+1; ++i){
//            //
//            //TGraph
//            //
//            Double_t num_x = 999; 
//            Double_t num_y = 999; 
//            Double_t num_y_hi = 999; 
//            Double_t num_y_low = 999; 
//
//            gr[k]->GetPoint(i,num_x,num_y);
//            num_y_hi = gr[k]->GetErrorYhigh(i);
//            num_y_low = gr[k]->GetErrorYlow(i);
//
//            double max_error = max(num_y_hi,num_y_low);
//
//            //Convert into TH1D
//            h[k]->SetBinContent(h[k]->FindBin(num_x), num_y);
//            h[k]->SetBinError(h[k]->FindBin(num_x), max_error);
//        }
//    }
//
//    //ratio histogram
//    h[0]->Divide(h[1]);
//
//    return h[0]; 
//
//}


int make_efficiencyplots(TString _file, TString _canvas, TString _path1, TString _output, TString _legtext){

    setTDRStyle();
    gROOT->SetBatch(kTRUE);


    TString _par = "";
    if(_canvas.Contains("pt_PLOT_abseta_bin0")){_par = "abseta_bin0";}
    else if(_canvas.Contains("pt_PLOT_abseta_bin1")){_par = "abseta_bin1";}
    else if(_canvas.Contains("pt_PLOT_abseta_bin2")){_par = "abseta_bin2";}
    else if(_canvas.Contains("pt_PLOT_abseta_bin3")){_par = "abseta_bin3";}

    TFile *f1 = TFile::Open(_path1 + _file);
    TCanvas* c1 = (TCanvas*) f1->Get(_canvas);
    TGraphAsymmErrors* eff1 = (TGraphAsymmErrors*)c1->GetPrimitive("hxy_fit_eff");

    int nbins = eff1->GetN();
    double x,y;
    eff1->GetPoint(0,x,y);
    double x_low = x-eff1->GetErrorXlow(0);
    eff1->GetPoint(nbins-1,x,y);
    double x_hi = x+eff1->GetErrorXhigh(nbins-1);

    TCanvas* c3 = new TCanvas("c3","c3");
    TPad *pad1 = new TPad("pad1", "pad1", 0, 0.1, 1, 1.0);
    pad1->SetBottomMargin(0.); 
    pad1->SetTopMargin(0.1); 
    pad1->Draw();
    pad1->cd();
    eff1->Draw("AP");
    eff1->SetTitle("");
    eff1->GetYaxis()->SetTitle("Efficiency");
    eff1->GetXaxis()->SetRangeUser(x_low, x_hi);
    eff1->GetXaxis()->SetLabelOffset(999);
    eff1->GetXaxis()->SetLabelSize(0);
    TString _xtitle = eff1->GetXaxis()->GetTitle();
    if(_xtitle.Contains("nVertices")){_xtitle = "N(primary vertices)";
    }else if (_xtitle.Contains("phi")){_xtitle = "muon #phi";}
    else if (_xtitle.Contains("eta")){_xtitle = "muon #eta";}
    else if (_xtitle.Contains("pt")){_xtitle = "muon p_{t} [GeV]"; /*pad1->SetLogx();*/}
    eff1->GetXaxis()->SetTitle(_xtitle);
    TString _title = eff1->GetXaxis()->GetTitle();
    eff1->GetXaxis()->SetTitle("");
    eff1->GetYaxis()->SetRangeUser(0.79, 1.1);
    //eff1->GetYaxis()->SetRangeUser(0.49, 1.05);
    eff1->GetYaxis()->SetTitleSize(27);
    eff1->GetYaxis()->SetTitleFont(63);
    eff1->GetYaxis()->SetLabelFont(43);
    eff1->SetMarkerStyle(20);
    eff1->GetYaxis()->SetLabelSize(20);
    eff1->GetYaxis()->SetTitleOffset(1.5);
    //
    eff1->GetXaxis()->SetTitleSize(27);
    eff1->GetXaxis()->SetLabelSize(20);
    eff1->GetXaxis()->SetTitle(_title);
    eff1->GetXaxis()->SetTitleFont(63);
    eff1->GetXaxis()->SetTitleSize(27);
    eff1->GetXaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
    CMS_lumi(pad1, 4, 11);
//
    TLegend* leg = new TLegend(0.45, 0.65, 0.75 , 0.85);
    leg->SetHeader(_legtext);
    TLegendEntry *header = (TLegendEntry*)leg->GetListOfPrimitives()->First();
    header->SetTextColor(1);
    header->SetTextFont(43);
    header->SetTextSize(20);
    TString _leg1 = "";
    TString _leg2 = "";
    cout<<"path1 is"<< _path1<<endl;
    if(_path1.Contains("DATA")){
	    _leg1 = "data";
	    //_leg1 = "beforeL2fix";
            if(_path1.Contains("_default")){_leg1 = "default";} 
	    else if(_path1.Contains("_CMSshape")) {_leg1 = "CMSshape";} 
    }
    else if(_path1.Contains("MC")){ 
        if(_path1.Contains("NLO")) _leg1 = "MC NLO"; 
        else if(_path1.Contains("LO")) _leg1 = "MC LO";
        else _leg1 = "MC";
    }

    leg->AddEntry(eff1, _leg1, "LP");
    
    leg->SetBorderSize(0.);
    leg->SetTextFont(43);
    leg->SetTextSize(20);
    leg->Draw();
    _file.ReplaceAll("root","pdf");
    TGaxis *axis = new TGaxis( -5, 20, -5, 220, 20,220,510,"");
    axis->SetLabelFont(43); // Absolute font size in pixel (precision 3)
    axis->SetLabelSize(15);
    axis->Draw();

    TString cname = _output + "Data_" + _file;
    cname.ReplaceAll(".pdf","_"+_par+".pdf");
    //c3->SaveAs(_output + _file); + "_" + _par);
    c3->SaveAs(cname);
    //_file.ReplaceAll("pdf","png");
    cname.ReplaceAll("pdf","png");
    c3->SaveAs(cname);

    return 0;

}

