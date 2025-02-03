# 2_List Element Removal
# Write a function that removes an element at a specified index from a list.
# Handle the IndexError by raising a custom exception if the index is out of range.

def remove_specified_index_element(my_list, index_to_remove):
    try:
        my_list.pop(index_to_remove)
        print(f"Updated list: {my_list}")
    except:
        raise IndexError("Error: Index is out of range.")

my_list = [10, 20, 30, 40, 50]
index_to_remove = 5
remove_specified_index_element(my_list, index_to_remove)