import os
# os.remove('./a.txt')
# os.rename('./aa.txt','newaa.txt')

import time
def date_format(longtime):
    s=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(longtime))
    return s

info=os.stat('./newaa.txt')

print(type(info))
print(info)

print('最近一次访问时间：',date_format(info.st_atime))
print('在windows操作系统中显示的文件的创建时间：',date_format(info.st_ctime))
print('最后一次修改时间：',date_format(info.st_mtime))
print('文件的大小（单位是字节）：',info.st_size)

# os.startfile('calc.exe')
os.startfile(r'C:\Users\Lenovo\AppData\Local\Programs\Python\Python313\python.exe')