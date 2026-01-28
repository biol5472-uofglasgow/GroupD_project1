import json
import os 
import datetime



#tool versions, parameters, timestamps ect: 
def write_json(folder_path, output_path):
    j_data = {"tool": "groupD_tool", 
                "tool version": "0.1.0", 
                "date and time":datetime.datetime.now(),
                "input file(s)": os.listdir(folder_path), 
                "output file(s)": os.listdir(output_path)}
    

    out_path = os.path.join(output_path, "run.json")
    with open (out_path, "w") as f: 
        f.write(json.dumps(j_data,indent=4, sort_keys=True, default=str))

    return out_path






