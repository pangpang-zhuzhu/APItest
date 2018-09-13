import xlrd
import os
proDir = os.path.split(os.path.realpath(__file__))[0]#该文件所在路径（不含该文件）E:\pangpang\interfaceTest\try \excel.py
# print(proDir)
def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = [] #空列表
    # get xls file's path
    xlsPath = os.path.join(proDir, xls_name)#拼接表格位置路径
    # open xls file
    file =xlrd.open_workbook(xlsPath)#打开表格
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)#根据sheet名字打开sheet
    # get one sheet's rows
    nrows = sheet.nrows#行总数
    #print(sheet.row_values(0))
    #确定列
    k = 1
    for k in sheet.row_values(0):#第一行的值，从第一列开始循环
        if sheet.row_values(0)[k] == "execute":#确定第1行的第k列是execute
            break#确定了execute列的k列
        else:
            k += 1
    #确定行
    for i in range(nrows):#rang(nrows)代表从0到nrows(不包括nrows)/第一行到最后一行
        #排除第一行而且该行execute的值为“y”
        if sheet.row_values(i)[k] != u'execute' and str.lower(sheet.row_values(i)[k]) == "y":#u表示将后面跟的字符串以unicode格式存储
            cls.append(sheet.row_values(i))#列表的尾部添加该行的值
    return cls











filename='E:\\test1.xlsx'
workbook = xlrd.open_workbook(filename)
sheets = workbook.sheet_names()
# print(sheets)
worksheet = workbook.sheet_names()[0]
print(worksheet) #得到表名称
yushuo_sheet= workbook.sheet_by_name('yushuo')#通过表名称获取
print(yushuo_sheet)#得到一个内存地址
nums = yushuo_sheet.nrows #得到行数
print(nums)

#获取整行整列的值-->得到的是个列表
rows = yushuo_sheet.row_values(0) #获取第一行的标题
cols = yushuo_sheet.col_values(1) #获取第二列的数据
print (rows)
print (cols)

# 获取单元格内容
para = yushuo_sheet.cell_value(1, 6)
print(para) #2行6列
url = yushuo_sheet.cell_value(1, 5)
print(url)
