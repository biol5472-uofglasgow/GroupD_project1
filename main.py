import logging
import os
import pyfastx
from parsing_files import FastQ_Typing



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

    from parsing_files import FASTQ, FASTQ_Qual

    '''
    Setting accepted filetypes and folder path variables

    '''
    folder_path = args.folder_path
    output_path = args.output_path
    fasta_filetypes = '' #making sure they are strings
    fasta_filetypes = ('.fasta', '.fasta.gz')

    fastq_filetypes = '' #making sure they are strings
    fastq_filetypes = ('.fastq', '.fastq.gz')


    if not os.path.isdir(folder_path):
        logger.error(f'Input path {args.output_path} could not be found. Please check your input and try again\n')
        raise SystemExit(1) #validating that input folder path exists, add error checking and logging, need to make these if statements and system exit if false
    
    output_path = args.output_path

    if not os.path.isdir(output_path):#
        logger.error(f'Output path {args.output_path} could not be found. Please check your input and try again\n')
        raise SystemExit(1) #validating that output folder path exists, add error checking logging etc later


    def fasta_reader(fastafile: str):

        for filename in os.listdir(folder_path):
            if filename.endswith(fasta_filetypes):
                try:
                    fasta_file = pyfastx.Fasta(os.path.join(folder_path, filename))
                    logger.info(f'{filename}') #logs the file names to the log, I made a test folder to test that this works
                    #make error checking to verify the folder paths exists and are valid

                    #Import the class and function that parses fasta and execute here
                    logger.info(f'The file {filename} will work')
                    #this will be replaced with the class.function() for fasta parsing
                    # print(FASTQ.avg_len(file))
                except RuntimeError as e:
                    logger.info(f'The file {filename} could not be read. Error: {e}') #log the error
                    break

            elif not filename.endswith(fasta_filetypes):
                logger.info(f'The file {filename} could not be read by the fasta reader') #log the file name of the non fasta/fastq file
                pass #skip over

    def fastq_reader(fastqfile: str):
        #     if filename.endswith(fastq_filetypes):
        try:
            fq = pyfastx.Fastq(os.path.join(folder_path, fastqfile))
            logger.info(f'{fastqfile}') #logs the file names to the log, I made a test folder to test that this works
            #make error checking to verify the folder paths exists and are valid

            #Import the class and function that parses fasta and execute here
            logger.info(f'The file {fastqfile} will be parsed')
            #this will be replaced with the class.function() for fasta parsing
            print(FASTQ.total_bases(fq))

        except RuntimeError as e:
            logger.info(f'The file {fastqfile} could not be read. Error: {e}') #log the error
            pass

        # if not filename.endswith(fasta_filetypes):
        #     logger.info(f'The file {filename} could not be read by the fasta reader') #log the file name of the non fasta/fastq file
        #     pass #skip over


    for filename in os.listdir(folder_path):
        if filename.endswith(fasta_filetypes):
            fasta_reader(fastafile=filename)
            print(f'Fasta file {filename} has been parsed')
            continue
        
        
        if filename.endswith(fastq_filetypes):
            fastq_reader(fastqfile=filename)
            print(f'Fastq file {filename} has been parsed')
            continue
        



 


    