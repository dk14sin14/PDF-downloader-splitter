from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

def split_pages(input_dir, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    total_file_count = 0
    err22_count = 0

    for i in Path(input_dir).rglob('*.pdf'):
        try:
            name = i.stem
            pdf = PdfFileReader(i.open('rb'), strict = False)
            total_page = pdf.getNumPages()
            print(f"saving page {i}, total pages is {total_page}")

            for p in range(0, total_page):
                output = PdfFileWriter()
                output.addPage(pdf.getPage(p))
                output_path = Path(output_dir).joinpath(f'{name}_{p+1}.pdf')
                with open(output_path, "wb") as outputStream:
                    output.write(outputStream)
                    total_file_count += 1
        except OSError:
            err22_count += 1
            print("OSErr22 occured")
            continue
    print(f"Total split files = {total_file_count}")
    print(f"OSErr22 count = {err22_count}")



split_pages("pdf_files", "split_files")
