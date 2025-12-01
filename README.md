# DNA-to-Protein-Translator
A structured and beginner-friendly genomic analysis pipeline designed to read DNA sequences, detect start/stop codons, translate nucleotide sequences into amino acids, and generate reproducible outputs for research and academic projects. Built using Python and Biopython, with a focus on clarity, modularity, and expandability for advanced bioinfo
# DNA to Protein Analysis: Comparative Amino Acid Study

This project demonstrates the ability to translate human gene DNA sequences into protein sequences and analyze the amino acid composition of each gene. It also includes a fully dynamic comparison system that analyzes every protein file inside the `results/` folder automatically and generates professional visualizations.

## 🎯 Project Objectives
- Translate human gene DNA sequences into protein sequences.
- Analyze the number and type of amino acids in each protein.
- Compare amino acid compositions across multiple genes using bar plots.
- Provide a fully dynamic pipeline that processes all protein files inside the `results/` folder without manual configuration.

## 🗂️ Project Structure
DNA_to_Protein_Analysis/
├─ data/ ← DNA sequence files (.fna / .fasta)
├─ results/ ← Generated protein sequence files (.txt)
├─ plots/ ← Amino acid composition plots
├─ scripts/ ← Python scripts
│ ├─ translate_dna.py
│ ├─ analyze_all_dynamic.py
├─ README.md ← Project documentation

## ⚡ How to Run
Run DNA-to-protein translation and then generate amino-acid comparison plots using these commands: python scripts/translate_dna.py  python scripts/analyze_all_dynamic.py

📊 Output Examples

All generated plots will be saved inside the plots/ directory.

Examples include:

Amino acid composition for each gene

Cross-gene comparison plot

Automatic detection and analysis of all protein files

🧬 Example Genes Used in This Project

ACTB — Beta-Actin

TP53 — Tumor protein p53

BRCA1 — Breast cancer type 1 susceptibility protein

EGFR — Epidermal growth factor receptor

(You can add any other gene to the data/ folder; the scripts will handle it automatically.)

🛠️ Skills Demonstrated

Practical bioinformatics workflows

DNA → protein translation

Data visualization with Matplotlib

Python scripting and automation

Research-grade project organization

Reproducible scientific analysis

🔗 GitHub Repository


