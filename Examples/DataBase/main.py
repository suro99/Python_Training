from product import add_product,delete_product,list_product, update_product
 
def menu():
    while True:
        print("\n======== Product Menu========")
        print("1. Add Product")
        print("2. List all Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
 
choice = input("Enter choice(1-5):")
 
if choice == "1":
    name=input("Enter product name")
    price=input("Enter product price")
    stock=input("Enter product stock")
    add_product(name,price,stock)
 
elif choice == "2":
    list_product()
 
elif choice == "3":
    pid=int(input("Enter product id to update"))
    price=input("Enter new price")
    stock=input("Enter new stock")
 
    update_product(pid,
    price=float(price) if price else None,
    stock=int(stock) if stock else None)
 
elif choice =="4":
    pid=int(input("Enter product id to delete"))
    delete_product(pid)
 
elif choice =="5":
    print("exiting.. the menu !!")
 
else:
    print("Wrong option !!")
 
if __name__ == "__main__":
    menu()