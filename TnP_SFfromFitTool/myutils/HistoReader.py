import ROOT
#from collections import Counter
import sys
from Efficiency import Efficiency
from Eff2DMap import Eff2DMap



class HistoReader:
    '''Contains a list of efficiency class'''

    def __init__(self, type_):
        #choose type to indentify the data/sample. e.g.: type = '2016 RunB', type = 'MC 92X'. Will be used for directory names and legends
        self.type_ = type_
        self.rooworksp = []
        self.fitResult = []
        #obtain information about numerator and denominator
        self.Num = ''
        self.Den = ''
        self.Type = None#can be data or mc
        self.Info= None#in case of data, can give addtional information
        self.ypar = None
        #Name of the x and y parameter. Used for the Json
        self.yparname = None
        self.xparname = None

        #Member below only relevent for 2D efficiencies       
        self.ylist = None #Array containing bins of secondary parameter. For 2D efficiency only
        self.eff2D = None #Map containing 2D efficicies
        pass

    def readfile(self, inputTree):
        #List of all efficiencies
        self.EffList = []
        file = ROOT.TFile.Open(inputTree)
        #Get Den and Num info
        self.Den= inputTree.split('_DEN_')[-1].split('_PAR_')[0]
        self.Num= inputTree.split('_DEN_')[0].split('_NUM_')[-1]


        rootoutput = file.GetDirectory('tpTree')
        nextkey = ROOT.TIter(rootoutput.GetListOfKeys())
        key = nextkey.Next()
        while (key): #loop
            if key.IsFolder() != 1:
                continue
            self.rawname = key.GetTitle()

            directory = rootoutput.GetDirectory(key.GetTitle())
            effdir = directory.GetDirectory('fit_eff_plots')
            if effdir:
                effList = effdir.GetListOfKeys()
                effKey = ROOT.TIter(effList)
                effkey = effKey.Next()
            else:
                print 'fit_eff_plots is not in the file'
                effkey = False
            AllEffList = []

            #Contain the list of bins
            xlist= None
            ylist= None 
            while (effkey):
                eff_ = effdir.Get(effkey.GetName()).GetListOfPrimitives()
                #Check if TH2D in list of primitive
                primIter = ROOT.TIter(eff_)
                prim = primIter.Next()

                isTH2F = False
                while (prim):
                    if prim.ClassName() == 'TH2F':
                        isTH2F = True 
                        xylist = self.getXYAxis(effdir.Get(effkey.GetName()).GetPrimitive(prim.GetName()))
                        xlist, ylist = xylist[0], xylist[1]
                        break
                    prim = primIter.Next()

                if not isTH2F: AllEffList.append(effkey.GetName())
                effkey = effKey.Next()
            self.EffRemover(AllEffList)

            for effkey in AllEffList:
                if not effkey.startswith(self.xpar+'_PLOT'):
                    continue

                cEff = effdir.Get(effkey)#TCanvas containing efficiency distribution
                hEff = cEff.GetPrimitive('hxy_fit_eff')

                ########
                #Only for 2D efficiencies
                #Check what is the xpar and what is the ypar (to fill the range)
                #print 'xlist',xlist
                #print 'ylist',ylist
                if xlist != None or ylist != None:
                    #print 'hEff.GetN()+1', hEff.GetN()+1
                    #print 'len(xlist)', len(xlist)
                    #print 'len(ylist)', len(ylist)
                    #a = hEff.GetXaxis()
                    #print 'number axis bins', a.GetNbins()
                    #print self.getGraphValue(hEff)[0]
                    #print xlist
                    #print self.contained(self.getGraphValue(hEff)[0], xlist)
                    #for i in range(0,a.GetNbins()):
                    #    print 'low'
                    #    print  a.GetBinLowEdge(i)
                    #    print 'center'
                    #    print a.GetBinCenter(i)

                    # the contained part is necessary in case some of the bins are empty (due to missing stats)
                    if hEff.GetN()+1 == len(xlist) or self.contained(self.getGraphValue(hEff)[0], xlist):
                        self.ylist = ylist
                    elif hEff.GetN()+1 == len(ylist) or self.contained(self.getGraphValue(hEff)[0], xlist):
                        self.ylist = xlist
                    else:
                        print '@ERROR: The bin parameters have not been retrived properly. Aborting'

                #print self.ylist

                ###
                #Write info about yparams bins
                yParBinInfo = effkey.split('PLOT')[1]
                yBinList = []
                for y in self.ypars:
                    if '%s_bin' %y in yParBinInfo:
                        yBin = int(yParBinInfo.split('%s_bin' %y)[1].split('_')[0])
                        yBinList.append('%s_bin%i' %(y,yBin))
                ####################
                #Add fit info
                ####################
                keyInDir = ROOT.TIter(directory.GetListOfKeys())
                subkey = keyInDir.Next()

                #Dictonary containing all fits. The key correspond to the bin number
                self.fitDic = {}
                while (subkey):
                    if subkey.IsFolder() != 1:
                        subkey = keyInDir.Next()
                        continue
                    if subkey.GetName() == 'fitter_tree' or subkey.GetName() == 'fit_eff_plots' or subkey.GetName() == 'cnt_eff_plots':
                        subkey = keyInDir.Next()
                        continue

                    yBinNotFound = False 
                    for yBin in yBinList:
                        if not yBin in subkey.GetName():
                            yBinNotFound = True
                        else: 
                            self.ypar = yBin

                    if yBinNotFound: 
                        subkey = keyInDir.Next()
                        continue
                  
                    xBin = int(subkey.GetName().split('%s_bin' %self.xpar)[1].split('_')[0])

                    ########
                    #Retrieve fit plots
                    ########
                    canvDir = rootoutput.GetDirectory(key.GetTitle()+"/"+subkey.GetName())
                    canv = canvDir.Get('fit_canvas')
                    if not canv:
                        print '%s has not been created. Fit is empty (probably due to low stats'%(key.GetTitle()+"/"+subkey.GetName())
                    
                    if canv:
                        self.fitResult.append(canvDir.Get('fitresults'))
                        self.rooworksp.append(canvDir.Get('w'))

                    nbin = self.getBinNumber(subkey.GetName())
                    if canv:
                        self.histoFromCanvas(canv, xBin)

                    del canv
                    
                    ###########

                       #subkey = keyInDir.Next()
                    if "ratio" in subkey.GetName():
                        theHistoPlot = rootoutput.Get(key.GetTitle()+"/"+subkey.GetName())
                    subkey = keyInDir.Next()
                    
                    #################
                    ##Handle plot bin
                    #################
                    ##BinName = subkey.GetName()
                self.orderFitHisto()
                print '-----------'
                print 'checking efficiency bins'
                self.getGraphValue(hEff)
                self.EffList.append(Efficiency(self.rawname, self.type_,  effkey, hEff, self.xpar, self.ypars, self.ypar, self.hpassing, self.funcpassing, self.hfailing, self.funcfailing, self.fitResult, self.rooworksp))
            if len(AllEffList) == 0:
                # try at least to recover the workspaces
                for subkey in directory.GetListOfKeys():
                    if not subkey.IsFolder(): continue
                    #print subkey.GetName()
                    subdir =  subkey.ReadObj()
                    canv=subdir.Get('fit_canvas')
                    self.fitResult.append(subdir.Get('fitresults'))
                    worksp = subdir.Get('w') if subdir.Get('w') else subdir.Get('')
                    for key2 in subdir.GetListOfKeys():
                        if (key2.InheritsFrom('RooWorkspace')): worksp = key2.ReadObj()
                    self.rooworksp.append(worksp)
                    print 'rooworkspace', subdir.Get('w')
                        
                    self.EffList.append(Efficiency(self.rawname, self.type_,  effkey, None, None, None, None, None, None, None, self.fitResult, self.rooworksp))

            key = nextkey.Next()

        #Make 2D map to store the efficiency
        if not self.ylist == None:
            self.Make2DMap()
        file.Close()

    def getBinNumber(self, s):
        binlist = []
        binStringList = s.split('bin')[1:]
        for b in binStringList:
            sbin = b.split('__')[0]
            try:
                nbin =int(sbin)
            except ValueError: 
                print '@ERROR: the nbin is not a string. Aborting'
            binlist.append(nbin)

        return nbin

    def EffRemover(self, AllEffList):
        '''When making 2D efficiencies (e.g. pt X eta), all permutation are stored in the .root file. Here only one set of efficiency is keep. The selection criteria is: efficiencies are ploted wrt the  parameter with the largerst number of bins '''
        keyPrefixList = []
        #print 'AllEffList is', AllEffList
        for key in AllEffList:
            keyPrefix = key.split('_PLOT')[0]
            keyPrefixList.append(keyPrefix)

        #print 'keyPrefixList is', keyPrefixList
        if len(keyPrefixList) > 0:
            self.xpar  = min(set(keyPrefixList), key=keyPrefixList.count)
            self.ypars = set(keyPrefixList)
            self.ypars.remove(self.xpar)
        else: 
            self.xpar = 0 
            self.ypars = []
        #print 'self.ypars are', self.ypars
        if len(self.ypars) > 0:
            self.yparname = list(self.ypars)[0]
        self.xparname = self.xpar

    def IsCurrentXparam(self, xpar, BinName):
        pass
    



    def histoFromCanvas(self, canvas, xbin):
        '''Read canvas containing passing, failing, passing+failing probe and fit function. Retrieve info and store them in Efficiency'''


        fitList = []
        for i in range(1,3):
            pad = canvas.GetPad(i)
            primList = pad.GetListOfPrimitives()
            primKey = ROOT.TIter(primList)
            prim = primKey.Next()

            hist = pad.GetPrimitive('h_data_binned')
            if i == 1:#passing muon
                fitfunc = pad.GetPrimitive('pdfPass_Norm[mass]')
            elif i == 2: 
                fitfunc = pad.GetPrimitive('pdfFail_Norm[mass]')
            fitList.append(hist)
            fitList.append(fitfunc)
        self.fitDic[xbin] = fitList
        pass

    def orderFitHisto(self):
        binlist = sorted(list(self.fitDic))
        self.hpassing = []
        self.funcpassing = []
        self.hfailing = []
        self.funcfailing = []
        for nbin in binlist:
            self.hpassing.append(self.fitDic[nbin][0])
            self.funcpassing.append(self.fitDic[nbin][1])
            self.hfailing.append(self.fitDic[nbin][2])
            self.funcfailing.append(self.fitDic[nbin][3])

    def SetNewRange(self, xmin, xmax):
        '''Clear the distributions and fit histograms within the a certain range'''

        for eff in self.EffList:
            eff.SetNewRange(xmin, xmax)

        #Redo 2D map to store the efficiency
        if not self.ylist == None:
            self.Make2DMap()

    def CleanBigError(self, threshold):

        for eff in self.EffList:
            eff.CleanBigError(threshold)

        #Redo 2D map to store the efficiency
        if not self.ylist == None:
            self.Make2DMap()

    def setLumi(self, lumi):
        for eff in self.EffList:
            eff.setLumi(lumi)

    def Sum(self, hr2):
        '''Sum of two Historeader. Results in one historeader that sums up both luminosity. All the efficiency distributions are summed by lumi'''
        for eff1 in self.EffList:
            for eff2 in hr2.EffList:
                if  eff1.name != eff2.name: continue
                eff1.SumEfficiency(eff2)

        #Add Run information (for legend)
        self.Info = self.Info + hr2.Info

        #Redo 2D map to store the efficiency
        if not self.ylist == None:
            self.Make2DMap()

    def Divide(self, hr2):
        '''Divide two Historeader. The historeader no longer stores efficiency but SF (in case of MC divided by data)'''
        for eff1 in self.EffList:
            for eff2 in hr2.EffList:
                if  eff1.name != eff2.name: continue
                eff1.DivideEfficiency(eff2)

    def DrawEfficiency(self):
        pass

    def setInfo(self, info):
        self.Info= info  

    def setType(self, t):        
        self.Type = t

    def getXYAxis(self, tg):
        '''Takes a 2D graphs and returns bins for the X axis and Y axis'''
        #Get X axis
        xa = tg.GetXaxis()
        ya = tg.GetYaxis()

        nx = tg.GetNbinsX()
        ny = tg.GetNbinsY()
        
        xlist = []
        ylist = []
        
        for x in range(1,nx+2):
            xlist.append(xa.GetBinLowEdge(x))

        for y in range(1, ny+2):
            ylist.append(ya.GetBinLowEdge(y))

        return [xlist, ylist]

    def Make2DMap(self):
        '''In case Histomaker contains a 2D efficiency, makes a map of the efficincy'''
        if self.ylist == None:
            print '@ERROR: ylist is None. This is not a 2D efficiency. Aborting'

        eff2D = Eff2DMap('NUM_%s_DEN_%s'%(self.Num, self.Den))

        #Fill the ybins
        eff2D.ybins = []
        for y0, y1 in zip(self.ylist[:-1],self.ylist[1:]):
            eff2D.ybins.append([y0,y1])

        ##Read 1D eff one by one to fill the 2D map
        # create x range. 
        xbins_ = []
        for eff in self.EffList:
            grVal = self.getGraphValue(eff.heff)
            #print 'grVal[0] is', grVal[0]
            #eff2D.nominal.append(grVal[1]) #adding ybins
            #eff2D.down.append(grVal[2]) #adding ybinsL
            #eff2D.up.append(grVal[3]) #adding ybinsH

            if eff == self.EffList[0]:
                xbins_ = grVal[0]
            # in case some of the x bins where missing (for example, empty pt bins), scan the other 1D distribution to recover missing x-bins
            else:
                for x in grVal[0]:
                    if not x in xbins_:
                        xbins_.append(x)

        eff2D.xbins = sorted(xbins_)

        print 'eff2D.xbins is', eff2D.xbins
        #sys.exit()
        #
        #eff2D.xbins = []
        for eff in self.EffList:
            # to fill the y bins in the map
            ybins = []
            ybinsL = []
            ybinsH = []

            grVal = self.getGraphValue(eff.heff)
            for xi in range(0, len(eff2D.xbins)):
                if eff2D.xbins[xi] in grVal[0]:
                    index = grVal[0].index(eff2D.xbins[xi])
                    if index >= len(grVal[0]) -1:
                        ybins.append(-1)
                        ybinsL.append(0)
                        ybinsH.append(0)
                    else: 
                    #print 'index is', index
                    #print 'grVal[1] is', grVal[1]
                        ybins.append(grVal[1][index])
                        ybinsL.append(grVal[2][index])
                        ybinsH.append(grVal[3][index])
                else: 
                    ybins.append(-1)
                    ybinsL.append(0)
                    ybinsH.append(0)

            eff2D.nominal.append(ybins) #adding ybins
            eff2D.down.append(ybinsL) #adding ybinsL
            eff2D.up.append(ybinsH) #adding ybinsH
            #eff2D.nominal.append(grVal[1]) #adding ybins
            #eff2D.down.append(grVal[2]) #adding ybinsL
            #eff2D.up.append(grVal[3]) #adding ybinsH

            #make xbins as pair (up, down)
        xbins_new = []
        for x0, x1 in zip(eff2D.xbins[:-1], eff2D.xbins[1:]):
            xbins_new.append([x0,x1])
        eff2D.xbins = xbins_new

        #xbins_new = []
        #for x0, x1 in zip(grVal[0][:-1],grVal[0][1:]):
        #    xbins_new.append([x0,x1])
        #if len(xbins_new) >= len(eff2D.xbins):
        #    eff2D.xbins = xbins_new

        print eff2D.xbins
        #sys.exit()

        #sys.exit()
        ##File parameter name
        eff2D.xname = self.xparname
        eff2D.yname = self.yparname
        #self.CleanMissingValues(eff2D)

        self.eff2D = eff2D

    #def CleanMissingValues(self, Map2D):
    #    '''In case the fit was empty in some particluar bins in a 2D map, replace those values by 0'''
    #    for y in range(0,len(Map2D.ybins)):
    #        for x in range(0,len(Map2D.xbins)):
    #            if len(Map2D.nominal[y]) <= x: 
    #                Map2D.nominal[y].append(-1)
    #                Map2D.down[y].append(-1)
    #                Map2D.up[y].append(-1)
    #    return Map2D
    #            #print 'will print all the bins'

    def getGraphValue(self, gr):
        '''Read TGraph and returns all values'''

        xbinsL = [] 
        ybins = [] 
        ybinsL = [] 
        ybinsH = [] 

        nbins = gr.GetN()
        bins = range(0,nbins)
        new_nbins = 0

        for bin_ in bins:
            x = ROOT.Double(999)
            y = ROOT.Double(999)
            gr.GetPoint(bin_,x,y)
            x_hi = gr.GetErrorXhigh(bin_)
            x_low = gr.GetErrorXlow(bin_)
            #print 'y is', y
            y_hi = gr.GetErrorYhigh(bin_)
            y_low = gr.GetErrorYlow(bin_)

            xbinsL.append(x - x_low)
            if bin_ == bins[-1]: 
                xbinsL.append(x + x_hi)
            ybins.append(y)
            ybinsL.append(y_low)
            ybinsH.append(y_hi)

            new_nbins += 1

        #print 'this is getGraphValue'
        #print xbinsL
        #print ybins
        #print ybinsL
        #print ybinsH

        return [xbinsL, ybins, ybinsL, ybinsH] 

    def contained(self, candidate, container):
        temp = container[:]
        try:
            for v in candidate:
                temp.remove(v)
            return True
        except ValueError:
            return False
        

if __name__ == "__main__":
    
    test_file = 'FitForTest/TnP_MC_NUM_hlt_Mu17_Mu8_OR_TkMu8_leg8_DEN_LooseIDnISO_PAR_pt_eta.root'

    hr = HistoReader()
    hr.readfile(test_file)
