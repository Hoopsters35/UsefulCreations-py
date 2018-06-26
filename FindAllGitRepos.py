"""Program to print directory paths of every directory containing a .git foldder"""

import os, sys

starting_directory = sys.argv[1]
output_file_name = sys.argv[2]
print('Starting directory: {}\nOutput file: {}'.format(starting_directory, output_file_name))


def search_dir(start_dir, output_file):
    for root, dirs, files in os.walk(start_dir):
        if '.git' in dirs:
            print('.git found in {}'.format(root))
            output_file.write(str(root) + "\n")
            dirs[:] = []



with open(output_file_name, 'w') as output_file:
    search_dir(starting_directory, output_file)