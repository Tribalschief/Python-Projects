number = int(input("Enter a element of string"))
array = []
for i in range(number):
    element = input("Enter the element: ")
    array.append(element)
length = list(map(len, array))
def filtering(length):
    return length > 5
result = list(filter(filtering, length))
print(result)
