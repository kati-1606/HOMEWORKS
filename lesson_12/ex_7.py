# 7_Find youngest student
# Write a function that takes a dictionary with information about students.
# Return info about the youngest student

def find_youngest_student(students_info):
    youngest_student = None
    youngest_age = list(students_info.values())[0]['age']

    for student, info in students_info.items():
        if info['age'] < youngest_age:
            youngest_age = info['age']
            youngest_student = info

    return youngest_student

students_info = {
    'student1': {
        'name': 'John Doe',
        'age': 20,
        'subjects': ['Math', 'Physics', 'English'],
        'scores': [7, 9, 9, 6],
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 19,
        'subjects': ['Chemistry', 'Biology', 'History'],
        'scores': [5, 6, 8, 10],
    },
    'student3': {
        'name': 'Bob Johnson',
        'age': 21,
        'subjects': ['Computer Science', 'Statistics', 'Psychology'],
        'scores': [8, 8, 9, 9, 9],
    }
}

youngest = find_youngest_student(students_info)
print(youngest)