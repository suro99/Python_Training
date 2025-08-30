s1 = "Samsung LED is good TV and is available in mutiple colors"
s2 = '                    Brand is good                                             '
s3 = """This is a good rband in the market
You can see multiple products of multiple categories
Available in all the major retail stores
you can buy online also.
"""
 
print([s1, s2, s3])
 
print(s1[2])
print(s1[0:6])
print(s1[0:10:2])  # step value
print(s1[-1])  # last character
print(s1[-4:])  # negative indexing including the last chafacter
print(s1[-4:-2])  # negative indexing eclusign the last character
print(s1[-5])  # negative indexing to fetch the 5th indexed character from last
print(s1[::-1])  # reversing the string
 
print("Length of the string s1:", len(s1))
 
print( s1 * 4) # repeating the string
 
print(s2.upper()) # converting to upper case
print(s2.lower()) # converting to lower case
print(s2.strip()) # removing leading and trailing spaces
print(s1.replace("is", "are")) # replacing the string
print(s3.split(" ")) # splitting the string based on space
print(s1.startswith("Sam")) # checking the starting of the string
print(s1.endswith("LED ")) # checking the ending of the string
print(s1.find("LED")) # finding the index of the substring
print(s1.count("in")) # counting the occurrence of a substring
 
v = "black, white, grey,darkblack"
res = v.split(",") # splitting the string based on comma
print(res)
x = "::".join(res) # joining the list elements with hyphen
print(x)
 
print("is" in s1) # membership test
reverse_Str = ''.join(reversed(s1)) # reversing the string using reversed() function
print(reverse_Str)
