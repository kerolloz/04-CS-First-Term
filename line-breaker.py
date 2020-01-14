import re
import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name, 'r') as input_file:
        with open("output.md", 'w') as output_file:
            for line in input_file:
                line = line[:-1] + "  \n"
                output_file.write(line)
