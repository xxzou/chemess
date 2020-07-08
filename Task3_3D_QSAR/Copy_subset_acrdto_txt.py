import os,shutil

all = [item[:-5] for item in os.listdir('../data/temp/good_mol2_v3.mdb') if item.endswith('mol2')]
subset_folders = [item for item in os.listdir('../data/temp/subset/')]
for subset_folder in subset_folders:
    txt_files = [item for item in os.listdir('../data/temp/subset/'+subset_folder) if item.endswith('.txt')]
    mol2_files = [item for item in os.listdir('../data/temp/subset/'+subset_folder) if item.endswith('.mol2')]
    os.mkdir('../data/temp/subset2/' + subset_folder)
    for txt_file in txt_files:
        shutil.copy('../data/temp/subset/' + subset_folder + '/' + txt_file,
                    '../data/temp/subset2/' + subset_folder)
        txt_content = open('../data/temp/subset/'+subset_folder+'/'+txt_file,'r').readlines()
        txt_namelist = [line.split(' ', maxsplit=1)[0] for line in txt_content[1:]]
        # input(txt_namelist)
        os.mkdir('../data/temp/subset2/'+subset_folder+'/'+txt_file[:-4]+'.mdb')
        for txt_name in txt_namelist:
            # continue
            shutil.copy('../data/temp/subset/'+subset_folder+'/'+txt_name+'.mol2',
                        '../data/temp/subset2/'+subset_folder+'/'+txt_file[:-4]+'.mdb')
        # print(type(txt_content))
    # input()