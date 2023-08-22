"""

Proiect Marketplace in FLASK:

Vine un client la noi cu cerința sa ii dezvoltăm o aplicație simplă de Marketplace.

Exemple Marketplace:
Produse de Cofetărie,
Produse de patiserie,
Coffee & Desert,
Produse si Ustensile de bucătărie
Electrocasnice și produse pentru birou

Cerințele lui sunt următoarele:
Sa aiba o baza de date
Sa putem adauga, lista, sterge utilizatori
Sa putem adauga, lista, sterge un produs
Sa putem adauga, lista, modifica, sterge o comanda

Implementați cat mai multe noțiuni învățate în sesiunile de curs anterioare:
- Principiile OOP si Design Patterns
- Iterators
- Generators
- Decorators
"""
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, user, products):
        self.order_id = order_id
        self.user = user
        self.products = products

class Marketplace:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, user):
        self.users.append(user)

    def list_users(self):
        return self.users

    def delete_user(self, user):
        self.users.remove(user)

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return self.products

    def delete_product(self, product):
        self.products.remove(product)

    def create_order(self, user, products):
        order_id = len(self.orders) + 1
        order = Order(order_id, user, products)
        self.orders.append(order)
        return order

    def list_orders(self):
        return self.orders

# Iterators
class ProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration

# Generators
def generate_product_names(products):
    for product in products:
        yield product.name

# Decorator
def secure_order(func):
    def wrapper(self, user, products):
        if user in self.users and all(product in self.products for product in products):
            return func(self, user, products)
        else:
            return "Error: Invalid user or products."
    return wrapper

# Usage
marketplace = Marketplace()

user1 = User(1, "John")
user2 = User(2, "Alice")

marketplace.add_user(user1)
marketplace.add_user(user2)

product1 = Product(1, "Cake", 10)
product2 = Product(2, "Cookies", 5)

marketplace.add_product(product1)
marketplace.add_product(product2)

order = marketplace.create_order(user1, [product1, product2])

print("Users:", marketplace.list_users())
print("Products:", marketplace.list_products())
print("Orders:", marketplace.list_orders())

# Using iterators
product_iterator = ProductIterator(marketplace.list_products())
for product in product_iterator:
    print("Product:", product.name)

# Using generators
product_names_generator = generate_product_names(marketplace.list_products())
for name in product_names_generator:
    print("Product Name:", name)

# Using decorator
@secure_order
def modify_order(marketplace, user, products):
    return marketplace.create_order(user, products)

modified_order = modify_order(marketplace, user1, [product1])
print("Modified Order:", modified_order)

"""
Marketplace -> PRODUSE COFETARIE
"""