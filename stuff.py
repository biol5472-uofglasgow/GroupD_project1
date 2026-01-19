#loading in a fasta file: 

#loading in the kinases file 
seq_dict = {}
with open('file/path') as kinase: 
    for line in kinase: 
        line = line.rstrip()
        if line.startswith(">"):
            toxo_gene_ID = line[1:]
        else: 
            seq_dict[toxo_gene_ID] = line


#function to calcule GC content: 
def calc_gc_content(seq):
    c_count = seq.count('C')
    g_count = seq.count('G')
    gc_content = ((c_count + g_count) / len(seq)) * 100
    #print(f'this is the GC content : {gc_content}%')
    return round(gc_content)

#length of sequence: 
def total_bases(seq): 
    length = len(seq)
    return length 

#n content
def n_content(Seq)