cd /netshare1/home1/szzhongxin/proj1/hansun/samtools/CHR

ICC4A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/4A/4A.bam
ICC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/5A/5A.bam
ICC9A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/9A/9A.bam
ICC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/10A/10A.bam

CHC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/5A/5A.bam
CHC6A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/6A/6A.bam
CHC7A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/7A/7A.bam
CHC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/10A/10A.bam


ICC4B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/4B/4B.bam
ICC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/5B/5B.bam
ICC9B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/9B/9B.bam
ICC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/10B/10B.bam

CHC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/5B/5B.bam
CHC6B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/6B/6B.bam
CHC7B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/7B/7B.bam
CHC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/10B/10B.bam

chr='chr21'


#samtools mpileup -uDf /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta -r $chr $ICC4A $ICC5A $ICC9A $ICC10A $CHC5A $CHC6A $CHC7A $CHC10A  $ICC4B $ICC5B $ICC9B $ICC10B $CHC5B $CHC6B $CHC7B $CHC10B > tmp.raw.${chr}.bcf
bcftools view -bvcg tmp.raw.${chr}.bcf > var.raw.${chr}.bcf
bcftools view var.raw.${chr}.bcf | vcfutils.pl varFilter  > var.flt.${chr}.vcf 
