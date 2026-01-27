import pytest
from src.yourtool.parsing_files import FASTQ, FASTQ_Qual, FASTA

##FASTA 
def test_avg_len():
    fa = FASTA('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/contigs.fasta')
    assert fa.avg_len == 68

def test_summary_row():
    fa = FASTA('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/contigs.fasta')
    assert fa.summary == [{'num_sequences': 2, 'average_length': 68.0}] ## set the value here - ask annalise 

def test_write_fasta_tsv():
    with pytest.raises(TypeError):
        fa=FASTA.records('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/contigs.fasta')

### FASTQ
def test_total_bases():
    fq = FASTQ("/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq")
    assert fq.total_bases == 48

def test_gc_content():
    fq =FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.gc_fraction == 54.16666793823242

def test_base_composition():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.base_composition == {'A':13, 'C':14, 'G':12, 'T':9, 'N': 0}

def test_A_count():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.A_count == 13

def test_C_count():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.C_count == 14

def test_G_count():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.G_count == 12

def test_T_count():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.T_count == 9

def test_N_count():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.N_count == 0

def test_fastq_avg_len():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.avg_len == 12

#THIS IS HOW it works with property
def test_phred_score():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.phred_score == 0

def test_fastq_qual_sum():
    fq = FASTQ_Qual('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/tests/sampleA.fastq')
    assert fq.read_info() == (4, 48, 40.0, 1)
"""
def test_fastq_qual_bases():
    fqq = FASTQ_Qual()
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    assert fqq.qual_bases == 48

def test_fastq_qual_q30():
    fqq = FASTQ_Qual()
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    assert fqq.q30_bases == 48

def test_mean_quality():
    fqq = FASTQ_Qual()
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    qsum = fqq.qual_sum
    qbases = fqq.qual_bases
    assert FASTQ_Qual.mean_quality(qsum, qbases) == 40.0 

def test_q30_frac():
    fqq = FASTQ_Qual()
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    q30 = fqq.q30_bases
    qbases = fqq.qual_bases
    assert FASTQ_Qual.mean_quality(q30, qbases) == 1.0
     
def test_read_fasta():
    fa = FASTA('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/contigs.fasta')
    assert fa.read_fasta == (2, ['chr1', 'chr2'], [68, 68], [50.0, 50.0], [4, 4]       """






#assert fq.N_count == {'A':13, 'C':14, 'G':12, 'T':9, 'N': 0}