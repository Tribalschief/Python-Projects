def add(abc:list):
    total = 0
    for i in abc:
        total += i
    return total
def multiply(abc:list):
    total = 1
    for i in abc:
        total *= i
    return total
number= [1,2,3,4]
print(add(number))
print(multiply(number))