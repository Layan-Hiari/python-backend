class Product:
    def init(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price -= discount

    def restock(self, amount):
        self.quantity += amount

    def get_price(self):
        return self.price

    def add(self, other):
        if self.product_id == other.product_id:
            return Product(self.product_id, self.name, self.price, self.quantity + other.quantity)
        else:
            raise ValueError("Products must have the same ID to add quantities.")

    def call(self):
        print(f"{self.name}: ${self.price:.2f}, Qty: {self.quantity}")


class DigitalProduct(Product):
    def init(self, product_id, name, price, quantity, file_size):
        super().init(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent > 20:
            percent = 20
        super().apply_discount(percent)


class PhysicalProduct(Product):
    def init(self, product_id, name, price, quantity, weight):
        super().init(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        super().apply_discount(percent)
        if self.get_price() < 5:
            self._Productprice = 5
#add → Combines quantities of two same products.

#call__ → Allows calling the object like a function to print summary.