#Important this did not work so the graph script was written in R to produce the graph

import pandas as pd
import matplotlib.pyplot as plt

#Load CVS
df = pd.read_csv("gc_window_trend.csv")

print("First few rows of the dataset:")
print(df.head())

#Round GC_content and GC3_content to 2 dp
df["GC_content"] = df["GC_content"].round(2)
df["GC3_content"] = df["GC3_content"].round(2)

#Plot GC and GC3 content
plt.plot(df["Position"], df["GC_content"], label="GC Content", color="gray")
plt.plot(df["Position"], df["GC3_content"], label="GC3 Content", color="black")

#Code for title and labels
plt.xlabel("Position in Gene")
plt.ylabel("GC Content(%)")
plt.title("GC and GC3 Content across Escherichia Coli Genes")
plt.legend()

plt.show()



