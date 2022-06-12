from pdflatex import PDFLaTeX
from pathlib import Path
import sys

file_name = sys.argv[1]

tex_file = Path.cwd() / file_name

pdfl = PDFLaTeX.from_texfile(tex_file)
pdf_data = pdfl.create_pdf()[0]
pdf_file = Path.cwd() / "{}.pdf".format(file_name[:-4])
pdf_file.write_bytes(pdf_data)

