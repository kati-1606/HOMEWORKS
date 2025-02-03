# 3_File Concatenation:
# Write a Python script that takes multiple text files as input
# and concatenates their contents into a single text file

input_files = ["file_1.txt", "file_2.txt", "file_3.txt"]

with open("output_3.txt", "w") as outfile:
    for filename in input_files:
            with open(filename, "r") as infile:
                outfile.write(infile.read() + "\n")

print(f"All files have been concatenated into 'output_3.txt'.")