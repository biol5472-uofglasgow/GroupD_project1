import json
import datetime
from . import main


#tool versions, parameters, timestamps ect: 
def write_json(): 
    j_data = {"tool": "groupD_tool", 
              "tool version": "0.1.0", 
              "date and time":datetime.datetime.now(),
              "input file(s)" : main.args.folder_path, 
              "output file(s)": main.args.output_path}

    return j_data

x = write_json()
print(json.dumps(j_data, default=default))







