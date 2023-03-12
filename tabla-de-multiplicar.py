"""
## caluculadora que retorna un lista con el resultado
lista = []

salir = False

while not salir:
    numero = int(input("Introduzca un numero: "))
    if numero != 0:
        lista.clear()
        for i in range (0,11):
            resultado = i * numero
            lista.append(resultado)
        print(lista)
    else:
        print("Adios")
        salir = True
"""


salir = False
print("induca un mumero para multiplocar y precione 0 para salir")

while not salir:
    numero = int(input("Introduzca un numero: "))
    if numero != 0 :
        for num in range(1,11):
            resul =  numero * num
            a = f"{numero} x {num}  = {resul}"
            print(a)
    
    else:
        print("adios")
        salir = True