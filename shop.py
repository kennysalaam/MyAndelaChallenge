class Shop(ShoppingCart):
  def __init__(self):
    ShoppingCart.__init__(self)
    self.quantity = 100
    
  def remove_item(self):
    self.quantity = self.quantity - 1