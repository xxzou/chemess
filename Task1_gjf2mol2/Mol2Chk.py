import zipfile

cord_mol2_zip = zipfile.ZipFile("../data/static/20200703_RE.zip", "r")
cord_mol2_namelist = []
for filename in cord_mol2_zip.namelist():
    if filename.endswith('.mol2'):
        cord_mol2_namelist.append(filename)

def find_sign_lines(file_str_list):
    #print(file_str_list)
    ATOM_sign_line = file_str_list.index('@<TRIPOS>ATOM')
    BOND_sign_line = file_str_list.index('@<TRIPOS>BOND')
    return ATOM_sign_line, BOND_sign_line

def probe_content(llist):
    print(llist[0])
    for item in llist[1]:
        print(item)
    for item in llist[2]:
        print(item)

def find_common_carbon(detail_list):
    for atom_info in detail_list[1]:
        for bond_info in detail_list[2]:
            if atom_info[0] in bond_info[1:3] and abnormal_carbon[0] in bond_info[1:3]:
                for bond_info in detail_list[2]:
                    if atom_info[0] in bond_info[1:3] and abnormal_carbon[1] in bond_info[1:3]:
                        return atom_info[0]
    return False

def find_6_member_ring(detail_list):
    ### gen map_list
    atom_no_list = [item[0] for item in detail_list[1]]
    bond_no_list = [item[1:3] for item in detail_list[2]]
    map_list = []
    for atom_no in atom_no_list:
        map_atom_list = []
        for bond_pair in bond_no_list:
            if atom_no in bond_pair:
                map_atom_list += bond_pair
        map_atom_list = list(set(map_atom_list))
        map_atom_list.remove(atom_no)
        map_list.append(map_atom_list)
    if False:
        print(detail_list[0])
        print(atom_no_list)
        print(bond_no_list)
        print(map_list)

    ### find_6_ring
    six_ring_list = []
    for atom_1 in atom_no_list:
        atom_2_list = list(map_list[int(atom_1)-1])
        for atom_2 in atom_2_list:
            atom_3_list = list(map_list[int(atom_2)-1])
            atom_3_list.remove(atom_1)
            if not atom_3_list:
                continue
            for atom_3 in atom_3_list:
                atom_4_list = list(map_list[int(atom_3) - 1])
                atom_4_list.remove(atom_2)
                if not atom_4_list:
                    continue
                for atom_4 in atom_4_list:
                    atom_5_list = list(map_list[int(atom_4) - 1])
                    atom_5_list.remove(atom_3)
                    if not atom_5_list:
                        continue
                    for atom_5 in atom_5_list:
                        atom_6_list = list(map_list[int(atom_5) - 1])
                        atom_6_list.remove(atom_4)
                        if not atom_6_list:
                            continue
                        for atom_6 in atom_6_list:
                            atom_7_list = list(map_list[int(atom_6) - 1])
                            atom_7_list.remove(atom_5)
                            if not atom_7_list:
                                continue
                            if atom_1 in atom_7_list:
                                ring_set = {atom_1,atom_2,atom_3,atom_4,atom_5,atom_6}
                                if ring_set not in six_ring_list:
                                    six_ring_list.append(ring_set)
    return(six_ring_list)


def rewrite(file_str_list,ATOM_sign_line,detail_list):
    out_text = '@<TRIPOS>MOLECULE\n'
    out_text += detail_list[0][12:-5]+'\n'
    out_text += '\n'.join(file_str_list[2:ATOM_sign_line])
    out_text += '\n@<TRIPOS>ATOM\n'
    out_text += '\n'.join(['\t\t'.join(item) for item in detail_list[1]])
    out_text += '\n@<TRIPOS>BOND\n'
    out_text += '\n'.join(['\t\t'.join(item) for item in detail_list[2]])
    out_text += '\n'
    f_out = open('../data/temp/good_mol2_v2/'+detail_list[0][12:-5]+'.mol2','a')
    print(out_text, file=f_out)
    f_out.close()
    # input()




for filename in cord_mol2_namelist:
    source_mol2 = cord_mol2_zip.read(filename)
    file_str_list = source_mol2.decode().split('\n')
    # file_str_list = source_mol2.decode().split('\r\n')
    # print(file_str_list)
    # input(len(source_mol2.decode().split('\n')))
    ATOM_sign_line, BOND_sign_line = find_sign_lines(file_str_list)

    detail_list = [filename]
    detail_list.append([item.split() for item in file_str_list[ATOM_sign_line+1:BOND_sign_line]])
    detail_list.append([item.split() for item in file_str_list[BOND_sign_line+1:-1]])

    for bond_info in detail_list[2]:
        if bond_info[-1] == 'am':
            bond_info[-1] = '1'

    #probe_content(detail_list)
    #input()

    ### FIND ABNORMAL CARBON

    #print(detail_list[0])
    non_ar_carbon = [atom_info[0] for atom_info in detail_list[1] if atom_info[1] == 'C' and atom_info[5] != 'C.ar']
    abnormal_carbon = [atom_no for atom_no in non_ar_carbon
                       if sum([int(bond_info[3]) for bond_info in detail_list[2] if atom_no in bond_info[1:3] and bond_info[3].isdigit()]) != 4]

    if abnormal_carbon and len(abnormal_carbon)!=2:
        print(detail_list[0]+' different than 2 abnormal carbon!')
        print(abnormal_carbon)

    ### FIND 6 RING

    six_ring_list = find_6_member_ring(detail_list)


    ### SWITCH SINGLE BOND AND DOUBLE BOND
    ### NOT ENOUGH
    '''
    if abnormal_carbon and len(abnormal_carbon)==2:
        common_carbon_no = find_common_carbon(detail_list)
        if not common_carbon_no:
            print(detail_list[0])
    '''

    ### MODIFY ABNORMAL RING

    sign_1 = False
    for ring_set in six_ring_list:
        if not sign_1 and ring_set > set(abnormal_carbon):
            sign_1 = True
            for atom_no in ring_set:
                for atom_info in detail_list[1]:
                    if atom_info[0] == atom_no:
                        atom_info[5] = atom_info[5][0]+'.ar'
                for bond_info in detail_list[2]:
                    if set(bond_info[1:3]) < ring_set:
                        bond_info[3] = 'ar'
    if not sign_1:
        print(detail_list[0]+' abnormal not in 6 ring!')


    ### WRITE OUTPUT
    rewrite(file_str_list, ATOM_sign_line, detail_list)


