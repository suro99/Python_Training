# The above code demonstrates exception handling in file operations.
# It checks for the existence of a directory, renames or creates it accordingly,
# and attempts to read a file while handling potential errors gracefully.
# It ensures that resources are properly managed using try-except-finally blocks.
# This is a basic example of how to handle exceptions in Python.
# The code also includes comments explaining each step for clarity.
# The code is structured to provide a clear understanding of exception handling mechanisms in Python.

import os 
path = 'D:\\Python_Kolkata_Programs\\File_Handling\\back'
if os.path.exists(path):
    print(" the directory is present ")
    os.rename(path, 'D:\\Python_Kolkata_Programs\\backed-up')
    print(" the directory is renamed ")
else:
    print(" the directory is not present ")
    os.mkdir(path)
    print(" the directory is created ")
try:
    f = open('D:\\Python_Kolkata_Programs\\File_Handling\\students.txt', 'r')
    content = f.read()
    print(content)
except FileNotFoundError:
    print(" The file is not present ")
finally:
    try:
        f.close()
    except NameError:
        pass

#################################################################################

# This code demonstrates custom exception handling in Python.
# It defines a custom exception class RangeError to handle specific range violations.
# The program prompts the user to input two numbers and checks if the first number is within a valid range.
# If the first number is out of range, it raises a RangeError.
# It also handles potential ZeroDivisionError and ValueError exceptions that may occur during input and division.
# The use of try-except-else-finally blocks ensures that exceptions are caught and handled appropriately,
# and that a completion message is printed regardless of whether an exception occurred.
# The code is structured to provide a clear understanding of custom exception handling mechanisms in Python.
# The code also includes comments explaining each step for clarity.
class RangeError(Exception): pass
try:
    number1 = int(input("Enter a number: "))
    if number1 >50 and number1 <100: raise RangeError("number1 should be between 0 and 50")
    number2 = int(input("Enter a second number: "))
    result = number1/number2
except ZeroDivisionError as e:
    print("exception caught:",e)
except ValueError as e:
    print("exception caught:",e)
except RangeError as e:
    print("custom error caught:",e)
else:
    print("The result is:", result)
finally:
    print("Execution completed.")
