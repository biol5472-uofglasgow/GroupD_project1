# Group D Project 1


## Project 1 — FASTA/FASTQ QC metrics (per-sample table)

Goal: Compute basic QC metrics per input file/sample and write a cohort table suitable for a report.

Summary: Reads one or more FASTA/FASTQ files, computes basic quality control (QC)
metrics per sample (e.g. number of sequences/reads, total bases, length stats, GC%, 
N-content; for FASTQ optionally mean quality score), and outputs a per-sample results 
table


## Input files    

The file(s) run from the terminal need to be in a folder to be run.    
They can be in either FASTA or FASTQ format.      

### <ins> Fasta files </ins>
- Header line starts with '>'
- Contains sequence data


### <ins> Fastq file </ins>     
Header line starts with '@'
Sequence line
Separator line '+', sometimes followed by sequence identifier


## Output files   

Multiple files will be output into a specified folder     
This will contain a tsv file, a run.json, and an additional folder containing HTML link(s)       

### <ins> The tsv results file </ins>    
For FASTA files a table containing one row per sample, with columns such as: 
- sample ID
- sample length
- gc fraction
- A/C/T/G count
- N count 
      

For FASTQ files a table containing one row per sample, with columns such as:  
- filename
- total bases 
- GC fraction
- average length
- phred score 
- nucleotide base counts
- read count
- number of bases with a quality score over 30
- mean quality 
- the fraction of bases with a quality score of over 30



### <ins> The run.json file </ins>     
This should contain:    
- the tool name and version  
- the date and time of the run
- input files
- output files  

### <ins> The HTML folder </ins>    
A sub-folder containing the HTML link(s) should be produced that contains tables from the TSV


## How to run
run using this format: 

set up a virtual environment in python:       
```
python -m venv .venv
source .venv/bin/activate
pip install -U pip
```    


install the tool with:      
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps groupD_tool  
```   

view help and arguments:     
```
groupD_tool -h
```      
or:     

```
groupD_tool --help
```      


running the tool:      
```
groupD_tool <input_folder> <output_folder> --log_name <log_name>
```    
     

- where --input_folder is the folder containing the fasta/fastq files you want to test
- and --output_folder is where you wish the results to be output to
- and --log_name is the name you wish to call the log    


For example: 
```
groupD_tool /path/to/samples_folder /path/to/Results/ --log_name log
```      

## How to run tests

Running unit and integration tests with hatch

```
hatch test
```

Tested on python 3.9.23


## Libraries used: 
- pyfastx version 2.3.0
- jinja2 version 3.1.6
- mypy for type checking (not included in install package)
- testing

