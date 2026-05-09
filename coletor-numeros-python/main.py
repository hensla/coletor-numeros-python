numero = []
loop = 1

while True:
    n = int(input(f"Informe o {loop}° número inteiro (para parar digite 0): "))
    if n == 0:
        break
    numero.append(n)
    loop+= 1

print(numero)