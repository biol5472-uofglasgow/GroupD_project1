import pyfastx
import csv
from typing import Any, Tuple


'''
Takes in a Fasta file and gets records from it.
Sets properties of data commonly found in fasta files.
'''
class FASTA: 

    def __init__(self, path: str) -> None:
        self._fa = pyfastx.Fasta(path)


    @property
    def avg_len(self) -> float:
        return self._fa.mean #avg length of bases
    

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
    def read_counting(self) -> Tuple[int, int]:
        read_count = 0
        total_bases = 0
        for seq in self._fa:
            read_count += 1
            total_bases += len(seq.seq)
        return read_count, total_bases

'''
Writes parsed fasta records to tsv file
'''
def write_fasta_tsv(records: list[dict], output_path: str):
    if not records:
        return 
    
    if not isinstance(records, list) or not records:
        raise TypeError(
            f"records must be a non-empty list of dicts, got {type(records)}"
        )

    if not isinstance(records[0], dict):
        raise TypeError(
            f"records[0] must be dict, got {type(records[0])}"
        )

    
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
        
    
'''
Parses FASTQ files using pyfastx functions
'''
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

'''
Parses Fastq files and returns sequence quality info
'''
class FASTQ_Qual:


    def __init__(self, path: str) -> None:
        self._fq = pyfastx.Fastq(path)

    
    def read_info(self) -> tuple[int, int, float, float]:
        read_count = 0
        qual_sum = 0 #total sum of all the ASCII values
        qual_bases = 0 #the bases
        q30_bases = 0 #bases with quality scores over 30
        read_name = ''
    #get info for all reads in the file: 
        for r in self._fq:
            read_count += 1
            numeric_read_qual = (r.quali) #numerical value of the read quality (40, 0) ect
            for q in numeric_read_qual:
                qual_sum += q   #adds the number to qual_sum
                qual_bases += 1 #counts the bases
                #if the quality is over 30 then add to over 30 bases: 
                if q >= 30:
                    q30_bases += 1
        return (
            read_count,
            qual_bases,
            qual_sum / qual_bases if qual_bases else 0,
            q30_bases /qual_bases if qual_bases else 0,
        )

'''
Assigns the data fields acquired from the fastq file into columns and calls the write_fasta function

'''
def process_fastq(full_path: str, output_path: str, filename: str):

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
        "bases_qual>30": qual_bases,
        "mean_qual": mean_qual,
        "q30_fraction": q30_fraction,
    }
    records: list[dict[str, Any]]
    records = [summary_record]


    write_fastq_tsv(records, output_path)
    
'''
Checks for fastq records and writes to a tsv file
'''
def write_fastq_tsv(records: list[dict], output_path: str):
    if not records:
        return

    
    fieldnames = records[0].keys()

    with open(output_path, "w", newline="") as tsvfile:
        writer = csv.DictWriter(
            tsvfile,
            fieldnames=fieldnames,
            delimiter="\t"
        )

        writer.writeheader()
        writer.writerows(records)

