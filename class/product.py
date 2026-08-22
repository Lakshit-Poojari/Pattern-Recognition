class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, quantity):
        self.quantity = quantity
        return self.price * self.quantity

    def display_product(self):
        return self.name

p1 = Product("chips", 20 )
print(p1.display_product())
print(p1.total_price(4))