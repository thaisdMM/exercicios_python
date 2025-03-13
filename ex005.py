#Média de Notas: Peça três notas ao usuário e calcule a média. Informe se ele foi aprovado (média ≥ 7).

print("Grades until 10")
grade1 = float(input("Enter the first grade: "))
#print(grade1) #teste
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
##print(grade1, grade2, grade3) #teste
average = (grade1 + grade2 + grade3) / 3
#print(average) #teste

if average >= 7:
   print(f"Average: {average:.2f}: PASSED!!!")
else:
   print(f"Average: {average:.2f}: Failed.")