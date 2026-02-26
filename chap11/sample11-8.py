import os
print('当前的工作路径：',os.getcwd())
lst=os.listdir()
print('当前路径下的所有目录及文件：',lst)
print('指定路径下的所有目录及文件：',os.listdir('E:/workspace/PycharmProjects/PythonProject1'))
# os.mkdir('好好学习')
# os.makedirs('./aa/bb/cc')
# os.rmdir('./好好学习')
# os.removedirs('./aa/bb/cc')

os.chdir('E:/workspace/PycharmProjects/PythonProject1')
print('当前的工作路径：',os.getcwd())

for dirs,dirlst,filelst in os.walk('E:/workspace/PycharmProjects/PythonProject1'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('----------------------------')