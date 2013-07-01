def pep(inF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[1] and fields[2] =='':
            D.setdefault(fields[1],[])
            D[fields[1]].append(0)
        elif fields[1]:
            D.setdefault(fields[1],[])
            D[fields[1]].append(1)
        if fields[2]:
            D.setdefault(fields[2],[])
            D[fields[2]].append(2)
        if fields[3]:
            D.setdefault(fields[3],[])
            D[fields[3]].append(3)
        fds = fields[4].split(':')
        i = 4
        for item in fds:
            D.setdefault(item,[])
            D[item].append(i)
            i += 1
    inFile.close()
    ouFile = open(inF+'.pep','w')
    for k in D:
        if sum(D[k])==0:
            ouFile.write(k+'\n')
    ouFile.close()

pep('KR-0.2013_05_31_15_31_15_qry.peptides-pep')
pep('K-0.2013_05_31_15_31_15-2_qry.peptides-pep')
pep('ED-0.2013_05_31_16_23_30-3_qry.peptides-pep')
