import pyfastx#
import argparse
#import run
import csv
from typing import Protocol, Any




# class FastQ_Typing(Protocol):

    # fq = pyfastx.Fastq
    # size: int
    # id: str
    # seq: str
    # gc_content: float
    # composition: float
    # avglen: float
    # phred: float
# class FASTA_Typing(Protocol):

# sample_id, n_seqs_or_reads, total_bases, mean_len, gc_fraction, 
# n_fraction
    # fa = pyfastx.Fasta
    # # id: str
    # # seq: str
    # # mean: float
    # # name: str
    # # gc_content: float
    # # composition: #unsure about some of the typing here
    # # samp_id: str
    # # fasta_gc: float
    # # n_count: int

    # fasta_read_count = 0

class FASTA: 

    def __init__(self, path: str) -> None:
        self._fa = pyfastx.Fasta(path)


    @property
    def avg_len(self):
        return self._fa.mean #avg length of bases/ - might need to do count?

    @property
    def records(self) -> list[dict]:
        """
        Per-sequence records.
        Each dict = one TSV row.
        """
        rows: list[dict] = []

        for seq in self._fa:
            comp = seq.composition

            rows.append({
                "samp_id": seq.name,
                "length": len(seq),
                "gc_content": seq.gc_content,
                "A_count": comp.get("A", 0),
                "C_count": comp.get("C", 0),
                "G_count": comp.get("G", 0),
                "T_count": comp.get("T", 0),
                "N_count": comp.get("N", 0),
            })

        return rows
    
    @property
    def read_counting(self) -> int:
        read_count = 0
        total_bases = 0
        for seq in self._fa:
            read_count += 1
            total_bases += len(seq.seq)
        return read_count, total_bases
            
    @property 
    def average_len(self):
        lengths = [len(seq) for seq in self._fa]
        return sum(lengths) / len(lengths) if lengths else 0
    

    @property
    def summary(self) -> list[dict]:
        """
        File-level summary (single-row TSV).
        """
        lengths = [len(seq) for seq in self._fa]

        summary_row = {
            "num_sequences": len(lengths),
            "average_length": sum(lengths) / len(lengths) if lengths else 0,
        }

        return [summary_row]

def write_fasta_tsv(records, output_path):
    if not records:
        return # NOTE write an error cacther thing here
    
    if not isinstance(records, list) or not records:
        raise TypeError(
            f"records must be a non-empty list of dicts, got {type(records)}"
        )

    if not isinstance(records[0], dict):
        raise TypeError(
            f"records[0] must be dict, got {type(records[0])}"
        )
    
    #to check if the list contains {}
    if len(records) == 0: 
        raise TypeError("records must be non-empty list of dicts")
    
    #if the dictionary inside the list has values:
    if len(records[0]) == 0:
        raise TypeError("records must be non-empty list of dicts")

    fieldnames = records[0].keys()

    with open(output_path, "w", newline="") as tsvfile:
        writer = csv.DictWriter(
            tsvfile,
            fieldnames=fieldnames,
            delimiter="\t"
        )

        writer.writeheader()
        writer.writerows(records)
        
    

class FASTQ:

    def __init__(self, path: str):
        self._fq = pyfastx.Fastq(path)

    @property
    def total_bases(self) -> int:
        return self._fq.size

    @property
    def gc_fraction(self) -> float:
        return self._fq.gc_content
    
    @property
    def base_composition(self) -> dict:
        return self._fq.composition

    @property
    def A_count(self) -> int:
        return self._fq.composition.get("A", 0)

    @property
    def C_count(self) -> int:
        return self._fq.composition.get("C", 0)

    @property
    def G_count(self) -> int:
        return self._fq.composition.get("G", 0)

    @property
    def T_count(self) -> int:
        return self._fq.composition.get("T", 0)

    @property
    def N_count(self) -> int:
        return self._fq.composition.get("N", 0)
    
    @property
    def avg_len(self) -> float:
        return self._fq.avglen

    @property
    def phred_score(self) -> float:
        return self._fq.phred

