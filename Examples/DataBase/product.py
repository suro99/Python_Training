from db import get_connection
 
#create a product
def add_product(name,price,stock):
    conn = get_connection()
    cursor = conn.cursor()
    query = "Insert into products(name,price,stock) values(%s,%s,%s)"
    cursor.execute(query,(name,price,stock))
    conn.commit()
    print(f"Product '{name}' is added succesfully !!")
    cursor.close()
    conn.close()
 
 
#fetch all the products
def list_product():
    conn = get_connection()
    cursor = conn.cursor()
    query = "select * from products"
    cursor.execute(query)
rows = cursor.fetchall()
print("Products below")
 
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Stock:{row[3]}")
 
cursor.close()
conn.close()
 
#update the product
def update_product(product_id,price=None,stock=None):
    conn = get_connection()
    cursor = conn.cursor()
 
if price is not None:
    cursor.execute("update products set price=%s where id=%s",(price,product_id))
if stock is not None:
    cursor.execute("update products set stock=%s where id=%s",(stock,product_id))
 
conn.commit()
print(f"Product ID{product_id} updated successfully !!")
cursor.close()
conn.close()
 
 
#delete a product
def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "delete from product where id=%s",(product_id)
    cursor.execute(query)
    conn.commit()
    print(f"Product '{product_id}' is deleted succesfully !!")
    cursor.close()
    conn.close()