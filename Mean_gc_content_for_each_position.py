#Load libraries to use in script
import numpy as np
import pandas as pd

#Load CSV file with the data and read it into the df
data = pd.read_csv("gc_window_trend.csv")

#Group data by Position and then calculate mean and std for GC and GC3 content
summary = data.groupby("Position").agg(
    mean_gc_content=("GC_content", "mean"),
    std_gc_content=("GC_content", "std"),
    mean_gc3=("GC3_content", "mean"),
    std_gc3=("GC3_content", "std"),
).reset_index()

#Save the data to new CSV file and print a message when finished
summary.to_csv("mean_std_gc_gc3_ecoli.csv", index=False)
print("Summary file created:'mean_std_gc_gc3_ecoli.csv'")