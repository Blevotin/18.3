class House():
    house_history = []
    def __init__(self, name, number_of_floors,):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.house_history} удален")

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        House.house_history.append(instance)
        return instance

    def __repr__(self):
        return f"{self.name}"

    def go_to(self, new_floor):
        if new_floor <= 0:
            return print("Такого этажа нет")
        if new_floor <= self.number_of_floors:
            for i in range(new_floor):
                if i < self.number_of_floors:
                    print(i+1)
        else:
            print("Такого этажа не существует")
    def __len__(self):
        return  (self.number_of_floors)
    def __str__(self):
        return f"Название: {self.name}, Количество этажей {self.number_of_floors})"
    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        return False
    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        return False
    def __le__(self, other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        return False
    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        return False
    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        return False
    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        return False
    def __add__(self, value, ojp):
        self.houses_history.append(ojp)
        self.number_of_floors+=value;
        return self
    def __radd__(self, value):
        self.number_of_floors+=value;
        return self.number_of_floors

a = House("Жк", 23, )
# a.go_to(23)
print("\n")
print(House.house_history)
a = House("4", 23)
print(a.house_history)
del(a)
print(a.house_history)
# print(a == b)
# print(a >= b)
# print(a != b)
# print(a <= b)
# print(a + 3)
# print(3 + a)





