# Lambda functions
# A lambda function is a small anonymous function - functions without a name
# lambda arguments : expression

def add(x,y):
    return x+y
    print(add(2,4))
 
add_lambda = lambda x,y: x+y # single line expression
print(add_lambda(10,20))
 
nums = [2,3,4,5,7,8]
sqaured = list(map(lambda x: x**2,nums))
print(sqaured)
 
even = list(filter(lambda x: x%2 == 0, nums))
print(even)
 
students = [
('Viren',89),
('Ravi',90),
('Charlie',34)
]
 
sorted_a = sorted(students, key=lambda x: x[1])
print(sorted_a)
 
max_value = lambda x,y: x if x>y else y
print(max_value(34,89))

result = lambda n: n>1 and all(n%i !=0 for i in range(2, int( n**0.5)+1))
print(result(4))
print(result(17))
print(result(31))