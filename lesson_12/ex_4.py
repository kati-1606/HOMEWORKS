# 4_Find Index Function
# Write a function that finds the index of a given element in a list.
# If the element is not present, return -1

def get_index_of_element_in_a_list(sequence, element):
    for i in range(len(sequence)):
        if sequence[i] == element:
            return i
    return -1
print(get_index_of_element_in_a_list([1, 2, 3, 4, 5], 3))
print(get_index_of_element_in_a_list([1, 2, 3, 4, 5], 6))