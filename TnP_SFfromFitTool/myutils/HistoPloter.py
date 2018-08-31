import ROOT
from Efficiency import Efficiency
import os
import sys
import numpy as np
import copy as copy
import math

import array
#import FitDiagnostics


ROOT.gROOT.LoadMacro('include/GoodnessOfFit.cc+')
ROOT.gROOT.LoadMacro('include/KSandADWithToys.cc+')
ROOT.gROOT.LoadMacro('myutils/tdrstyle.C')
ROOT.gROOT.LoadMacro('myutils/CMS_lumi.C')
#sys.exit()

ROOT.RooMsgService.instance().setGlobalKillBelow(ROOT.RooFit.WARNING)



class HistoPloter:
    '''Plot the relevant histogram, fits'''

    def __init__(self, outputpath):
        self.outputpath = outputpath
        self.effUpRange = 1.1
        self.effDownRange = 0.8
        self.ratioDownRange = 0.85
        self.ratioUpRange = 1.15
        #h.GetYaxis().SetRangeUser(0.85,1.15)
        self.KSs      = [] 
        self.ADs      = [] 
        self.maxPulls = []
        self.chi2s    = []
        self.sFactors = []
        #For sys study. Only thake minimum and maxium of the plot
        self.MinMax = False

    def setRatioRange(self, ratioDownRange, ratioUpRange):
        self.ratioDownRange = ratioDownRange
        self.ratioUpRange = ratioUpRange
    def setEffRange(self, effDownRange, effUpRange):
        self.effUpRange = effUpRange
        self.effDownRange = effDownRange

    def CreateOutputFolder(self, subfolder = None):
        '''Create output path to store the files if not existing'''
        if subfolder:
            directory = self.outputpath + '/' + subfolder
        else: 
            directory = self.outputpath

        if not os.path.exists(directory):
            print directory, 'is not existing, creating it'
            os.makedirs(directory)
        else: 
            print directory, 'exists'

        os.system('cp include/index.php %s'%directory)

        return directory

    def FormatOutputPath(self, path):
        '''Modify output path (remvove space, etc)'''
        return path.replace(' ','').replace('&','And')

    def TGraph2TH1F(self, gr):
        '''Convert a TGraphAsymmErrors to TH1F. Errors are conservative i.e. max of the low/high error is take'''
        nbins = gr.GetN()
        bins = range(0,nbins)
        xbins = np.array([0 for i in range(0,nbins+1)],dtype=np.float64)
        for bin_ in bins:
            x = ROOT.Double(999)
            y = ROOT.Double(999)
            gr.GetPoint(bin_,x,y)
            x_hi = gr.GetErrorXhigh(bin_)
            x_low = gr.GetErrorXlow(bin_)
            if bin_ == nbins -1:
                xbins[bin_] = x - x_low
                xbins[bin_+1] = x + x_hi
            else:
                xbins[bin_] = x - x_low

        #print 'xbins is', xbins
        h = ROOT.TH1F('h', 'h', nbins, xbins)
        h.Sumw2()

        for bin_ in bins:
            num_x = ROOT.Double(999)
            num_y = ROOT.Double(999) 
            num_y_hi = 999 
            num_y_low = 999 

            gr.GetPoint(bin_,num_x,num_y)
            num_y_hi = gr.GetErrorYhigh(bin_)
            num_y_low = gr.GetErrorYlow(bin_)

            max_error = max(num_y_hi,num_y_low)

            #Convert into TH1D
            h.SetBinContent(h.FindBin(num_x), num_y)
            h.SetBinError(h.FindBin(num_x), max_error)
            #print 'max error is', max_error

        return h

    def GetMinMaxTH1F(self, THList, name=''):
        '''Get list of histograms. Loops over each bin to compute max and min value, that are then returned'''

        #print THList[0].ClassName()

        #If list of TGraph (used for the eff plots)
        if THList[0].ClassName() == 'TGraphAsymmErrors':

            nbins = THList[0].GetN()
            bins = range(0,nbins)
            xbins       = np.array([0 for i in range(0,nbins)],dtype=np.float64)
            xbinsL      = np.array([0 for i in range(0,nbins)],dtype=np.float64)
            xbinsH      = np.array([0 for i in range(0,nbins)],dtype=np.float64)
            MAXybins    = np.array([0 for i in range(0,nbins)],dtype=np.float64)
            MINybins    = np.array([0 for i in range(0,nbins)],dtype=np.float64)
            ybinsL      = np.array([0 for i in range(0,nbins)],dtype=np.float64)
            ybinsH      = np.array([0 for i in range(0,nbins)],dtype=np.float64)

            for bin_ in bins:
                x = ROOT.Double(999)
                y = ROOT.Double(999)
                THList[0].GetPoint(bin_,x,y)
                x_hi = THList[0].GetErrorXhigh(bin_)
                x_low = THList[0].GetErrorXlow(bin_)
                xbins[bin_]     = x
                xbinsH[bin_]    = x_hi
                xbinsL[bin_]    = x_low

            #h = ROOT.TH1F('h', 'h', nbins, xbins)

            for bin_ in bins:
                bmin = -99
                bmax = 99
                for gr in THList:
                    num_y = ROOT.Double(999) 
                    num_x = ROOT.Double(999) 

                    gr.GetPoint(bin_,num_x,num_y)
                    if bmin < num_y:
                        bmin = num_y
                    if bmax > num_y:
                        bmax = num_y

                MAXybins[bin_]  = bmax
                MINybins[bin_]  = bmin


            #print 'PRINTING ALL THE BINS'
            #print xbins   
            #print xbinsL  
            #print xbinsH  
            #print MAXybins
            #print MINybins
            #print ybinsL  
            #print ybinsH  

            #MAXybinsL = MAXybins 
            #MAXybinsH = MAXybins
            #MINybinsL = MINybins
            #MINybinsH = MINybins

            grlow   = ROOT.TGraphAsymmErrors(nbins, xbins, MINybins, xbinsL, xbinsH, ybinsL, ybinsH)
            grhigh  = ROOT.TGraphAsymmErrors(nbins, xbins, MAXybins, xbinsL, xbinsH, ybinsL, ybinsH)
            return [grlow, grhigh]

        #If list of TH1 (used in the ratio)
        else: 
            histo = THList[0]
            xaxis = histo.GetXaxis()
            nbins = histo.GetNbinsX()
            xbins = np.array([0 for i in range(0,nbins+1)],dtype=np.float64)
            for bin_ in range(0,nbins+1):
                xbins[bin_] = xaxis.GetBinLowEdge(bin_+1)

            hlow = ROOT.TH1F('hlow_%s'%name, 'hlow_%s'%name, nbins, xbins)
            hhigh = ROOT.TH1F('hhigh_%s'%name, 'hhigh_%s'%name, nbins, xbins)

            for i in range(1,nbins+1):
                bmin  = 99
                bmax  = -99
                for h in THList:
                    bc = h.GetBinContent(i)
                    if bc > bmax:
                        bmax = bc
                    if bc < bmin:
                        bmin = bc
                    hlow.SetBinContent(i, bmin)
                    hhigh.SetBinContent(i, bmax)
            return [hlow, hhigh]
                


    def PlotFit(self, eff):
        '''Plot and save fits for a given efficiency'''
        print 'we are here'
        #Start by creating directory if not existing
        #directory = self.CreateOutputFolder('%s/%s/%s'%('Plots/Fits',eff.type_.replace(' ',''),eff.name.replace('&','and'),))
        directory = self.FormatOutputPath('%s/%s/%s'%('Plots/Fits',eff.type_,eff.name))
        directory = self.CreateOutputFolder(directory)


        # fit diagnostics in a different subdirectory 
        directoryDiag = self.FormatOutputPath('%s/%s/%s'%('Plots/FitDiagnostic',eff.type_,eff.name))
        directoryDiag = self.CreateOutputFolder(directoryDiag)


        directories = {}

        directories['Good'] = self.FormatOutputPath('%s/%s/%s/%s'%('Plots/FitDiagnostic',eff.type_,eff.name,'Good'))
        directories['Good'] = self.CreateOutputFolder(directories['Good'])
        directories['Med']  = self.FormatOutputPath('%s/%s/%s/%s'%('Plots/FitDiagnostic',eff.type_,eff.name,'Med'))
        directories['Med']  = self.CreateOutputFolder(directories['Med'])
        directories['Bad']  = self.FormatOutputPath('%s/%s/%s/%s'%('Plots/FitDiagnostic',eff.type_,eff.name,'Bad'))
        directories['Bad']  = self.CreateOutputFolder(directories['Bad'])

        print 'eff.hpassing is', eff.hpassing
        print 'eff.funcpassing is', eff.funcpassing
        print 'eff.hfail is', eff.hfailing
        print 'eff.funcfail is', eff.funcfailing
        print 'eff.rooworksp is', eff.rooworksp     
        nbin = 0 
        if eff.hpassing:
            print 'len is', len(zip(eff.hpassing, eff.funcpassing, eff.hfailing, eff.funcfailing))

        for w in eff.rooworksp:
            if not w: continue
            nbin += 1
            mass = w.var('mass')
            data = w.data('data')

            results = {}
            # KS_pf      = []
            # AD_pf      = []
            # maxPull_pf = []
            # chi_pf     = []
            # sFactor_pf = []
            


            for ty in ['Pass','Fail']:
                frame   = mass.frame()
                redData = data.reduce(ROOT.RooArgSet(mass), "_efficiencyCategory_==%d"%(1 if ty == 'Pass' else 0))
                redData.Print()
                hist = ROOT.RooAbsData.createHistogram(redData, ty+'Hist',mass)

                pdf     = w.pdf('pdf'+ty)
                redData.plotOn(frame)
                pdf    .plotOn(frame)
                
                pullHist = frame.pullHist()
                hPullHist=ROOT.TGraph(pullHist)
                
                resHist  = frame.residHist()
                hResHist = ROOT.TGraph(resHist)

                x = ROOT.Double(0); y = ROOT.Double(0)
                x2 = ROOT.Double(0); y2 = ROOT.Double(0)
                ys = []
                ys2= []

                sumRes   = 0
                integral = 0

                for i in range(1, pullHist.GetN()+1):
                    pullHist.GetPoint(i, x, y)
                    resHist.GetPoint(i,x2,y2)
                    sumRes = sumRes + abs(y2)
                    integral = integral + hist.GetBinContent(i)
                    ys.append(ROOT.Double(y))
                    ys2.append(0 if not hist.GetBinContent(i) else ROOT.Double(y)/math.sqrt(hist.GetBinContent(i)))

                

                c = ROOT.TCanvas('c','c')
                c.cd()
                frame.Draw()

                pullFrame = mass.frame()
                pullFrame.addPlotable(pullHist)


                maxPull = max(ys)
                minPull = min(ys)

                sFactor = frame.chiSquare() / math.sqrt(data.numEntries()) #sumRes / integral

                maxPull = max(map(abs, [maxPull,minPull]))
                

                KS=ROOT.EvaluateADDistance(pdf, redData, mass, True)
                AD=ROOT.EvaluateADDistance(pdf, redData, mass, False)

                # model = ROOT.RooStats.ModelConfig()
                # model.SetPdf(pdf)
                # calculator = ROOT.RooStats.AsymptoticCalculator(data, model, model)
                

                # KS = ROOT.Double(0.)
                # AD = ROOT.Double(0.)
                
                # ROOT.KSandADWithToys(KS, AD, redData, pdf, mass)
                

                # check whether the tnp is on Z or J/psi
                latPosition = 110 if frame.GetXaxis().GetXmax() > 10 else 3.15
                
                tl1 = ROOT.TLatex(latPosition,0.10*frame.GetMaximum(), '#chi^{2}/ndof = %4.2f'%frame.chiSquare())
                tl2 = ROOT.TLatex(latPosition,0.15*frame.GetMaximum(), 'maxPull = %4.2f'%maxPull )
                tl3 = ROOT.TLatex(latPosition,0.20*frame.GetMaximum(), 'KS = %4.2f'%(KS*math.sqrt(data.numEntries())))
                tl4 = ROOT.TLatex(latPosition,0.25*frame.GetMaximum(), 'AD = %4.2f'%AD )
                tl5 = ROOT.TLatex(latPosition,0.30*frame.GetMaximum(), 'S-factor = %4.3f'%sFactor )
                
                result = { 'KS'     : KS*math.sqrt(data.numEntries()),
                           'AD'     : AD,
                           'maxPull': maxPull,
                           'chi2'   : frame.chiSquare(),
                           'sFactor': sFactor 
                           }

                results[ty] = result

                # KS_pf     .append(KS*math.sqrt(data.numEntries()))     
                # AD_pf     .append(AD                             )                                  
                # maxPull_pf.append(maxPull                        )
                # chi_pf    .append(frame.chiSquare()              )
                # sFactor_pf.append(sFactor                        )

                tl1.Draw('same')
                tl2.Draw('same')
                tl3.Draw('same')
                tl4.Draw('same')
                tl5.Draw('same')

                c.SaveAs(directory+'/%s_%i.pdf' %(ty, nbin))
                c.SaveAs(directory+'/%s_%i.png' %(ty, nbin))
                c.SaveAs(directory+'/%s_%i.root'%(ty, nbin))

                c.IsA().Destructor(c)
                hist.IsA().Destructor(hist)


            # move fits to the diagnostic folders :D
            print type(results)
            print results
            diagLabel= FitDiagnostics.FitDiagnostics(results)

            for ty in 'Pass,Fail'.split(','):
                for ext in 'root,png,pdf'.split(','):
                    os.system('cp %s %s'%(directory+'/%s_%i.%s'%(ty,nbin,ext), directories[diagLabel]))
                
            # self.KSs     .append(max(KS_pf))
            # self.ADs     .append(max(AD_pf))
            # self.maxPulls.append(max(maxPull_pf))
            # self.chi2s   .append(max(chi_pf))
            # self.sFactors.append(max(sFactor_pf))

