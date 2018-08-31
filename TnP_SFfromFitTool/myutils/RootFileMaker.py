import ROOT
import json
#import pickle

class RootFileMaker:
    '''Make a root files storing the results of the 2D map'''

    def __init__(self, filename):
        self.filename = filename
        self.zlow = None
        self.zhigh = None

    def cutstomRange(self, zlow, zhigh):
        self.zlow = zlow
        self.zhigh = zhigh

    def makeROOT(self, Eff2MmapList):
        f = ROOT.TFile('%s.root'%self.filename,"RECREATE")
        for eff in Eff2MmapList:
            h2  = eff.getTH2D()
            if self.zlow != None and self.zhigh != None:
                h2.GetZaxis().SetRangeUser(self.zlow, self.zhigh)
            h2.Write()

            #save pdf, png
            ROOT.gStyle.SetOptStat(0)
            ROOT.gStyle.SetPaintTextFormat('.3f')
            c = ROOT.TCanvas('c','c')
            c.SetLogx()
            h2.Draw()
            c.SaveAs('%s.pdf'%self.filename)
            c.SaveAs('%s.png'%self.filename)

        f.Close()

