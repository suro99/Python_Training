class Product:
    def get_details(self):
        print("This is a generic product")
       
class Electronics(Product):
    def get_details(self):
        print("Electronics is a 1 year guarantee product")
       
class Clothing(Product):
    def get_details(self):
        print("Clothing is available in all brands")
       
products = [Electronics(), Clothing()]
 
for item in products:
    item.get_details()