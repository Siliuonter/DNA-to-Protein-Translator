import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def compare_amino_acids(results_folder):
    """
    Reads all *_protein.txt files inside the results folder,
    counts amino acids for each gene, and plots a comparative bar chart.

    Parameters:
        results_folder (str): Path to the folder containing protein TXT files.
    """

    # List all protein files
    all_files = [f for f in os.listdir(results_folder) if f.endswith("_protein.txt")]

    if not all_files:
        print("No protein files found in the results folder.")
        return

    # 20 standard amino acids
    aa_list = list("ACDEFGHIKLMNPQRSTVWY")

    gene_counts = {}

    for file_name in all_files:
        file_path = os.path.join(results_folder, file_name)

        # Read protein sequence while skipping FASTA headers
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            protein_seq = "".join(line.strip() for line in lines if not line.startswith(">"))

        counts = Counter(protein_seq)
        gene_name = file_name.replace("_protein.txt", "")
        gene_counts[gene_name] = [counts.get(aa, 0) for aa in aa_list]

        print(f"Processed {gene_name}")

    # Create a grouped bar chart
    x = np.arange(len(aa_list))
    width = 0.8 / len(gene_counts)

    plt.figure(figsize=(20, 7))
    for i, (gene, counts) in enumerate(gene_counts.items()):
        plt.bar(x + i * width, counts, width=width, label=gene)

    plt.xticks(x + width * (len(gene_counts) - 1) / 2, aa_list)
    plt.xlabel("Amino Acid")
    plt.ylabel("Count")
    plt.title("Amino Acid Composition Comparison Across All Genes")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("=== Amino Acid Comparison Tool ===")
    results_path = input("Enter the path to your 'results' folder: ").strip()

    if not os.path.isdir(results_path):
        print("Invalid path. Please enter a valid directory.")
    else:
        compare_amino_acids(results_path)
