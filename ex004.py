# # Tabuada: O usuário informa um número e o programa exibe a tabuada desse número de 1 a 10.

# number = int(input("Digit a number from 1 to 10: "))

# print(f"multiplication table {number}")
# print(f"{number} x {1:2} = {number * 1}")
# print(f"{number} x {2:2} = {number * 2}")
# print(f"{number} x {3:2} = {number * 3}")
# print(f"{number} x {4:2} = {number * 4}")
# print(f"{number} x {5:2} = {number * 5}")
# print(f"{number} x {6:2} = {number * 6}")
# print(f"{number} x {7:2} = {number * 7}")
# print(f"{number} x {8:2} = {number * 8}")
# print(f"{number} x {9:2} = {number * 9}")
# print(f"{number} x {10:2} = {number * 10}")

number = int(input("Digit a number for see mutiplication table: "))
for i in range(1,11):
   print(f"{number} x {i:2} = {number * i }")