import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your data (tab-separated!)
df = pd.read_csv("results/top_upregulated.txt", sep="\t", header=None)

# Rename columns
df.columns = ["gene", "control", "treated", "log2FoldChange"]

# Fake p-values (since we don’t have real ones)
df["padj"] = 0.01  # placeholder

# Plot
plt.figure()
plt.scatter(df["log2FoldChange"], -np.log10(df["padj"]), s=20)

plt.xlabel("Log2 Fold Change")
plt.ylabel("-Log10 p-value")
plt.title("Volcano Plot (Approximate)")

plt.savefig("results/volcano_plot.png")
plt.show()
