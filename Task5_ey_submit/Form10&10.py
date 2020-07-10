'''
LATTER FOUND TO BE UNNECESSARY
'''


import os,shutil

root_path = '..\\\data\\temp\\ROUND3_TOFREQ_v3\\'
gjf_namelist = [item for item in os.listdir(root_path) if item.endswith('.gjf')]
print(gjf_namelist)

new_path = '..\\\data\\temp\\ROUND3_TOFREQ_v4\\'
for i in range(10):
    i_path = new_path + str(i) + '\\'
    os.mkdir(i_path)
    for j in range(10):
        j_path = i_path + str(j) + '\\'
        os.mkdir(j_path)
        for k in range(10):
            num = int(str(i)+str(j)+str(k))
            if num >= len(gjf_namelist):
                continue
            shutil.copy(root_path+gjf_namelist[num],j_path)
            #print(i,j,k)
