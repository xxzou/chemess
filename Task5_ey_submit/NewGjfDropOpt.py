import os

root_path = 'C:\\Users\\xxzou\\Desktop\\GS\\20200709_cleanup\\ROUND3_TOFREQ_v2\\'

raw_gjfs = [item for item in os.listdir(root_path) if item.endswith('.gjf')]

print(len(raw_gjfs))

for raw_gjf in raw_gjfs:
    raw_gjf_file = open(root_path+raw_gjf,'r')
    raw_gjf_content = raw_gjf_file.readlines()
    if raw_gjf_content[3] != '#p B3LYP/6-31G* opt freq\n':
        print(raw_gjf_content[3])
    if '_' in raw_gjf_content[2]:
        # print(raw_gjf_content[2], end='')
        raw_gjf_content[2] = raw_gjf_content[2][:raw_gjf_content[2].index('_')]+'\n'
        # print(raw_gjf_content[2])
    if '_' in raw_gjf_content[5]:
        raw_gjf_content[5] = raw_gjf_content[5][:raw_gjf_content[5].index('_')]+'\n'

    out_file = open(root_path+'ROUND3_TOFREQ_v3\\'+raw_gjf,'a')
    out_file.writelines(raw_gjf_content)
    out_file.close()
    print(raw_gjf_content[0:10])
    # input()