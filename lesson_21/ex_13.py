# Sets Exercise:
# Write a function that checks if two sets are disjoint (have no common elements).

def are_sets_disjoint(set1, set2):
    return set1.isdisjoint(set2)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

print(are_sets_disjoint(set1, set2))
print(are_sets_disjoint(set1, set3))