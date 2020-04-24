# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

# sum up each list; see who is the highest; loop over each and percentage = value / highest * 100
# fill up another dict with the same keys of the average values

totals = {}

for something in student_grades.values():
    max_length = 0
    if len(something) > max_length:
        max_length = len(something)

total_points = max_length * 100

for name, grade in student_grades.items():
    totals.update({name: sum(grade)})
print(totals)

for key, value in totals.items():
    if key == max(totals):
        print(key, 'has the highest score with a total of:', value)
        totals_highest_score = value

curve = total_points - totals_highest_score

new_dict = {}

for key, value in totals.items():
    new_grade = curve + value
    new_dict.update({key: new_grade / max_length})
print('Totals with new grades:', new_dict)