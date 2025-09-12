import glob
import re

files = glob.glob("/home/kolkata/Python/st*.txt") + glob.glob("/home/kolkata/Python/*.csv")
print(files)
 
text = "The price of the product is very high"
match = re.search(r"product",text)
if match:
    print(" It is found: ", match.group())
   
 
text = "Yesterday was Thursday, Today is Friday and tomorrow will be Saturday"
pattern = r"\b(Thursday|Friday)\b"
new_text = re.sub(pattern,"weekday",text) 
# print(new_text)
pattern = r"\b(Saturday)\b"
new_text1 = re.sub(pattern,"weekend",text)
print(new_text, new_text1)