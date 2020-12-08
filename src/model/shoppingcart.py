from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        self.products.append(product)

    def dis_10(self):
        return 10

    def dis_15(self):
      return 15

    def no_dis(self):
	    return 0

    def check_discount(self,product_code):

      switch_discount = {
          'DIS_10': self.dis_10,
          'DIS_15': self.dis_15
        }

      return switch_discount.get(product_code[:6], self.no_dis)()

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
