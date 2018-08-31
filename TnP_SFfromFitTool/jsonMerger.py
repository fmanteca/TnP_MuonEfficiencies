import json 

filLst = ['/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunBCDEF_SF_ID.json',
          '/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunGH_SF_ID.json',
          '/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunBCDEF_SF_ISO.json',
          '/eos/cms/store/group/phys_muon/fernanpe/SFs_Legacy_rereco2016/RunGH_SF_ISO.json']

for fil in filLst:
    cosas = [] 
    for i in range(1,4):
        theFil = open(fil.replace('.json','_part%d.json'%i),'r')
        cosas.append(json.loads( theFil.read()))
        theFil.close()
        
    for a in cosas[0]: 
        for b in cosas[0][a]:
            for c in cosas[0][a][b]: 
                cosas[0][a][b][c].update(cosas[1][a][b][c])
                cosas[0][a][b][c].update(cosas[2][a][b][c])                
#                print c
#                for d in  cosas[0][a][b][c]:
#                    print d



    kk = json.dumps( cosas, indent=4, sort_keys=True)
    outfile = open(fil.split('/')[-1],'w')
    outfile.write(kk)
    outfile.close()
