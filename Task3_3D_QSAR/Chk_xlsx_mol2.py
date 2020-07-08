import xlrd,xlwt
import os

wb_main = xlrd.open_workbook('../data/static/所有数据_20200709.xlsx')
print('###this xlsx file contain sheets:###')
print(wb_main.sheet_names())
input()

se_main = wb_main.sheet_by_name('20200708(pIC+uM)')
nrow_main, ncol_main = se_main.nrows, se_main.ncols
# print(nrow_main, ncol_main)

se_main_rowlist = []
se_main_title_list1 = se_main.row_values(0)[1:]
se_main_title_list2 = se_main.row_values(1)[1:]
#se_main_title_list1[0] = 'NO'
for nom in range(len(se_main_title_list1)-1):
    if se_main_title_list1[nom+1] == '':
        se_main_title_list1[nom+1] = se_main_title_list1[nom]
se_main_title_list3 = [se_main_title_list1[i]+'-'+se_main_title_list2[i] for i in range(len(se_main_title_list1))]
if False:
    print(se_main_title_list1)
    print(se_main_title_list2)
    print(se_main_title_list3)

for curr_row in range(nrow_main-2):
    # input(se_main.row_values(curr_row))
    #row_value = se_main.row_values(curr_row)
    #print('row%s value is %s' %(curr_row, row_value))
    se_main_rowlist.append(se_main.row_values(curr_row+2))
se_main_rowlist.pop()
if False:
    print(se_main_rowlist[0])
    print(se_main_rowlist[-1])


'''
se_main_collist = []
for curr_col in range(ncol_main):
    #row_value = se_main.row_values(curr_row)
    #print('row%s value is %s' %(curr_row, row_value))
    se_main_collist.append(se_main.col_values(curr_col)[1:])
'''

se_main_collist = [[row[i] for row in se_main_rowlist] for i in range(ncol_main)]
#print(se_main_collist[0])

all = [item[:-5] for item in os.listdir('../data/temp/good_mol2_v3.mdb') if item.endswith('mol2')]
in_all_not_in_xlsx = []
for item in all:
    if item not in se_main_collist[0]:
        in_all_not_in_xlsx.append(item)
in_xlsx_not_in_all = []
for item in se_main_collist[0][:-1]:
    if item not in all:
        in_xlsx_not_in_all.append(item)

print('###following item found in mol2, not in xlsx:###')
print(in_all_not_in_xlsx)
paper_ianix = list(set([item[:item.rindex('-')] for item in in_all_not_in_xlsx]))
paper_ianix.sort()
print('###following paper contain item found in mol2, not in xlsx:###')
print(paper_ianix)
for item in paper_ianix:
    continue
    print(item)
paper_ixnia = list(set([item[:item.rindex('-')] for item in in_xlsx_not_in_all]))
paper_ixnia.sort()
print('###following item found in xlsx, not in mol2:###')
print(paper_ixnia)
for item in paper_ixnia:
    continue
    print(item)
#print(paper_ianix,paper_ixnia)

print('################################################################')
print('###interity chk finished, next generate IC/EC data for subset###')
print('################################################################')

subset_folders = [item for item in os.listdir('../data/temp/subset/')]
print('###following subsets found in temp folder###')
print(subset_folders)
for subset_folder in subset_folders:
    mol2_files = [item[:-5] for item in os.listdir('../data/temp/subset/'+subset_folder+'/') if item.endswith('.mol2')]
    subset_data_row = [item for item in se_main_rowlist if item[0] in mol2_files]
    subset_data_col = [[row[i] for row in subset_data_row] for i in range(len(subset_data_row[0]))]
    out_lists = []
    for title in se_main_title_list3:
        title_no = se_main_title_list3.index(title)
        out_lists.append([title,['name',title]])
        for item in mol2_files:
            for item2 in subset_data_row:
                if item == item2[0] and item2[title_no+1] != '':
                    out_lists[-1].append([item,item2[title_no+1]])
        out_lists[-1].append(len(out_lists[-1])-2)
    out_lists.sort(reverse=True, key=lambda item:item[-1])
    for lists in out_lists[:6]:
        print(len(lists))
        lists[0] = lists[0].replace('μ','u')
        lists[0] = lists[0].replace('/', '-')
        out_file = open('../data/temp/subset/'+subset_folder+'/'+str(len(lists)-3)+'-'+subset_folder[:-4]+'-'+lists[0]+'.txt', 'a')
        for item in lists[1:-1]:
            print(item[0]+' '+str(item[1]),file=out_file)
    #input()
    if False:
        for item in out_lists:
            print(item)
        #input()
    if False:
        print(subset_folder, len(mol2_files))
        #print(subset_data_row)
        # print(subset_data_col[0])
        print(max([len(x) for x in [[item for item in col if item != ''] for col in subset_data_col[1:]]]))
