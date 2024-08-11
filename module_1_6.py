my_dict = {"Sasha": 2004, "Andrey": 2006, "Stepa": 2002}
print("Dict:", my_dict)
print("Existing value:", my_dict["Sasha"])
print("Not existing value:", my_dict.get("Pasha"))
my_dict["Artem"] = 1996
my_dict["Nastya"] = 2005
deleted_value = my_dict.pop("Andrey")
print("Deleted value:", deleted_value)
print("Modified dictionary:", my_dict)
my_set = {1, "Orange", 53.342, 7, "Orange", (5, 3, 2.4)}
print("Set:", my_set)
my_set.add("Watermelon")
my_set.add(21)
my_set.discard(7)
print("Modified set:", my_set)

