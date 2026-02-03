import shutil
import os
import csv
from pathlib import Path
#from src.groupD_tool.parsing_files import write_fasta_tsv

from jinja2 import Environment, FileSystemLoader


OUTPUT_FILE_NAME = 'Results.html'
TEMPLATE_NAME = 'HTML_template.HTML'


#class/jinja2 example from here: https://brandonjay.dev/posts/2021/write-html-in-python-with-jinja2


class HtmlGenerator(object):
    def __init__(self, template_name: str = "HTML_template.HTML"):
        module_dir = Path(__file__).resolve().parent
        template_dir = module_dir/"template"

        self.env = Environment(loader=FileSystemLoader(str(template_dir)))
        self.template_name = template_name
    
    #tsvfile.write(f"\nread_count : {RC}\naverage_length : {average_len}\ntotal_bases : {AL}")
    def read_tsv(self, tsv_path: str): 
        with open(tsv_path, newline="") as f: 
            reader = csv.DictReader(f, delimiter="\t")
            rows = list(reader)
            columns = reader.fieldnames or []
            
        return columns, rows


    #function will insert the read count/total bases/average length only in the fasta as this is not calculated for the FASTQ 
    #it is not in the table as the value should be the same for all samples
    #should join to the results dir that contains the tsv files and create new sub folder containing the html pages
    #uses the html template found in template/

    def generate(self, tsv_path:str, file_form:str, output_path: str, html_name: str, filename:str, rc:int, tb:int, al:float):
        if rc != 0:
            results_dir = os.path.join(output_path, 'Results_html')
            os.makedirs(results_dir, exist_ok=True)

            rc = f"read count is : {rc}"
            tb = f"total bases is : {tb}"
            al = f"average length is : {al}"
            

            columns, rows = self.read_tsv(tsv_path)
            template = self.env.get_template(self.template_name)
            html = template.render(title = "QC Results", columns=columns, rows=rows, n_samples = len(rows), tsv_name=os.path.basename(tsv_path), file_form=file_form, filename = filename, rc = rc, tb = tb, al = al)

            out_path = os.path.join(results_dir, html_name)
            with open(out_path, "w", encoding="utf-8") as html_file: 
                html_file.write(html)
            #print(f"results in report found at: {out_path}")
            return out_path
        
        else: 
            results_dir = os.path.join(output_path, 'Results_html')
            os.makedirs(results_dir, exist_ok=True)
            

            columns, rows = self.read_tsv(tsv_path)
            template = self.env.get_template(self.template_name)
            html = template.render(title = "QC Results", columns=columns, rows=rows, n_samples = len(rows), tsv_name=os.path.basename(tsv_path), file_form=file_form, filename=filename)

            out_path = os.path.join(results_dir, html_name)
            with open(out_path, "w", encoding="utf-8") as html_file: 
                html_file.write(html)
            #print(f"results in report found at: {out_path}")
            return out_path


