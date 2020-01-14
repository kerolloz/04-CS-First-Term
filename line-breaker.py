import re


if __name__ == "__main__":
    with open("data-mining.md", 'r') as input_file:
        with open("output.md", 'w') as output_file:
            for line in input_file:
                line = line[:-1] + "  \n"
                output_file.write(line)
