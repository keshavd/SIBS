import sys
import string
from math import ceil

Codon = {}
inFile = open('/netshare1/home1/people/hansun/Data/CodonUsage')
for line in inFile:
    line = line.strip()
    fields = line.split()
    Codon[fields[0]]=fields[1]
inFile.close()

HG = {}
inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        HG[line1]=line2
    else:
        break
inFile.close()

def translate(seq,start,end,FROM,TO):
    # start,end:count from 1.
    six = []
    trans = string.maketrans('atcgATCG','tagcTAGC')
    if seq[start-1:end].upper()== FROM:
        seq_to = seq[0:start-1]+TO+seq[end:]
        seq_rev = string.translate(seq[::-1],trans)
        seq_to_rev = string.translate(seq_to[::-1],trans)

        for i in range(3):
            pep = []
            for j in range(i,len(seq),3):
                c = seq[j:j+3].upper()
                if len(c) == 3:
                    pep.append(Codon[c])
            s = start - i
            e = end - i 
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])
        for i in range(3):
            pep = []
            for j in range(i,len(seq_rev),3):
                c = seq_rev[j:j+3].upper()
                if len(c) == 3:
                    pep.append(Codon[c])
            s = len(seq_rev) - end + 1 - i
            e = len(seq_rev) - start + 1 - i
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])

        end = start + len(TO) - 1
        for i in range(3):
            pep = []
            for j in range(i,len(seq_to),3):
                c = seq_to[j:j+3].upper()
                if len(c) == 3:
                    pep.append(Codon[c])
            s = start - i
            e = end - i 
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])
        for i in range(3):
            pep = []
            for j in range(i,len(seq_to_rev),3):
                c = seq_to_rev[j:j+3].upper()
                if len(c) == 3:
                    pep.append(Codon[c])
            s = len(seq_to_rev) - end + 1 - i
            e = len(seq_to_rev) - start + 1 - i
            six.append([''.join(pep),int(ceil(s/3.0)),int(ceil(e/3.0))])

        return six

    else:
        print('warning:'+'\t'+seq+'\t'+str(start)+'\t'+str(end)+'\t'+FROM+'\t'+TO)

#six = translate('CAGCACCTCCCTGATGGGGACAAAACGCCCATGTCCGAGCGGCTGGACGACACGGAGCCCTATTTCATCGGGATCTTTTGCTTCGAGGCAGGGATCAAA',)
#six = translate('CCGAGGCAGGGATCAAAGATCAGCCTA',11,15,'GATCA','AT')
#six = translate('CCGAGGCAGGGATCAAAGATCAGCCTA',11,11,'G','A')
#print(six)

L = 40


def snv_indel(inF):
    inFile = open(inF)
    ouFile = open(inF+'.pep','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[26]
        FROM = fields[29].upper()
        TOs = fields[30].upper().split(',')
        start = int(fields[27])
        end = int(fields[27])+len(FROM)-1
        s = start - L -1
        e = end + L
        seq = HG[ch][s:e]
        for TO in TOs:
            six = translate(seq, L+1, L+len(FROM), FROM, TO)
            for i in range(6):
                ouFile.write('>'+ch+':'+str(start)+':'+str(end)+':'+FROM+':'+TO+':'+'REF-'+str(i)+':'+str(six[i][1])+':'+str(six[i][2])+':'+six[i][0][six[i][1]-1:six[i][2]]+'\n')
                ouFile.write(six[i][0]+'\n')
                ouFile.write('>'+ch+':'+str(start)+':'+str(end)+':'+FROM+':'+TO+':'+'ALT-'+str(i)+':'+str(six[i+6][1])+':'+str(six[i+6][2])+':'+six[i+6][0][six[i+6][1]-1:six[i+6][2]]+'\n')
                ouFile.write(six[i+6][0]+'\n')
    inFile.close()
    ouFile.close()

    snv_indel_splicing(inF)

def snv_indel_splicing(inF):
    RefGene = {}
    inFile = open('refGene-2013-04-22.txt')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        RefGene.setdefault(line,[[fields[2],fields[3]]])
        starts = fields[9].split(',')
        ends = fields[10].split(',')
        for i in range(len(starts)-1):
            RefGene[line].append([int(starts[i]),int(ends[i])])
    inFile.close()

    inFile = open(inF)
    ouFile = open(inF+'.pep','a')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[26]
        FROM = fields[29].upper()
        TOs = fields[30].upper().split(',')
        start = int(fields[27])
        end = int(fields[27])+len(FROM)-1
        for k in RefGene:
            if ch == RefGene[k][0][0]:
                for j in range(1,len(RefGene[k])):
                    if RefGene[k][j][1] - L < end < RefGene[k][j][1]:
                        try:
                            s1 = start - L -1
                            e1 = RefGene[k][j][1] 
                            s2 = RefGene[k][j+1][0]  
                            e2 = RefGene[k][j+1][0] + L-(RefGene[k][j][1]-end)
                            seq = HG[ch][s1:e1]+HG[ch][s2:e2]
                            for TO in TOs:
                                six = translate(seq, L+1, L+len(FROM), FROM, TO)
                                for i in range(6):
                                    ouFile.write('>'+ch+':'+str(start)+':'+str(end)+':'+FROM+':'+TO+':'+'Splicing-REF-'+str(i)+':'+str(six[i][1])+':'+str(six[i][2])+':'+six[i][0][six[i][1]-1:six[i][2]]+'\n')
                                    ouFile.write(six[i][0]+'\n')
                                    ouFile.write('>'+ch+':'+str(start)+':'+str(end)+':'+FROM+':'+TO+':'+'Splicing-ALT-'+str(i)+':'+str(six[i+6][1])+':'+str(six[i+6][2])+':'+six[i+6][0][six[i+6][1]-1:six[i+6][2]]+'\n')
                                    ouFile.write(six[i+6][0]+'\n')
                        except:
                            print('Warning:\t'+line)
                            print('Warning:\t'+k)

                    elif RefGene[k][j][0] < start < RefGene[k][j][0] + L:
                        try:
                            s1 = RefGene[k][j-1][1]-(L - (start - RefGene[k][j][0])) -1
                            e1 = RefGene[k][j-1][1] 
                            s2 = RefGene[k][j][0]  
                            e2 = end + L
                            seq = HG[ch][s1:e1]+HG[ch][s2:e2]
                            for TO in TOs:
                                six = translate(seq, L+1, L+len(FROM), FROM, TO)
                                for i in range(6):
                                    ouFile.write('>'+ch+':'+str(start)+':'+str(end)+':'+FROM+':'+TO+':'+'Splicing-REF-'+str(i)+':'+str(six[i][1])+':'+str(six[i][2])+':'+six[i][0][six[i][1]-1:six[i][2]]+'\n')
                                    ouFile.write(six[i][0]+'\n')
                                    ouFile.write('>'+ch+':'+str(start)+':'+str(end)+':'+FROM+':'+TO+':'+'Splicing-ALT-'+str(i)+':'+str(six[i+6][1])+':'+str(six[i+6][2])+':'+six[i+6][0][six[i+6][1]-1:six[i+6][2]]+'\n')
                                    ouFile.write(six[i+6][0]+'\n')
                        except:
                            print('Warning:\t'+line)
                            print('Warning:\t'+k)


    inFile.close()
    ouFile.close()


snv_indel('sum_snv.exome_summary.nonsynonymous-splicing')
snv_indel('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing')
snv_indel('sum_snv.exome_summary.indel')
snv_indel('sum_snv.exome_summary.indel.overall.filter')


