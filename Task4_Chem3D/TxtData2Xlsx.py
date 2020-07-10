import os
import re
import time,xlwt

workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('Chem3D_data')

t0 = time.time()
path1 = '..\\data\\temp\\Chem3D_rawdata_gjf\\'
path2 = '..\\data\\temp\\Chem3D_rawdata_mol2\\'
good_path_list = []

namelist = os.listdir(path1)
win1,win2 = 0, 0
for name in namelist:
    size1,size2 = os.path.getsize(path1+name) , os.path.getsize(path2+name)
    if size1 > size2:
        good_path_list.append(path1+name)
        #win1 += 1
        #print(size1)
    elif size1 == size2:
        good_path_list.append(path1 + name)
        #win1 += 1
        #win2 += 1
        #print(size1)
    else:
        good_path_list.append(path2 + name)
        #win2 += 1
        #print(size2)

# print(win1,win2)

# (good_path_list)
data_title_list = []
data_list_len_list = []
data_title_list =  ['Model/', 'ChemPropPro: Boiling Point/Kelvin', 'ChemPropPro: Critical Pressure/Bar', 'ChemPropPro: Critical Temperature/Kelvin', 'ChemPropPro: Critical Volume/cm^3/mol', 'ChemPropPro: Gibbs Free Energy/kJ/mol', 'ChemPropPro: Heat Of Formation/kJ/mol', "ChemPropPro: Henry's Law Constant/", 'ChemPropPro: Ideal Gas Thermal Capacity/J/(mol.K)', 'ChemPropPro: LogP/', 'ChemPropPro: Melting Point/Kelvin', 'ChemPropPro: Mol Refractivity/cm^3/mol', 'ChemPropPro: Vapor Pressure/Pascal', 'ChemPropPro: Water Solubility/mg/L', 'Log(p)......../1', 'St..deviation./1', "by Crippen's fragmentation/1", 'Log(p)......../2', 'St..deviation./2', "by Viswanadhan's fragmentation/1", 'Log(p)......../3', 'St..deviation./3', "by Broto's method/Chim.Theor.,19,71(1984).", 'MR............/[cm.cm.cm/mol]1', 'St..deviation./4', "by Crippen's fragmentation/2", 'MR............/[cm.cm.cm/mol]2', 'St..deviation./5', "by Viswanadhan's fragmentation/2", '1. method: H/log[unitless]', 'Estimation of mean error../', 'Normal Boiling Point [p=1atm]/[K]1', 'Standard Error/[K]1', 'Normal Boiling Point [p=1atm]/[K]2', 'Standard Error/was not estimated.1', 'Freezing Point [p=1atm]/[K]', 'Standard Error/[K]2', 'Critical Temperature/[K]', 'Standard Error/was not estimated.2', 'Critical Pressure/[bar]', 'Standard Error/was not estimated.3', 'Critical Volume/[cm.cm.cm/mol]', 'Standard Error/was not estimated.4', 'Heat of Formation [T=298.15K, p=1atm]/[kJ/mol]', 'Standard Error/was not estimated.5', 'Gibbs Energy [T=298.15K, p=1atm]/[kJ/mol]', 'Standard Error/was not estimated.6', 'Ideal gas thermal capacity for T= 298.15 [K] and p=1atm/[J/(mol.K)]', 'Standard Error/was not estimated.7', 'ChemPropPro: Lipinski Rule/', 'ChemPropStd: Formal Charge/', 'ChemPropStd: Connolly Accessible Area/Angstroms Squared', 'ChemPropStd: Connolly Molecular Area/Angstroms Squared', 'ChemPropStd: Connolly Solvent Excluded Volume/Angstroms Cubed', 'ChemPropStd: Exact Mass/g/Mol', 'ChemPropStd: Mass/', 'ChemPropStd: Mol Weight/', 'ChemPropStd: Number of HBond Acceptors/', 'ChemPropStd: Number of HBond Donors/', 'ChemPropStd: Ovality/', 'ChemPropStd: Principal Moment/', 'ChemPropStd: Elemental Analysis/', 'ChemPropStd: m/z/', 'ChemPropStd: Mol Formula/', 'ChemPropStd: Mol Formula HTML/', 'CLogP Driver: Mol Refractivity/', 'CLogP Driver: Partition Coefficient/', 'Molecular Networks: LogP/Log Units', 'Molecular Networks: LogS/Log Units', 'Molecular Networks: PKa/Log Units', 'Molecular Topology: Balaban Index/', 'Molecular Topology: Cluster Count/', 'Molecular Topology: Molecular Topological Index/', 'Molecular Topology: Num Rotatable Bonds/Bond(s)', 'Molecular Topology: Polar Surface Area/Angstroms Squared', 'Molecular Topology: Radius/Atom(s)', 'Molecular Topology: Shape Attribute/', 'Molecular Topology: Shape Coefficient/', 'Molecular Topology: Sum Of Degrees/', 'Molecular Topology: Sum Of Valence Degrees/', 'Molecular Topology: Topological Diameter/Bond(s)', 'Molecular Topology: Total Connectivity/', 'Molecular Topology: Total Valence Connectivity/', 'Molecular Topology: Wiener Index/']

