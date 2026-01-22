import pyfastx#
import argparse
import run
from typing import Iterable, Iterator, Callable, Protocol

class File:
    #function that will take the input file and see if it is FASTA/FASTQ based on the first line: 
    #if theres no "> or @ then will return none, need to add proper error handling into this later"
    #will return string of either "FASTA" or "FASTQ": 
    def __init__(self, file: str) -> None:
        self._file = file

    def file_format(self, path): 
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
path = run.args.folder_path
# file_form = File.file_format(path)
# print(f"file format is : {file_form}")


# if file_form == "FASTQ":

class FastQ_Typing(Protocol):

    fq = pyfastx.Fastq
    size: int


class FASTQ:
    #so can do only this next bit if its a FASTQ file, will fail if its a FASTA file: 
    #extracts info from the FASTQ file, can put this into the FATSQ_parse() function mentioned above 
    # total_bases: int

    def __init__(self, id: str, seq: str) -> None:
        self.id = id
        self.seq = seq
        self._self = self
    
    # get the path of the FASTQ file and assign it to be fq 
    def FASTQ_path(self) -> str:
        fq = pyfastx.Fastq(path)
        return fq

    #for total bases: 
    @staticmethod
    def total_bases(fq: FastQ_Typing) -> int:
        total_bases = fq.size
        return total_bases
        

    #GC content of FASTQ file: 
    def gc_content(self, fq) -> float:
        GC_cont = fq.gc_content
        return GC_cont

    #composition of bases in FASTQ maybe?
    def N_cont(self, fq) -> float:
        comp = fq.composition
        return comp

    #get average length of reads (the whole file - may need to be changed):
    # @staticmethod
    def avg_len(self, fq) -> float:
        alen = fq.avglen
        return alen

    #get phred score - affects the quality score conversion: 
    def phred_score(self, fq) -> float:
        p_score = fq.phred
        return(p_score)
    #read counts

    read_count = 0
    qual_sum = 0 #total sum of all the ASCII values
    qual_bases = 0 #the bases
    q30_bases = 0 #bases weith quality scores over 30

class FASTQ_Qual:
    def __init__(self, id: str, seq: str, read_count) -> None:
        self._self = self
        self.id = id
        self.seq = seq
        self._read_count = read_count

    @property
    def id(self) -> str:
        return self._read_count 

    def read_info(self, fq):
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
    # @staticmethod  
    def mean_quality(self, qual_sum, qual_bases) -> float:
        mean_qual = qual_sum / qual_bases
        return mean_qual
    
    def q30_frac(self, q30_bases, qual_bases) -> float:
        q30_fraction = q30_bases / qual_bases
        return q30_fraction
    # print(f"mean qual {self.mean_qual}, q30 fraction  {30_fraction}")


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



# sample_id, n_seqs_or_reads, total_bases, mean_len, gc_fraction, n_fraction
#  parsing the FASTA file:
# elif file_form == "FASTA":
# class Fasta: 
#     def __init__(self, id: str, seq: str) -> None:
#         self.id = id
#         self.seq = seq.upper
#     def fasta_path(self):
#         fa = pyfastx.Fasta(main.filename)
#         return fa
    
#     fasta_read_count = 0
#     def avg_len(self, fa):
#         fasta_av_len = (fa.mean) #avg length of bases/ - might need to do count?
#         return fasta_av_len
#     def read_fasta(self, fa):
#         for seq in fa: 
#             fasta_read_count += 1 
#             samp_id = (seq.name) #seq ename
#             #fasta_av_len = (seq.mean) #avg length of bases/ - might need to do count?
#             fasta_gc = (seq.gc_content) #GC fraction
#             n_count = (seq.composition) #shows composition of bases - maybe n content?
#         return fasta_read_count, samp_id, fasta_gc, n_count   
#     print(f"fasta read count {fasta_read_count}")
#     print(f"sample id {samp_id}")
#     print(f"fasta av length {fasta_av_len}")
#     print(f"fasta GC {fasta_gc}")
#     print(f"n count {n_count}")




# else: 
#     print("incorrect file format needs to be fASTA/Q")
#     #raise ...

# class Output:
