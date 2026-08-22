class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

area = Circle(2)
print(area.area())
print(area.perimeter())


class Employe():
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role", self.role)
        print("department", self.department)
        print("salary", self.salary)

class Engineer(Employe):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("SDE", "Engineer", 20000)
e1 = Employe("Accountant", "Finance", 20000)
e1.showDetails()

e2 = Engineer("aakash", 21)
e2.showDetails()


class Order:

    def __init__(self, name):
        self.name = name

    def showItem(self):
        print(self.name)

class orderPrice(Order):
    def __init__(self, price):
        self.price = price
        super().__init__("Chips")


    def __gt__(self, o1):
        return self.price > o1.price
        
o1 = orderPrice(12)

o2 = orderPrice(14)

print(o1 > o2)
print(o2 > o1)