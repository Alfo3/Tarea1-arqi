import random

#-------------------------------
# DEFINICION DE CONVERSIONES
#-------------------------------

def decimal_binario(numero): #de decimal a binario, funciona yipi
    if numero == 0:
        return "0"
    bits = []
    while numero > 0:
        bits.append(str(numero % 2))
        numero = numero // 2
    return ''.join(reversed(bits)) #el join y '' es mandatorio, pq si no queda una lista asi
                                    #['1', '0', '1']
                                    # queda como texto y ademas queda como lista, y no como binario

def decimal_octal(numero): #de decimal a octal, funciona yipi
    if numero == 0:
        return "0"
    bits = []
    while numero > 0:
        bits.append(str(numero % 8))
        numero = numero // 8
    return ''.join(reversed(bits)) #la misma explicacion q arriba >:(

def decimal_hexa(numero):
    if numero == 0:
        return "0"
    simbolos ='0123456789ABCDEF'
    bits = []
    while numero > 0:
        bits.append(simbolos[numero % 16])
        numero = numero // 16
    return ''.join(reversed(bits))

def binario_decimal(chain):
    value = 0
    for i, caracter in enumerate(reversed(str(chain))):
        value += int(caracter) * (2**i)
    return value

def octal_decimal(chain):
    value = 0
    for i, caracter in enumerate(reversed(str(chain))):
        value += int(caracter) *  (8**i)
    return value

def hexa_decimal(chain): #hexa solo funciona cuando 
    value = 0
    simbolos = '0123456789ABCDEF'
    for i, caracter in enumerate(reversed(str(chain))): 
        value += simbolos.index(caracter.upper()) * (16**i)
    return value


#-------------------------------
# MENU DE OPCIONES
#-------------------------------

def menu():
    while True:
        print("Bienvenido al menu de opciones")
        print("1) Generar Codigo 🐈")
        print("2) Descifrar el Codigo 🤓")
        print("3) Salir")

        option = input("Selecciona lo que quieres hacer: ").strip()

        if option == '1':
            return 1 #aqui ira la funcion para generar codigo dependiendo de la dificultad
        elif option == '2':
            return 1 #aqui ira la funcion para descifrar
        elif option == '3':
            break # aqui se sale del programa nomas
        else:
            print("Opcion no valida, porfavor intenta denuevo")

menu()
        