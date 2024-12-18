calls = 0


def count_calls():
    global calls
    calls += 1
    return calls
count_calls()

calls = count_calls()
print(calls)


def string_info(string):
    string_1= len (string)
    string_2 = string.upper()
    string_3= string.lower()
    return string_1, string_2, string_3
    #count_calls()
str_=string_info("КраКозябра")
print(str_)

# def is_contains(string, list_to_search):
#     if string in list_to_search:
#         return
# is_str = is_contains('Колушата',['бутявка', 'Колушата'] )
# print(is_str)

#     count_calls()
#print(is_contains)
# print(string_info)
# print(count_calls)
# print(calls)


