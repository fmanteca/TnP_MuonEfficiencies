#!/bin/bash

#Data

#BC
#ID
###loose id

bsub -q 8nh -u pippo1234 run.sh ID_BC looseid gentrack data_all dataidBC pt_eta default
bsub -q 8nh -u pippo1234 run.sh ID_BC tightid gentrack data_all dataidBC pt_eta default

# bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal looseid gentrack data_all dataidBC_nominal pt_eta default
# bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal mediumid gentrack data_all dataidBC_nominal pt_eta default
# bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal mediumidprompt gentrack data_all dataidBC_nominal pt_eta default
# bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal tightid gentrack data_all dataidBC_nominal pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal highptid gentrack data_all dataidBC_nominal newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal trkhighptid gentrack data_all dataidBC_nominal newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal softid gentrack data_all dataidBC_nominal pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal looseid gentrack data_all dataidDE_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal mediumid gentrack data_all dataidDE_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal mediumidprompt gentrack data_all dataidDE_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal tightid gentrack data_all dataidDE_nominal pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal highptid gentrack data_all dataidDE_nominal newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal trkhighptid gentrack data_all dataidDE_nominal newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal softid gentrack data_all dataidDE_nominal pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal looseid gentrack data_all dataidF_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal mediumid gentrack data_all dataidF_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal mediumidprompt gentrack data_all dataidF_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal tightid gentrack data_all dataidF_nominal pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_nominal highptid gentrack data_all dataidF_nominal newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_nominal trkhighptid gentrack data_all dataidF_nominal newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal softid gentrack data_all dataidF_nominal pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal looseid gentrack mc_all mcidBC_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal mediumid gentrack mc_all mcidBC_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal mediumidprompt gentrack mc_all mcidBC_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal tightid gentrack mc_all mcidBC_nominal pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal highptid gentrack mc_all mcidBC_nominal newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal trkhighptid gentrack mc_all mcidBC_nominal newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_nominal softid gentrack mc_all mcidBC_nominal pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal looseid gentrack mc_all mcidDE_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal mediumid gentrack mc_all mcidDE_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal mediumidprompt gentrack mc_all mcidDE_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal tightid gentrack mc_all mcidDE_nominal pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal highptid gentrack mc_all mcidDE_nominal newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal trkhighptid gentrack mc_all mcidDE_nominal newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_nominal softid gentrack mc_all mcidDE_nominal pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal looseid gentrack mc_all mcidF_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal mediumid gentrack mc_all mcidF_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal mediumidprompt gentrack mc_all mcidF_nominal pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal tightid gentrack mc_all mcidF_nominal pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_nominal highptid gentrack mc_all mcidF_nominal newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_nominal trkhighptid gentrack mc_all mcidF_nominal newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_nominal softid gentrack mc_all mcidF_nominal pt_eta default








# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up looseid gentrack data_all dataidBC_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up mediumid gentrack data_all dataidBC_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up mediumidprompt gentrack data_all dataidBC_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up tightid gentrack data_all dataidBC_mass_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up highptid gentrack data_all dataidBC_mass_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up trkhighptid gentrack data_all dataidBC_mass_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up softid gentrack data_all dataidBC_mass_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up looseid gentrack data_all dataidDE_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up mediumid gentrack data_all dataidDE_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up mediumidprompt gentrack data_all dataidDE_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up tightid gentrack data_all dataidDE_mass_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up highptid gentrack data_all dataidDE_mass_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up trkhighptid gentrack data_all dataidDE_mass_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up softid gentrack data_all dataidDE_mass_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up looseid gentrack data_all dataidF_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up mediumid gentrack data_all dataidF_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up mediumidprompt gentrack data_all dataidF_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up tightid gentrack data_all dataidF_mass_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up highptid gentrack data_all dataidF_mass_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up trkhighptid gentrack data_all dataidF_mass_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up softid gentrack data_all dataidF_mass_up pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up looseid gentrack mc_all mcidBC_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up mediumid gentrack mc_all mcidBC_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up mediumidprompt gentrack mc_all mcidBC_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up tightid gentrack mc_all mcidBC_mass_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up highptid gentrack mc_all mcidBC_mass_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up trkhighptid gentrack mc_all mcidBC_mass_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_up softid gentrack mc_all mcidBC_mass_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up looseid gentrack mc_all mcidDE_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up mediumid gentrack mc_all mcidDE_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up mediumidprompt gentrack mc_all mcidDE_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up tightid gentrack mc_all mcidDE_mass_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up highptid gentrack mc_all mcidDE_mass_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up trkhighptid gentrack mc_all mcidDE_mass_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_up softid gentrack mc_all mcidDE_mass_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up looseid gentrack mc_all mcidF_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up mediumid gentrack mc_all mcidF_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up mediumidprompt gentrack mc_all mcidF_mass_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up tightid gentrack mc_all mcidF_mass_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up highptid gentrack mc_all mcidF_mass_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up trkhighptid gentrack mc_all mcidF_mass_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_up softid gentrack mc_all mcidF_mass_up pt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down looseid gentrack data_all dataidBC_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down mediumid gentrack data_all dataidBC_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down mediumidprompt gentrack data_all dataidBC_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down tightid gentrack data_all dataidBC_mass_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down highptid gentrack data_all dataidBC_mass_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down trkhighptid gentrack data_all dataidBC_mass_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down softid gentrack data_all dataidBC_mass_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down looseid gentrack data_all dataidDE_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down mediumid gentrack data_all dataidDE_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down mediumidprompt gentrack data_all dataidDE_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down tightid gentrack data_all dataidDE_mass_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down highptid gentrack data_all dataidDE_mass_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down trkhighptid gentrack data_all dataidDE_mass_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down softid gentrack data_all dataidDE_mass_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down looseid gentrack data_all dataidF_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down mediumid gentrack data_all dataidF_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down mediumidprompt gentrack data_all dataidF_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down tightid gentrack data_all dataidF_mass_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down highptid gentrack data_all dataidF_mass_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down trkhighptid gentrack data_all dataidF_mass_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down softid gentrack data_all dataidF_mass_down pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down looseid gentrack mc_all mcidBC_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down mediumid gentrack mc_all mcidBC_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down mediumidprompt gentrack mc_all mcidBC_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down tightid gentrack mc_all mcidBC_mass_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down highptid gentrack mc_all mcidBC_mass_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down trkhighptid gentrack mc_all mcidBC_mass_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_mass_down softid gentrack mc_all mcidBC_mass_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down looseid gentrack mc_all mcidDE_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down mediumid gentrack mc_all mcidDE_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down mediumidprompt gentrack mc_all mcidDE_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down tightid gentrack mc_all mcidDE_mass_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down highptid gentrack mc_all mcidDE_mass_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down trkhighptid gentrack mc_all mcidDE_mass_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_mass_down softid gentrack mc_all mcidDE_mass_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down looseid gentrack mc_all mcidF_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down mediumid gentrack mc_all mcidF_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down mediumidprompt gentrack mc_all mcidF_mass_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down tightid gentrack mc_all mcidF_mass_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down highptid gentrack mc_all mcidF_mass_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down trkhighptid gentrack mc_all mcidF_mass_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_mass_down softid gentrack mc_all mcidF_mass_down pt_eta default




# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up looseid gentrack data_all dataidBC_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up mediumid gentrack data_all dataidBC_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up mediumidprompt gentrack data_all dataidBC_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up tightid gentrack data_all dataidBC_tag_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up highptid gentrack data_all dataidBC_tag_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up trkhighptid gentrack data_all dataidBC_tag_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up softid gentrack data_all dataidBC_tag_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up looseid gentrack data_all dataidDE_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up mediumid gentrack data_all dataidDE_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up mediumidprompt gentrack data_all dataidDE_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up tightid gentrack data_all dataidDE_tag_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up highptid gentrack data_all dataidDE_tag_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up trkhighptid gentrack data_all dataidDE_tag_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up softid gentrack data_all dataidDE_tag_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up looseid gentrack data_all dataidF_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up mediumid gentrack data_all dataidF_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up mediumidprompt gentrack data_all dataidF_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up tightid gentrack data_all dataidF_tag_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up highptid gentrack data_all dataidF_tag_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up trkhighptid gentrack data_all dataidF_tag_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up softid gentrack data_all dataidF_tag_up pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up looseid gentrack mc_all mcidBC_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up mediumid gentrack mc_all mcidBC_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up mediumidprompt gentrack mc_all mcidBC_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up tightid gentrack mc_all mcidBC_tag_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up highptid gentrack mc_all mcidBC_tag_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up trkhighptid gentrack mc_all mcidBC_tag_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_up softid gentrack mc_all mcidBC_tag_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up looseid gentrack mc_all mcidDE_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up mediumid gentrack mc_all mcidDE_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up mediumidprompt gentrack mc_all mcidDE_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up tightid gentrack mc_all mcidDE_tag_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up highptid gentrack mc_all mcidDE_tag_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up trkhighptid gentrack mc_all mcidDE_tag_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_up softid gentrack mc_all mcidDE_tag_up pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up looseid gentrack mc_all mcidF_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up mediumid gentrack mc_all mcidF_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up mediumidprompt gentrack mc_all mcidF_tag_up pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up tightid gentrack mc_all mcidF_tag_up pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up highptid gentrack mc_all mcidF_tag_up newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up trkhighptid gentrack mc_all mcidF_tag_up newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_up softid gentrack mc_all mcidF_tag_up pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down looseid gentrack data_all dataidBC_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down mediumid gentrack data_all dataidBC_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down mediumidprompt gentrack data_all dataidBC_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down tightid gentrack data_all dataidBC_tag_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down highptid gentrack data_all dataidBC_tag_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down trkhighptid gentrack data_all dataidBC_tag_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down softid gentrack data_all dataidBC_tag_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down looseid gentrack data_all dataidDE_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down mediumid gentrack data_all dataidDE_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down mediumidprompt gentrack data_all dataidDE_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down tightid gentrack data_all dataidDE_tag_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down highptid gentrack data_all dataidDE_tag_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down trkhighptid gentrack data_all dataidDE_tag_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down softid gentrack data_all dataidDE_tag_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down looseid gentrack data_all dataidF_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down mediumid gentrack data_all dataidF_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down mediumidprompt gentrack data_all dataidF_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down tightid gentrack data_all dataidF_tag_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down highptid gentrack data_all dataidF_tag_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down trkhighptid gentrack data_all dataidF_tag_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down softid gentrack data_all dataidF_tag_down pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down looseid gentrack mc_all mcidBC_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down mediumid gentrack mc_all mcidBC_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down mediumidprompt gentrack mc_all mcidBC_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down tightid gentrack mc_all mcidBC_tag_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down highptid gentrack mc_all mcidBC_tag_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down trkhighptid gentrack mc_all mcidBC_tag_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_tag_down softid gentrack mc_all mcidBC_tag_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down looseid gentrack mc_all mcidDE_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down mediumid gentrack mc_all mcidDE_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down mediumidprompt gentrack mc_all mcidDE_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down tightid gentrack mc_all mcidDE_tag_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down highptid gentrack mc_all mcidDE_tag_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down trkhighptid gentrack mc_all mcidDE_tag_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_tag_down softid gentrack mc_all mcidDE_tag_down pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down looseid gentrack mc_all mcidF_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down mediumid gentrack mc_all mcidF_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down mediumidprompt gentrack mc_all mcidF_tag_down pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down tightid gentrack mc_all mcidF_tag_down pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down highptid gentrack mc_all mcidF_tag_down newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down trkhighptid gentrack mc_all mcidF_tag_down newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_tag_down softid gentrack mc_all mcidF_tag_down pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar looseid gentrack data_all dataidBC_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar mediumid gentrack data_all dataidBC_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar mediumidprompt gentrack data_all dataidBC_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar tightid gentrack data_all dataidBC_signalvar pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar highptid gentrack data_all dataidBC_signalvar newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar trkhighptid gentrack data_all dataidBC_signalvar newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar softid gentrack data_all dataidBC_signalvar pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar looseid gentrack data_all dataidDE_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar mediumid gentrack data_all dataidDE_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar mediumidprompt gentrack data_all dataidDE_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar tightid gentrack data_all dataidDE_signalvar pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar highptid gentrack data_all dataidDE_signalvar newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar trkhighptid gentrack data_all dataidDE_signalvar newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar softid gentrack data_all dataidDE_signalvar pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar looseid gentrack data_all dataidF_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar mediumid gentrack data_all dataidF_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar mediumidprompt gentrack data_all dataidF_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar tightid gentrack data_all dataidF_signalvar pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar highptid gentrack data_all dataidF_signalvar newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar trkhighptid gentrack data_all dataidF_signalvar newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar softid gentrack data_all dataidF_signalvar pt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar looseid gentrack mc_all mcidBC_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar mediumid gentrack mc_all mcidBC_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar mediumidprompt gentrack mc_all mcidBC_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar tightid gentrack mc_all mcidBC_signalvar pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar highptid gentrack mc_all mcidBC_signalvar newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar trkhighptid gentrack mc_all mcidBC_signalvar newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_BC_signalvar softid gentrack mc_all mcidBC_signalvar pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar looseid gentrack mc_all mcidDE_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar mediumid gentrack mc_all mcidDE_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar mediumidprompt gentrack mc_all mcidDE_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar tightid gentrack mc_all mcidDE_signalvar pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar highptid gentrack mc_all mcidDE_signalvar newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar trkhighptid gentrack mc_all mcidDE_signalvar newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_DE_signalvar softid gentrack mc_all mcidDE_signalvar pt_eta default

# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar looseid gentrack mc_all mcidF_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar mediumid gentrack mc_all mcidF_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar mediumidprompt gentrack mc_all mcidF_signalvar pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar tightid gentrack mc_all mcidF_signalvar pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar highptid gentrack mc_all mcidF_signalvar newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar trkhighptid gentrack mc_all mcidF_signalvar newpt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ID_F_signalvar softid gentrack mc_all mcidF_signalvar pt_eta default




































# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tightiso tightid  data_all dataidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal looseiso tightid  data_all dataidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tightiso mediumid  data_all dataidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal looseiso mediumid  data_all dataidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal looseiso looseid  data_all dataidBC_nominal  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tklooseiso highptid  data_all dataidBC_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tklooseiso trkhighptid  data_all dataidBC_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tktightiso trkhighptid  data_all dataidBC_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tktightiso highptid data_all dataidBC_nominal newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tightiso tightid  data_all dataidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal looseiso tightid  data_all dataidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tightiso mediumid  data_all dataidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal looseiso mediumid  data_all dataidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal looseiso looseid  data_all dataidDE_nominal  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tklooseiso highptid  data_all dataidDE_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tklooseiso trkhighptid  data_all dataidDE_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tktightiso trkhighptid  data_all dataidDE_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tktightiso highptid data_all dataidDE_nominal newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tightiso tightid  data_all dataidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal looseiso tightid  data_all dataidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tightiso mediumid  data_all dataidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal looseiso mediumid  data_all dataidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal looseiso looseid  data_all dataidF_nominal  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tklooseiso highptid  data_all dataidF_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tklooseiso trkhighptid  data_all dataidF_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tktightiso trkhighptid  data_all dataidF_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tktightiso highptid data_all dataidF_nominal newpt_eta default




# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tightiso tightid  data_all dataidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up looseiso tightid  data_all dataidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tightiso mediumid  data_all dataidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up looseiso mediumid  data_all dataidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up looseiso looseid  data_all dataidBC_mass_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tklooseiso highptid  data_all dataidBC_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tklooseiso trkhighptid  data_all dataidBC_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tktightiso trkhighptid  data_all dataidBC_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tktightiso highptid data_all dataidBC_mass_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tightiso tightid  data_all dataidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up looseiso tightid  data_all dataidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tightiso mediumid  data_all dataidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up looseiso mediumid  data_all dataidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up looseiso looseid  data_all dataidDE_mass_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tklooseiso highptid  data_all dataidDE_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tklooseiso trkhighptid  data_all dataidDE_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tktightiso trkhighptid  data_all dataidDE_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tktightiso highptid data_all dataidDE_mass_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tightiso tightid  data_all dataidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up looseiso tightid  data_all dataidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tightiso mediumid  data_all dataidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up looseiso mediumid  data_all dataidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up looseiso looseid  data_all dataidF_mass_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tklooseiso highptid  data_all dataidF_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tklooseiso trkhighptid  data_all dataidF_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tktightiso trkhighptid  data_all dataidF_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tktightiso highptid data_all dataidF_mass_up newpt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tightiso tightid  data_all dataidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down looseiso tightid  data_all dataidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tightiso mediumid  data_all dataidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down looseiso mediumid  data_all dataidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down looseiso looseid  data_all dataidBC_mass_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tklooseiso highptid  data_all dataidBC_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tklooseiso trkhighptid  data_all dataidBC_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tktightiso trkhighptid  data_all dataidBC_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tktightiso highptid data_all dataidBC_mass_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tightiso tightid  data_all dataidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down looseiso tightid  data_all dataidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tightiso mediumid  data_all dataidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down looseiso mediumid  data_all dataidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down looseiso looseid  data_all dataidDE_mass_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tklooseiso highptid  data_all dataidDE_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tklooseiso trkhighptid  data_all dataidDE_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tktightiso trkhighptid  data_all dataidDE_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tktightiso highptid data_all dataidDE_mass_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tightiso tightid  data_all dataidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down looseiso tightid  data_all dataidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tightiso mediumid  data_all dataidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down looseiso mediumid  data_all dataidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down looseiso looseid  data_all dataidF_mass_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tklooseiso highptid  data_all dataidF_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tklooseiso trkhighptid  data_all dataidF_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tktightiso trkhighptid  data_all dataidF_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tktightiso highptid data_all dataidF_mass_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tightiso tightid  data_all dataidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar looseiso tightid  data_all dataidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tightiso mediumid  data_all dataidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar looseiso mediumid  data_all dataidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar looseiso looseid  data_all dataidBC_signalvar  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tklooseiso highptid  data_all dataidBC_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tklooseiso trkhighptid  data_all dataidBC_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tktightiso trkhighptid  data_all dataidBC_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tktightiso highptid data_all dataidBC_signalvar newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tightiso tightid  data_all dataidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar looseiso tightid  data_all dataidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tightiso mediumid  data_all dataidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar looseiso mediumid  data_all dataidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar looseiso looseid  data_all dataidDE_signalvar  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tklooseiso highptid  data_all dataidDE_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tklooseiso trkhighptid  data_all dataidDE_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tktightiso trkhighptid  data_all dataidDE_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tktightiso highptid data_all dataidDE_signalvar newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tightiso tightid  data_all dataidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar looseiso tightid  data_all dataidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tightiso mediumid  data_all dataidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar looseiso mediumid  data_all dataidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar looseiso looseid  data_all dataidF_signalvar  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tklooseiso highptid  data_all dataidF_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tklooseiso trkhighptid  data_all dataidF_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tktightiso trkhighptid  data_all dataidF_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tktightiso highptid data_all dataidF_signalvar newpt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tightiso tightid  data_all dataidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up looseiso tightid  data_all dataidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tightiso mediumid  data_all dataidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up looseiso mediumid  data_all dataidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up looseiso looseid  data_all dataidBC_tag_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tklooseiso highptid  data_all dataidBC_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tklooseiso trkhighptid  data_all dataidBC_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tktightiso trkhighptid  data_all dataidBC_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tktightiso highptid data_all dataidBC_tag_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tightiso tightid  data_all dataidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up looseiso tightid  data_all dataidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tightiso mediumid  data_all dataidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up looseiso mediumid  data_all dataidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up looseiso looseid  data_all dataidDE_tag_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tklooseiso highptid  data_all dataidDE_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tklooseiso trkhighptid  data_all dataidDE_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tktightiso trkhighptid  data_all dataidDE_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tktightiso highptid data_all dataidDE_tag_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tightiso tightid  data_all dataidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up looseiso tightid  data_all dataidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tightiso mediumid  data_all dataidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up looseiso mediumid  data_all dataidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up looseiso looseid  data_all dataidF_tag_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tklooseiso highptid  data_all dataidF_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tklooseiso trkhighptid  data_all dataidF_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tktightiso trkhighptid  data_all dataidF_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tktightiso highptid data_all dataidF_tag_up newpt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tightiso tightid  data_all dataidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down looseiso tightid  data_all dataidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tightiso mediumid  data_all dataidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down looseiso mediumid  data_all dataidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down looseiso looseid  data_all dataidBC_tag_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tklooseiso highptid  data_all dataidBC_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tklooseiso trkhighptid  data_all dataidBC_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tktightiso trkhighptid  data_all dataidBC_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tktightiso highptid data_all dataidBC_tag_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tightiso tightid  data_all dataidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down looseiso tightid  data_all dataidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tightiso mediumid  data_all dataidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down looseiso mediumid  data_all dataidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down looseiso looseid  data_all dataidDE_tag_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tklooseiso highptid  data_all dataidDE_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tklooseiso trkhighptid  data_all dataidDE_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tktightiso trkhighptid  data_all dataidDE_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tktightiso highptid data_all dataidDE_tag_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tightiso tightid  data_all dataidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down looseiso tightid  data_all dataidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tightiso mediumid  data_all dataidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down looseiso mediumid  data_all dataidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down looseiso looseid  data_all dataidF_tag_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tklooseiso highptid  data_all dataidF_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tklooseiso trkhighptid  data_all dataidF_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tktightiso trkhighptid  data_all dataidF_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tktightiso highptid data_all dataidF_tag_down newpt_eta default








# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tightiso tightid  mc_all mcidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal looseiso tightid  mc_all mcidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tightiso mediumid  mc_all mcidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal looseiso mediumid  mc_all mcidBC_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal looseiso looseid  mc_all mcidBC_nominal  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tklooseiso highptid  mc_all mcidBC_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tklooseiso trkhighptid  mc_all mcidBC_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tktightiso trkhighptid  mc_all mcidBC_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_nominal tktightiso highptid mc_all mcidBC_nominal newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tightiso tightid  mc_all mcidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal looseiso tightid  mc_all mcidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tightiso mediumid  mc_all mcidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal looseiso mediumid  mc_all mcidDE_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal looseiso looseid  mc_all mcidDE_nominal  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tklooseiso highptid  mc_all mcidDE_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tklooseiso trkhighptid  mc_all mcidDE_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tktightiso trkhighptid  mc_all mcidDE_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_nominal tktightiso highptid mc_all mcidDE_nominal newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tightiso tightid  mc_all mcidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal looseiso tightid  mc_all mcidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tightiso mediumid  mc_all mcidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal looseiso mediumid  mc_all mcidF_nominal  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal looseiso looseid  mc_all mcidF_nominal  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tklooseiso highptid  mc_all mcidF_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tklooseiso trkhighptid  mc_all mcidF_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tktightiso trkhighptid  mc_all mcidF_nominal  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_nominal tktightiso highptid mc_all mcidF_nominal newpt_eta default




# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tightiso tightid  mc_all mcidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up looseiso tightid  mc_all mcidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tightiso mediumid  mc_all mcidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up looseiso mediumid  mc_all mcidBC_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up looseiso looseid  mc_all mcidBC_mass_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tklooseiso highptid  mc_all mcidBC_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tklooseiso trkhighptid  mc_all mcidBC_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tktightiso trkhighptid  mc_all mcidBC_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_up tktightiso highptid mc_all mcidBC_mass_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tightiso tightid  mc_all mcidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up looseiso tightid  mc_all mcidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tightiso mediumid  mc_all mcidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up looseiso mediumid  mc_all mcidDE_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up looseiso looseid  mc_all mcidDE_mass_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tklooseiso highptid  mc_all mcidDE_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tklooseiso trkhighptid  mc_all mcidDE_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tktightiso trkhighptid  mc_all mcidDE_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_up tktightiso highptid mc_all mcidDE_mass_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tightiso tightid  mc_all mcidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up looseiso tightid  mc_all mcidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tightiso mediumid  mc_all mcidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up looseiso mediumid  mc_all mcidF_mass_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up looseiso looseid  mc_all mcidF_mass_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tklooseiso highptid  mc_all mcidF_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tklooseiso trkhighptid  mc_all mcidF_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tktightiso trkhighptid  mc_all mcidF_mass_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_up tktightiso highptid mc_all mcidF_mass_up newpt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tightiso tightid  mc_all mcidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down looseiso tightid  mc_all mcidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tightiso mediumid  mc_all mcidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down looseiso mediumid  mc_all mcidBC_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down looseiso looseid  mc_all mcidBC_mass_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tklooseiso highptid  mc_all mcidBC_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tklooseiso trkhighptid  mc_all mcidBC_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tktightiso trkhighptid  mc_all mcidBC_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_mass_down tktightiso highptid mc_all mcidBC_mass_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tightiso tightid  mc_all mcidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down looseiso tightid  mc_all mcidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tightiso mediumid  mc_all mcidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down looseiso mediumid  mc_all mcidDE_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down looseiso looseid  mc_all mcidDE_mass_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tklooseiso highptid  mc_all mcidDE_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tklooseiso trkhighptid  mc_all mcidDE_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tktightiso trkhighptid  mc_all mcidDE_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_mass_down tktightiso highptid mc_all mcidDE_mass_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tightiso tightid  mc_all mcidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down looseiso tightid  mc_all mcidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tightiso mediumid  mc_all mcidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down looseiso mediumid  mc_all mcidF_mass_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down looseiso looseid  mc_all mcidF_mass_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tklooseiso highptid  mc_all mcidF_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tklooseiso trkhighptid  mc_all mcidF_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tktightiso trkhighptid  mc_all mcidF_mass_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_mass_down tktightiso highptid mc_all mcidF_mass_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tightiso tightid  mc_all mcidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar looseiso tightid  mc_all mcidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tightiso mediumid  mc_all mcidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar looseiso mediumid  mc_all mcidBC_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar looseiso looseid  mc_all mcidBC_signalvar  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tklooseiso highptid  mc_all mcidBC_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tklooseiso trkhighptid  mc_all mcidBC_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tktightiso trkhighptid  mc_all mcidBC_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_signalvar tktightiso highptid mc_all mcidBC_signalvar newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tightiso tightid  mc_all mcidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar looseiso tightid  mc_all mcidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tightiso mediumid  mc_all mcidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar looseiso mediumid  mc_all mcidDE_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar looseiso looseid  mc_all mcidDE_signalvar  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tklooseiso highptid  mc_all mcidDE_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tklooseiso trkhighptid  mc_all mcidDE_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tktightiso trkhighptid  mc_all mcidDE_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_signalvar tktightiso highptid mc_all mcidDE_signalvar newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tightiso tightid  mc_all mcidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar looseiso tightid  mc_all mcidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tightiso mediumid  mc_all mcidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar looseiso mediumid  mc_all mcidF_signalvar  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar looseiso looseid  mc_all mcidF_signalvar  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tklooseiso highptid  mc_all mcidF_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tklooseiso trkhighptid  mc_all mcidF_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tktightiso trkhighptid  mc_all mcidF_signalvar  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_signalvar tktightiso highptid mc_all mcidF_signalvar newpt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tightiso tightid  mc_all mcidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up looseiso tightid  mc_all mcidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tightiso mediumid  mc_all mcidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up looseiso mediumid  mc_all mcidBC_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up looseiso looseid  mc_all mcidBC_tag_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tklooseiso highptid  mc_all mcidBC_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tklooseiso trkhighptid  mc_all mcidBC_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tktightiso trkhighptid  mc_all mcidBC_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_up tktightiso highptid mc_all mcidBC_tag_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tightiso tightid  mc_all mcidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up looseiso tightid  mc_all mcidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tightiso mediumid  mc_all mcidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up looseiso mediumid  mc_all mcidDE_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up looseiso looseid  mc_all mcidDE_tag_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tklooseiso highptid  mc_all mcidDE_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tklooseiso trkhighptid  mc_all mcidDE_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tktightiso trkhighptid  mc_all mcidDE_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_up tktightiso highptid mc_all mcidDE_tag_up newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tightiso tightid  mc_all mcidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up looseiso tightid  mc_all mcidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tightiso mediumid  mc_all mcidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up looseiso mediumid  mc_all mcidF_tag_up  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up looseiso looseid  mc_all mcidF_tag_up  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tklooseiso highptid  mc_all mcidF_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tklooseiso trkhighptid  mc_all mcidF_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tktightiso trkhighptid  mc_all mcidF_tag_up  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_up tktightiso highptid mc_all mcidF_tag_up newpt_eta default



# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tightiso tightid  mc_all mcidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down looseiso tightid  mc_all mcidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tightiso mediumid  mc_all mcidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down looseiso mediumid  mc_all mcidBC_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down looseiso looseid  mc_all mcidBC_tag_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tklooseiso highptid  mc_all mcidBC_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tklooseiso trkhighptid  mc_all mcidBC_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tktightiso trkhighptid  mc_all mcidBC_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_BC_tag_down tktightiso highptid mc_all mcidBC_tag_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tightiso tightid  mc_all mcidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down looseiso tightid  mc_all mcidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tightiso mediumid  mc_all mcidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down looseiso mediumid  mc_all mcidDE_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down looseiso looseid  mc_all mcidDE_tag_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tklooseiso highptid  mc_all mcidDE_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tklooseiso trkhighptid  mc_all mcidDE_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tktightiso trkhighptid  mc_all mcidDE_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_DE_tag_down tktightiso highptid mc_all mcidDE_tag_down newpt_eta default


# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tightiso tightid  mc_all mcidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down looseiso tightid  mc_all mcidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tightiso mediumid  mc_all mcidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down looseiso mediumid  mc_all mcidF_tag_down  pt_eta default
# # bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down looseiso looseid  mc_all mcidF_tag_down  pt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tklooseiso highptid  mc_all mcidF_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tklooseiso trkhighptid  mc_all mcidF_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tktightiso trkhighptid  mc_all mcidF_tag_down  newpt_eta default
#  bsub -q 8nh -u pippo1234 run.sh ISO_F_tag_down tktightiso highptid mc_all mcidF_tag_down newpt_eta default









