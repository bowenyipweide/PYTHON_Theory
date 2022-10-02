#For loop 
numbers = [1, 2, 3]
new_list = []
for n in numbers:
  add_1 = n + 1
  new_list.append(add_1)
  
#List Comprehension 
numbers = [1, 2, 3] or "Bowen" or range(1,5)
new_list / new_letter / new_range = [new_item for item in list] or [letter for letter in list] or [new_item for item in range(1,5)]
#list represent numbers 
#item represent items in the list
#add_1 = n + 1 reppresent new_item of expression
new_list = [n + 1 for n in numbers]

#condition List Comprehension 
name = ["Bowen", "bobo", "bibi"]
new_list = [new_item for item in list if test]

short_names = [name for name in names if len(name) < 4]
long_names = [name.upper() for name in names if len(name) > 4]

#Python sequence: 
list 
range 
string 
tuple


#Dictionary Comprehension
new_dict = {new_key:new_value for (key:value) in dict.items()}

example 
import random
names = ['alex', 'beth', 'caroline', 'dave']
students_scores = {student:random.randint(1,100) for student in names}
#loop entire value of student_scores
passed_students = {student:score for (student,score) in students_score.items() if score >= 60} 