#         for hp, fp, hf, ff, w in zip(eff.hpassing, eff.funcpassing, eff.hfailing, eff.funcfailing, eff.rooworksp):
#             nbin += 1
#             print 'nbin is', nbin
#             mass = w.var('mass')
#             data = w.data('data')     

#             framePass = mass.frame()
#             frameFail = mass.frame()

#             #Draw passing
#             c = ROOT.TCanvas('c','c')
#             c.cd()
#             hp.Draw()
#             fp.Draw('same')
            
#             dataPass=data.reduce(ROOT.RooArgSet(mass), "_efficiencyCategory_==1")
#             pdfPass =w.pdf('pdfPass')
#             dataPass.plotOn(framePass)
#             pdfPass.plotOn(framePass)
#             print hp

#             maxPull = max( map( abs, [framePass.pullHist().GetMaximum(),framePass.pullHist().GetMinimum()]))
#             print maxPull
#             print hp.getYAxisMax()
# #            tl = ROOT.TLatex(110,0.1*hp.getYAxisMax(), '#chi^{2}/4 = %4.2f'%fp.chiSquare(hp,4))
#             tl = ROOT.TLatex(110,0.1*hp.getYAxisMax(), '#chi^{2}/ndof = %4.2f'%framePass.chiSquare())

#             print 0.1*hp.getYAxisMax()
#             tl = ROOT.TLatex(110,0.1*hp.getYAxisMax(), 'maxPull = %4.2f'%maxPull)
#             print '#chi^{2}/4 = %4.2f'%fp.chiSquare(hp,4)
#             tl.Draw('same')
#             c.SaveAs(directory+'/pass_%i.pdf'%nbin)
#             c.SaveAs(directory+'/pass_%i.png'%nbin)
#             c.SaveAs(directory+'/pass_%i.root'%nbin)


