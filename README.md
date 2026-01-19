#Group D project 1

Input files: 
Fasta/Fastq file

Output files: 
tsv
run.json
flags.tsv
filtered fasta


About Fasta Files:
Header line, starts with '>'
Contains sequence data

About Fastq files:
Header line starts with '@'
Sequence line
Separator line '+', sometimes followed by sequence identifier

Project 1 — FASTA/FASTQ QC metrics (per-sample table)
Goal: Compute basic QC metrics per input file/sample and write a cohort table suitable 
for a report.

Summary: Reads one or more FASTA/FASTQ files, computes basic quality control (QC)
metrics per sample (e.g. number of sequences/reads, total bases, length stats, GC%, 
N-content; for FASTQ optionally mean quality score), and outputs a per-sample results 
table

Inputs: FASTA and/or FASTQ files (optionally via a simple manifest samples.tsv).
Core outputs:

Required:

• qc.tsv (one row per sample) with fields such as:
o sample_id, n_seqs_or_reads, total_bases, mean_len, gc_fraction, 
n_fraction

o (FASTQ optional) mean_qual, q30_fraction
• run.json

Optional: 

• flags.tsv: sample-level flags/outliers with reasons (useful for downstream 
workflows)

• (If FASTA input) filtered.fasta (or filtered_ids.txt): optional pass/fail subset output, 
if your spec includes filtering

Recommended libraries (optional): biopython (SeqIO) or pyfastx for reading 
FASTA/FASTQ reliably.
3

Tips:

• Start by defining the exact columns of your qc.tsv, then write one small parser 
that yields (id, seq, qual) records and test it on the fixtures.

• Keep metrics simple and testable; focus on clean parsing and deterministic 
aggregation.

