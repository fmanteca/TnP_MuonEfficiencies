// KS and AD with toys
// Author: Sergio Sanchez Cruz

#include <RooRealVar.h>
#include <RooAbsPdf.h>
#include <RooAbsData.h>
#include <TH1.h>
#include <algorithm>  
#include "GoodnessOfFit.cc"


void KSandADWithToys( Double_t& KS, Double_t& AD, RooAbsData& data, RooAbsPdf& pdf, RooRealVar& mass)
{

  const int nToys = 1000;

  float KSobs = EvaluateADDistance(pdf, data, mass, true);
  float ADobs = EvaluateADDistance(pdf, data, mass, false);

  for (int k = 0; k < nToys; ++k){
    RooDataSet* toys = pdf.generate(RooArgSet(mass));
    RooAbsData* theToys = (RooAbsData*) toys;
    float KStoy = EvaluateADDistance(pdf, *theToys, mass, true);
    float ADtoy = EvaluateADDistance(pdf, *theToys, mass, false);
    
    if (KStoy > KSobs) KS += 1/float(nToys);
    if (ADtoy > ADobs) AD += 1/float(nToys);
  }

} 
