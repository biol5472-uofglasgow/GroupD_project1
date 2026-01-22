# from Bio.Seq import SeqIO
# from Bio.Seq import Seq, MutableSeq
import argparse
import logging
from main import main #importing our main.py file's functions

'''
Setting up argparser to take in arguments at the terminal
'''
parser = argparse.ArgumentParser(description=' \n', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('folder_path', help='Input the pathway to the folder containing your fasta/fastq files.\n') #remember to put in checks/exceptions for files in folder that may not be fasta or fastq
parser.add_argument('output_path', help= 'The pathway to the folder to store the output files') #User can specify folder pathway for output files tobe stored
parser.add_argument('log_name', help= 'The name for the log', default='FastaFastQParser') #user can specify the log file name
args = parser.parse_args()

#calling main function/method from main.py, using args input at terminal
if __name__ == '__main__':
    main(args)
