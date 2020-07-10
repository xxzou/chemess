import os

root_path = '..\\\data\\temp\\ROUND3_TOFREQ_v3\\'

raw_gjfs = [item for item in os.listdir(root_path) if item.endswith('.gjf')]

print(len(raw_gjfs))
input()

for raw_gjf in raw_gjfs:
    raw_gjf_file = open(root_path+raw_gjf,'r')
    raw_gjf_content = raw_gjf_file.readlines()
    raw_gjf_content.append('\n')
    out_file = open(root_path+'ROUND3_TOFREQ_v5\\'+raw_gjf,'a')
    out_file.writelines(raw_gjf_content)
    out_file.close()
    # print(raw_gjf_content[0:10])
    # input()