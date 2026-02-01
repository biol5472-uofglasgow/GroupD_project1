import logging
import os
import pyfastx
import json
import datetime
from .parsing_files import FASTQ, FASTQ_Qual, FASTA, write_fasta_tsv, write_fastq_tsv, process_fastq
from typing import Any
from .HTML_script import HtmlGenerator




#tool versions, parameters, timestamps ect: 
def write_json(folder_path:str, output_path:str):
    j_data = {"tool": "groupD_tool", 
                "tool version": "0.1.0", 
                "date and time":datetime.datetime.now(),
                "input file(s)": os.listdir(folder_path), 
                "output file(s)": os.listdir(output_path)}
    
    out_path = os.path.join(output_path, "run.json")
    with open (out_path, "w") as f: 
        f.write(json.dumps(j_data,indent=4, sort_keys=True, default=str))

    return out_path


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
                logger.info(f'Parsing file: {filename}')
                records = fa.records
                al = fa.avg_len
                rc, tb =  fa.read_counting
              

                out_file = os.path.join(
                    output_path,
                    f"{os.path.splitext(filename)[0]}_records.tsv"
                )

                records: list[dict[str, Any]]

        
                write_fasta_tsv(records, out_file)
                logger.info(f'Output written to {out_file}')

                

                hfile = os.path.splitext(filename)[0]
                html_name = (f"{hfile}.html")
                html = HtmlGenerator(template_name="HTML_template.HTML") 
                file_form = "FASTA"
                html.generate(out_file, file_form, output_path, html_name, filename, rc, tb, al) 

            elif filename.endswith(fastq_filetypes):

                out_file = os.path.join(
                    output_path,
                    f"{os.path.splitext(filename)[0]}.tsv"
               )

                process_fastq(full_path, out_file, filename)
                logger.info(f'Output written to {out_file}')
                
                hfile = os.path.splitext(filename)[0]
                html_name = (f"{hfile}.html")
                html = HtmlGenerator(template_name="HTML_template.HTML") 
                file_form = "FASTQ"
                html.generate(out_file, file_form, output_path, html_name, filename, rc = 0, tb = 0, al = 0)
                
  
        except RuntimeError as e:
            logger.info(f'The file {filename} could not be read. Error: {e}') #log the error
            raise SystemExit(1) # NOTE, wondering if you guys think SystemExit here is appropriate? Do we want to stop running if a file is broken? or just skip over it?



    json_path = write_json(folder_path = args.folder_path, output_path = args.output_path)
    logger.info(f"json written to {json_path}")


