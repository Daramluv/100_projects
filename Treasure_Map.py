line1 = ["□", "□", "□"]
line2 = ["□", "□", "□"]
line3 = ["□", "□", "□"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
mapping = print('''\
  A  b  c 
1 □  □  □
2 □  □  □
3 □  □  □''')
position = input("where do you want to put the treasure?: (예:B1) ")
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1])-1

map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")