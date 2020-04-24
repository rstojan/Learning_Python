# Print the name and grade percentage of the student with the highest total of points.

# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

totals = {}

for name, grade in student_grades.items():
    totals.update({name: sum(grade)})
print(totals)

for key, value in totals.items():
    if key == max(totals):
        print(key, 'has the highest score with a total of:', value)