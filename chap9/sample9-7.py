class Student:
    school='北京XXX教育'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'我叫{self.name}，今年{self.age}岁了')

stu=Student('ysj',18)
stu2=Student('陈梅梅',20)
print(stu.name,stu.age)
print(stu2.name,stu2.age)

stu2.gender='男'
print(stu2.name,stu2.age,stu2.gender)

def introduce():
    print('我是一个普通的函数，我被动态绑定成了stu2对象的方法')

stu2.fun=introduce
stu2.fun()