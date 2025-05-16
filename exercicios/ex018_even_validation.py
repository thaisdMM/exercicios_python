# 9. Validador de número par
# Fique pedindo um número até o usuário digitar um número par.

while True:
    number = int(input("Enter an even number to validate: "))
    if number % 2 == 0:
        print("Correct validation.")
        break
    else:
        print("Wrong validation. Try again.")
print("\nProgram ended.")
