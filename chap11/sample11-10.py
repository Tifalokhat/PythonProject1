import os.path
print('获取目录或文件的绝对路径：',os.path.abspath('./b.txt'))
print('判断目录或文件在磁盘上是否存在：',os.path.exists('b.txt'))
print('判断目录或文件在磁盘上是否存在：',os.path.exists('newb.txt'))
print('判断目录或文件在磁盘上是否存在：',os.path.exists('./好好学习.txt'))
print('拼接路径：',os.path.join('E:/workspace/PycharmProjects/PythonProject1/chap11','b.txt'))
print('分割文件的名和文件后缀名：',os.path.splitext('b.txt'))
print('提取文件名：',os.path.basename('E:/workspace/PycharmProjects/PythonProject1/chap11/b.txt'))
print('提取路径：',os.path.dirname('E:/workspace/PycharmProjects/PythonProject1/chap11/b.txt'))

print('判断一个路径是否是有效路径：',os.path.isdir('E:/workspace/PycharmProjects/PythonProject1/chap11'))
print('判断一个路径是否是有效路径：',os.path.isdir('E:/workspace/PycharmProjects/PythonProject1/chap110'))

print('判断一个路径是否是有效文件：',os.path.isfile('E:/workspace/PycharmProjects/PythonProject1/chap11/b.txt'))
print('判断一个路径是否是有效文件：',os.path.isfile('E:/workspace/PycharmProjects/PythonProject1/chap11/bbb.txt'))