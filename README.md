# Group D project 1


## Collaborators 


## Project 1 — FASTA/FASTQ QC metrics (per-sample table)

Goal: Compute basic QC metrics per input file/sample and write a cohort table suitable for a report.

Summary: Reads one or more FASTA/FASTQ files, computes basic quality control (QC)
metrics per sample (e.g. number of sequences/reads, total bases, length stats, GC%, 
N-content; for FASTQ optionally mean quality score), and outputs a per-sample results 
table


## Input files 
### Fasta files 
- Header line starts with '>'
- Contains sequence data


### Fastq file
Header line starts with '@'
Sequence line
Separator line '+', sometimes followed by sequence identifier


## Output files 
### tsv file 
For FASTA files a table containing one row per sample, with columns such as: 
- sample ID
- number of sequences or reads
- total bases
- mean length
- gc fraction
- A/C/T/G count
- n fraction

For FASTQ files a table containing one row per sample, with columns such as: 
- filename
- mean quality 
- the fraction of bases with a quality score of over 30
- total bases 
- GC fraction
- average length 
- phred score 
- read count




### a run.json file: 
This should contain pipeline/tool versions, parameters, timestamp, etc

### HTML file
A HTML link should be produced that contains the tables produced


## How to run
run using this format: 

to set up the environment:       
```python -m venv .venv```          
```source .venv/bin/activate```   

install the tool with:     
```pip install -U pip```       
```pip install -e .```   

view help and arguments:     
```groupD_tool -h```      
```groupD_tool --help```      

To build the project:     
```python -m pip install -U build```     
```python -m build```     


run the tool:      
```groupD_tool --input_folder --output_folder --log_name```   

- where --input_folder is the fasta/fastq files you want to test
- and --output_folder is the folder you wish to store the results in
- and --log_name is the name you wish to call the log 



## Libraries used: 
- pyfastx
- jinja2
- mypy
- testing

