import pyfastx


#function that will take the input file and see if it is FASTA/FASTQ based on the first line: 
#will return string of either "FASTA" or "FASTQ": 
def file_format(path) -> str: 
    #can check the headers first: 
    with open(path) as f:
        for line in f:
            line = line.strip()
            
            if not line:
                continue
            elif line.startswith(">"):
                return "FASTA"
            elif line.startswith("@"):
                return "FASTQ"
            breaks


#ALSO this which uses pyfastx and can work if using the headers dont work??: 
"""
    try:
        pyfastx.Fastq(path)
        return "FASTQ"
    except Exception:
        pass

    try:
        pyfastx.Fasta(path)
        return "FASTA"
    except Exception:
        pass

    raise ValueError(f"file format must be fasta/fastq : {path}") """



#obvi switch this for the actual file:
#is hard coded now but can use the ArgParse:
path = '/Users/georgecollins/Desktop/PG uni/BIOL5472 SoftDev/GroupD_project1/sampleA.fastq' 

file_form = file_format(path)
print(f"file format is : {file_form}")



"""
#now can do if its fasta?: 
#have functions for either FASTQ or FASTA?
if file_form == "FASTQ":
    FASTQ_parse()
elif file_form == "FASTA":
    FASTA_parse()
else: 
    print("")
    raise ...
"""


#so can do only this next bit if its a FASTQ file, will fail if its a FASTA file: 
#extracts info from the FASTQ file, can put this into the FATSQ_parse() function mentioned above 
fq = pyfastx.Fastq(path)

#for readcounts: 
RQ = len(fq)

#for total bases: 
total_bases = fq.size

#GC content of FASTQ file: 
GC_cont = fq.gc_content

#composition of bases in FASTQ
comp = fq.composition

#get average length of reads:
alen = fq.avglen

#max and min length of reads: 
max_len = fq.maxlen 
min_len = fq.minlen 

#minimum quality score: 
min_qual = fq.minqual 

#get phred score - affects the quality score conversion: 
p_score = fq.phred


#guess fastq quality encoding system: 
codingsys = fq.encoding_type

#read counts
read_count = 0
qual_sum = 0 #total sum of all the ASCII values
qual_bases = 0 #the bases
q30_bases = 0 #bases weith quality scores over 30



#get info for all reads in the file: 
for r in fq:
    read_count += 1
    read_name = (r.name)  #name of read
    read_seq = (r.seq)  #read sequence
    read_qual = (r.qual)  # read quality (IIIII!!!!!) ect
    numeric_read_qual = (r.quali) #numerical value of the read quality (40, 0) ect

    for q in r.quali:
        qual_sum += q   #adds the number to qual_sum
        qual_bases += 1 #counts the bases
        #if the quality is over 30 then add to over 30 bases: 
        if q >= 30:
            q30_bases += 1
        #now the mean qual/bases and the mean Q30/bases : 
mean_qual = qual_sum / qual_bases
q30_fraction = q30_bases / qual_bases
print(f"mean qual {mean_qual}, q30 fraction  {q30_fraction}")

print(f"the read count is {read_count}")


#to get the info for the output file : mean wual and Q30: 
"""
qual_sum = 0 #total sum of all the ASCII values
qual_bases = 0 #the bases
q30_bases = 0 #bases weith quality scores over 30
#put into the loop: 

for r in fq:
    for q in r.quali:
        qual_sum += q   #adds the number to qual_sum
        qual_bases += 1 #counts the bases
        #if the quality is over 30 then add to over 30 bases: 
        if q >= 30:
            q30_bases += 1

#now the mean qual/bases and the mean Q30/bases : 
mean_qual = qual_sum / qual_bases
q30_fraction = q30_bases / qual_bases
print(mean_qual, q30_fraction)
"""



#additional info?/stuff I found on the documentation website/adjusted for this: 
"""
##this could work for parsing fasta/fastq:
try:
    fq = pyfastx.Fastq(path)
    fmt = "FASTQ"
except Exception:
    fa = pyfastx.Fasta(path)
    fmt = "FASTA"
"""



#q30????:
"""
def phred_scores(qual: str) -> list[int]:
    return [ord(ch) - 33 for ch in qual]

    qual = "!!!!!!!!IIIIIIII"
    scores = phred_scores(qual)

    mean_q = sum(scores) / len(scores)
    q30_fraction = sum(1 for q in scores if q >= 30) / len(scores)

    print(scores)# [0, 40, 40]
    print(mean_q)# 30.0
    print(q30_fraction)# 0.75
"""



#for iterating: 
"""
for name, seq, qual in pyfastx.Fastq('/Users/georgecollins/Desktop/PG uni/BIOL5472 SoftDev/sampleB.fastq', build_index=False): 
    print(name)
    print(seq)
    print(qual)"""