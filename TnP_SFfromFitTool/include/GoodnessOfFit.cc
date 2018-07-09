// Taken from the HiggsCombineTool. All the credits to the authors

#ifndef GOODNESS_H
#define GOODNESS_H

#include <RooRealVar.h>
#include <RooAbsPdf.h>
#include <RooAbsData.h>
#include <TH1.h>
#include <algorithm>  


Double_t EvaluateADDistance(RooAbsPdf& pdf, RooAbsData& data, RooRealVar& observable, bool kolmo, int verbose=0) {
    typedef std::pair<double, double> double_pair;
    std::vector<double_pair> data_points;
    Int_t n_data = data.numEntries();
    Double_t s_data = data.sumEntries();

    const RooArgSet* datavals;
    RooRealVar* observable_val;
    for (int i = 0; i < n_data; i++) {
        datavals = data.get(i);
        observable_val = (RooRealVar*)(datavals->find(observable.GetName()));
        data_points.push_back(std::make_pair(observable_val->getVal(), data.weight()));
    }

    std::stable_sort(data_points.begin(), data_points.end(),
         [](double_pair i, double_pair j) {
           return i.first < j.first;
         });

    double test_stat = 0.;
    double current_cdf_val = 0.;
    double last_cdf_val = 0.;
    double empirical_df = 0.;
    double observableval = 0.;
    double bin_prob = 0.;
    double distance = 0.;

    // CDF of the PDF
    // If RooFit needs to use the scanning technique then increase the number
    // of sampled bins from 1000 to 10000
    std::auto_ptr<RooAbsReal> cdf(pdf.createCdf(observable, RooFit::ScanParameters(10000, 2)));

    int bin = 0;
    for (std::vector<double_pair>::const_iterator d = data_points.begin();
         d != data_points.end(); d++, ++bin) {
        // observableval = ((d+1)->first + d->first)/2.; // d->first is middle of bin, want upper edge.
      
        // This is a better way to get the upper bin edge in the case where we
        // have variable bin widths (I hope)
        observableval = observable.getBinning().binHigh(
            observable.getBinning().binNumber(d->first));
        observable.setVal(observableval);
        // observable.bin
        current_cdf_val = cdf->getVal();
        empirical_df += d->second/s_data;


        if (kolmo){
            distance = std::abs(empirical_df-current_cdf_val);
            if (verbose >= 3) {
              std::cout << "Observable: " << observableval << "\tdata: " << d->second << "\tedf: " << empirical_df << "\tcdf: " << current_cdf_val << "\tdistance: " << distance << "\n";
            }
            if (distance > test_stat) test_stat = distance;
        }else{
            bin_prob = current_cdf_val-last_cdf_val;
            distance = s_data*pow((empirical_df-current_cdf_val), 2)/current_cdf_val/(1.-current_cdf_val)*bin_prob;
            if (current_cdf_val >= 1.0) {
              distance = 0.;
            }
            if (verbose >= 3) {
              std::cout << "Observable: " << observableval << "\tdata: " << d->second << "\tedf: " << empirical_df << "\tcdf: " << current_cdf_val << "\tdistance: " << distance << "\n";
            }
            // from L. Demortier, CDF/ANAL/JET/CDFR/3419
            test_stat += distance;
        }
        last_cdf_val = current_cdf_val;
    }


    // if (kolmo){
    //     if (test_stat < oldlimit) test_stat = oldlimit; // The test statistic of the Kolmogorov-Smirnov test is the maximum of the test statistics of all individual PDFs.
    // }else{
    //     test_stat += oldlimit; // The test statistic of the Anderson-Darling test is the sum of the test statistics of all individual PDFs.
    // }
    return test_stat;
}

#endif
