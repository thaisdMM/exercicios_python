# 6️⃣ Lista de Compras: O usuário pode adicionar itens a uma lista de compras. Quando ele digitar “sair”, o programa exibe a lista completa.

def shopping_item(shopping_list, new_item_list):
   item_list = ""
   item_list = new_item_list
   shopping_list.append(item_list)
   print(f"The item: {item_list} has been added to the list successefully")
   return

def show_list(shopping_list):
   print("SHOPPING LIST: ")
for indice, item_list in enumerate (item_list, start = 1):
   print(f"{indice}. {item_list}")

shopping_list = []

while True:
   print("Shopping list")
   print("\n1. Add items")
   print("2. EXIT")

   choice = input("\nEnter your choice: ").strip()   

   if choice == "1":
      new_item_list = input("\nEnter the item for your shopping list: ")
      
      shopping_item(shopping_list, new_item_list)

   elif choice == "3":
      show_list(shopping_list)

   elif choice == "2":
      print("\nYou have choosen to EXIT.")
      break
print(f"\nThese are the items on your SHOPPING LIST: \n{shopping_list}") # não está adicionando nada
print("\nProgam finished")