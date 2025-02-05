import os

# Directory containing the ROOT files
root_files_dir = "/home/sungbino/study/sbnd/cohpi/python/output/"

# Output text file
output_txt_file = "nudf_h5_list.txt"

# List all ROOT files in the directory
root_files = [os.path.join(root_files_dir, f) for f in os.listdir(root_files_dir) if f.endswith("nudf.h5")]

# Write the list to the text file
with open(output_txt_file, "w") as file:
    for root_file in root_files:
        file.write(f"{root_file}\n")

print(f"List of ROOT files saved to {output_txt_file}")
