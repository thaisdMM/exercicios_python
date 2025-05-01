# 10. Descobridor de maior valor
# Peça números ao usuário até ele digitar 0. Depois mostre qual foi o maior número digitado.

count_numbers = bigger_number = 0
while True:
    number = int(input("Enter a number or 0 to finish: "))
    if number == 0:
        print(f"You enter {number} to finished.")
        break
    if count_numbers == 1:
        bigger_number = number
    elif bigger_number < number:
        bigger_number = number
    print("You want to continue to find the bigger number.")
    count_numbers += 1

print(f"\nYou entered {count_numbers} numbers.")
print(f"The bigger number entered was: {bigger_number}")
print("Program ended.")
