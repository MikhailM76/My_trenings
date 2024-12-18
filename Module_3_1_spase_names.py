calls = 0
def count_calls():
    pass
def string_info(string):
    count_calls()
    return len(string), "string".upper,"string".lower

def is_contains(string, list_to_search):
    if string in list_to_search:
        is_contains == True
    else:
        is_contains == False

    count_calls()
print(is_contains)
print(string_info)
print(count_calls)
print(calls)


