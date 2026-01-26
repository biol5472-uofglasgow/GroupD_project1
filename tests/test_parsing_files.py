import pytest
from parsing_files import File
from parsing_files import FASTQ
from parsing_files import FASTQ_Qual
from parsing_files import Fasta

def test_file_format():
    path = ("/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq")
    assert File.file_format(path) == "FASTQ"

def test_fASTQ_format():
    path = ("/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/contigs.fasta")
    assert File.file_format(path) == "FASTA"

def test_total_bases():
    fq = FASTQ.FASTQ_path("/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq")
    assert FASTQ.total_bases(fq) == 48

def test_gc_content():
    fq =FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert FASTQ.gc_content(fq) == 54.16666793823242

def test_N_cont():
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert FASTQ.N_cont(fq) == {'A':13, 'C':14, 'G':12, 'T':9, 'N': 0}

def test_avg_len():
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert FASTQ.avg_len(fq) == 12

def test_phred_score():
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    assert FASTQ.phred_score(fq) == 0

def test_fastq_qual_sum():
    fqq = FASTQ_Qual()
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    assert fqq.qual_sum == 1920

def test_fastq_qual_bases():
    fqq = FASTQ_Qual()
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    assert fqq.qual_bases == 48

def test_fastq_qual_q30():
    fqq = FASTQ_Qual()
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    assert fqq.q30_bases == 48

def test_mean_quality():
    fqq = FASTQ_Qual()
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    qsum = fqq.qual_sum
    qbases = fqq.qual_bases
    assert FASTQ_Qual.mean_quality(qsum, qbases) == 40.0

def test_q30_frac():
    fqq = FASTQ_Qual()
    fq = FASTQ.FASTQ_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/sampleA.fastq')
    fqq.read_info(fq)
    q30 = fqq.q30_bases
    qbases = fqq.qual_bases
    assert FASTQ_Qual.mean_quality(q30, qbases) == 1.0

def test_avg_len():
    fa = Fasta.fasta_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/contigs.fasta')
    assert Fasta.avg_len(fa) == 68

def test_read_fasta():
    fa = Fasta.fasta_path('/Users/amritatrehan/Desktop/Software_proj/GroupD_project1/contigs.fasta')
    assert Fasta.read_fasta(fa) == (2, ['chr1', 'chr2'], [68, 68], [50.0, 50.0], [4, 4]) 
