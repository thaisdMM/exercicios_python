#Soma de Números: O usuário digita vários números e, ao digitar 0, o programa exibe a soma de todos.

soma = 0

while True:
   choice = int(input("Enter 0 to EXIT or enter a number to sum: "))

   if choice != 0:
      soma += choice

   if choice == 0:
      print(f"The sum result is: {soma}")
      print("Finished program")
      break