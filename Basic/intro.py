import win32com.client

# word=win32com.client.Dispatch('Word.Application')
# word.visible=True

excel=win32com.client.Dispatch('Excel.Application')
excel.visible=True
wb=excel.Workbooks.Add()
ws=wb.Worksheets('Sheet1')

ws.Cells(1,1).Value='Hello World'
wb.SaveAs('D:\\work\\VSStudio\\Kiwoom\\test.xlsx')
excel.Quit()

# wb=excel.Workbooks.Open('D:\\work\\VSStudio\\Kiwoom\\python_test.xlsx')
# ws=wb.ActiveSheet
# print(ws.Cells(1,1).Value)
# excel.Quit()