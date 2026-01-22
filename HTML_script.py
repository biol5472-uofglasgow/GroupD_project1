import shutil
import os

from jinja2 import Environment
from jinja2 import FileSystemLoader


TEMPLATE_NAME = 'sample_template.html'
OUTPUT_FILE_NAME = 'sample_output.html'


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


if __name__ == '__main__':
    html_generator = HtmlGenerator(TEMPLATE_NAME)
    html_generator.generate()


# to save the results
#with open("my_new_file.html", "w") as fh:
#    fh.write(output_from_parsed_template)