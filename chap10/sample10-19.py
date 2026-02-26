import openpyxl
workbook=openpyxl.load_workbook('景区天气.xlsx')
sheet=workbook['景区天气']
lst=[]
for row in sheet.rows:
    sublst=[]
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)
for item in lst:
    print(item)