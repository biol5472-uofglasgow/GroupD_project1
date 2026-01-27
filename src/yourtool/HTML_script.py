import shutil
import os
import csv

from jinja2 import Environment, FileSystemLoader


OUTPUT_FILE_NAME = 'Results.html'
TEMPLATE_NAME = 'HTML_template.HTML'


#class/template example from here: https://brandonjay.dev/posts/2021/write-html-in-python-with-jinja2
#and documentation from here : https://jinja.palletsprojects.com/en/stable/api/#basics 
#to create tables/table design: https://www.w3schools.com/html/html_tables.asp


class HtmlGenerator(object):
    def __init__(self, template_name: str, template_dir: str):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template_name = template_name

    def _build_path(self, suffix:str)->str:
        current_directory = os.getcwd()
        return os.path.join(current_directory, suffix)
    
    def read_tsv(self, tsv_path: str): 
        with open(tsv_path, newline="") as f: 
            reader = csv.DictReader(f, delimiter="\t")
            rows = list(reader)
            columns = reader.fieldnames or []
        return columns, rows

    def generate(self, tsv_path:str, file_form:str):
        public_folder_path = self._build_path('Results')
        
        if os.path.isdir(public_folder_path):
            shutil.rmtree(public_folder_path)
        os.mkdir(public_folder_path)

        columns, rows = self.read_tsv(tsv_path)
        template = self.env.get_template(self.template_name)
        html = template.render(title = "QC Results", columns=columns, rows=rows, n_samples = len(rows), tsv_name=os.path.basename(tsv_path), file_form=file_form)

        out_path = self._build_path(f"Results/{OUTPUT_FILE_NAME}")
        with open(out_path, "w", encoding="utf-8") as html_file: 
            html_file.write(html)
        print(f"results in report found at: {out_path}")
        return out_path


