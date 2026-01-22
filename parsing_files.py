import pyfastx
path = '/Users/georgecollins/Desktop/PG uni/BIOL5472 SoftDev/GroupD_project1/contigs.fasta' 

class File:
    #function that will take the input file and see if it is FASTA/FASTQ based on the first line: 
    #if theres no "> or @ then will return none, need to add proper error handling into this later"
    #will return string of either "FASTA" or "FASTQ": 
    def __init__(self, file: str) -> None:
        self._file = file
    @staticmethod
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

#file_form = File.file_format(path)
#print(f"file format is : {file_form}")


class FASTQ:
    #so can do only this next bit if its a FASTQ file, will fail if its a FASTA file: 
    #extracts info from the FASTQ file, can put this into the FATSQ_parse() function mentioned above 
    def __init__(self, fq: str) -> None:
        self.fq = fq
    
    # get the path of the FASTQ file and assign it to be fq 
    @staticmethod
    def FASTQ_path(path) -> str:
        fq = pyfastx.Fastq(path)
        return fq

    #for total bases: 
    @staticmethod
    def total_bases(fq) -> float:
        total_bases = fq.size
        return total_bases

    #GC content of FASTQ file: 
    @staticmethod
    def gc_content(fq) -> float:
        GC_cont = fq.gc_content
        return GC_cont

    #composition of bases in FASTQ maybe?
    @staticmethod
    def N_cont(fq) -> float:
        comp = fq.composition
        return comp

    #get average length of reads (the whole file - may need to be changed):
    @staticmethod
    def avg_len(fq) -> float:
        alen = fq.avglen
        return alen

    #get phred score - affects the quality score conversion: 
    @staticmethod
    def phred_score(fq) -> float:
        p_score = fq.phred
        return(p_score)
    #read counts

    read_count = 0
    qual_sum = 0 #total sum of all the ASCII values
    qual_bases = 0 #the bases
    q30_bases = 0 #bases weith quality scores over 30

class FASTQ_Qual:
    def __init__(self, read_count: str) -> None:
        self._read_count = read_count

    @property
    def id(self) -> str:
        return self._read_count 

    @staticmethod
    def read_info(fq):
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
        return read_count, read_name, read_seq, read_qual, numeric_read_qual, qual_sum, qual_bases, q30_bases 
    @staticmethod
    def mean_quality(qual_sum, qual_bases) -> float:
        mean_qual = qual_sum / qual_bases
        return mean_qual
    @staticmethod
    def q30_frac(q30_bases, qual_bases) -> float:
        q30_fraction = q30_bases / qual_bases
        return q30_fraction
    #print(f"mean qual {mean_qual}, q30 fraction  {q30_fraction}")


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

class Fasta: 
    def __init__(self, fa: str) -> None:
        self.fa = fa

    @staticmethod
    def fasta_path():
        fa = pyfastx.Fasta(path)
        return fa
    
    @staticmethod
    def avg_len(fa) -> float:
        fasta_av_len = (fa.mean) #avg length of bases/ - might need to do count?
        return fasta_av_len
    
    @staticmethod
    def read_fasta(fa):
        fasta_read_count = 0
        for s in fa: 
            fasta_read_count += 1 
            samp_id = (s.name) #seq ename
            fasta_total = len(s.seq) #length of total bases
            #fasta_av_len = (seq.mean) #avg length of bases/ - might need to do count?
            fasta_gc = (s.gc_content) #GC fraction
            n_count = (s.composition) #shows composition of bases - maybe n content?
        return fasta_read_count, samp_id, fasta_total, fasta_gc, n_count   
    #print(f"fasta read count {fasta_read_count}")
    #print(f"sample id {samp_id}")
    #print(f"fasta av length {fasta_av_len}")
    #print(f"fasta GC {fasta_gc}")
    #print(f"n count {n_count}")

class Output:
    def __init__(self) -> None:
        self.fasta_read_count = fasta_read_count
    def write_tsv(self):
        with open('results.tsv', 'w') as output_table:
            output_table.write('Sample_ID\tn_seqs_of_reads\ttotal_bases\tmean_len\tgc_fraction\tn_fraction\n')

            for counter in range(fasta_read_count):
                output_table.write(f"{samp_id}\t{fasta_read_count}\t{fasta_total}\t{fasta_av_len}\t{fasta_gc}\t{n_count}\n")
    
if __name__ == '__main__':
        #obvi switch this for the actual file:
    #is hard coded now but can use the ArgParse:
    path = '/Users/georgecollins/Desktop/PG uni/BIOL5472 SoftDev/GroupD_project1/contigs.fasta' 

    file_form = File.file_format(path)
    print(f"file format is : {file_form}")

    #if file_form == "FASTQ":