#             framePull = mass.frame()
#             pull = framePass.pullHist()
#             framePull.addPlotable(pull,'P')

            
#             c2 = ROOT.TCanvas('c2','c2')
#             framePull.Draw()
#             c2.SaveAs(directory+'/pass_pull%i.png'%nbin)
#             print 'maximum and minimum are', 
#             for i in pull.GetX(): print i,

#             #Draw failing
#             c = ROOT.TCanvas('c','c')
#             c.cd()
#             hf.Draw()
#             ff.Draw('same')
#             dataFail=data.reduce(ROOT.RooArgSet(mass), "_efficiencyCategory_==0")
#             pdfFail = w.pdf('pdfFail')
#             dataFail.plotOn(frameFail)
#             pdfFail .plotOn(frameFail)
# #            tl = ROOT.TLatex(110,0.1*hf.getYAxisMax(), '#chi^{2}/4 = %4.2f'%ff.chiSquare(hf,4))
#             pull = frameFail.pullHist()
#             mn = ROOT.TMath.LocMin( pull.GetN(), pull.GetX())
#             mx = ROOT.TMath.LocMax( pull.GetN(), pull.GetX())

#             print 'maximum and minimum are', mn, mx, pull.GetN()
#             for i in pull.GetX(): print i,


#             maxPull = max( map( lambda x : abs(pull.GetX()[x]), [mn, mx] ))
#             tl = ROOT.TLatex(110,0.1*hf.getYAxisMax(), '#chi^{2}/ndof = %4.2f'%frameFail.chiSquare())
#             tl = ROOT.TLatex(110,0.2*hf.getYAxisMax(), 'maxPull = %4.2f'%maxPull)
#             print '#chi^{2}/4 = %4.2f'%ff.chiSquare(hf,4)
#             tl.Draw('same')
#             c.SaveAs(directory+'/fail_%i.pdf'%nbin)
#             c.SaveAs(directory+'/fail_%i.png'%nbin)
#             c.SaveAs(directory+'/fail_%i.root'%nbin)
#             print kk
    def PlotFitList(self, effList):
        '''Plot and save fits for a list of efficiencies'''
        print 'efflist is', effList
        for eff in effList:
            self.PlotFit(eff)

    def CheckFit(self, eff):
        '''Plot and save fits for a given efficiency'''

        #Start by creating directory if not existing
        #directory = self.CreateOutputFolder('%s/%s/%s'%('Plots/Fits',eff.type_.replace(' ',''),eff.name.replace('&','and'),))
        directory = self.FormatOutputPath('%s/%s/%s'%('Plots/Fits',eff.type_,eff.name))
        directory = self.CreateOutputFolder(directory)

        print 'eff.hpassing is', eff.hpassing
        print 'eff.funcpassing is', eff.funcpassing
        print 'eff.hfail is', eff.hfailing
        print 'eff.funcfail is', eff.funcfailing

        #print 'chi2', eff.funcfailing.chiSquare(eff.hfailing,4)
        #print 'chi2', eff.funcpassing.chiSquare(eff.hpassing,4)


    def CheckFitList(self, effList):
        '''Check if the fits are good enough (with several methods (to be built))'''
        for eff in effList:
            self.CheckFit(eff)

    def SetPadParemeter(self, h, s = 'up'):
        '''Set some style parameters for up/down pad. Used in PlotEff1D'''

        if s == 'up':
            h.SetMarkerStyle(22)
            h.SetMarkerColor(1)
            h.SetLineWidth(2)
            h.GetYaxis().SetTitle("Effciency")
            h.GetYaxis().SetRangeUser(self.effDownRange, self.effUpRange)
            h.GetYaxis().SetTitleSize(27)
            h.GetYaxis().SetTitleFont(63)
            h.GetYaxis().SetLabelFont(43)
            h.SetMarkerStyle(20)
            h.GetYaxis().SetLabelSize(20)
            h.GetYaxis().SetTitleOffset(1.5)
            h.GetXaxis().SetTitleSize(27)
            h.GetXaxis().SetLabelSize(20)
            h.GetXaxis().SetTitleFont(63)
            h.GetXaxis().SetTitleSize(27)
            h.GetXaxis().SetLabelFont(43)
        elif s == 'down':
            h.SetTitle("")
            #h.SetLineWidth(2)
            #h.SetLineColor(1)
            #h.SetMarkerStyle(20)
            #h.SetMarkerColor(1)
            h.GetYaxis().SetRangeUser(self.ratioDownRange, self.ratioUpRange)
            #h.GetYaxis().SetRangeUser(0.85,1.15)
            h.GetYaxis().SetTitle("DATA/MC")
            h.GetYaxis().SetNdivisions(505)
            h.GetYaxis().SetLabelSize(20)
            h.GetYaxis().SetTitleFont(63)
            h.GetYaxis().SetTitleOffset(1.5)
            h.GetYaxis().SetLabelFont(43)
            h.GetYaxis().SetTitleSize(27)
            h.GetXaxis().SetTitleSize(27)
            h.GetXaxis().SetLabelSize(20)
            h.GetXaxis().SetTitleFont(63)
            h.GetXaxis().SetTitleSize(27)
            h.GetXaxis().SetTitleOffset(3)
            h.GetXaxis().SetLabelFont(43)

    def SetHistoStyle(self, h, index):
        '''Modify color and style of the plot'''
        color = [4, 2, 6, 9, 50, 40, 30, 95, 51]
        marker= [22, 23, 21, 33, 24, 26, 27, 36]

        h.SetMarkerStyle(marker[index])
        h.SetMarkerColor(color[index])
        h.SetLineColor(color[index])
        h.SetLineWidth(2)
        
    def MakeLegend(self, ht, option = None):
        '''Make legend of a specifique hr'''
        #print 'ht.Type is', ht.Type
        if ht.Type == None:
            return None

        #if ht.Type == 'data': return 'DATA'
        #if ht.Type == 'MC': return 'MC'

        Info = ht.Info
        if option:
            Info = option

        if ht.Type == 'data':
            if ht.Info:
                return '%s %s' %('DATA', Info)
            else: 
                return 'DATA'
        if ht.Type == 'mc':
            if ht.Info:
                return '%s %s' %('MC', Info)
            else:
                return 'MC'
        else:
            return ht.Type
        #sys.exit()


    def PlotEff1D(self, hrList):
        '''Plot 1D efficiency distributions. Here effList is a container of efficiency lists. Each list should correspond to another sample. e.g. effList[0] a list of data efficiency, effList[1] a list of MC1 efficiency,  effList[2] a list of MC2 efficiency. All efficiencies will be ploted on the same canvas. The first list i.e. effList[0] will be used as reference in the ratio plot'''

        ROOT.setTDRStyle()
        if len(hrList[0].EffList) == 0: return

        effFolder = hrList[0].EffList[0].type_
        for hr in hrList[1:]:
            effFolder+= '_AND_%s'%hr.EffList[0].type_
        print '#######', effFolder
        effFolder = self.FormatOutputPath(effFolder)
        directory = self.CreateOutputFolder('%s/%s'%('Plots/Efficiency',effFolder))

        cDict = {} #Dictionnary of canvas
        effDict = {} #Store "Nominal efficiencies". Used to compute ratio

        theffDic = {}
        if len(hrList) == 1:
            for hr in hrList[0]:
                eff =  hr.EffList
                if not eff.heff: continue
                effname = eff.name
                c = ROOT.TCanvas('c_%s'%effname,'c_%s'%effname)

                theff = self.TGraph2TH1F(eff.heff)
                effDict[effname] = theff
                theff.GetYaxis().SetRangeUser( self.effDownRange, self.effUpRange)
                theff.SetLineColor(color_list[0])
                theff.SetLineStyle(linestyle_list[0])
                theff.SetMarkerStyle(markerstyle_list[0])
                theff.SetMarkerColor(color_list[0])
                theff.SetMarkerSize(20)
                theff.SetLineWidth(2)

                #if len(hrList) == 1:#no ratio needed if only one efficiency
                c.cd()
                theff.SetLineWidth(2)
                theff.DrawCopy()
                #eff.heff.Draw()
                cDict[effname] =  c
                print 'list len is 1'
                #sys.exit()

        elif hrList > 1:
            #Store all the efficiencies grouped by name. The first one is the one that defined the num of all the ratios
            theffDic = {}
            theratioDic = {}
            theXparDic = {}
            theYparDic = {}
            thelegendList = []
            numtext = self.selDic(hrList[0].Num)
            dentext = self.selDic(hrList[0].Den)
            lumientry = ''
            #For min and max
            theffDicMinMax = {}
            theratioDicMinMax = {}

            print '--------------'
            print 'hrList is', hrList
            for hr in hrList: 
                print 'hr is', hr
                effL = hr.EffList
                print 'yeah baby'

                if hr.Type == 'data':
                    if lumientry == '':
                        lumientry = 'Run'
                    if hr.Info:
                        lumientry += ' %s'%hr.Info

                #make legend
                legentry =  self.MakeLegend(hr)
                thelegendList.append(legentry)

                print 'effL is', effL
                for eff in effL:

                    effname = eff.name

                    print 'effname is',effname
                    #print 'theffDic is', theffDic
                    if not effname in theffDic:
                        theffDic[effname] = []
                        theratioDic[effname] = []
                        theXparDic[effname] = []
                        theYparDic[effname] = []

                    theff = eff.heff
                    theffDic[effname].append(theff)
                    theXparDic[effname] = eff.xpar
                    theYparDic[effname] = eff.ypar
                    print 'theffDic[effname]', theffDic[effname]

                    #Compute ratio
                    if len(theffDic[effname]) > 1:
                        print 'I AM GOING TO COMPUTE THE RATIO'
                        ratio = copy.copy(self.TGraph2TH1F(theffDic[effname][0])) 
                        den = copy.copy(self.TGraph2TH1F(theffDic[effname][-1]))
                        ratio.Divide(den)
                        theratioDic[effname].append(ratio) 
                        del den

                ##Compute the maximal up/down variations for the ratio and the efficiency
            #num_ = 0
            if self.MinMax == True:
                for hr in hrList: 
                    effL = hr.EffList
                    #make legend
                    thelegendList = [self.MakeLegend(hr, 'nominal'), self.MakeLegend(hr, 'down'), self.MakeLegend(hr, 'up')]

                    for eff in effL:
                        effname = eff.name
                        #UpDownEff = self.GetMinMaxTH1F(theffDic[effname],'%s_%i'%(effname,num_))
                        #UpDownRatio = self.GetMinMaxTH1F(theratioDic[effname],'%s_%i'%(effname,num_))
                        #theffDicMinMax[effname] = [copy.copy(theffDic[effname][0]), copy.copy(UpDownEff[0]), copy.copy(UpDownEff[1])]
                        #theratioDicMinMax[effname] = [copy.copy(UpDownRatio[0]), copy.copy(UpDownRatio[1])]
                        UpDownEff = self.GetMinMaxTH1F(theffDic[effname])
                        UpDownRatio = self.GetMinMaxTH1F(theratioDic[effname])
                        theffDicMinMax[effname] = [copy.copy(theffDic[effname][0]), copy.copy(UpDownEff[0]), copy.copy(UpDownEff[1])]
                        theratioDicMinMax[effname] = [copy.copy(UpDownRatio[0]), copy.copy(UpDownRatio[1])]
                #        num_ += 1

                theffDic = theffDicMinMax
                theratioDic = theratioDicMinMax

            for key in theffDic.keys():

                   c = ROOT.TCanvas('c_%s'%key,'c_%s'%key)

                   t = ROOT.TPad('t_%s'%effname,'t_%s'%effname, 0, 0.3, 1, 1.0)#top pad
                   t.SetBottomMargin(0.)
                   t.SetTopMargin(0.1)
                   t.Draw()
                   t.cd()

                   theffDic[key][0].Draw('AP')
                   print 'theratioDic',theratioDic
                   print 'the key is', key
                   xaxis = theratioDic[key][0].GetXaxis()
                   theffDic[key][0].GetXaxis().SetRangeUser(xaxis.GetBinLowEdge(1),xaxis.GetBinLowEdge(xaxis.GetNbins()+1))
                   self.SetPadParemeter(theffDic[key][0], 'up')


                   #Legend
                   leg = ROOT.TLegend(0.4, 0.65, 0.75 , 0.79)
                   headtext = ''
                   ypartext = ''
                   if dentext != '':
                       dentext = '%s'%dentext 
                   if theYparDic[key]:
                       ypartext = self.yParDic(theYparDic[key])
                       headtext = '%s/%s, %s'%(numtext, dentext, ypartext)
                   else:
                       headtext = '%s/%s'%(numtext, dentext)

                   theffDic[key][0].SetTitle(headtext)

                   latex = ROOT.TLatex()
                   latex.SetNDC()
                   latex.SetTextAngle(0)
                   latex.SetTextColor(ROOT.kBlack)
                   latex.SetTextFont(43)
                   latex.SetTextAlign(11)
                   latex.SetTextSize(20)
                   latex.DrawLatex(0.4,0.81, headtext)

                   leg.SetBorderSize(0)

                   #print thelegendList
                   if thelegendList[0]: leg.AddEntry(theffDic[key][0], str(thelegendList[0]),'LP')
           
                   index = 0
                   for effL in theffDic[key][1:]:
                       #print 'legentry is', thelegendList[index]
                       self.SetHistoStyle(effL, index)
                       index += 1
                       if thelegendList[index]: leg.AddEntry(effL, thelegendList[index],'LP')
                       effL.Draw('P')


                   if index == 2:#For "standard" data/MC plots (nice big font)
                       leg.SetTextFont(43)
                       leg.SetTextSize(20)
                   leg.Draw()

                   c.cd()
                   b = ROOT.TPad('b_%s'%effname,'b_%s'%effname, 0, 0., 1, 0.3)#bottom pad
                   b.SetTopMargin(0.0)
                   b.SetBottomMargin(0.35)
                   b.SetGridy()
                   b.Draw()
                   b.cd()

                   theratioDic[key][0].Draw()
                   self.SetHistoStyle(theratioDic[key][0],0)
                   self.SetPadParemeter(theratioDic[key][0], 'down')
                   theratioDic[key][0].GetXaxis().SetTitle(self.xParDic(theXparDic[key]))
                   index = 1
                   for rL in theratioDic[key][1:]:
                       rL.Draw('SAME')
                       self.SetHistoStyle(rL, index)
                       index += 1

                   ROOT.CMS_lumi(t, lumientry+'(13 TeV)', 11);
                   c.Update()

                   c.SaveAs(self.FormatOutputPath('%s/NUM_%s_DEN_%s_PAR_%s.pdf' %(directory,hrList[0].Num, hrList[0].Den, key)))
                   c.SaveAs(self.FormatOutputPath('%s/NUM_%s_DEN_%s_PAR_%s.png' %(directory,hrList[0].Num, hrList[0].Den,key)))
                   c.SaveAs(self.FormatOutputPath('%s/NUM_%s_DEN_%s_PAR_%s.root' %(directory,hrList[0].Num, hrList[0].Den,key)))


