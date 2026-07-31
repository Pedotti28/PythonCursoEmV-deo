from time import sleep
print("-=" * 10)
print("Contagem de 1 até 10 de 1 em 1")
for cont in range(1, 11):
    print(cont, end=" ")
    sleep(0.5)
print("FIM!")
print("-=" * 10)
print("Contagem de 10 até 0 de 2 em 2")
for cont in range(10, 0, -2):
    print(cont, end=" ")
    sleep(0.5)
print("FIM!")
print("-=" * 10)
print("Agora é sua vez de personalizar sua contagem.")


def contagem(i,f,p):
    if p == 0:
        p = 1
    if f - i > 0:
        while i <= f:
            print(f'{i}', end=" ")
            sleep(0.5)
            i += p
        print("FIM!")
    else:
        while i >= f:
            print(f'{i}', end=" ")
            sleep(0.5)
            i -= p
        print("FIM!")
    
