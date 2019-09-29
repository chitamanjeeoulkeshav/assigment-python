list1 = []
list2 = []


listlength1 = int(input("Enter the length of your list 1:"))

print("Enter the numbers you wish to put in the list 1:")


for i in range (listlength1):
    datalist1= int(input())
    list1.append(datalist1)

listlength2 = int(input("Enter the length of your list 2:"))

print("Enter the numbers you wish to put in the list 2:")


for j in range (listlength2):
    datalist2 = int(input())
    list2.append(datalist2)


print("List 1 is:",list1)
print("list 2 is:",list2)
print("__________________")


list3=[]


for odd in list1:
    if(odd % 2 != 0):


     list3.append(odd)
for even in list2:
     if(even % 2 ==0):

      list3.append(even)



print("List 3 with odd numbers from list 1 and even numbers from list 2:", list3)