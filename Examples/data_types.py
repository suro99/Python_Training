integer_number = 30.89
floating_number = 3.14566
complex_number = 3 +7j
 
is_active = True
text = "Hello, World!"    # text or String
empty_value = None
 
print("This is the int value with: ", integer_number , " ->" , type(integer_number))
print("This is the complex value ", complex_number , " ->" , type(complex_number))
 
print("This is the value", is_active , " ->" , type(is_active))
print("This is thevaue  ", empty_value , " ->" , type(empty_value))
print("\n" + "-"*50 + "\n")
 
# Below are the complex types
numbers = [45,36,78,89,23]    # list
coordinates = (10.0, 20.0)    # tuple
unique_numbers = {1, 2, 3, 4, 5, 2, 4}    # set = no duplicate values
person = {"name": "John", "age": 30}    # dictionary = key-value pairs
print(numbers)
 
samplefrozenSet = frozenset(unique_numbers)   # frozenset = immutable set
print(samplefrozenSet)
 