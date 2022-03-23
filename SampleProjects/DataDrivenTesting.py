import xlrd

loc = "E:/Login.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

p1 = sheet.cell(0, 0).value
print(p1)