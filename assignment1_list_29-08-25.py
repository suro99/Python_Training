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
