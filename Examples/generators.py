#Generator
 
def count_down(n):
    while n>0:
        yield n
        n = n-2
        print("n ", n)
 
for i in count_down(5):
    print(i)
 
 
def somexample():
    print("start generator")
    yield 1
    print("yielded 1, resuming")
    yield 2
    print("yielded 2, resuming")
    yield 3
    print("yielded 3, resuming")
 
gen = somexample()
 
print("first next()", next(gen))
print("second next()", next(gen))
print("third next()", next(gen))