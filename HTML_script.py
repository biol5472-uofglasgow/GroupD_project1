import shutil
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader
#from parsing_files import Output

#Output.write_tsv


TEMPLATE_NAME = 'HTML_template.HTML'
OUTPUT_FILE_NAME = 'results.html'

# class from here: https://brandonjay.dev/posts/2021/write-html-in-python-with-jinja2
class HtmlGenerator(object):
    def __init__(self, template_name):
        self.template_name = template_name
        self.env = Environment(loader=FileSystemLoader('template'))

    def _build_path(self, suffix):
        # Build the full file path based on our current directory
        current_directory = os.getcwd()
        return os.path.join(current_directory, suffix)

    def generate(self):
        public_folder_path = self._build_path('public')
        # If the public folder exists, then throw it away so we can regenerate it
        if os.path.isdir(public_folder_path):
            shutil.rmtree(public_folder_path)
        os.mkdir(public_folder_path)

    def generate(self):
        public_folder_path = self._build_path('public')
        # If the public folder exists, then throw it away so we can regenerate it
        if os.path.isdir(public_folder_path):
            shutil.rmtree(public_folder_path)
        os.mkdir(public_folder_path)

        # Get Jinja template
        template = self.env.get_template(self.template_name)
        with open(self._build_path('public/%s' % OUTPUT_FILE_NAME), 'w') as html_file:
            html = template.render(title="Sample Page", content = "testing HTML")
            # Write the rendered template to the html file
            html_file.write(html)


if __name__ == '__main__':
    html_generator = HtmlGenerator(TEMPLATE_NAME)
    html_generator.generate()

    '''for line in results.tsv: #dont have yet
        with open('results.html', 'w', encoding="utf-8") as fh:
            fh.write(content)
            #print(f"wrote to {filename}")'''




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