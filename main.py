import logging
import os
import pyfastx
from parsing_files import FASTQ, FASTQ_Qual, FASTA, write_fasta_tsv, write_fastq_tsv, process_fastq
from typing import Any
from HTML_script import HtmlGenerator



def main(args):

    '''
    Logging setup
    Logs information, errors, etc in a file
    '''

    logger = logging.getLogger(__name__)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        fh = logging.FileHandler(f'{args.log_name}.log')
        fh.setLevel(logging.INFO)
        fh.setFormatter(logging.Formatter('%(levelname)s - %(asctime)s - %(message)s'))
        logger.addHandler(fh)


    '''
    Setting accepted filetypes and folder path variables

    '''
    folder_path = args.folder_path
    output_path = args.output_path
    fasta_filetypes = '' #making sure they are strings
    fasta_filetypes = ('.fasta', '.fasta.gz', '.fa')

    fastq_filetypes = '' #making sure they are strings
    fastq_filetypes = ('.fastq', '.fastq.gz')


    '''
    Validating folder paths

    '''
                    
    if not os.path.isdir(folder_path):
        logger.error(f'Input path {folder_path} could not be found. Please check your input and try again\n')
        raise SystemExit(1) #validating that input folder path exists, add error checking and logging, need to make these if statements and system exit if false

    if not os.path.isdir(output_path):#
        logger.error(f'Output path {output_path} could not be found. Please check your input and try again\n')
        raise SystemExit(1) #validating that output folder path exists, add error checking logging etc later


    '''
    Defining output actions per file
    
    '''

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)


        try:
            if filename.endswith(fasta_filetypes):
                fa = FASTA(full_path)
                logger.info(f'{filename}') #logs the file names to the log, I made a test folder to test that this works
                #make error checking to verify the folder paths exists and are valid
                logger.info(f'The file {filename} will work')
                #this will be replaced with the class.function() for fasta parsing
                fa = FASTA(full_path)
                records = fa.records

                out_file = os.path.join(
                    output_path,
                    f"{os.path.splitext(filename)[0]}_records.tsv"
                )

                records: list[dict[str, Any]]
                # records = [record]

        
                write_fasta_tsv(records, out_file)
                html = HtmlGenerator(template_name="HTML_template.html", template_dir="template")
                file_form = "FASTA"
                html.generate(filename, file_form)

            elif filename.endswith(fastq_filetypes):

                out_file = os.path.join(
                    output_path,
                    f"{os.path.splitext(filename)[0]}.tsv"
                )

                process_fastq(full_path, out_file, filename)
                
                html = HtmlGenerator(template_name="HTML_template.html", template_dir="template")
                file_form = "FASTQ"
                html.generate(filename, file_form)
                
            
        except RuntimeError as e:
            logger.info(f'The file {filename} could not be read. Error: {e}') #log the error
            raise SystemExit(1) # NOTE, wondering if you guys think SystemExit here is appropriate? Do we want to stop running if a file is broken? or just skip over it?


'''

NOTE to myself for tomorrow's workflow:

Each file does output information now, but missing some columns, check on columns for each output.
Loop mean_qual and q30_fraction in to fastq output and make sure it's as expected
'''
#         def fastq_reader(filename: str):
#             #     if filename.endswith(fastq_filetypes):
#             try:
#                 fa = pyfastx.Fastq(os.path.join(folder_path, filename))
#                 logger.info(f'{fq}') #logs the file names to the log, I made a test folder to test that this works
#                 #make error checking to verify the folder paths exists and are valid

#                 #Import the class and function that parses fasta and execute here
#                 logger.info(f'The file {fq} will be parsed')
#                 #this will be replaced with the class.function() for fasta parsing

#                 #this is where we will loop in the output write function once its ready!
#                 print(fq.total_bases())
#                 print(fq.gc_fraction())
#                 print(fq.N_cont())
#                 print(fq.avg_len())
#                 print(fq.phred_score())
#                 print(fq.read_info())

#             except RuntimeError as e:
#                 logger.info(f'The file {fq} could not be read. Error: {e}') #log the error
#                 pass



# for filename in os.listdir(folder_path):
#     if filename.endswith(fasta_filetypes):
#         fa = pyfastx.Fasta(os.path.join(folder_path, filename))
#         with open(f'{filename}_output.tsv') as output:
#             #name of new file, how to grab the name of the original file
#             output.write(fasta_reader(fa))
#             print(f'Fasta file {fa} has been parsed')
#             continue


#     if filename.endswith(fastq_filetypes):
#         fq = pyfastx.Fastq(os.path.join(folder_path, filename))
#         fastq_reader(fq)
#         print(f'Fastq file {filename} has been parsed')
#         continue

           
    # def FASTA_write_tsv(self, fasta_read_count, samp_id, fasta_total, fasta_gc, n_count, fasta_av_len):
    #         fa = pyfastx.Fastq(os.path.join(folder_path, filename))
    #         with open(f'{filename}_output.tsv') as output:
    #             output.write('Sample_ID\tn_seqs_of_reads\ttotal_bases\tmean_len\tgc_fraction\tn_fraction\n')
    #             output.write(f"{samp_id}\t{fasta_read_count}\t\t{fasta_total}\tt{fasta_av_len}\t\t{fasta_gc}\t\t{n_count}\n")
                            

    # def FASTQ_write_tsv(self, meanq_data, qual30_data):
    #     with open('results.tsv', 'w') as output_table:
    #         output_table.write(f'Mean_Quality\tqual_over_30\n')
    #     #Output mean_qual and qual over 30

