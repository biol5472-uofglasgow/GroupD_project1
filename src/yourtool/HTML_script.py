import shutil
import os
import csv
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


OUTPUT_FILE_NAME = 'Results.html'
TEMPLATE_NAME = 'HTML_template.HTML'


#class/template example from here: https://brandonjay.dev/posts/2021/write-html-in-python-with-jinja2


class HtmlGenerator(object):
    def __init__(self, template_name: str, template_dir: str):
        module_dir = Path(__file__).resolve().parent
        template_dir = module_dir.parent.parent/"template"

        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template_name = template_name
    
    def read_tsv(self, tsv_path: str): 
        with open(tsv_path, newline="") as f: 
            reader = csv.DictReader(f, delimiter="\t")
            rows = list(reader)
            columns = reader.fieldnames or []
        return columns, rows

    def generate(self, tsv_path:str, file_form:str):
        results_dir = os.path.join('Results')
        os.makedirs(results_dir, exist_ok=True)

        columns, rows = self.read_tsv(tsv_path)
        template = self.env.get_template(self.template_name)
        html = template.render(title = "QC Results", columns=columns, rows=rows, n_samples = len(rows), tsv_name=os.path.basename(tsv_path), file_form=file_form)

        out_path = os.path.join(f"Results/{OUTPUT_FILE_NAME}")
        with open(out_path, "w", encoding="utf-8") as html_file: 
            html_file.write(html)
        #print(f"results in report found at: {out_path}")
        return out_path


