
def find_dict_with_value(list_of_dicts, search_string):
    return next((d for d in list_of_dicts if any(search_string.lower() in v.lower() for v in d.values())), None)

list_of_dicts = [
    {'key1': 'test', 'key2': 'acb'},
    {'key1': 'test1', 'key2': 'abc', 'key3': 'cbf'},
    {'key1': 'test2', 'key2': 'def', 'key3': 'qwe'}
]

search_value = 'sachin'
result_dict = find_dict_with_value(list_of_dicts, search_value)

if result_dict:
    print(f"Dictionary containing '{search_value}' in a value: {result_dict}")
else:
    print(f"No dictionary found containing '{search_value}' in any value.")
