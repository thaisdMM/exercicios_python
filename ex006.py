# 6️⃣ Lista de Compras: O usuário pode adicionar itens a uma lista de compras. Quando ele digitar “sair”, o programa exibe a lista completa.

shopping_list = []

while True:
   print("Shopping list")
   print("1. Add items")
   print("2. EXIT")

   choice = input("Enter your choice: ").strip()   
   if choice == "2":
      print("You have choosen to EXIT.")
      break
print("Progam finished")