import requests
import xlrd
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



# url = 'http://restapi-test1.fishsaying.com/sso/login/normal'
# Parameter =
#
#     {
#     'account': 'test_ff',
#     'password':'123456',
#     # 'isRemember':'true',
#     # 'service':'100',
#     # 'service':'201'
# }

# header = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Origin':'http://test-1.yushuoyun.com',
#     'Referer':'http://test-1.yushuoyun.com/login',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#     'X-Requested-With':'XMLHttpRequest'
# }

response = requests.post(url, para)

print(response.json())

# url_login = 'http://restapi-test1.fishsaying.com/cultural-cloud/user/cloud/login'
# Parameter