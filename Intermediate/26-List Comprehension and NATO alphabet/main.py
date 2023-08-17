
with open("file1.txt") as file1:
    file1_list = file1.read().splitlines()
    #print (file1_list)

with open("file2.txt") as file2:
    file2_list = file2.read().splitlines()
    #print (file2_list)

result = [int(num) for num in file1_list if num in file2_list]
#
# # Write your code above 👆
#
print(result)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
student_scores = {student:random.randint(1,100) for student in names}

#passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
passed_students = {student: score for (student,score) in student_scores.items() if score>35}
print(passed_students)

