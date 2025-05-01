# 6. Soma dos pares
# Peça 10 números e mostre a soma apenas dos números pares digitados.
even_sum = even_numbers = 0

for even in range(0, 10):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even_sum += number
        even_numbers += 1
print(f"Number of even numbers: {even_numbers}")
print(f"Sum of even numbers: {even_sum}")
