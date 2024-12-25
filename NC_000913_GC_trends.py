#Analysing GC and GC3 of NC_000913
#Testing code to download fasta files and play around with code from tutorial

from Bio import Entrez, SeqIO
import csv

#Set email for Entrez
Entrez.email = "yathukamal11@gmail.com"

# #Step 1: Download E. coli CDS in FASTA format
# def download_ecoli_cds():
#     ecoli_accession_id = "NC_000913"
# #Fetch data using Entrez function
#     handle = Entrez.efetch(db="nucleotide", id=ecoli_accession_id, rettype="fasta_cds_na",retmode="text")
# #Write the fetched cds to a fasta file
#     with open("ecoli_cds.fasta", "w") as file:
#         file.write(handle.read())
#     handle.close()
#     print("Downloaded ecoli_cds.fasta")

#Initial list to store sequences
bad_seq = []

#Function to check start and stop codons
def check_start_stop(seq, gene_id):
    #check for start codon(ATG)
    start_list = ["ATG","GTG","TTG"]
    first_codon = seq[:3]
    if first_codon not in start_list:
        print(f"Bad first codon: {first_codon} for gene {gene_id}")
        bad_seq.append("Not_ATG")
    else:
        bad_seq.append("Good_start")

    #Check for stop codon
    stop_list = ["TAG", "TGA", "TAA"]
    last_codon = seq[-3:]
    if last_codon not in stop_list:
        print(f"Bad last codon: {last_codon} for gene {gene_id}")
        bad_seq.append("Not_stop")
    else:
        bad_seq.append("Good_stop")

#Function to calculate GC and GC3
def calculate_gc_content(seq):
    gc_content = round((seq.count("G") + seq.count("C")) / len(seq) * 100)

    seq3 = seq[2::3]
    gc3_content = round((seq3.count("G") + seq3.count("C")) / len(seq3) * 100 if len(seq3) > 0 else 0)

    return gc_content, gc3_content

#Step 2 process FASTA file
def calculate_gc_trends(input_fasta="ecoli_cds.fasta", output_csv="ecoli_gc_trends.csv"):
    records = SeqIO.parse(input_fasta, "fasta")

#Write into CSV file
    with open(output_csv, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["ID", "GC_Content", "GC3_Content", "Bad_Seq"])

#Process each record in the FASTA file
        for record in records:
            gene_id = record.id
            sequence = record.seq

            global bad_seq
            bad_seq = []
            check_start_stop(sequence, gene_id)

            gc_content, gc3_content = calculate_gc_content(sequence)

            csv_writer.writerow([record.id, gc_content, gc3_content, ",".join(bad_seq)])

        print(f"Results saved to {output_csv}")

calculate_gc_trends()
