#深圳A股股票编码代码import xlrdimport osfrom xlrd import open_workbookfrom xlwt import easyxffrom xlutils.copy import copydef save(i,a):   excel = r"D:\SHENZHENCopy.xls"   rb = open_workbook(excel)   wb = copy(rb)   s = wb.get_sheet(0)   s.write(i,21,a)   os.remove(excel)   wb.save(excel)excel = 'D:\shenzhen.xlsx'workbook = open_workbook(excel)sheet = workbook.sheet_by_index(0)rows = sheet.nrowsprint rowsfor i in range(1,rows):    a = sheet.cell(i,20).value    try:      print i      a =  int(a)      print a      a =  hex(a)      a = str(a)      a = a[2:]      if len(a) ==1:          a = '000' + a      if len(a) ==2:          a = '00' + a      if len(a) ==3:          a = '0' + a      a = '401110000000' + a      print a      save(i,a)    except Exception,e:        print e