import xlrd,xlwt

wb_main = xlrd.open_workbook('./data/static/名字对照.xlsx')
# print(wb_main.sheet_names())

se_main = wb_main.sheet_by_name('chem0207')
nrow_main, ncol_main = se_main.nrows, se_main.ncols
# print(nrow_main, ncol_main)

se_main_list = []
se_main_title_list = se_main.row_values(0)
for curr_row in range(nrow_main-1):
    #row_value = se_main.row_values(curr_row)
    #print('row%s value is %s' %(curr_row, row_value))
    se_main_list.append(se_main.row_values(curr_row+1))

#print(len(se_main_list))
#print(se_main_title_list)
#print(se_main_list[0])


