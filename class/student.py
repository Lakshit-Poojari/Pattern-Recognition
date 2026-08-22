class Student:
    def __init__(self, name, age, marks):
        self.name= name
        self.age= age
        self.marks=marks

    def displayInfo(self):
        print("Name of student is ", self.name, "age is ", self.age , "and marks is ", self.marks)

    def isPassed(self):
        if self.marks >= 35:
            print(self.name , " is passed")
        else:
            print(self.name, "is Failed")

s1 = Student("Rahul", 20, 75)
s1.displayInfo()
s1.isPassed()

s2 = Student("sam", 10, 25)
s2.displayInfo()
s2.isPassed()