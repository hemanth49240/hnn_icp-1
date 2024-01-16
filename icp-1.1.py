m = input("Enter a string: ")
char_list = list(m)

s = int(input("Enter the number of characters to be deleted: "))


characters_to_delete = set()

for i in range(s):
    o = input("Enter the character to be deleted: ")
    characters_to_delete.add(o)


char_list = [char for char in char_list if char not in characters_to_delete]

reversed_list = char_list[::-1]
result_string = ''.join(reversed_list)

print("Resultant string:", result_string)
