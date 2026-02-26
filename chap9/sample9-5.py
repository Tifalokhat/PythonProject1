class Student:
    school='北京XXX教育'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'我叫{self.name}，今年{self.age}岁了')

    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')

    @classmethod
    def cm(cls):
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')

stu=Student('ysj',18)
print(stu.name,stu.age)
print(Student.school)

stu.show()
Student.cm()
Student.sm()