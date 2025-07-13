list_1 = [1,2,3,4,5]
list_2 = list_1.copy()

print(list_2)

list_2[0] = "hello"
print("normal list" , list_1)
print("modify list : ",list_2)