# Multiple Exceptions:
# Write a function that performs the following tasks:
# Accepts a list and an index as input.
# Attempts to access the element at the given index in the list.
# Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not

def access_element(lst, index):
    try:
        element = lst[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range.")
    finally:
        print("Task completed.")

my_list = [10, 20, 30, 40, 50]
access_element(my_list, 2)  # Valid index
access_element(my_list, 10)  # Invalid index
