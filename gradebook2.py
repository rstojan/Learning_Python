# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

# assignments = []

# for grades in student_grades.values():
#     assignments.append(grades[0])
# average = sum(assignments) / len(assignments)
# print(assignments)
# print('The average is:', average)

# I want to take the corresponding positional item in each value from the dictionary 
# (list) into a new list; 
# sum the entries in that new array and divide them by the number of items.
# Then print the results as a list 

averages = []
tmp_list = []
count = 0

while count !=5:
    for grades in student_grades.values():
        tmp_list.append(grades[count])
    print('tmp_list for postion', count, 'is', tmp_list)
    averages.append(sum(tmp_list) / len(tmp_list))
    print('Averages list contents:', averages)
    tmp_list = []
    count += 1

print('The average for each assignment is:', averages)