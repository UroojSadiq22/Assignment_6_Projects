# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative!")
        self._price = new_price
        print(f"\nUpdating price...")
    
    @price.deleter
    def price(self):
        print("\nDeleting price...")
        del self._price

product = Product(100)
print("Initial Price:", product.price)

product.price = 150
print("Updated Price:", product.price)

del product.price



