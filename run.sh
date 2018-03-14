#!/bin/bash
cd `dirname $0`

eval `scramv1 runtime -sh`
cmsRun fitMuon2.py $1 $2 $3 $4 $5 $6 $7
