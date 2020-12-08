from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        self.products.append(product)

    def check_discount(self,product_code):
        if product_code.startswith('DIS'):
            num_dis = int(''.join(filter(str.isdigit,product_code))[:2])
            return num_dis
        else:
            return 0

    def calculate_points(self, dicount, price):
      if dicount == 0:
        return price / 5
      else:
        return price / dicount

    def calculate_price(self, discount, price):
      return price - (price * discount/100)

    def checkout(self):
        total_price = 0.00
        loyalty_points_earned = 0.00
        for product in self.products:
            discount = self.check_discount(product.product_code)
            total_price += self.calculate_price(discount, product.price)
            loyalty_points_earned += self.calculate_points(discount, product.price)
        return Order(int(loyalty_points_earned), total_price)


    def __str__(self):
        product_list = "".join('%s'%product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
