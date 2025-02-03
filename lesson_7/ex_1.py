# 1_Arrange string characters such that lowercase letters should come first

my_string = "PyNaTive"
lowercase = ""
uppercase = ""
for letter in my_string:
    if letter.islower():
        lowercase += letter
    else :
        uppercase += letter

new_string = lowercase + uppercase
print(new_string)