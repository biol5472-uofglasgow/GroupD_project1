from Bio.Seq import SeqIO
from Bio.Seq import Seq, MutableSeq
import argparse
import logging

'''
Setting up argparser to take in arguments at the terminal
'''
parser = argparse.ArgumentParser(description=' \n', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('fasta_file', help='Input the fasta file name you want to parse')
parser.add_argument('fastaq_file', help='Input the vcf file name you want to parse\n')
parser.add_argument('', help= 'Input the fasta file name you want to parse')
parser.add_argument('output_prefix', help='Input the name for output')
args = parser.parse_args()

'''
Logging setup
Logs information, errors, etc in a file
'''

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'{args.output_prefix}.log')
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter('%(levelname)s - %(asctime)s - %(message)s'))
logger.addHandler(fh)