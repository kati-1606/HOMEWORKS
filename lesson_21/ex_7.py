# Tuple Exercise:
# Write a function that swaps the values of two tuples.

def swap_tuples(tuple1, tuple2):
    return tuple2, tuple1

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

swapped_tuple1, swapped_tuple2 = swap_tuples(tuple1, tuple2)

print(f"Original tuple1: {tuple1}")
print(f"Original tuple2: {tuple2}")
print(f"Swapped tuple1: {swapped_tuple1}")
print(f"Swapped tuple2: {swapped_tuple2}")
