import pytest
import pyfastx
from groupD_tool.parsing_files import FASTQ, FASTQ_Qual, FASTA, write_fasta_tsv

##FASTA 
def test_avg_len():
    fa = FASTA('tests/contigs.fasta')
    assert fa.avg_len == 68

def test_summary_row():
    fa = FASTA('tests/contigs.fasta')
    assert fa.summary == [{'num_sequences': 2, 'average_length': 68.0}] 

def test_main_fasta():
    with pytest.raises(RuntimeError):
        FASTA('tests/force_error_tests/false_contigs.fasta')

def test_write_fasta_tsv_null():
    records = []
    assert write_fasta_tsv(records, "out.tsv") is None

def test_write_fasta_tsv():
    with pytest.raises(TypeError):
        records = [2, 3]
        write_fasta_tsv(records, "out.tsv")

def test_write_empty_fasta_tsv():
    with pytest.raises(TypeError):
        records = [{}, {}]
        write_fasta_tsv(records, "out.tsv")    

def test_read_counting():
    fa = FASTA('tests/contigs.fasta')
    assert fa.read_counting == (2, 136)

def test_average_len():
    fa = FASTA('tests/contigs.fasta')
    assert fa.average_len == (68)

### FASTQ
def test_total_bases():
    fq = FASTQ("tests/sampleA.fastq")
    assert fq.total_bases == 48

def test_gc_content():
    fq =FASTQ('tests/sampleA.fastq')
    assert fq.gc_fraction == 54.16666793823242

def test_base_composition():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.base_composition == {'A':13, 'C':14, 'G':12, 'T':9, 'N': 0}

def test_A_count():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.A_count == 13

def test_C_count():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.C_count == 14

def test_G_count():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.G_count == 12

def test_T_count():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.T_count == 9

def test_N_count():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.N_count == 0

def test_fastq_avg_len():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.avg_len == 12

#THIS IS HOW it works with property
def test_phred_score():
    fq = FASTQ('tests/sampleA.fastq')
    assert fq.phred_score == 0

def test_iter_reads():
    fq = FASTQ_Qual('tests/sampleA.fastq')
    reads = list(fq.iter_reads())
    assert reads == [('readA1', 'ACGTACGTACGT', 'IIIIIIIIIIII'), ('readA2', 'ACGTACGTACGA', 'IIIIIIIIIIII'), ('readA3', 'ACGTACGTACGG', 'IIIIIIIIIIII'), ('readA4', 'ACGTACGTACCC', 'IIIIIIIIIIII')]

def test_fastq_qual_sum():
    fq = FASTQ_Qual('tests/sampleA.fastq')
    assert fq.read_info() == (4, 48, 40.0, 1)





#assert fq.N_count == {'A':13, 'C':14, 'G':12, 'T':9, 'N': 0}
