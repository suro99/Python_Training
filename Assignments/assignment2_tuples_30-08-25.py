## Questions ##
# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
 
# Access and print the second element of the tuple product.
 
# Slice and print the last two elements of the product tuple.
 
# Check whether "Electronics" is present in the product tuple and print a message.
 
 
# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
 
# Find and print the maximum and minimum price from the prices tuple.
 
# Use a loop to print each item from the product tuple on a new line.
 
 
# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
 
# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
 
# Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
 
 
# Unpack the tuple product into three variables and print each variable.
 
# Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.


## Answers ##
product = ("Laptop", 50000, 'Black' ,'Samsung' and "Electronics")
print(product)  # print whole tuple
print(product[1])  # Second Element
print(product[len(product)-2:])  # Last Elements 2 elements
if "Electronics" in product:     #Mmeberhsip Test
    print("Electronics is present in the tuple") # Searching for Electronics string

product_price = (1000, 1500, 1200, 1100, 900)
print ("Count of 1000 in the tuple: ", product_price.count(1000)) # count 1000 occours in the tuple

print("Minimum Price:", min(product_price)) # min price in the tuple
print("Maximum Price:", max(product_price)) # max price in the tuple

for a in product_price:
    print(a)  # print elements in new line
    
list1 = list(product_price)
list1[2] = 55000
print(list1)  # print elements after modifying the value

product = product + ('In Stock',) # Append a new char in the tuple
print(product)

removelist = list(product)
removelist.remove('Electronics') # Remove a char in the tuple indirectly
product = tuple(removelist)
print (product)

product, price, colour, stock = product  #Unpacking the tuple
print ('product: ', product, ', price: ', price, ', Colour: ', colour, ', Stock: ', stock )

nested = (product_price, product)  #tuple within the tuple = nested tuples
print("The nested tuple is ", nested)

print("Accessing nested 2nd tuple element:", nested[1][1])  # accessing 2nd element
