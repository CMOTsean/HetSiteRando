#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:33:49 2022

@author: sean
"""

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import pandas as pd
import numpy as np
import os
import random 

random.seed = (12345)
sys.argv[1] == infile
sys.argv[2] == outfile
#sys.argv[2] == num_repeats
comment_lines=''

def skip_rows_count(filein_path):
    global comment_lines
    with open(filein_path, "r") as fin:
        count = 0
        for l in fin.readlines():
            if l.startswith("#"):
                count+=1
                comment_lines += l
            else:
                return count-1

def zygosity_check(sample):
    geno = sample[:3]
    if geno in ['./.', '.|.']:
        return 'no_call'
    elif geno in ['0/0', '0|0']:
        return 'homo_ref'
    elif geno[0] == geno[1]:
        return 'homo_alt'
    else:
        return 'het'

def select_base(row, samp_dict):
    if len(row['REF']) == 1 and len(row['ALT']) == 1:
        cur_rand = random.randint(0,1)
        for sample in samps:
            s_geno = zygosity_check(row[sample])
            if s_geno == 'homo_ref':
                samp_dict[sample] += row['REF']
            elif s_geno == 'homo_alt':
                samp_dict[sample] += row['ALT']
            elif s_geno == 'no_call':
                samp_dict[sample] += "-"
            elif s_geno == 'het':
                if cur_rand == 0:    
                    samp_dict[sample] += row['REF']
                elif cur_rand == 1:
                    samp_dict[sample] += row['ALT']


vcf = pd.read_csv(infile, sep="\t", skiprows=skip_rows_count(infile))
vcf.rename(columns={"#CHROM": "CHROM"}, inplace=True)
samps = list(vcf.columns[9:])

for m in range(1, 101):
    print("ROUND: "+str(m))
    samp_dict = {}
    for s in samps:
        samp_dict[s] = ''
        
    for i, r in vcf.iterrows():
        select_base(r, samp_dict)
    
    list_of_seqs=[]
    for s in samps:
        list_of_seqs.append(SeqRecord(Seq(samp_dict[s]), id=s))
    
    SeqIO.write(list_of_seqs, outfile, "fasta")


    
    