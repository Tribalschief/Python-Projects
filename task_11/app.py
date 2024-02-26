def generate_n_chars(n, c):
    number = int(input("Enter the number: "))
    n = number
    char = input("Enter the character: ")
    c = char
    return c * n
result = generate_n_chars(3, 'x')
print(result)