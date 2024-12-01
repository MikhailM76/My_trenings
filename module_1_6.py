# словари
my_dict={"Вова":"мастер","Петя":"слесарь","Александр Сергеевич":"поэт"}
print(my_dict)
#print(type(my_dict))
print(my_dict["Петя"])
print(my_dict.get("Вася", "Такого имени нет! "))
my_dict["Коля"]="Певец"
my_dict["Филипп"]="Просто Царь"
print(my_dict)
a = my_dict.pop("Коля")
print(my_dict)
print(a)
print()
#множества
my_set={1,2,3,3,2,1,False, True, False, "Задание", "Урок","Задание"}
print(my_set)
my_set.add(4)
print(my_set)
my_set.add(5)
print(my_set)
my_set.update([4,5])
print(my_set)
my_set.discard(False)
print(my_set)
