def generar_primo(numero):
    lista = list(range(2, (numero + 1)))
    indice = 0 
    while lista[indice]**2 <= numero:
        for i in lista: 
            if i != lista[indice]:
                if i % lista[indice] == 0: 
                    lista.remove(i)
        indice = indice + 1  
    return lista 

print("Generar todos los primos de 3, 4 y 5 cifras")
cantidad = int(input("Elegir cantidad de cifras que desea: ")) 
if cantidad == 3:
    print("Todos los primos de 3 cifras")
    primos1 = generar_primo(999)
    for i in primos1:
        if i > 99:
            print(i)
if cantidad == 4:
    print("Todos los primos de 4 cifras")
    primos2 = generar_primo(9999)
    for i in primos2: 
        if i > 999:
            print(i)
if cantidad == 5:
    print("Todos los primos de 5 cifras")
    primos3 = generar_primo(99999)
    for i in primos3: 
        if i > 9999:
            print(i)
