import argparse

from . import main

'''
Setting up argparser to take in arguments at the terminal
'''
def cli(): 
  parser = argparse.ArgumentParser(description=' \n', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('folder_path', help='Input the pathway to the folder containing your fasta/fastq files.\n')
  parser.add_argument('output_path', help= 'Input the pathway to the folder you want to store the output files') #User can specify folder pathway for output files to be stored
  parser.add_argument('--log_name', help= 'Input the name you want to use for the log file', default='FastaFastQParser') #user can specify the log file name
  args = parser.parse_args()

# calling the functions from main.py
  main.main(args)
