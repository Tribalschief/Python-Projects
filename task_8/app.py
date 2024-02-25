def is_palindrome(string):
    palindrome = string[::-1]
    if string == palindrome:
        return True
    else:
        return False

string = input("Enter a string: ")
print(is_palindrome(string))