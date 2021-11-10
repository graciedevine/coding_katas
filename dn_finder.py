import PyPDF2


pdfFileObj = open("05.10.2021 (7) Achs $36,945.23 EDITED KEYED 05.11.21 TG.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
content = pageObj.extractText()


search_word = "1932541"
if search_word in content:
    print("Debit note found.")
else:
    print("Debit note not found.")

pdfFileObj.close()
