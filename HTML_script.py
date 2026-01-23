import shutil
import os
import csv

from jinja2 import Environment, FileSystemLoader

#from parsing_files import Output
#Output.write_tsv


TEMPLATE_NAME = 'HTML_template.HTML'
OUTPUT_FILE_NAME = 'Results.html'

#class/template example from here: https://brandonjay.dev/posts/2021/write-html-in-python-with-jinja2
#and documentation from here : https://jinja.palletsprojects.com/en/stable/api/#basics 
#to create tables: https://www.w3schools.com/html/html_tables.asp
class HtmlGenerator(object):
    def __init__(self, template_name: str, template_dir: str):
        self.template_name = template_name
        self.env = Environment(loader=FileSystemLoader(template_dir))

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
        print(f"results in report : {out_path}")
                               


"""
        # Get Jinja template
        template = self.env.get_template(self.template_name)
        with open(self._build_path('public/%s' % OUTPUT_FILE_NAME), 'w') as html_file:
            html = template.render(title="Sample Page", content = "testing HTML")
            # Write the rendered template to the html file
            html_file.write(html)"""


if __name__ == '__main__':
    tsv_path = "results.tsv"
    html_generator = HtmlGenerator(template_dir="template", template_name=TEMPLATE_NAME)
    html_generator.generate(tsv_path)



# to save the results
#with open("my_new_file.html", "w") as fh:
#    fh.write(output_from_parsed_template)
#---------- OR ------------------------------


"""
import csv
import os
import pandas as pd
def tsv2html(tsv_file_name, html_file_name):
    df = pd.read_csv(tsv_file_name,sep='\t', header=0)
    old_width = pd.get_option('display.max_colwidth')
    pd.set_option('display.max_colwidth', -1)  

    with open(html_file_name,'w') as html_file:
        html_file.write(df.to_html(index=False))
    pd.set_option('display.max_colwidth', old_width)

if __name__ == "__main__":
   tsv2html(results.tsv, results.html)"""