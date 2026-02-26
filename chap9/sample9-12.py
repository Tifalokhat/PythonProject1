class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'大家好，我叫：{self.name}，我今年：{self.age}岁')

class Student(Person):
    def __init__(self,name,age,stuno):
        super().__init__(name,age)
        self.stuno=stuno

    def show(self):
        super().show()
        print(f'我来自XXX大学，我的学号是：{self.stuno}')

class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

    def show(self):
        #super().show()
        print(f'大家好，我叫：{self.name}，我今年{self.age}岁，我的工作科室是：{self.department}')

stu=Student('陈梅梅',20,'1001')
stu.show()
doctor=Doctor('张一一',32,'外科')
doctor.show()
