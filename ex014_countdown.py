# 5. Contador regressivo
# Peça um número e faça uma contagem regressiva até zero.
from time import sleep

print("+=+" * 10)
number = int(input("Enter a number to start countdown: "))
print(f" Countdown from {number} ".center(30, "-"))
for i in range(number, -1, -1):
    print(f"{i:^30}")
    sleep(0.5)
print("+=+" * 10)
print("\nProgram finalized!")
