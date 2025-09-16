# In call by value, the value of actual parameter is copied to formal parameter.
# In call by value, if we change the value of formal parameter, the actual parameter
# will not be changed.

def modify(x):
    x = x +10
    print("inside the function: " , x)
 
a= 5
modify(a)
print("outside function ", a)

 
def result(lst):
    lst.append(10)
    print("inside function ", lst)
 
my_list = [1,2,3]
result(my_list)
print("outside function ", my_list)

# call by value = Immutable type int
# Immutable type: int, float, string, tuple etc. 