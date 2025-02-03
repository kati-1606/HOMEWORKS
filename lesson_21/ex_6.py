# Tuple Exercise:
# Create a tuple of student names and their corresponding scores.
# Write a function to find the student with the highest score.

def find_top_student(students_scores):
    top_student = max(students_scores, key=lambda student: student[1])
    return top_student

students_scores = (("Alice", 90), ("Bob", 85), ("John", 92), ("David", 88))
top_student = find_top_student(students_scores)

print(f"The student with the highest score is: {top_student[0]} with a score of {top_student[1]}")
