# 3_Write a Python program to check whether a given
# string is number or not using Lambda.

is_num = lambda q: q.replace('.', '', 1).isdigit() or q[0] == '-' and q[1:].replace('.', '', 1).isdigit()

print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print(is_num('python'))