dict1=dict()
inFile=open('FDR.pep.annotated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=1
inFile.close()

inFile=open('FDR.pep.contaminated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[0] in dict1 :
        print(fields[0])
inFile.close()


