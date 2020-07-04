'''
abandoned!!!
'''



import zipfile

cord_gjf_zip = zipfile.ZipFile("../data/static/ROUND3_TOFREQ_v2.zip", "r")
cord_gjf_namelist = []
for filename in cord_gjf_zip.namelist():
    if filename.endswith('.gjf'):
        # cord_gjf_namelist.append(filename[17:-4])
        cord_gjf_namelist.append(filename)

#eg_file = cord_gjf_zip.read(cord_gjf_namelist[0])
#print(eg_file.decode('utf-8'))

import os

for filename in cord_gjf_namelist:
    #source_gjf = cord_gjf_zip.read(filename)
    #middle_gjf = open(filename[17:-4]+'.txt','a')
    cmmd = ''
    #cmd_out = os.popen(cmmd)
