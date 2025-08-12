class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return f"{self.name} ({self.category}) -  {self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name.lower() != name.lower()]

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def display_order(self):
        for item in self.items:
            print(item.display())
        print(f"Total: ${self.calculate_total():.2f}")


item1 = MenuItem("Bites", 7 , "Appetizer")
item2 = MenuItem("chocolate", 11 , "Main")
item3 = MenuItem("Lava Cake", 7 , "Dessert")

order = Order()
order.add_item(item1)
order.add_item(item2)
order.add_item(item3)

order.remove_item("Bites")

order.display_order()

