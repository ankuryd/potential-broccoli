import re
import sys
import pdfplumber
import PyPDF2

def is_subseq(x, y):
    it = iter(y)
    return all(c in it for c in x)

filename = sys.argv[1]

pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
total = pdfReader.numPages

valid_pages = []
last_text = None

with pdfplumber.open(filename) as pdf:
    for i in range(total):
        page = pdf.pages[i]
        text = page.extract_text()
        text = re.sub(r'\s+', ' ' ,re.sub(r'\n+', ' ', text))
        text = ' '.join(sorted(text.split(' ')))
        if last_text and is_subseq(last_text, text):
            valid_pages.pop()
        valid_pages.append(i)
        last_text = text
        page.close()

pdfWriter = PyPDF2.PdfFileWriter()
outputpdf = filename.split('.pdf')[0] + '_cleaned.pdf'

for page in valid_pages:
    pdfWriter.addPage(pdfReader.getPage(page))
     
with open(outputpdf, 'wb') as f:
    pdfWriter.write(f)

pdfFileObj.close()
