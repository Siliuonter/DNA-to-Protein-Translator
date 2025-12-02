from Bio import SeqIO
import os

def translate_all_genes(input_folder, output_folder):
    """
    Translates all DNA FASTA/FNA files inside the input folder into protein sequences.
    
    Parameters:
        input_folder (str): Path to the folder containing .fasta or .fna files.
        output_folder (str): Path to the folder where protein files will be saved.
    """

    # Create output folder if needed
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("Translation started...")

    # Process all files in the input directory
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith((".fna", ".fasta")):
            input_path = os.path.join(input_folder, file_name)

            # Read all FASTA/FNA sequences
            for record in SeqIO.parse(input_path, "fasta"):
                dna_seq = record.seq

                # Translate DNA to protein (stop at the first stop codon)
                protein_seq = dna_seq.translate(to_stop=True)

                # Prepare output file path
                output_file = os.path.join(output_folder, f"{record.id}_protein.txt")

                # Write protein sequence
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(f">Protein_{record.id}\n")
                    f.write(str(protein_seq))

                print(f"Translated {record.id} -> {output_file}")

    print("Translation finished.")


if __name__ == "__main__":
    print("=== DNA → Protein Translator ===")
    print("Enter your folders (no quotes needed):")

    # Ask for user paths
    input_dir = input("Path to your DNA input folder: ").strip()
    output_dir = input("Path for saving protein files: ").strip()

    # Run the translator
    translate_all_genes(input_dir, output_dir)
