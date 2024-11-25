first=int (input("Введите первое целое число: "))
second=int (input("Введите второе целое число: "))
third=int (input("Введите третье целое число: "))
if first==second==third:
    print (3, "Все числа равны!")
elif first!=second and first!=third  and second!=third:
    print(0,"Одинаковых чисел нет!")
elif first==second or first==third  or second==third:
    print(2, " Два одинаковых числа!")
