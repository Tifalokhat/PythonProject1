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

class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

stu=Student('陈梅梅',20,'1001')
stu.show()
doctor=Doctor('张一一',32,'外科')
doctor.show()
