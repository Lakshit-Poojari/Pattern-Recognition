class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("hi", self.name, "your avg is", sum/3)

s1 = Student("Lakshit", [5, 5, 5])
s1.avg()