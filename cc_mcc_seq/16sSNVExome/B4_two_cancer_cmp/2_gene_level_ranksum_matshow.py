from PyPlot.PyPlotClass import *

score=1

def gene_heatmap(iFile,sampleNameList,oFile,figsize=0,rowList=[]) :
    geneList=list()
    list1=list()
    row=0
    inFile=open(iFile)
    if rowList:
        for line in inFile :
            row+=1
            if row in rowList :
                line=line.strip()
                fields=line.split('\t')
                geneList.append(fields[1])
                list1.append([int(x) for x in fields[-8:]])
    else:
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            N=[int(x) for x in fields[-8:]]
            if sum(N[0:4])-sum(N[4:8])>score or sum(N[0:4])-sum(N[4:8])<-score:
                geneList.append(fields[1])
                print(fields[1])
                list1.append([int(x) for x in fields[-8:]])
    inFile.close()
    list2 = []
    gList = []
    gList2 = []
    inFile = open('SNV.exome.somatic.nonsynonymous')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] in geneList and fields[0] not in gList2:
            gList.append(fields[1]+':'+fields[0])
            gList2.append(fields[0])
            list2.append(list1[geneList.index(fields[0])])
    inFile.close()
    pp=PyPlot(oFile)
    if figsize:
        pp.heatmap(list2,xLabel=sampleNameList,yLabel=gList,row=False,col=False,figsize=figsize,grid=True)
    else:
        pp.heatmap(list2,xLabel=sampleNameList,yLabel=gList,row=False,col=False,grid=True)

gene_heatmap('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'matshow.somatic.nonsynonymous_1_30.pdf',rowList=range(1,31))
gene_heatmap('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'matshow.somatic.nonsynonymous_diff.pdf',figsize=(12,24))


#gene_heatmap('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(1,500),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_1_1451.pdf',figsize=(8,40))
#gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(61,91),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_61_90.pdf')
#gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(91,121),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_91_120.pdf')
#gene_matshow('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test',range(121,151),['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'somatic.nonsynonymous_121_150.pdf')
