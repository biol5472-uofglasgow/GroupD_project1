import pyfastx
from HTML_script import HtmlGenerator

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

class FASTQ_Qual:
    def __init__(self) -> None:
       ## self._read_count = read_count
        self.qual_sum = 0
        self.qual_bases = 0
        self.q30_bases = 0
        #self.read_count = 0

    def fastq_qual(self, numeric_read_qual: list[int]) -> None:
        for q in numeric_read_qual:
            self.qual_sum += q   #adds the number to qual_sum
            self.qual_bases += 1 #counts the bases
            #if the quality is over 30 then add to over 30 bases: 
            if q >= 30:
                self.q30_bases += 1
            #now the mean qual/bases and the mean Q30/bases 
    
    def read_info(self, fq):
        read_count = 0
        # qual_sum = 0 #total sum of all the ASCII values
        # qual_bases = 0 #the bases
        # q30_bases = 0 #bases weith quality scores over 30
    #get info for all reads in the file: 
        for r in fq:
            read_count += 1
            read_name = (r.name)  #name of read
            read_seq = (r.seq)  #read sequence
            read_qual = (r.qual)  # read quality (IIIII!!!!!) ect
            numeric_read_qual = (r.quali) #numerical value of the read quality (40, 0) ect
            
            self.fastq_qual(numeric_read_qual) 
        return read_count, read_name, read_seq, read_qual, numeric_read_qual 
    @staticmethod
    def mean_quality(qual_sum, qual_bases) -> float:
        mean_qual = qual_sum / qual_bases
        return mean_qual
    @staticmethod
    def q30_frac(q30_bases, qual_bases) -> float:
        q30_fraction = q30_bases / qual_bases
        return q30_fraction
    #print(f"mean qual {mean_qual}, q30 fraction  {q30_fraction}")



#sample_id, n_seqs_or_reads, total_bases, mean_len, gc_fraction, n_fraction
#parsing the FASTA file:

class Fasta: 
    def __init__(self, fa: str) -> None:
        self.fa = fa

    @staticmethod
    def fasta_path(path):
        fa = pyfastx.Fasta(path)
        return fa
    
    @staticmethod
    def avg_len(fa) -> float:
        fasta_av_len = (fa.mean) #avg length of bases/ - might need to do count?
        return fasta_av_len
    
    @staticmethod
    def read_fasta(fa):
        fasta_read_count = 0
        samp_id = []
        fasta_total = []
        fasta_gc = []
        n_count = []

    
        for s in fa: 
            fasta_read_count += 1 
            samp_id.append(s.name) #seq ename
            fasta_total.append(len(s.seq)) #length of total bases
            #fasta_av_len = (seq.mean) #avg length of bases/ - might need to do count?
            fasta_gc.append(s.gc_content) #GC fraction
            n = (s.composition) #shows composition of bases - maybe n content?
            n_count.append(n["N"])
        return fasta_read_count, samp_id, fasta_total, fasta_gc, n_count   
    #print(f"fasta read count {fasta_read_count}")
    #print(f"sample id {samp_id}")
    #print(f"fasta av length {fasta_av_len}")
    #print(f"fasta GC {fasta_gc}")
    #print(f"n count {n_count}")

class Output:
    def __init__(self, data) -> None:
        self.data = data
        #self.fasta_read_count = fasta_read_count
    def FASTA_write_tsv(fasta_read_count, samp_id, fasta_total, fasta_gc, n_count, fasta_av_len):

        with open('results.tsv', 'w') as output_table:
            output_table.write('Sample_ID\tNo. of seqs/reads\ttotal bases\tmean len\tgc fraction\tn fraction\n')
            for s, t, gc, n in zip(samp_id, fasta_total, fasta_gc, n_count):
                output_table.write(f"{s}\t{fasta_read_count}\t{t}\t{fasta_av_len}\t{gc}\t{n}\n")        

    def FASTQ_write_tsv(meanq_data, qual30_data):
        with open('results.tsv', 'w') as output_table:
            output_table.write(f'Mean_Quality\tqual_over_30\n')

            for counter in range():
                output_table.write(f"{meanq_data}\t{qual30_data}\n")
    
    
if __name__ == '__main__':
        #obvi switch this for the actual file:
    #is hard coded now but can use the ArgParse:
    path = '/Users/georgecollins/Desktop/PG uni/BIOL5472 SoftDev/GroupD_project1/contigs.fasta' 

    file_form = File.file_format(path)
    print(f"file format is : {file_form}")

    #just adding stuff on the end so that it generates a Results.tsv so that i can test the html
    #can take out if this is what is being done in main.py
    if file_form == "FASTA":
        fa = Fasta.fasta_path(path)
        fasta_read_count, samp_id, fasta_total, fasta_gc, n_count = Fasta.read_fasta(fa)
        fasta_av_len = Fasta.avg_len(fa)
        #print(data, len_data)
        out = Output.FASTA_write_tsv(fasta_read_count, samp_id, fasta_total, fasta_gc, n_count, fasta_av_len)
        #out.FASTA_write_tsv()

    elif file_form == "FASTQ":
        data = FASTQ(path)
        meanq_data = FASTQ_Qual.mean_quality(data)
        qual30_data = FASTQ_Qual.q30_frac(data)
        out = Output(meanq_data, qual30_data)
        out.write_tsv()

    else:
        print("incorrect file format")
