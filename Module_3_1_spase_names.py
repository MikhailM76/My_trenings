calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        if i.lower() == string:
            return True
    return False


print(string_info("КраКоЗябра"))
print(string_info("рОдоДендРоН"))
print(is_contains('Колушата', ['бутявка', 'Колушата']))
print(is_contains("Барвинок", ["Просьба", "цветы", "не рвать"]))
print(calls)
