# Contagem Progressiva: Peça um número ao usuário e exiba uma contagem de 1 até esse número.
# o exemplo abaixo cria uma lista com o range e gasta mais memória

# number = int(input("Digit a number: "))
# print(f"\nCount 1 to number {number} = {list(range(1,number +1))}")

# Esse exemplo conta sem criar lista

number = int(input("Digit a number: "))

for i in range(1, number +1 ):
   print(i)