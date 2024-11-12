#Import libraries to be used in the script
from Bio import Entrez, SeqIO
import csv

#Function to calculate GC (and GC3) content from a fasta file to a csv file using a window size of 50 and a step size of 10
def calculate_gc_trends(input_fasta="ecoli_cds.fasta", output_csv = "gc_window_trend.csv", window_size=50,step_size=10):
    records = SeqIO.parse(input_fasta, "fasta")

#Creat a CSV file for writing into and add some headers
    with open(output_csv, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Gene_ID", "Position", "GC_content", "GC3_content"])

#Loop through each gene in the FASTA file and extract the gene ID and sequence
        for record in records:
            gene_id = record.id
            sequence = record.seq

#Loop through the sequence using sliding window method
            for start in range(0,len(sequence)- window_size + 1, step_size):
                window_seq = sequence[start:start+window_size]

                #Calculate overall GC content for this window
                gc_content = (window_seq.count("G") + window_seq.count("C")) / len(window_seq) * 100


                #Calculate GC3 content
                gc3_bases = window_seq[2::3]
                if len(gc3_bases) > 0:
                    gc3_content = (gc3_bases.count("G") + gc3_bases.count("C")) / len(gc3_bases) * 100
                else:
                    gc3_content = 0

                #Write the results into the CSV file
                csv_writer.writerow([gene_id,start + 1, gc_content, gc3_content])

#Run function
calculate_gc_trends()