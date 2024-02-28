def max(number:list[int])->int:
    max = 0
    for i in number:
        if i > max:
            max = i
    return max
num = int(input("Enter the number of element"))
array = []
for i in range(num):
    element = int(input("Enter the element: "))
    array.append(element)

result = max(array)
print(result)