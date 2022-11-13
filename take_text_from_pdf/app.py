import PyPdf2
pdf = open('Digitalcommunication.pdf' , 'rd')
reader= PyPdf2.PdfFileReader(pdf)
page=reader.getpage(0)
print(page.extractText())