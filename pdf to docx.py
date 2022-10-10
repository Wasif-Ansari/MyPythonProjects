from pdf2docx import Converter

pdf_file = "- Goldman Sachs.pdf"
docx_file = "out.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
