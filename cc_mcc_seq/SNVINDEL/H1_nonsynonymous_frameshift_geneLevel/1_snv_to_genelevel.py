def uniqueList(inList):
    ouList=list()
    for item in inList :
        if item not in ouList :
            ouList.append(item)
    return ouList



def snv_level_to_gene_level(iFileList,oFile,sampleNum) :
    ouFile=open(oFile+'.geneLevel','w')
    dict1=dict()
    list1=list()
    for item in iFileList :
        inFile=open(item)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            dict1.setdefault(fields[0],[0]*sampleNum)
            list1.append(fields[0])
            for i,item in enumerate(fields[-sampleNum:]) :
                dict1[fields[0]][i]+=int(item)
        inFile.close()
    for item in uniqueList(list1) :
        ouFile.write(item+'\t'+'\t'.join([str(x) for x in dict1[item]])+'\n')
    ouFile.close()

snv_level_to_gene_level(['SNV.exome.somatic.nonsynonymous','INDEL.exome.somatic.frameshift'],'somatic.nonsynonymous.frameshift',8)

