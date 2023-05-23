def primo(n):
    resultado = False
    if n == 1: resultado
    elif (n==2 or n==3): resultado = True
    else:
        for i in range(2, n-1):
            if n % i == 0:
                resultado = False
                break
            else: resultado= True
    return resultado
#


def  primo2(n):
    i = 2
    lista = []
    while i <= n:
        if primo(i):
            lista.append(i)
        i += 1
    return lista
#


y = int(input("Digite um número: "))
soma = y*2 + 5
somap = 0
at2 = primo2(soma)
print(at2)
print(sum(at2))



