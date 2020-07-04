import xlrd,xlwt

wb_main = xlrd.open_workbook('./data/static/名字对照.xlsx')
# print(wb_main.sheet_names())

se_main = wb_main.sheet_by_name('chem0207')
nrow_main, ncol_main = se_main.nrows, se_main.ncols
# print(nrow_main, ncol_main)

se_main_rowlist = []
se_main_title_list = se_main.row_values(0)
for curr_row in range(nrow_main-1):
    #row_value = se_main.row_values(curr_row)
    #print('row%s value is %s' %(curr_row, row_value))
    se_main_rowlist.append(se_main.row_values(curr_row+1))

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
#print(len(se_main_collist))


import zipfile

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

cord_gjf_namelist = ReadFromMol2Zip()
# cord_gjf_namelist = ReadFromGjfZip()

for item in se_main_collist[1]:
    if item not in cord_gjf_namelist:
        print(item+': in xlsx not in zip')

for item in cord_gjf_namelist:
    if item not in se_main_collist[1]:
        print(item+': in zip not in xlsx')
