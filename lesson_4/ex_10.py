# SALARIES
#  10_Given the salaries of three employees working at a department,
#  find the amount of money by which the salary of the highest-paid employee differs
#  from the salary of the lowest-paid employee.
#  The input consists of three positive integers-the salaries of the employees.
#  Output a single number, the difference between the top and the bottom salaries

salary1 = int(input("Enter the salary of the first employee: "))
salary2 = int(input("Enter the salary of the second employee: "))
salary3 = int(input("Enter the salary of the third employee: "))
highest_salary = salary1
lowest_salary = salary1
if salary2 > highest_salary:
    highest_salary = salary2
if salary3 > highest_salary:
    highest_salary = salary3
if salary2 < lowest_salary:
    lowest_salary = salary2
if salary3 < lowest_salary:
    lowest_salary = salary3
difference = highest_salary - lowest_salary
print("The difference between the highest and lowest salaries is:", difference)
