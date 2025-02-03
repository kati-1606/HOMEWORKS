# 1_Write a python function, which add a new value with given key in dict.

def add_to_dict(d, key, value):
    d[key] = value
    return d
my_dict = {'a': 1, 'b': 2}
result = add_to_dict(my_dict, 'c', 3)
print(result)


# 2_Write a python program which concat 2 dicts.

def concat_dicts(dict1, dict2):
    return dict1 | dict2
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = concat_dicts(dict1, dict2)
print(result)


# 3_Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers

def create_cubed_dict(N):
    cubed_dict = {}
    for i in range(1, N+1):
        cubed_dict[i] = i**3
    return cubed_dict
result = create_cubed_dict(5)
print(result)


# 4_Write a python function which create dict
# from 2 lists with the same length

def create_dict_from_lists(keys, values):
    if len(keys) != len(values):
        return "The lists must have the same length"
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = create_dict_from_lists(keys, values)
print(result)

