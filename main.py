import PyPDF2

# open, rotate, and save as new pdf

# open pdf in binary mode with 'rb'
with open('test_pdfs/converter_gates_schematic.pdf', 'rb') as file:
    # create PyPDF reader and get page
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    # create writer
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    # write in binary mode with 'wb'
    with open('test_pdfs/rotated.pdf', 'wb') as new_file:
        writer.write(new_file)

