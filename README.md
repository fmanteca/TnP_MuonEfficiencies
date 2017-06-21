# SKIMS:

#ID: 

#Different mass bin for ID / ISO efficiencies

#Data

./skimTree /eos/cms/store/group/phys_muon/hbrun/dataCommissioning/checkFirstData/TnPTree_Express_Run2017B_296966_to_297101.root  /eos/cms/store/group/phys_muon/fernanpe/checkFirstData/TnPTree_Express_Run2017B_296966_to_297101_skimmedID.root -r "all" -k "HighPt Medium PF TMOST Tight2012 Track_HP abseta combRelIsoPF04dBeta dB dzPV eta mass pair_newTuneP_mass pair_newTuneP_probe_pt pair_probeMultiplicity pt relTkIso tag_IsoMu24 tag_combRelIsoPF04dBeta tag_nVertices tag_pt tag_instLumi tkHitFract TM numberOfMatchedStations tkValidHits tkExpHitIn tkExpHitOut tkPixelLay tkTrackerLay weight" -c "((pt > 20 || pair_newTuneP_probe_pt >20) && mass > 70 && mass < 130.1  && tag_combRelIsoPF04dBeta < 0.2 && tag_combRelIsoPF04dBeta> -0.5 && tag_pt > 26 && tag_IsoMu24==1 && abseta <2.401 && pair_probeMultiplicity == 1)"


#MC:

./skimTree /eos/cms/store/group/phys_muon/hbrun/dataCommissioning/checkFirstData/MC_902_DY.root /eos/cms/store/group/phys_muon/fernanpe/checkFirstData/MC_902_DY_skimmedID.root -r "all" -k "HighPt Medium PF TMOST Tight2012 Track_HP abseta combRelIsoPF04dBeta dB dzPV eta mass pair_newTuneP_mass pair_newTuneP_probe_pt pair_probeMultiplicity pt relTkIso tag_IsoMu24 tag_combRelIsoPF04dBeta tag_nVertices tag_pt tag_instLumi tkHitFract TM numberOfMatchedStations tkValidHits tkExpHitIn tkExpHitOut tkPixelLay tkTrackerLay weight" -c "((pt > 20 || pair_newTuneP_probe_pt >20) && mass > 70 && mass < 130.1  && tag_combRelIsoPF04dBeta < 0.2 && tag_combRelIsoPF04dBeta> -0.5 && tag_pt > 26 && tag_IsoMu24==1 && abseta <2.401 && pair_probeMultiplicity == 1)"



#ISO:

#Data

./skimTree /eos/cms/store/group/phys_muon/hbrun/dataCommissioning/checkFirstData/TnPTree_Express_Run2017B_296966_to_297101.root  /eos/cms/store/group/phys_muon/fernanpe/checkFirstData/TnPTree_Express_Run2017B_296966_to_297101_skimmedISO.root -r "all" -k "HighPt Medium PF TMOST Tight2012 Track_HP abseta combRelIsoPF04dBeta dB dzPV eta mass pair_newTuneP_mass pair_newTuneP_probe_pt pair_probeMultiplicity pt relTkIso tag_IsoMu24 tag_combRelIsoPF04dBeta tag_nVertices tag_pt tag_instLumi tkHitFract TM numberOfMatchedStations tkValidHits tkExpHitIn tkExpHitOut tkPixelLay tkTrackerLay weight" -c "((pt > 20 || pair_newTuneP_probe_pt >20) && mass > 77 && mass < 130.1  && tag_combRelIsoPF04dBeta < 0.2 && tag_combRelIsoPF04dBeta> -0.5 && tag_pt > 26 && tag_IsoMu24==1 && abseta <2.401 && pair_probeMultiplicity == 1)"


#MC 

./skimTree /eos/cms/store/group/phys_muon/hbrun/dataCommissioning/checkFirstData/MC_902_DY.root /eos/cms/store/group/phys_muon/fernanpe/checkFirstData/MC_902_DY_skimmedISO.root -r "all" -k "HighPt Medium PF TMOST Tight2012 Track_HP abseta combRelIsoPF04dBeta dB dzPV eta mass pair_newTuneP_mass pair_newTuneP_probe_pt pair_probeMultiplicity pt relTkIso tag_IsoMu24 tag_combRelIsoPF04dBeta tag_nVertices tag_pt tag_instLumi tkHitFract TM numberOfMatchedStations tkValidHits tkExpHitIn tkExpHitOut tkPixelLay tkTrackerLay weight" -c "((pt > 20 || pair_newTuneP_probe_pt >20) && mass > 77 && mass < 130.1  && tag_combRelIsoPF04dBeta < 0.2 && tag_combRelIsoPF04dBeta> -0.5 && tag_pt > 26 && tag_IsoMu24==1 && abseta <2.401 && pair_probeMultiplicity == 1)"



