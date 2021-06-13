import functools as ft

fil = open("2.txt", "r")
# print(sum([len(line) for line in file.read().replace("\n", "")])) #the letters sum
# print(ft.reduce(lambda x, y: x if len(x) > len(y) else y, fil)) #the longest  name
# def short_name(file): # output the shortest names
# min_len = len(ft.reduce(lambda x, y: y if len(x) > len(y) else x, file.read().replace("\n", " ").split()))
# file.seek(0)
# return print("\n".join([n for n in file.read().replace("\n", " ").split() if len(n) == min_len]))
# short_name(fil)

# file_2 = open("name_length.txt", "w") # copy len from one file to another .
# file_2.write("\n".join([str(len(n)) for n in fil.read().split()]))
# file_2.close()
# fil.close()

# b = int(input("Enter a number\n:")) # Enter a number and out word that equal len wore
# def out(n):
#   return "\n".join([b for b in fil.read().split() if len(b) == n])
# print(out(b))
