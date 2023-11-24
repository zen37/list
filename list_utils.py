def remove_duplicates(lst):
    unique_map = {}  # This is a dictionary (hashmap) in Python

    for element in lst:
        unique_map[element] = True

    unique = list(unique_map.keys())

    return unique