# PU REWEIGHT

#./addNVtx “data” “mc” output.root

#ID:

./addNVtxWeight "/eos/cms/store/group/phys_muon/fernanpe/checkFirstData/TnPTree_Express_Run2017B_296966_to_297101_skimmedID.root" "/eos/cms/store/group/phys_muon/fernanpe/checkFirstData/MC_902_DY_skimmedID.root" /eos/cms/store/group/phys_muon/fernanpe/checkFirstData/MC_902_DY_skimmedID_weighted.root

#ISO:

./addNVtxWeight "/eos/cms/store/group/phys_muon/fernanpe/checkFirstData/TnPTree_Express_Run2017B_296966_to_297101_skimmedISO.root" "/eos/cms/store/group/phys_muon/fernanpe/checkFirstData/MC_902_DY_skimmedISO.root" /eos/cms/store/group/phys_muon/fernanpe/checkFirstData/MC_902_DY_skimmedISO_weighted.root



# Efficiencies ID

#Data:

cmsRun fitMuon2.py ID tightid gentrack data_all dataid pt default 2 > kk.txt

cmsRun fitMuon2.py ID tightid gentrack data_all dataid eta default 2 > kk.txt

cmsRun fitMuon2.py ID tightid gentrack data_all dataid vtx default 2 > kk.txt


cmsRun fitMuon2.py ID looseid gentrack data_all dataid pt default 2 > kk.txt

cmsRun fitMuon2.py ID looseid gentrack data_all dataid eta default 2 > kk.txt

cmsRun fitMuon2.py ID looseid gentrack data_all dataid vtx default 2 > kk.txt


cmsRun fitMuon2.py ID mediumid gentrack data_all dataid pt default 2 > kk.txt

cmsRun fitMuon2.py ID mediumid gentrack data_all dataid eta default 2 > kk.txt

cmsRun fitMuon2.py ID mediumid gentrack data_all dataid vtx default 2 > kk.txt




#MC: 

cmsRun fitMuon2.py ID tightid gentrack mc_all mcid pt default 2 > kk.txt

cmsRun fitMuon2.py ID tightid gentrack mc_all mcid eta default 2 > kk.txt

cmsRun fitMuon2.py ID looseid gentrack mc_all mcid pt default 2 > kk.txt

cmsRun fitMuon2.py ID looseid gentrack mc_all mcid eta default 2 > kk.txt


cmsRun fitMuon2.py ID mediumid gentrack mc_all mcid pt default 2 > kk.txt

cmsRun fitMuon2.py ID mediumid gentrack mc_all mcid eta default 2 > kk.txt



#quitar weight

cmsRun fitMuon2.py ID tightid gentrack mc_all mcid vtx default 2 > kk.txt

cmsRun fitMuon2.py ID looseid gentrack mc_all mcid vtx default 2 > kk.txt

cmsRun fitMuon2.py ID mediumid gentrack mc_all mcid vtx default 2 > kk.txt



# EFFICIENCIES ISO

#Data:

cmsRun fitMuon2.py ISO tightiso mediumid data_all dataiso pt default 2 > kk.txt

cmsRun fitMuon2.py ISO tightiso mediumid data_all dataiso eta default 2 > kk.txt

cmsRun fitMuon2.py ISO tightiso mediumid data_all dataiso vtx default 2 > kk.txt



#MC:

cmsRun fitMuon2.py ISO tightiso mediumid mc_all mciso pt default 2 > kk.txt

cmsRun fitMuon2.py ISO tightiso mediumid mc_all mciso eta default 2 > kk.txt


#quitar weight

cmsRun fitMuon2.py ISO tightiso mediumid mc_all mciso vtx default 2 > kk.txt






# RatioPlots

python make_ratioplots.py ID DATA_dataid MC_mcid

python make_ratioplots.py ISO DATA_dataiso MC_mciso




# FitPlots

python retrieve_plots.py ID DATA_dataid

python retrieve_plots.py ID MC_mcid

python retrieve_plots.py ISO DATA_dataiso

python retrieve_plots.py ISO MC_mciso


