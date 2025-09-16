# In call by reference, the address of actual parameter is copied to formal parameter.
# In call by reference, if we change the value of formal parameter, the actual parameter
# will also be changed.

def result(lst):
    lst = [0,0,0,0] # new list
    print("inside function ", lst)
 
my_list = [1,2,3]
result(my_list)
print("outside function ", my_list)
# call by reference = Mutable type list
# Mutable type: list, dict, set etc.