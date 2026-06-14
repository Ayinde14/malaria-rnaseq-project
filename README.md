# RNA-Seq Analysis of Malaria Infection (GSE156791)

## 📌 Project Overview

This project performs differential gene expression analysis on RNA-seq data to identify genes associated with malaria infection. The dataset used is **GSE156791** from the Gene Expression Omnibus (GEO).

---

## 🎯 Aim

To identify differentially expressed genes between infected and control samples in a malaria RNA-seq dataset.

---

## 🧪 Objectives

* Download and preprocess RNA-seq data from GEO
* Construct a gene expression matrix
* Perform differential expression analysis
* Visualize results using volcano plots and heatmaps
* Identify biologically significant genes

---

## 📂 Dataset

* Source: GEO (GSE156791)
* Type: RNA-seq (processed expression values)
* Samples: ~72
* Features: 12,375 genes

---

## ⚙️ Methodology

### 1. Data Acquisition

* Downloaded supplementary files using `GEOquery`
* Extracted `.gz` expression files

### 2. Data Processing

* Read all sample files into R
* Merged into a single expression matrix
* Rows: genes (ENSEMBL IDs)
* Columns: samples

### 3. Sample Grouping

* Control: samples labeled with **V1**
* Infected: samples labeled with **V3**

### 4. Differential Expression Analysis

* Used **limma** (since data was already normalized)
* Built design matrix and contrast model
* Applied empirical Bayes moderation

### 5. Visualization

* Volcano plot to identify significant genes
* Heatmap for expression patterns

---

## 📊 Results

* Total genes analyzed: 12,375
* Significant genes identified: **15**

### Key Findings:

* Several genes were **upregulated in infected samples**
* Some genes showed **strong downregulation**
* One gene showed a very large negative fold change (~ -6), indicating strong biological impact

---

## 📈 Visualizations

### Volcano Plot

* Highlights significantly differentially expressed genes
* Thresholds: p-value < 0.05 and |logFC| > 1

### Heatmap

* Shows clustering of significant genes
* Clear separation between infected and control samples

---

## 🧬 Interpretation

* Infection leads to a **targeted gene expression response**
* A small number of genes show strong regulation changes
* These genes may play roles in:

  * Immune response
  * Infection pathways
  * Host-pathogen interaction

---

## 💡 Significance

* Identifies candidate biomarkers for malaria infection
* Provides insights into host response mechanisms
* Demonstrates a complete RNA-seq analysis workflow

---

## 🛠 Tools & Packages

* R
* GEOquery
* limma
* pheatmap

---

## 📌 Conclusion

This project successfully demonstrates how to analyze RNA-seq data from GEO, identify differentially expressed genes, and interpret biological significance using statistical and visualization tools.

---

## 🚀 Future Work

* Perform pathway enrichment analysis (GO/KEGG)
* Map ENSEMBL IDs to gene symbols
* Validate findings with additional datasets

---

## 👤 Author
SALAM QADRI OPEYEMI
Your Name
GitHub: https://github.com/YOUR_USERNAME

