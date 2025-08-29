age = 56
 
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
   
marks= 67
 
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
   
# switch case  
match marks:
    case 90:
        print("Grade A")
    case 75:
        print("Grade B")
    case 60:
        print("Grade C")
    case _:
        print("Grade D")
       
# while loop
number = 1
 
while number < 1:
    print(number)
    number += 1
   
print("below is the do-while loop")
# do-while loop
number = 1
 
while True:
    print(number)
    number += 1
    if number > 1:
        break
   
# break
for i in range(1,6):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
 
    print("Current number i =", i)
   
# continue
for i in range(1,10):
    if i == 5:
        print("Skipping the value", i)
        continue
    print("num i =", i)
   
r = list(range(1,10,2))
print(r)
 