##############
#All dictionnaries to make the plots
##############



    def xParDic(self, par):
        '''Maps x parameter to propet latex expression (for plots)'''
        dic = {'pt':'muon p_{T} [GeV]','pair_newTuneP_probe_pt':'muon tune p_{T}','tag_pt':'muon 2 p_{T}'}
        return dic[par]

    def yParDic(self, par):
        dic = {
                'abseta_bin0':'#||{#eta} #leq 0.9',
                'abseta_bin1':'0.9 #leq #||{#eta} #leq 1.2',
                'abseta_bin2':'1.2 #leq #||{#eta} #leq 2.1',
                'abseta_bin3':'2.1 #leq #||{#eta} #leq 2.4'}

        return dic[par]

    def selDic(self, num):
        dic = {'MediumID':'Medium Id',
                'MediumPromptID':'Medium Id prompt',
                'LooseID':'Loose Id',
                'HighPtID':'High p_{T} Id',
                'HighPtIDandIPCut':'High p_{T} Id',
                'TrkHighPtID':'Tracker High p_{T} Id',
                'SoftID':'Soft Id',
                'TightID':'Tight Id', 
                'TightIDandIPCut':'Tight Id',
                'TightRelIso':'Tight Iso',
                'LooseRelIso':'Loose Iso',
                'TightRelTkIso':'Tight Trk Iso',
                'LooseRelTkIso':'Loose Trk Iso',
                'TightIso4':'Tight Iso',
                'UltraTightIso4':'Rel. Iso < 0.06',
                'IsoMu27':'IsoMu27',
                'hlt_Mu17Mu8_leg17':'IsoMu17',
                'LooseIDnISO':'Loose ID+ISO',
                'hlt_Mu17Mu8_leg8':'leg 8',
                'hlt_Mu17Mu8_leg8_tag17':'leg 8',
                'hlt_Mu17Mu8_leg17':'leg 17',
                'hlt_Mu17Mu8_leg17_tag8':'leg 17',
                'dZ':'dZ',
                'genTracks':'',
                'empty':''
                }

        print 'num is', num
        return dic[num]
