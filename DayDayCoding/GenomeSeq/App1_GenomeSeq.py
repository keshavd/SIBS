from GenomeSeqClass import GenomeSeq 
gs=GenomeSeq()
#gs.quality_pass_012_csv('sum_snp.exome_summary.csv',10)
#gs.quality_pass_012_csv('sum_snp2.exome_summary.csv',10)
#gs.select_no_synonymous_no_unknown('sum_snp.exome_summary.pass012')
#gs.select_no_synonymous_no_unknown('sum_snp2.exome_summary.pass012')
###gs.multi_calling_split('sum_snp.exome_summary.pass012.nonsynonymous',[-10],['10A'])
#gs.multi_calling_split('sum_snp.exome_summary.pass012.nonsynonymous',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['10A','1A','2A','3A','4A','5A','6A','7A','8A','9A'])
#gs.plot_snv_number([7058,8631,8542,8737,8735,8846,8791,8789,8933,7900])


#gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.nonsynonymous.1A','sum_snp3.exome_summary.pass012.nonsynonymous.1B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB')
#gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.nonsynonymous.4A','sum_snp3.exome_summary.pass012.nonsynonymous.4B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB')
#gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.nonsynonymous.5A','sum_snp3.exome_summary.pass012.nonsynonymous.5B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.5AB')
#gs.tumor_minus_normal_to_somatic('sum_snp.exome_summary.pass012.nonsynonymous.9A','sum_snp3.exome_summary.pass012.nonsynonymous.9B','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.9AB')
#gs.combine_single_somatic(['sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.5AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.9AB'],'sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB')

#gs.snv_level_to_gene_level('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB',4)
#gs.gene_two_group_ranksum_test('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB.gene_level',[-4,-3,-2],[-3,-2,-1])
#gs.gene_two_group_ranksum_test_matshow('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB.gene_level',50,['1A','4A','5A','9A'])
gs.gene_significant_mutated('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1459AB.gene_level',[-4,-3,-2,-1])

#gs.venn_diagram('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.5AB',filename='set3.venn.pdf',setname1='tumor',setname2='normal',setname3='dbsnp')
#gs.venn_diagram('sum_snp13.exome_summary.pass012.nonsynonymous.somatic.1AB','sum_snp13.exome_summary.pass012.nonsynonymous.somatic.4AB',filename='set2.venn.pdf',setname1='tumor',setname2='dbsnp')


#gs.make_false_normal_calling_out('sum_snp.exome_summary.csv','sum_snp34.exome_summary.csv',110)
#d={'SAMD11  chr1    877831  877831  T       C       2':[1,2,3,4],'SAMD12  chr1    87731  87731  T       C       2':[3,4,5,6],'SAMD13  chr10    877831  877831  T       C       2':[5,6,7,8],'SAMD11  chr9    87781  87781  T       C       2':[10,11,12,13]}
#gs.sort_dict_by_chrom_postition(d,'haha')
