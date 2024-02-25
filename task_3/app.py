def length_of_string(args:str):
  count = 0
  for i in args:
      count += 1
  print(count)
input_string = input("Enter a string: ")
length_of_string(input_string)