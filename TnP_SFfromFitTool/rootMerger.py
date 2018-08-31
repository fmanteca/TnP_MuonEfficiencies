import ROOT as r 
import array as array

filLst = ['/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunBCDEF_SF_ID.root',
          '/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunGH_SF_ID.root',
          '/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunBCDEF_SF_ISO.root',
          '/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunGH_SF_ISO.root']

mierdas = [] 




for fil in filLst: 
    cosas = {}
    for i in range(1,4):
        theFil = r.TFile.Open(fil.replace('.root','_part%d.root'%i))
        mierdas.append(theFil)
        for f in theFil.GetListOfKeys():
            if not f.GetName() in cosas:
                cosas[f.GetName()] = []
            cosas[f.GetName()].append( f.ReadObj() )

    for k in cosas: 
        binning1 = [ cosas[k][0].GetXaxis().GetBinLowEdge(x) for x in  range(1,cosas[k][0].GetXaxis().GetNbins()+1)]
        binning2 = [ cosas[k][1].GetXaxis().GetBinLowEdge(x) for x in  range(1,cosas[k][1].GetXaxis().GetNbins()+1)]
        binning3 = [ cosas[k][2].GetXaxis().GetBinLowEdge(x) for x in  range(1,cosas[k][2].GetXaxis().GetNbins()+1)] 
  
        binning1.append( cosas[k][0].GetXaxis().GetBinLowEdge(cosas[k][0].GetXaxis().GetNbins()) + cosas[k][0].GetXaxis().GetBinWidth(cosas[k][0].GetXaxis().GetNbins()))
        binning2.append( cosas[k][1].GetXaxis().GetBinLowEdge(cosas[k][1].GetXaxis().GetNbins()) + cosas[k][1].GetXaxis().GetBinWidth(cosas[k][1].GetXaxis().GetNbins()))
        binning3.append( cosas[k][2].GetXaxis().GetBinLowEdge(cosas[k][2].GetXaxis().GetNbins()) + cosas[k][2].GetXaxis().GetBinWidth(cosas[k][2].GetXaxis().GetNbins()))


        allBins = sorted( [ [ binning1, cosas[k][0]],  [binning2, cosas[k][1]], [binning3, cosas[k][2]]], key=lambda x: x[0][0])
        onlyBins = allBins[0][0]
        onlyBins.extend(allBins[1][0])
        onlyBins.extend(allBins[2][0])

        
        binningy = [ cosas[k][0].GetYaxis().GetBinLowEdge(x) for x in  range(1,cosas[k][0].GetYaxis().GetNbins()+1)]
        binningy.append( cosas[k][0].GetYaxis().GetBinLowEdge(cosas[k][0].GetYaxis().GetNbins()) + cosas[k][0].GetYaxis().GetBinWidth(cosas[k][0].GetYaxis().GetNbins()))
        
        print k 
        histo = r.TH2D(k, '', len(onlyBins)-1, array.array('d',onlyBins), len(binningy)-1, array.array('d',binningy))
        for binsx, hist in allBins:
            for x1, x2 in zip(binsx,binsx[1:]):
                for y1, y2 in zip(binningy, binningy[1:]):
                    xbin = histo.GetXaxis().FindBin( (x1+x2)/2)
                    ybin = histo.GetYaxis().FindBin( (y1+y2)/2)
            
                    xbinPre = hist.GetXaxis().FindBin( (x1+x2)/2)
                    ybinPre = hist.GetYaxis().FindBin( (y1+y2)/2)
                    

                    histo.SetBinContent(xbin,ybin, hist.GetBinContent( xbinPre, ybinPre))
                    histo.SetBinError  (xbin,ybin, hist.GetBinError  ( xbinPre, ybinPre))
                       
        outfile = r.TFile.Open(fil.split('/')[-1],'update')
        print 'writing', k
        histo.Write()
        outfile.Close()

