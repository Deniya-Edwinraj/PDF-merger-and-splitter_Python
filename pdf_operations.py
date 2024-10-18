from PyPDF2 import PdfReader, PdfWriter
import os

def merge_pdfs(file_paths, output_path):
    pdf_writer = PdfWriter()
    for path in file_paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    with open(output_path, 'wb') as out_file:
        pdf_writer.write(out_file)

def split_pdf(file_path, page_range, output_folder):
    pdf_reader = PdfReader(file_path)
    page_numbers = []

    for part in page_range.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            page_numbers.extend(range(start - 1, end)) 
        else:
            page_numbers.append(int(part) - 1)  

    for page_number in page_numbers:
        if 0 <= page_number < len(pdf_reader.pages):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])

            output_path = os.path.join(output_folder, f"split_page_{page_number + 1}.pdf")
            with open(output_path, 'wb') as out_file:
                pdf_writer.write(out_file)

