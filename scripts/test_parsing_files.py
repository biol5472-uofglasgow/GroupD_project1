import pytest
from parsing_files import File
from parsing_files import FASTQ
from parsing_files import FASTQ_Qual
from parsing_files import Fasta

def test_file_format():
    line = (">ACGT")
    assert File.file_format(line) == "FASTA"

def test_fASTQ_format():
    line = ("@ACGT")
    assert File.file_format(line) == "FASTQ"

def test_total_bases():
    fq = "ACTGACTG"
    assert FASTQ.total_bases(fq) == 8 