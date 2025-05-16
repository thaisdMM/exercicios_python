# 3. Tabuada com for
# Peça um número e mostre a tabuada dele de 1 a 10.

number = int(input("Enter a number to display its multiplication table: "))
print(f"MULTIPLICATION TABLE for {number}:")
print("-" * 30)
for i in range(1, 11):
    print(f"{number} x {i:2} = {i * number}")
