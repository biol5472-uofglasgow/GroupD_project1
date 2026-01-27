# Group D project 1
## Collaborators: 


## Input files: 
### Fasta files: 
Header line, starts with '>'
Contains sequence data


### Fastq file
Header line starts with '@'
Sequence line
Separator line '+', sometimes followed by sequence identifier


## Output files: 
### tsv file: 
a table containing one row per sample, with columns such as: 
- sample ID
- number of sequences or reads
- total bases
- mean length
- gc fraction
- n fraction


### a run.json file: 
This should contain 



## Project 1 — FASTA/FASTQ QC metrics (per-sample table)

Goal: Compute basic QC metrics per input file/sample and write a cohort table suitable for a report.

Summary: Reads one or more FASTA/FASTQ files, computes basic quality control (QC)
metrics per sample (e.g. number of sequences/reads, total bases, length stats, GC%, 
N-content; for FASTQ optionally mean quality score), and outputs a per-sample results 
table

## Libraries used: 
pyfastx
jinja2
SeqIO

