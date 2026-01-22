import pyfastx

class File:
    #function that will take the input file and see if it is FASTA/FASTQ based on the first line: 
    #if theres no "> or @ then will return none, need to add proper error handling into this later"
    #will return string of either "FASTA" or "FASTQ": 
    def __init__(self, file: str) -> None:
        self._file = file

    def file_format(self, path) -> str: 
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
                break


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
path = '/Users/georgecollins/Desktop/PG uni/BIOL5472 SoftDev/GroupD_project1/contigs.fasta' 

file_form = File.file_format(path)
print(f"file format is : {file_form}")


if file_form == "FASTQ":
    #so can do only this next bit if its a FASTQ file, will fail if its a FASTA file: 
    #extracts info from the FASTQ file, can put this into the FATSQ_parse() function mentioned above 
    fq = pyfastx.Fastq(path)

    #for total bases: 
    total_bases = fq.size

    #GC content of FASTQ file: 
    GC_cont = fq.gc_content

    #composition of bases in FASTQ
    comp = fq.composition

    #get average length of reads:
    alen = fq.avglen

    #get phred score - affects the quality score conversion: 
    p_score = fq.phred

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
                
    def mean_quality() -> float:
        mean_qual = qual_sum / qual_bases
        return mean_qual
    
    def q30_frac(mean_qual) -> float:
        q30_fraction = q30_bases / qual_bases
        return q30_fraction
    print(f"mean qual {mean_qual}, q30 fraction  {q30_fraction}")


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



    #for iterating: 
    """
    for name, seq, qual in pyfastx.Fastq('/Users/georgecollins/Desktop/PG uni/BIOL5472 SoftDev/sampleB.fastq', build_index=False): 
        print(name)
        print(seq)
        print(qual)"""



#sample_id, n_seqs_or_reads, total_bases, mean_len, gc_fraction, n_fraction
#parsing the FASTA file:
elif file_form == "FASTA":
    fa = pyfastx.Fasta(path)
    fasta_read_count = 0
    fasta_av_len = (fa.mean) #avg length of bases/ - might need to do count?

    for seq in fa: 
        fasta_read_count += 1 
        samp_id = (seq.name) #seq ename
        #fasta_av_len = (seq.mean) #avg length of bases/ - might need to do count?
        fasta_gc = (seq.gc_content) #GC fraction
        n_count = (seq.composition) #shows composition of bases - maybe n content?

    print(f"fasta read count {fasta_read_count}")
    print(f"sample id {samp_id}")
    print(f"fasta av length {fasta_av_len}")
    print(f"fasta GC {fasta_gc}")
    print(f"n count {n_count}")




else: 
    print("incorrect file format needs to be fASTA/Q")
    #raise ...


