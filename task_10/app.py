def overlapping(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False


num = int(input("Enter the number of element"))
l1 = []
for i in range(num):
    element = input("Enter the element first:")
    l1.append(element)
l2 = []
for i in range(num):
    element = input("Enter the element second:")
    l2.append(element)
result = overlapping(l1, l2)
print(result)