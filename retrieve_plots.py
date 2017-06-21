import ROOT as r
import os

debug = False

def save_canvas(_folder, _file, _folder_out):
    _fit_folder = _file.replace('.root', '')

    if not os.path.exists(_folder_out + _fit_folder):
        os.makedirs(_folder_out + _fit_folder)
        
    _folder_out += _fit_folder
    
    if debug: print 'the folder out is', _folder_out
    
    f = r.TFile.Open(_folder+_file)
    for key in f.GetListOfKeys():
        c = r.gROOT.GetClass(key.GetClassName())
        if str(c).find('TDirectoryFile') != -1:
            r.gDirectory.cd(key.GetName())
            for key2 in r.gDirectory.GetListOfKeys():
                c2 = r.gROOT.GetClass(key2.GetClassName())
            if str(c2).find('TDirectoryFile') != -1:
                r.gDirectory.cd(key2.GetName())
                for key3 in r.gDirectory.GetListOfKeys():
                    c3 = r.gROOT.GetClass(key3.GetClassName())
                    if str(c3).find('TDirectoryFile') != -1 and key3.GetName().find('_eff') == -1:
                        r.gDirectory.cd(key3.GetName())
                        for key4 in r.gDirectory.GetListOfKeys():
                            c4 = r.gROOT.GetClass(key4.GetClassName())
                            if key4.GetName() == 'fit_canvas' and str(c4).find('TCanvas') != -1:
                                canvas  = key4.ReadObj()
                                _plot = key3.GetName()
                                if debug: print "_plot is", _plot
                                canvas.SaveAs(_folder_out + '/' +rename_fit(_plot) + '.pdf')
                        r.gDirectory.cd("..")
                r.gDirectory.cd("..")
            r.gDirectory.cd("..")

def rename_fit(_plot):

    _plot = _plot.replace('_pair_probeMultiplicity_bin0_','')
    _plot = _plot.replace('_tag_combRelIsoPF04dBeta_bin0__tag_pt_bin0__tag_IsoMu20_pass_','')
    return _plot

import sys, os
args = sys.argv[1:]
iteration = '1'
if len(args) > 0: iteration =  args[0]
if debug: print "The iteration is ", iteration
_sample = ''
if len(args) > 1: _sample =  args[1]
if debug: print "The sample is", _sample 

_folder = os.getcwd() + '/Efficiency' + iteration + '/' + _sample + '/'
_folder_out = _folder +  'FitPlots/'
if not os.path.exists(_folder + '/FitPlots'):
    os.makedirs(_folder + '/FitPlots')

dir = os.listdir(_folder)
for file in dir:
    #if 'tkRelIso' in file: continue
    if file.find('TnP_') != -1:
        save_canvas(_folder, file, _folder_out) 




