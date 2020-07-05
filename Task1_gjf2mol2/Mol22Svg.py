'''
OK TO RUN HERE.
REMERBER TO CLEAR ./data/temp
'''

import os,time
for filename in os.listdir('..\\data\\temp\\good_mol2'):
    print(filename)
    cmmd = 'obabel ..\\data\\temp\\good_mol2\\'+filename+' -O ..\\data\\temp\\good_png\\'+filename[:-5]+'.png -d'
    cmd_out = os.popen(cmmd)
    # input()
    time.sleep(0.2)