# class FASTQ_Qual_Typing(Protocol):
#Required outputs from fastq files
# sample_id, n_seqs_or_reads, total_bases, mean_len, gc_fraction, 
# n_fraction, mean_qual, q30_fraction, run.json
    # fq = pyfastx.Fastq
    # id: str
    # seq: str
    # read_count: int

    # q: int
    # qual_sum: float
    # qual_bases: float

    # q30_bases: int
    
class FASTQ_Qual:


    def __init__(self, path: str) -> None:
        self._fq = pyfastx.Fastq(path)

# a tidier way of storing these, may be preferred over the list method used in read_info, can link with output writing when needed
    def iter_reads(self):
        for r in self._fq:
            yield r.name, r.seq, r.qual

    
    def read_info(self):
        read_count = 0
        qual_sum = 0 #total sum of all the ASCII values
        qual_bases = 0 #the bases
        q30_bases = 0 #bases weith quality scores over 30
        read_name = ''
    #get info for all reads in the file: 
        for r in self._fq:
            read_count += 1
            # read_name = r.description  #name of read left this out because its not helpful
            
            # read_seq = (r.seq)  #read sequence
            # read_qual = (r.qual)  # read quality (IIIII!!!!!) ect
            numeric_read_qual = (r.quali) #numerical value of the read quality (40, 0) ect
            
            # reads.append((read_name, read_seq, read_qual)) #adding the read info variables for each read to the list remove this if going with def method

            for q in numeric_read_qual:
                qual_sum += q   #adds the number to qual_sum
                qual_bases += 1 #counts the bases
                #if the quality is over 30 then add to over 30 bases: 
                if q >= 30:
                    q30_bases += 1
                    # return q30_bases
                    # mean_qual = qual_sum / qual_bases if qual_bases else 0
                    # q30_fraction = q30_bases /qual_bases if qual_bases else 0
                    # return mean_qual, q30_fraction
        return (
            read_count,
            qual_bases,
            qual_sum / qual_bases if qual_bases else 0,
            q30_bases /qual_bases if qual_bases else 0,
        )
    '''           
    instead of returning every variable in a long string in order to use the mean_quality and q30_frac methods
    calculate the values within the read_info function, assign to new variables, and then return them.
    Can still use the returned values for writing output this way
    # '''  


def process_fastq(full_path, output_path, filename):

    fq= FASTQ(full_path)
    fqq= FASTQ_Qual(full_path)
    read_count, qual_bases, mean_qual, q30_fraction = fqq.read_info()
    mean_qual = f"{mean_qual: .2f}"
    q30_fraction = f"{q30_fraction: .2f}"
    #read_count, qual_bases, mean_qual, q30_fraction = fqq.read_info()
    
    summary_record = {
        "filename": filename, # NOTE None of the options pyfastx gives for name or id are helpful, so using filename here
        "total_bases": fq.total_bases,
        "gc_fraction": fq.gc_fraction,
        "avg_len": fq.avg_len,
        "phred_score": fq.phred_score,
        "A_count": fq.A_count,
        "C_count": fq.C_count,
        "G_count": fq.G_count,
        "T_count": fq.T_count,
        "N_count": fq.N_count,
        "read_count": read_count,
        "qual_bases": qual_bases,
        "mean_qual": mean_qual,
        "q30_fraction": q30_fraction,
    }
    records: list[dict[str, Any]]
    records = [summary_record]


    write_fastq_tsv(records, output_path)
    

def write_fastq_tsv(records, output_path):
    if not records:
        return # NOTE write an error cacther thing here

    
    fieldnames = records[0].keys()

    with open(output_path, "w", newline="") as tsvfile:
        writer = csv.DictWriter(
            tsvfile,
            fieldnames=fieldnames,
            delimiter="\t"
        )

        writer.writeheader()
        writer.writerows(records)

