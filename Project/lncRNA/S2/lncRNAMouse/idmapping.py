def myset(mylist):
    list1=list()
    for item in mylist :
        if item not in list1 :
            list1.append(item)
    return list1


inFile1=open('lncrna_mouse_ucsc/lncrna_ucsc_mouse','r')

inFile1.readline()
inFile1.readline()

dict1=dict()
for line in inFile1 :
    fields=line.split('\t')
    key=fields[12].upper()
    dict1.setdefault(key,[])
    dict1[key].append(fields[12])
    dict1[key].append(fields[1])
inFile1.close()


'''
for key in dict1 :
    idset=set(dict1[key])
    print(key+'\t'+'\t'.join(idset))
'''
import sys

inFile2=open(sys.argv[1],'r')

ouFile1=open(sys.argv[1]+'_mapped','w')
ouFile2=open(sys.argv[1]+'_unmapped','w')

for line in inFile2 :
    line=line.strip()
    lineUpper=line.upper()
    if lineUpper in dict1 :
        idset=myset(dict1[lineUpper])
        ouFile1.write(line+'\t'+'\t'.join(idset)+'\n')
    else :
        ouFile2.write(line+'\n')

inFile2.close()

ouFile1.close()
ouFile2.close()



