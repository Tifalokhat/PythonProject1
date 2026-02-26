import weather
import openpyxl
html=weather.get_html()
lst=weather.parse_html(html)
workbook=openpyxl.Workbook()
sheet=workbook.create_sheet('景区天气')
for item in lst:
    sheet.append(item)

workbook.save('景区天气.xlsx')