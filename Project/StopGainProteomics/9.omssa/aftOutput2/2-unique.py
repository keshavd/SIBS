inFile = open('3-stopgain-protein')
ouFile = open('3-stopgain-protein-unique2','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D = {}
    for item in fields[1:]:
        x = ':'.join([item.split(':')[0],item.split(':')[2],item.split(':')[3]])
        D[x]=1
    ouFile.write(fields[0]+'\t')
    d = D.items()
    d.sort(cmp=lambda x,y:cmp(int(x[0].split(':')[-1]),int(y[0].split(':')[-1])))
    for item in d:
        ouFile.write(item[0]+'\t')
    ouFile.write('\n')
inFile.close()
ouFile.close()
