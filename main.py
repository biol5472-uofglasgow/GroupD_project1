import logging
import os


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

    #if fasta ->
    if not os.path.isdir(args.folder_path):
        raise SystemExit(1) #validating that input folder path exists, add error checking and logging, need to make these if statements and system exit if false

    if not os.path.isdir(args.output_path):
        raise SystemExit(1) #validating that output folder path exists, add error checking logging etc later



    for filename in os.listdir(args.folder_path): #gets all the files inside the folder specified at the CLI
        logger.info(f'{filename}') #logs the file names to the log, I made a test folder to test that this works
        #make error checking to verify the folder paths exists and are valid


    #if fastq ->