import os
import re

def find_dipole(line):
    global dipole
    ifline = lastline
    ifline = ifline.replace('Dipole moment (field-independent basis, Debye):',
                              'Dipole moment (field-independent basis, Debye):@')
    if ifline != lastline:
        dipole = line[84:104]
        

def find_polarizability(line):
    outline = line.replace('Exact polarizability:',
                              'Exact polarizability:@\t')
    if outline != line:
        outfile.write(outline)

def ifstart_find_Frequencies(line):
    global if_find_Freq
    ifline = line
    ifline = ifline.replace('Harmonic frequencies',
                              'Harmonic frequencies@')
    if ifline != line:
        if_find_Freq = 1
def ifend_find_Frequencies(line):
    global if_find_Freq
    global Freq
    ifline = line
    ifline = ifline.replace('Thermochemistry',
                              '@Thermochemistry')
    if ifline != line:
        if_find_Freq = 0                            
def find_Frequencies(line):
    global Freq
    outline = line.replace('Frequencies --','')
    if outline != line:
        Freq = Freq + outline[:-1]

def find_Molecular_mass(line):
    outline = line.replace('Molecular mass:',
                              'Molecular mass:@\t')
    outline = line.replace('amu',
                              '')
    if outline != line:
        outfile.write(outline)

def find_CV_E(line):
    ifline = lastlastline
    ifline = ifline.replace('CV',
                              'CV@')
    if ifline != lastlastline:
        CV = line[31:50]
        S = line[50:69]
        outfile.write('HeatCapacity'+'\t'+str(float(CV))+'\n')
        outfile.write('Entropy'+'\t'+str(float(S))+'\n')

def find_RMS(line):
    global RMS
    ifline = line
    ifline = ifline.replace('Cartesian Forces:',
                              'Cartesian Forces:@')
    if ifline != line:
        RMS = line[43:59]

def find_SCF_ZeroPoint(line):
    global SCFfile
    global SCF
    global ZeroPoint
    ifline = lastline
    ifline = ifline.replace('ZeroPoint',
                              'ZeroPoint@')
    if ifline != lastline:    
        SCFline = lastlastline[1:-1]+lastline[1:-1]+line[1:-1]
        SCFline = SCFline.replace( '|','\n')
        print(SCFline,file=SCFfile)
        SCFfile.close()
        SCFfile = open(filename[:-3]+"SCFfile", "r",encoding='utf-8')
        for line2 in SCFfile:
            ifline = line2
            ifline = ifline.replace('HF=',
                              'HF=@')
            if ifline != line2:
                SCF = line2[3:-1]
            ifline2 = line2
            ifline2 = ifline2.replace('ZeroPoint=',
                              'ZeroPoint=@')
            if ifline2 != line2:
                ZeroPoint = line2[10:-1]
        SCFfile.close()
        
            

    
    
        
for file in os.listdir(os.getcwd()):
    if file.endswith(('.out')):
        filename = os.getcwd() + '\\' + file
        infile = open(filename,'r',encoding='utf-8')
        outfile = open(filename[:-3]+"out.txt", "w",encoding='utf-8')
        SCFfile = open(filename[:-3]+"SCFfile", "w",encoding='utf-8')
        print(infile)
        lastline = ''
        lastlastline = ''
        Freq = ''
        if_find_Freq = 0
        CV = ''
        S = ''
        dipole = ''
        RMS = ''
        SCF = ''
        ZeroPoint = ''
        
        for line in infile:
            find_dipole(line)
            find_polarizability(line)
            find_Molecular_mass(line)
            find_CV_E(line)
            find_RMS(line)
            find_SCF_ZeroPoint(line)
            if if_find_Freq == 0:
                ifstart_find_Frequencies(line)
            if if_find_Freq == 1:
                find_Frequencies(line)
                ifend_find_Frequencies(line)
            
            lastlastline = lastline
            lastline = line
        outfile.write('dipole'+'\t'+str(float(dipole))+'\n')
        outfile.write('RMS Force'+'\t'+str(float(RMS))+'\n')
        outfile.write('SCF Energy'+'\t'+str(SCF)+'\n')
        outfile.write('Zero-Point Energy'+'\t'+str(ZeroPoint)+'\n')
        outfile.write('Frequencies'+'\t'+Freq)
        
            
        infile.close()
        outfile.close()
        SCFfile.close()
