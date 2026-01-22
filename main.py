import logging
import os
from parsing_files import FASTQ, FASTQ_Qual, Fasta


#Where it is decided whether the file is fasta or fastq and set down the appropriate pathway for parsing
def main(args):

    '''
    Logging setup
    Logs information, errors, etc in a file
    '''

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(f'{args.log_name}.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter('%(levelname)s - %(asctime)s - %(message)s'))
    logger.addHandler(fh)

    
    if not os.path.isdir(args.folder_path):
        logger.error(f'Input path {args.output_path} could not be found. Please check your input and try again\n')
        raise SystemExit(1) #validating that input folder path exists, add error checking and logging, need to make these if statements and system exit if false

    if not os.path.isdir(args.output_path):#
        logger.error(f'Output path {args.output_path} could not be found. Please check your input and try again\n')
        raise SystemExit(1) #validating that output folder path exists, add error checking logging etc later

    
    for filename in os.listdir(args.folder_path): #gets all the files inside the folder specified at the CLI
        logger.info(f'{filename}') #logs the file names to the log, I made a test folder to test that this works
        #make error checking to verify the folder paths exists and are valid

        if filename.endswith() not in ('fasta', 'fasta.gz', '.fastq', 'fastq.gz'):
            logger.info(f'The file {filename} could not be read') #log the file name of the non fasta/fastq file
            pass #skip over

        if filename.endswith in ('.fasta', '.fasta.gz') == True:
            #Import the class and function that parses fasta and execute here
            logger.info(f'The file {filename} will work')
             #this will be replaced with the class.function() for fasta parsing
        if filename.endswith in ('.fastq', '.fastq.gz') == True:
            logger.info(f'The file {filename} will work')  #this will be replaced with the class.function() for fastq parsing
            print(FASTQ.avg_len)
            print(FASTQ_Qual.mean_quality)


    #put parsers in classes in another file, and then in for loop here, determine if file is fasta or fastq and execute the appropriate parser functions
    #

 


    