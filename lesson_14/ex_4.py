# 4_File Splitting:
# Develop a Python Function that reads a large text file (input.txt)
# and splits it into smaller files, each containing a specified number of lines.
# Function paramis ter the number of lines per file.
# Generate multiple output files (output1.txt, output2.txt, etc.)

def split_file(input_file, lines_per_file):
    with open(input_file, "r") as infile:
        lines = infile.readlines()

    num_files = (len(lines) + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"output{i + 1}.txt"
        start_line = i * lines_per_file
        end_line = start_line + lines_per_file

        with open(output_file, "w") as outfile:
            for line in lines[start_line:end_line]:
                outfile.write(line)
        print(f"File '{output_file}' created.")

input_file = "input_4.txt"
lines_per_file = 1
split_file(input_file, lines_per_file)
