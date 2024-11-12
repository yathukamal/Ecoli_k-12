# Ecoli_k-12
## Python Files
1. NC_000913_GC_trends.py - Initial code to download FASTA file, load it into a CSV file and play around with code from tutorial. Corresponding files are ecoli_cds.fasta and ecoli_gc_trends.
2. NC_000913_GC_trends_sliding_window.py - Script to calculate GC and GC3 content using a window size of 50 and step size of 10. The corresponding file is gc_window_trend.csv
3. Mean_gc_content_for_each_position - Calculates the mean and standard deviation of GC and GC3 content for each position along the sequence. (The positions of various genes were averaged e.g. Gene, Position, GC content, A, 1, 32, B, 1, 28, C, 1, 34 ; the mean for position 1 would be 31)

## Data files
4. ecoli_cds.fasta - FASTA file
5. ecoli_gc_trends.csv - GC/GC3 content of whole sequence for each gene ID
6. gc_window_trend.csv - GC/GC3 content of different positions within the sequence for every gene ID
7. mean_std_gc_gc3_ecoli.csv - Adding gene IDs together for each position to find the mean and std GC and GC3 content
