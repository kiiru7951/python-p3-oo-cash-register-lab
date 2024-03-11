#!/usr/bin/env python3
import ipdb

class CashRegister:
  def __init__(self, discount=0):
    self.items = []
    self.total = 0
    self.discount = discount    
    self.prices = []
    self.items_list = []
 
  def add_item(self, item, amount, quantity=1):
    self.quantity = quantity
    self.items.extend([item] * quantity)
    self.items_list.extend([item])
    self.total += amount * quantity
    self.prices.extend([amount] * quantity)
    return self.total

  def apply_discount(self):
    discounted_total = self.total - (self.total * self.discount / 100)
    if self.discount != 0:
      print(f"After the discount, the total comes to ${int(discounted_total)}.")
    else:
      print("There is no discount to apply.")
    self.total = int(discounted_total)
  
  def void_last_transaction(self):
    if self.items:
        print(self.items)
        print(self.items_list)
        last_price = self.prices.pop()
        print(last_price)
        print(self.total)
        self.total = self.total - (last_price* self.quantity)
        print(self.total)
        self.items = self.items_list[:-1]
        print(self.items)
        if self.items == []:
          self.total = 0.0
          print("Total if all items are removed == 0.0:", self.total)
    return self.total


register = CashRegister()
register.add_item("oranges", 6.56, 5)
register.add_item("tomato", 1.76, 2)
print(register.void_last_transaction())
print(register.total)
# Last test took me sooo long :)