n = soma = cont = maior = menor = 0
repetir = 'S'

while repetir in "Ss":
    n = int(input("Digite um número? "))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    soma += n
    repetir = str(input('Quer continuar? (S/N)')).upper().strip()[0]

soma = soma / cont
print('Você digitou {} números e a média entre eles foi de {}'.format(cont, soma))
print('O maior valor é {} e o menor é {}'.format(maior, menor))
