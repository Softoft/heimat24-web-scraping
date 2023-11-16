import os

from PyPDF2 import PdfWriter, PdfReader


def merge_pdfs(directory, output_filename):
    pdf_writer = PdfWriter()

    for item in os.listdir(directory):
        if item.endswith('.pdf'):
            print(item)
            try:
                file_path = os.path.join(directory, item)
                pdf_reader = PdfReader(file_path)

                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
            except Exception as e:
                print(f"Failed to add {item}: {e}")

    with open(output_filename, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)


if __name__ == '__main__':
    directory = 'data/toulon_pdf'
    output_filename = 'merged.pdf'
    merge_pdfs(directory, output_filename)
