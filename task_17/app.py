array = ["Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets","Sit on a potato pan, Otis","Lisa Bonet ate no basil","Satan, oscillate my metallic sonatas","I roamed under it as a tired nude Maori", "Rise to vote sir","Dammit, I'm mad!"]
def is_palindrome(items:list[str])->None:
 for char in array:
        chars = char.lower().replace(" ", "")
        if chars == chars[::-1]:
           print(True)
        else:
            print(False)
print(is_palindrome(array))
