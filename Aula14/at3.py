numero = input("Digite um número: ")
soma = 0
multiplicacao = 1
for i in numero:
    soma += int(i)
    multiplicacao *= int(i)

print(f" a soma de todos os números é {soma}, e a multiplicação é {multiplicacao}")