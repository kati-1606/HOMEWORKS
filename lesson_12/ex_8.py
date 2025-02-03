# 8_Find student with highest average score
# Write a function that takes a dictionary with information about students.
# Return info about the youngest student

def get_highest_average_student(students_info):
    highest_avg = 0
    best_student = None
    for student_key, student_data in students_info.items():
        avg_score = sum(student_data['scores']) / len(student_data['scores'])
        if avg_score > highest_avg:
            highest_avg = avg_score
            best_student = student_data
    return best_student


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

highest_avg_student = get_highest_average_student(students_info)
youngest_student = get_youngest_student(students_info)
print("Student with the highest average score:", highest_avg_student)
print("Youngest student:", youngest_student)

