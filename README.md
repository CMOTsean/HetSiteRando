# HetSiteRando
site based heterozygous randomiser to prepare SNP alignments for phylogeny construction

##Running the script
Run the script like so: python site_based_het_randomizer.py infile outfile

##I/O
Infile: multi-sample vcf file
Outfile: FASTA containing entries for each sample in the vcf file of equal length

##Description
This tool was created for the use case where you want to create a SNP-based tree for a diploid and heterozygous organism. In this case we have to resolve heterozygous sites to either the reference or alternate allele. 
In some cases, researchers randomly choose REF or ALT for each sample at each site. An issue occurs here where two samples which are both heterozygous at a site now have a 0.25 chance of having different alleles called, despite identical genotypes.
This can artificially lengthen branches in phylogenies, particularly at the tips, and might bias trees even more where there is a range in zygosity.
This tool sets it so ALL heterozygous samples at a given site are called the same (REF or ALT).
