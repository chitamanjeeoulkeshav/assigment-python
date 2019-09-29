menu = ["Panadol", "Pain-killer", "Sendodye", "Band-aid", "Beccham-flu"]
print(menu)


m = str(input("Enter the item you want to add: "))
menu.append(m)
print(menu)

m1 = str(input("Enter the item you want to remove: "))
if m1 in menu:
    menu.remove(m1)
    print(menu)
else:
    print("Re-check the item.")


m2 = str(input("Enter the item you want to add: "))
position = int(input("Enter the position where you want to add it: "))
if position < len(menu):
    menu.insert(position, m2)
    print(menu)
else:
    print("Re-check the item.")
