#example 1
nums = [1,2,3,4,5]
 
it = iter(nums)
try:
    while True:
        print(next(it))
except StopIteration as e:
    print(e)
    
    
for i in nums:   
    print(i)


#example 2
numbers = [89,34,56,67,23]

it1 = iter(numbers) # get iterator

for res in numbers:
    print(next(it1))

