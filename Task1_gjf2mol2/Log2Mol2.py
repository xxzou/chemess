'''
DON'T RUN HERE!!!RUN WITH gaussian output file folder!!!
works great, output in '20200703_RE.zip'
'''

import os,time
for filename in os.listdir('..\ROUND3_OK_OUT'):
    print(filename)
    if '_' in filename:
        cmmd = 'obabel ..\\ROUND3_OK_OUT\\'+filename+' -O '+filename[:-10]+'.mol2'
    else:
        cmmd = 'obabel ..\\ROUND3_OK_OUT\\'+filename+' -O '+filename[:-4]+'.mol2'
    cmd_out = os.popen(cmmd)
    time.sleep(0.2)
