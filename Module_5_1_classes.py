class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print("Такого этажа не существует")

        # else:
        #     new_floor



adr = House('ЖК Эльбрус,', 30)
adr.go_to(1)
print(adr.name, adr.new_floor)









# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#     def say_info (self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age}")
#     def birthday (self):
#         self.age +=1
#         print(f'У меня день рождения, мне теперь {self.age}')
#
#
#
# den = Human('Михаил', 47)
# den.birthday()
# den.say_info()
# print(den.name, den.age)






