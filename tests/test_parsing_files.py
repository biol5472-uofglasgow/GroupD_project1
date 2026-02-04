import pytest
import os
import pyfastx
import json
from groupD_tool.main import main
from collections import namedtuple
from groupD_tool.parsing_files import FASTQ, FASTQ_Qual, FASTA, write_fasta_tsv

'''
Setting up context fixtures for which files are being tested
'''
@pytest.fixture
def FASTA_fixture():
    return FASTA('tests/contigs.fasta')

@pytest.fixture
def FASTQ_fixture():
    return FASTQ('tests/sampleA.fastq')

@pytest.fixture
def FASTQ_Qual_fixture():
    return FASTQ_Qual('tests/sampleA.fastq')


'''
Unit testing of functions utilizing sample fixture files
'''
##FASTA 
def test_avg_len(FASTA_fixture):
    fa = FASTA_fixture
    assert fa.avg_len == 68

def test_main_fasta():
    with pytest.raises(RuntimeError):
        FASTA('tests/force_error_tests/false_contigs.fasta')

def test_write_fasta_tsv_null():
    records = []
    assert write_fasta_tsv(records, "out.tsv") is None

def test_write_fasta_tsv():
    with pytest.raises(TypeError):
        records = [2, 3]
        write_fasta_tsv(records, "out.tsv") #type: ignore

def test_write_empty_fasta_tsv():
    with pytest.raises(TypeError):
        records = [{}, {}]
        write_fasta_tsv(records, "out.tsv")    

def test_read_counting(FASTA_fixture):
    fa = FASTA_fixture
    assert fa.read_counting == (2, 136)

### FASTQ
def test_total_bases(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.total_bases == 48

def test_gc_content(FASTQ_fixture):
    fq =FASTQ_fixture
    assert fq.gc_fraction == 54.16666793823242

def test_base_composition(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.base_composition == {'A':13, 'C':14, 'G':12, 'T':9, 'N': 0}

def test_A_count(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.A_count == 13

def test_C_count(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.C_count == 14

def test_G_count(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.G_count == 12

def test_T_count(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.T_count == 9

def test_N_count(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.N_count == 0

def test_fastq_avg_len(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.avg_len == 12

def test_phred_score(FASTQ_fixture):
    fq = FASTQ_fixture
    assert fq.phred_score == 0

def test_fastq_qual_sum(FASTQ_Qual_fixture):
    fq = FASTQ_Qual_fixture
    assert fq.read_info() == (4, 48, 40.0, 1)

'''
Integration test
Testing expected output files match what was output
and that sampleB output matches what we expect
'''
def test_main():
    try: #making sure that the output testing directory exists
        os.mkdir('IntegrationTestOutputs')

    except FileExistsError:
        pass
    #Set up
    ArgsType = namedtuple('ArgsType', 'folder_path output_path log_name')
    args = ArgsType(folder_path='tests', output_path='IntegrationTestOutputs', log_name='FastaFastQParser')

    #Here is the test 
    main(args)
    #Asserting that the actual output files match the expected and that all of the expected files are in the actual output
    expected_output_files = [
        "sampleB.tsv",
        "Results_html",
        "sampleA.tsv",
        "contigs_records.tsv"
    ]
    with open('IntegrationTestOutputs/run.json', 'r') as file:
        json_data = json.load(file)
        actual_output_files = json_data.get('output file(s)', [])
        for filename in actual_output_files:
            if filename != 'run.json':
                assert filename in expected_output_files
        for filename in expected_output_files:
            assert filename in actual_output_files
    #Asserting that the sampleB output is correct
    expected_sampleB_output = 'sampleB.fastq	60	50.0	15.0	33	14	14	14	14	4	4	60	 34.67	 0.87'
    with open('IntegrationTestOutputs/sampleB.tsv', 'r') as file:
        file.readline()
        actual_sampleB_output = file.readline().strip()
        assert expected_sampleB_output == actual_sampleB_output
    
