import pdfplumber
with pdfplumber.open('C:\\Users\\Lenovo\\Desktop\\求职\\resume.pdf') as pdf:
    for i in pdf.pages:
        print(i.extract_text())
        print(f'----------{i.page_number}页结束')