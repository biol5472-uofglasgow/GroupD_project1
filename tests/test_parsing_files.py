import pytest
from parsing_files import FASTQ, FASTQ_Qual, FASTA

def test_total_bases():
    fq = FASTQ("/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq")
    assert fq.total_bases == 48

def test_gc_content():
    fq =FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert fq.gc_fraction == 54.16666793823242

def test_N_count():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert fq.N_count == 0

def test_fastq_avg_len():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert fq.avg_len == 12

#THIS IS HOW it works with property
def test_phred_score():
    fq = FASTQ('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert fq.phred_score == 0

def test_fastq_qual_sum():
    fq = FASTQ_Qual('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fq.read_info(fq)
    assert fq.read_count == 1920

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


def test_avg_len():
    fa = FASTA('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/contigs.fasta')
    assert fa.avg_len == 68


def test_read_fasta():
    fa = FASTA('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/contigs.fasta')
    assert fa.read_fasta == (2, ['chr1', 'chr2'], [68, 68], [50.0, 50.0], [4, 4]) 