# 写入excel
# 参数对应 行, 列, 值
for num,item in enumerate(data_title_list):
    # continue
    worksheet.write(0,num+1, label = item)
# 保存

for data_file_name in good_path_list:
    # print(good_path_list.index(data_file_name))
    if False and 'CFE-2008-ZL-1' not in data_file_name:
        continue
    if False and 'LYH-2009-CMC-1537-1K' not in data_file_name:
        continue
    if False and 'LJ-2006-CPB-1249-24' not in data_file_name:
        continue
    data_file = open(data_file_name,'r')
    data_content = data_file.readlines()
    data_list = []
    problem = False

    for line in data_content:
        # print(line[:-1])
        line = line[:-1]

        if line.startswith('error'):
            continue
        if line.strip().endswith(':') or line.strip().endswith('=') :
            continue
        if 'Method is not usable' in line:
            continue
        if 'failed' in line:
            continue
        if '=' in line and ':' in line and '[' in line and not 'unitless' in line:
            data_list.append([item.strip() for item in line.split(':')])
        elif '=' in line and ':' in line:
            data_list.append([item.strip() for item in line.split('=')])
        elif '=' in line:
            data_list.append([item.strip() for item in line.split('=')])
        elif ':' in line:
            data_list.append([item.strip() for item in line.split(':')])
        else:
            continue
        if '[' in data_list[0]:
            problem = data_list[0][data_list[0].index('['):data_list[0].index(']')+1]
            data_list[0] = data_list[0].replace(problem,'')
        if 'Ideal gas thermal capacity for T' in line:
            data_list.pop()
            data_list.append([item.strip() for item in line.split(':')])
        if line.startswith('ChemPropStd: Principal Moment'):
            data_list.pop()
            data_list.append([item.strip() for item in line.split('=')])
            data_list[-1][1] = data_list[-1][1].replace(' ',',')
        if line.startswith('Molecular Networks: PKa') and 'pKa:' in line:
            # print(line)
            data_list.pop()
            pka_list = [item.strip() for item in line.split('=')]
            pka_info = re.split('pKa:|Atom:|  ', pka_list[1])
            pka_list.pop()
            if len(pka_info) == 4:
                pka_list.append(pka_info[2]+' Log Units')
                data_list.append(pka_list)
            if len(pka_info) == 6:
                pka_list.append(str(min(float(pka_info[2]),float(pka_info[4])))+' Log Units')
                data_list.append(pka_list)

        if_long_text = ('ChemPropPro: Lipinski Rule' in line
                        or 'ChemPropStd: Elemental Analysis' in line
                        or 'ChemPropStd: m/z' in line)
        if if_long_text:
            data_list.pop()
            data_list.append([item.strip() for item in line.split('=')])
            data_list[-1][1] = data_list[-1][1].replace(' ','')

        # data_list.append(problem)
        if problem:
            data_list[-1] += problem
            problem = False

    for item_num,item in enumerate(data_list):
        if len(item) > 1 and ' ' in item[1]:
            tmp_list = item[1].split(' ',maxsplit=1)
            item.pop()
            item += tmp_list
        # item = [item[1],item[0]+'/'+' '.join(item[2:])]
        data_list[item_num] = [item[1],item[0]+'/'+' '.join(item[2:])]
        # print((item))




    # print('--------------------END OF PHASE 1--------------------')



    i = 1
    for j,item in enumerate(data_list):
        for k,item2 in enumerate(item):
            if "Crippen's fragmentation" in item2:
                data_list[j][k] += str(i)
                i += 1
    i = 1
    for j,item in enumerate(data_list):
        for k,item2 in enumerate(item):
            if "Viswanadhan's fragmentation" in item2:
                data_list[j][k] += str(i)
                i += 1

    if True and len(data_list) == 84 :
        for item in data_list:
            continue
            print(item[1])
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[20][1] += '3'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '3'
        data_list[24][1] += '4'
        data_list[27][1] += '5'
        data_list[23][1] += '1'
        data_list[26][1] += '2'
        for item in data_list[14:28]:
            continue
            print(item)
        data_list[31][1] += '1'
        data_list[33][1] += '2'
        data_list[32][1] += '1'
        data_list[36][1] += '2'
        data_list[34][1] += '1'
        data_list[38][1] += '2'
        data_list[40][1] += '3'
        data_list[42][1] += '4'
        data_list[44][1] += '5'
        data_list[46][1] += '6'
        data_list[48][1] += '7'
        for item in data_list[31:49]:
            continue
            print(item)
        #print([item[1] for item in data_list])
        #input('waiting')

    if True and len(data_list) == 82 :
        for item in data_list:
            continue
            print(item[1])
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[20][1] += '3'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '3'
        data_list[24][1] += '4'
        data_list[27][1] += '5'
        data_list[23][1] += '1'
        data_list[26][1] += '2'
        for item in data_list[14:28]:
            continue
            print(item)
        data_list[29][1] += '1'
        data_list[31][1] += '2'
        data_list[30][1] += '1'
        data_list[34][1] += '2'
        data_list[32][1] += '1'
        data_list[36][1] += '2'
        data_list[38][1] += '3'
        data_list[40][1] += '4'
        data_list[42][1] += '5'
        data_list[44][1] += '6'
        data_list[46][1] += '7'
        for item in data_list[29:47]:
            continue
            print(item)
        # input('waiting')

    if True and len(data_list) == 81 :
        for item in data_list[14:25]:
            continue
            print(item[1])
        # input('waiting')
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '4'
        data_list[24][1] += '5'
        data_list[20][1] += '1'
        data_list[23][1] += '2'
        for item in data_list[14:28]:
            continue
            print(item)
        st_line = 28
        data_list[st_line+0][1] += '1'
        data_list[st_line+2][1] += '2'
        data_list[st_line+1][1] += '1'
        data_list[st_line+5][1] += '2'
        data_list[st_line+3][1] += '1'
        data_list[st_line+7][1] += '2'
        data_list[st_line+9][1] += '3'
        data_list[st_line+11][1] += '4'
        data_list[st_line+13][1] += '5'
        data_list[st_line+15][1] += '6'
        data_list[st_line+17][1] += '7'
        for item in data_list[st_line+0:st_line+18]:
            continue
            print(item)
        # input('waiting')

    if True and len(data_list) == 79:
        for item in data_list[14:25]:
            continue
            print(item[1])
        # input('waiting')
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '4'
        data_list[24][1] += '5'
        data_list[20][1] += '1'
        data_list[23][1] += '2'
        for item in data_list[14:25]:
            continue
            print(item)
        st_line = 26
        data_list[st_line + 0][1] += '1'
        data_list[st_line + 2][1] += '2'
        data_list[st_line + 1][1] += '1'
        data_list[st_line + 5][1] += '2'
        data_list[st_line + 3][1] += '1'
        data_list[st_line + 7][1] += '2'
        data_list[st_line + 9][1] += '3'
        data_list[st_line + 11][1] += '4'
        data_list[st_line + 13][1] += '5'
        data_list[st_line + 15][1] += '6'
        data_list[st_line + 17][1] += '7'
        for item in data_list[st_line + 0:st_line + 18]:
            continue
            print(item)
        # input('waiting')

    if True and len(data_list) == 74:
        for item in data_list:
            continue
            print(item[1])
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[20][1] += '3'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '3'
        data_list[24][1] += '4'
        data_list[27][1] += '5'
        data_list[23][1] += '1'
        data_list[26][1] += '2'
        for item in data_list[14:28]:
            continue
            print(item)
        st_line = 29
        data_list[st_line + 0][1] += '1'
        data_list[st_line + 2][1] += '2'
        data_list[st_line + 1][1] += '1'
        data_list[st_line + 3][1] += '1'
        data_list[st_line + 5][1] += '2'
        data_list[st_line + 7][1] += '3'
        data_list[st_line + 9][1] += '5'
        for item in data_list[st_line + 0:st_line + 10]:
            continue
            print(item)
        # input('waiting')

    if True and len(data_list) == 68:
        for item in data_list:
            continue
            print(item[1])
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[20][1] += '3'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '3'
        data_list[24][1] += '4'
        data_list[27][1] += '5'
        data_list[23][1] += '1'
        data_list[26][1] += '2'
        for item in data_list[14:28]:
            continue
            print(item)
        st_line = 29
        data_list[st_line + 0][1] += '1'
        data_list[st_line + 2][1] += '2'
        data_list[st_line + 1][1] += '1'
        data_list[st_line + 3][1] += '1'
        for item in data_list[st_line + 0:st_line + 4]:
            continue
            print(item)
        # input('waiting')

    if True and len(data_list) == 65:
        for item in data_list:
            continue
            print(item[1])
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '4'
        data_list[24][1] += '5'
        data_list[20][1] += '1'
        data_list[23][1] += '2'
        for item in data_list[14:25]:
            continue
            print(item)
        st_line = 26
        data_list[st_line + 0][1] += '1'
        data_list[st_line + 2][1] += '2'
        data_list[st_line + 1][1] += '1'
        data_list[st_line + 3][1] += '1'
        for item in data_list[st_line + 0:st_line + 4]:
            continue
            print(item)
        # input('waiting')

    if True and len(data_list) == 64:
        for item in data_list:
            continue
            print(item[1])
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[20][1] += '3'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '3'
        data_list[24][1] += '4'
        data_list[27][1] += '5'
        data_list[23][1] += '1'
        data_list[26][1] += '2'
        for item in data_list[14:28]:
            continue
            print(item)
        # input('waiting')

    if True and len(data_list) == 61:
        for item in data_list:
            continue
            print(item[1])
        data_list[14][1] += '1'
        data_list[17][1] += '2'
        data_list[15][1] += '1'
        data_list[18][1] += '2'
        data_list[21][1] += '4'
        data_list[24][1] += '5'
        data_list[20][1] += '1'
        data_list[23][1] += '2'
        for item in data_list[14:25]:
            continue
            print(item)
        # input('waiting')






    # print('--------------------END OF PHASE 2--------------------')
    # print('--------------------TEST PART--------------------')




    if False and len(data_list) not in data_list_len_list:
        print('-'*100)
        print('-' * 100)
        print(len(data_list))
        print(data_file_name)
        for item in data_list:
            print((item))
        data_list_len_list.append(len(data_list))

    for item in data_list:
        if False and  item[1] not in data_title_list:
            # continue
            print('-' * 50)
            print(data_file_name)
            print(item)
            data_title_list.append(item[1])
    # print(data_title_list)
    # print(len(data_list))
    # print([item[1] for item in data_list])
    for item in data_list:
        continue
        print(item[1])
    # input()


    # print('--------------------OUT WRITE STARTS--------------------')

    row_num = good_path_list.index(data_file_name)+1
    worksheet.write(row_num, 0, label=data_file_name[data_file_name.rindex('\\')+1:-4])
    for item in data_list:
        # continue
        col_num = data_title_list.index(item[1]) +1
        # print(row_num, col_num, item[0], item[1])
        worksheet.write(row_num, col_num, label=item[0])

    workbook.save('Excel_test.xls')
    # input('waiting')

