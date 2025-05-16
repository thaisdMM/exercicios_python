#Calculadora Simples: Escreva um programa que peça dois números ao usuário e uma operação (+, -, *, /) e retorne o resultado.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
subtracao = n1 - n2
#print(soma, subtracao) # teste
multiplicacao = n1 * n2
divisao = n1 / n2
#print(multiplicacao, divisao)

operacao = input("Digite a operação. As opções disponiveis são soma(+), subtracao(-), multiplicacao(x) e divisao(/) ")
if operacao == "soma":
   resultado = soma
elif operacao == "subtracao" or operacao == "subtração":
   resultado = subtracao
elif operacao == "multiplicacao" or operacao == "multiplicação":
   resultado = multiplicacao
elif operacao == "divisao" or operacao == "divisão":
   resultado = divisao


print(f"A operaçao é {operacao} e o resultado é {resultado}")