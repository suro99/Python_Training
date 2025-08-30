## Questions ##
# Write a Python program that manages a list of student scores. Perform the following operations step-by-step:
# Create an empty list to store scores.
# Append the scores: 85, 90, 78, 92, 88
# Insert the score 80 at index 
# Remove the score 92 from the list
# Sort the scores in ascending order
# Reverse the list
# Find and print the maximum and minimum score
# Check if 90 is in the list
# Print the total number of scores
# Slice and print the first three scores
# find the last element from the list
# replace the score with new score on the index 2
# create a new copied list also
# Write a program to assign a grade based on the score:
# If score > 90: Grade A
# If score > 80: Grade B
# If score > 70: Grade C
# If score > 60: Grade D
# Else: Grade F
# Use nested if-else.


## Answers ##
student_score = [85, 90, 78, 92, 88]
print("Student Score: ", student_score)
student_score.insert(1, 80) # inserting 80 at the first
print("Student Score After Insertion: ", student_score)
student_score.remove(92) # removing 92 from the list
print("Student Score After Removal: ", student_score)
student_score.sort() # sorting the list
print("Student Score After Sorting: ", student_score)
student_score.reverse() # reversing the list
print("Student Score After Reversing: ", student_score)
print("Student Max Score: ", max(student_score))
print("Student Min Score: ", min(student_score))
print("Is 90 score present: ", 90 in student_score)
print("Sum of list ", sum(student_score))
print("first three scores, student_score", student_score[:3])
print("Last element, student_score", student_score.pop())
student_score[2] = 20  # updating with new score
print("Updated Grocery List:", student_score)
copy_list = student_score.copy()  # copying the list to a new list
print("Copied Grocery List:", copy_list)
for i in student_score:
    if i > 90:
        print("Grade A")
    else: 
        if i > 80:
            print("Grade B")
        else:
            if i > 70:
                print("Grade C")
            else:
                if i > 60:
                    print("Grade D")
                else:
                    print("Grade F")
