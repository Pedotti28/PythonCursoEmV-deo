lar = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))

def area(lar, comp):
    a = lar * comp
    print(f"A área de um terreno {lar} x {comp} é de {a}m².")


area(lar, comp)