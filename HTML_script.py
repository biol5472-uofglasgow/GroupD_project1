import shutil
import os
import csv

from jinja2 import Environment, FileSystemLoader


OUTPUT_FILE_NAME = 'Results.html'
TEMPLATE_NAME = 'HTML_template.HTML'


#class/template example from here: https://brandonjay.dev/posts/2021/write-html-in-python-with-jinja2
#and documentation from here : https://jinja.palletsprojects.com/en/stable/api/#basics 
#to create tables: https://www.w3schools.com/html/html_tables.asp
#also: https://medium.com/@KRVPerera/using-jinja-to-generate-html-pages-3fb54cf8fbc8 

class HtmlGenerator(object):
    def __init__(self, template_name: str, template_dir: str):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template_name = template_name

    def _build_path(self, suffix:str)->str:
        # Build the full file path based on our current directory
        current_directory = os.getcwd()
        return os.path.join(current_directory, suffix)
    
    def read_tsv(self, tsv_path: str): 
        with open(tsv_path, newline="") as f: 
            reader = csv.DictReader(f, delimiter="\t")
            rows = list(reader)
            columns = reader.fieldnames or []
        return columns, rows

    def generate(self, tsv_path:str):
        public_folder_path = self._build_path('public')
        # If the public folder exists, then throw it away so we can regenerate it
        if os.path.isdir(public_folder_path):
            shutil.rmtree(public_folder_path)
        os.mkdir(public_folder_path)

        columns, rows = self.read_tsv(tsv_path)
        template = self.env.get_template(self.template_name)
        html = template.render(title = "QC Results", columns=columns, rows=rows, n_samples = len(rows), tsv_name=os.path.basename(tsv_path))

        out_path = self._build_path(f"public/{OUTPUT_FILE_NAME}")
        with open(out_path, "w", encoding="utf-8") as html_file: 
            html_file.write(html)
        print(f"results in report found at: {out_path}")


if __name__ == '__main__':
    tsv_path = "results.tsv"
    
    html_generator = HtmlGenerator(template_dir="template", TEMPLATE_NAME = 'HTML_template.HTML')
    html_generator.generate(tsv_path)

