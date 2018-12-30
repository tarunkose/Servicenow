
import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on', num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('Incident')
ws.write(0, 0, 'Incident', style0)
ws.write(0, 1, 'Opened By', style0)
ws.write(0, 2, 'start time', style0)
ws.write(1, 0, 'inc')
ws.write(1, 1, 'Tko')
ws.write(1, 2, datetime.now(), style1)



wb.save('D:/example.xls')
