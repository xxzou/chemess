import zipfile

cord_mol2_zip = zipfile.ZipFile("../data/static/20200703_RE.zip", "r")
cord_mol2_namelist = []
for filename in cord_mol2_zip.namelist():
    if filename.endswith('.mol2'):
        cord_mol2_namelist.append(filename)

def find_sign_lines(file_str_list):
    ATOM_sign_line = file_str_list.index('@<TRIPOS>ATOM')
    BOND_sign_line = file_str_list.index('@<TRIPOS>BOND')
    return ATOM_sign_line, BOND_sign_line

def probe_content(llist):
    print(llist[0])
    for item in llist[1]:
        print(item)
    for item in llist[2]:
        print(item)



for filename in cord_mol2_namelist:
    source_mol2 = cord_mol2_zip.read(filename)
    file_str_list = source_mol2.decode().split('\n')
    # input(len(source_mol2.decode().split('\n')))
    ATOM_sign_line, BOND_sign_line = find_sign_lines(file_str_list)

    detail_list = [filename]
    detail_list.append([item.split() for item in file_str_list[ATOM_sign_line+1:BOND_sign_line]])
    detail_list.append([item.split() for item in file_str_list[BOND_sign_line+1:-1]])

    #probe_content(detail_list)
    #input()

    non_ar_carbon = [atom_info[0] for atom_info in detail_list[1] if atom_info[1] == 'C' and atom_info[5] != 'C.ar']
    abnormal_carbon = [atom_no for atom_no in non_ar_carbon if sum([int(bond_info[3]) for bond_info in detail_list[2] if atom_no in bond_info[1:3]]) != 4]
    print(detail_list[0])
    print(abnormal_carbon)
    input()