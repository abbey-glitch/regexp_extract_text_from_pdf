from PyPDF2 import PdfReader
import re
# txt = "welcome to our channel of exercise, the spirit of exercise"
# pattern = "exercise"
# for match in re.finditer(pattern, txt):
#     s = match.start()
#     d = match.end()
#     print(txt[s:d])
# check = txt.endswith('L')
# print(check)
# check = re.findall(pattern, txt)
# doc_txt = open("frame.pdf")
pdf_text = PdfReader("frame.pdf")

reader = pdf_text.pages
pattern = "flaskanddjango.*\s.*\s.*\s.*"
note = ''
for readers in reader:
    txt = readers.extract_text()
    for txts in re.finditer(pattern, txt, re.IGNORECASE):
        note += txts.group()
        print(txts.group())

print(note)