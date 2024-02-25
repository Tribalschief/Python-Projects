def translate(text:str):
    vowel = 'aeiou'
    translated = ''
    for char in text:
        if char in vowel:
            translated += char
        else:
            translated += char + 'o' + char
    return translated

text = input("Enter what u want to translate: ")
print(translate(text))