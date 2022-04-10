class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def __add__(self, other):
        pret=self.price+other.price
        return pret

class Phone(Product):
    def __init__(self, name, price, ram, cpu):
        Product.__init__(self, name, price)
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        return f"The new {self.name} is an unforgettable experience, CPU {self.cpu}, RAM {self.ram}."

class Refrigerator(Product):
    def __init__(self, name, price, energy_label):
        Product.__init__(self, name, price)
        self.energy_label = energy_label

    def __str__(self):
        return f"Enjoy fresh food with {self.name}, energy label {self.energy_label}."

class Stock:
    def __init__(self, list_stock):
        self.list_stock = []
        for product in list_stock:
            self.list_stock.append(product)

    def add(self, new_product):
        self.list_stock.append(new_product)
    
    def remove(self, product_name):
        for i in self.list_stock:
          if i == product_name:
            self.list_stock.remove(i)

    def view(self):
       return self.list_stock

class Cart:
    def __init__(self):
        self.list_cart = []

    def add(self, new_product):
        self.list_cart.append(new_product)

    def remove(self, product_name):
         for i in self.list_cart:
          if i.name == product_name:
            self.list_cart.remove(i)

    def view(self):
        return self.list_cart

    def cart_checkout(self):
        sum=0
        for i in self.list_cart:
            sum=sum+i.price
        del self.list_cart
        return sum

class Store:
    def __init__(self, stock):
        self.stock = stock
        self.customer_carts = dict() #! de explicat in enunt: dict(customer_id, cart)

    def login(self, customer_id):
        self.customer_carts[customer_id] = Cart()

    def add_to_cart(self, customer_id, product_name):
        for product in self.stock.list_stock:
              if product_name == product.name:
                  if customer_id in self.customer_carts.keys():
                        self.customer_carts[customer_id].add(product)
                        self.stock.remove(product_name)
        #    self.customer_carts[customer_id].add(product_name)
        #if self.customer_id in self.customer_carts:
        #    self.customer_carts=list(self.customer_carts)
        #    self.customer_carts.append(self.product_name)
        #    self.customer_carts=dict(self.customer_carts)
        #    print(type(self.customer_carts))
        #    stock.remove(self.product_name)

    def remove_from_cart(self, customer_id, product_name):
        if customer_id in self.customer_carts.keys():
          for product in self.customer_carts[customer_id].list_cart:
                if product_name == product.name:
                  self.customer_carts[customer_id].remove(product_name)
                  self.stock.add(product)
        #if self.customer_id in self.customer_carts:
        #    for i in self.customer_carts:
        #        if i==self.product_name:
        #            self.customer_carts[customer_id].remove(i)
                #    cart=list(self.customer_carts)
                #    cart.remove(i)
                #    self.customer_carts=tuple(cart)
                #    stock.add(self.product_name)
                    
    def view_cart(self, customer_id):
        x=[]
        if customer_id in self.customer_carts.keys():
          for produs in self.customer_carts[customer_id].view():
              x.append((produs.name, produs.price))
        return x
    
    def checkout(self, customer_id):
        if customer_id in self.customer_carts.keys():
           return self.customer_carts[customer_id].cart_checkout()

test_product = Product('Samsung Toaster', 20)
test_product2 = Product('Nokia', 100)
test_phone = Phone("Alcatel", 13, '4GB', 'Intel')
list_products = []
list_products.append(Phone('Iphone 12', 300, '4GB', 'A14 Bionic'))
list_products.append(Phone('Samsung Galaxy S20', 200, '8GB', 'Exynos Octa-core'))
list_products.append(Phone('Huawei P40', 250, '6GB', 'Exynos Octa-core'))
list_products.append(Refrigerator('Arctic CR-420', 500, 'A+'))
list_products.append(Refrigerator('Heinner CR-20', 100, 'A'))
stock = Stock(list_products)
stock.add(Phone('Iphone 5', 160, '2GB', 'Apple A8'))
stock.remove('Huawei P40')
cart = Cart()
cart.add(Phone('Iphone 5', 100, '2GB', 'Apple A8'))
cart.add(Phone('Iphone 12', 200, '8GB', 'Apple A16'))
cart.add(Refrigerator('Arctic E-100', 800, 'A+'))
print(test_product+test_product2)
print(test_phone)
for product in list_products:
    print(product)
for product in stock.view():
    print(product)
print(cart.cart_checkout())
store = Store(stock)
store.login('batgirl123')
store.login('pavelintruder1')
store.add_to_cart('batgirl123', 'Iphone 12')
store.add_to_cart('pavelintruder1', 'Megaphone X')
store.add_to_cart('pavelintruder1', 'Iphone 12')
store.remove_from_cart('batgirl123', 'Iphone 12')
store.add_to_cart('batgirl123', 'Samsung Galaxy S20')
store.add_to_cart('batgirl123', 'Heinner CR-20')
print(store.view_cart('batgirl123'))
print(store.checkout('batgirl123'))
print(store.view_cart('pavelintruder1'))
print(store.checkout('pavelintruder1'))
