import xlrd,xlwt

wb_main = xlrd.open_workbook('C:\\Users\\xxzou\\Desktop\\所有数据_20200709.xlsx')
print(wb_main.sheet_names())
# input()

se_main = wb_main.sheet_by_name('20200708(pIC+uM)')
nrow_main, ncol_main = se_main.nrows, se_main.ncols
# print(nrow_main, ncol_main)

se_main_rowlist = []
se_main_title_list = se_main.row_values(0)
for curr_row in range(nrow_main-2):
    #row_value = se_main.row_values(curr_row)
    #print('row%s value is %s' %(curr_row, row_value))
    se_main_rowlist.append(se_main.row_values(curr_row+2))

'''
se_main_collist = []
for curr_col in range(ncol_main):
    #row_value = se_main.row_values(curr_row)
    #print('row%s value is %s' %(curr_row, row_value))
    se_main_collist.append(se_main.col_values(curr_col)[1:])
'''

se_main_collist = [[row[i] for row in se_main_rowlist] for i in range(ncol_main)]

#print(len(se_main_list))
#print(se_main_title_list)
#print(se_main_list[0])
print(len(se_main_collist[0]))
print(se_main_collist[0])
input()

import zipfile,os

def ReadFromGjfZip():
    cord_gjf_zip = zipfile.ZipFile("./data/static/ROUND3_TOFREQ_v2.zip", "r")
    cord_gjf_namelist = []
    for filename in cord_gjf_zip.namelist():
        if filename.endswith('.gjf'):
            cord_gjf_namelist.append(filename[17:-4])
        # print(filename[17:-4])
    return cord_gjf_namelist

def ReadFromMol2Zip():
    cord_gjf_zip = zipfile.ZipFile("./data/static/20200703_RE.zip", "r")
    cord_gjf_namelist = []
    for filename in cord_gjf_zip.namelist():
        if filename.endswith('.mol2'):
            cord_gjf_namelist.append(filename[12:-5])
            # print(filename[12:-5])
    return cord_gjf_namelist

# cord_gjf_namelist = ReadFromMol2Zip()
# cord_gjf_namelist = ReadFromGjfZip()

root_path = 'C:\\Users\\xxzou\\Desktop\\GS\\20200709_cleanup\\ROUND3_TOFREQ_v3\\'
cord_gjf_namelist = [item[:-4] for item in os.listdir(root_path) if item.endswith('.gjf')]
print(cord_gjf_namelist)
input()

for item in se_main_collist[0]:
    if item not in cord_gjf_namelist:
        # print(item+': in xlsx not in zip')
        pass

for item in cord_gjf_namelist:
    if item not in se_main_collist[0]:
        print(item+': in zip not in xlsx')

'CFE-2008-ZL-2'
'CFE-2008-ZL-2'
