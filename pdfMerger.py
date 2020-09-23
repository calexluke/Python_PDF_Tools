import PyPDF2
import sys
import os

# run this program from the command line with one argument after the .py file: the name of the combined pdf to be
# created. The program loops through each item in the the present working directory and merges all pdf files into one

new_pdf_name = sys.argv[1]
source_dir = os.getcwd()

# create merger object
merger = PyPDF2.PdfFileMerger()

# loop through all files in directory
for file in os.listdir(source_dir):
    if file.endswith('pdf'):
        merger.append(file)
merger.write(new_pdf_name)

