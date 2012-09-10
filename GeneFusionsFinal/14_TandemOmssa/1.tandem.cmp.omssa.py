inFile=open('Tandem.FDR.pep.genefusions.final.pos.3.3')

D1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    pep=fields[0]
    D1.setdefault(pep,[0,0])
    D1[pep][0]=int(fields[1])
inFile.close()

inFile=open('Omssa.FDR.pep.genefusions.final.pos.3.3')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    pep=fields[0]
    D1.setdefault(pep,[0,0])
    D1[pep][1]=int(fields[1])
inFile.close()

ouFile=open('Tandem.Omssa.FDR.pep.genefusions.final.pos.3.3','w')
ouFile1=open('Tandem.not.Omssa.FDR.pep.genefusions.final.pos.3.3','w')
ouFile2=open('Tandem.Omssa.not.FDR.pep.genefusions.final.pos.3.3','w')
for key in D1 :
    if D1[key][0] > 0 and D1[key][1] > 0 :
        ouFile.write(key+'\t'+str(D1[key][0])+'\t'+str(D1[key][1])+'\n')
    if D1[key][0] == 0 and D1[key][1] > 0 :
        ouFile1.write(key+'\t'+str(D1[key][0])+'\t'+str(D1[key][1])+'\n')
    if D1[key][0] > 0 and D1[key][1] == 0 :
        ouFile2.write(key+'\t'+str(D1[key][0])+'\t'+str(D1[key][1])+'\n')



ouFile.close()
ouFile1.close()
ouFile2.close()




