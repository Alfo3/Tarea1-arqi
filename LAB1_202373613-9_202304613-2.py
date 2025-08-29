import random

#-------------------------------
# DEFINICION DE CONVERSIONES
#-------------------------------

def decimal_binario(numero): #de decimal a binario
    if numero == 0:
        return "0"
    bits = []
    while numero > 0:
        bits.append(str(numero % 2))
        numero = numero // 2
    return ''.join(reversed(bits)) #el join y '' es mandatorio, pq si no queda una lista asi
                                    #['1', '0', '1']
                                    # queda como texto y ademas queda como lista, y no como binario
                                    #lo mismo pa todos los demas

def decimal_octal(numero): #de decimal a octal
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
# LOGICA MENU
#-------------------------------
def elegir_dificultad(nivel):
    while True:
        print()
        print("Elige el sistema a hackear")
        print("1) Firewall:     Binario -> Decimal")
        print("2) Servidor:     Octal   -> Decimal")
        print("3) Memoria:      Hexadecimal -> Decimal")
        dificultad=(input("> "))
        if(not(dificultad=='1' or dificultad=='2' or dificultad=='3')):
            print("Error al elegir dificultad, por favor intente nuevamente\n")
        else:
            print()
            if(dificultad=='1'):
                print("Has escogido firewall!")
                return dificultad
            elif(dificultad=='2' and nivel>=3):
                print("Has escogido servidor!")
                return dificultad
            elif(dificultad=='3' and nivel>=5):
                print("Has escogido memoria!")
                return dificultad
            else:
                print("No puedes escoger esta dificultad ya que eres nivel muy bajo, prueba hackeando sistemas inferiores.\n")

def generar_decimal(dificultad):
    match dificultad:
        case '1':
            decimal=random.randint(1,63)
        case '2':
            decimal=random.randint(1,511)
        case '3':
            decimal=random.randint(1,4095)
    return decimal

def generar_codigo(decimal, dificultad):
    match dificultad:
        case '1':
            codigo=decimal_binario(decimal)
        case '2':
            codigo=decimal_octal(decimal)
        case '3': 
            codigo=decimal_hexa(decimal)
    return codigo

def descifrar_codigo():
    global nivel, codigo, decimal, dificultad
    respuesta=0
    while respuesta != -1:
        print("Debes convertir el código ", codigo, "a decimal.")
        respuesta=int(input("Ingresa una respuesta. (-1 si deseas salir).\n>"))
        if respuesta==decimal:
            print("Felicidades, has descifrado correctamente el código.")
            nivel = subir_nivel(dificultad, nivel)
            codigo = None   #estos 3 de aca resetean el codigo generado
            decimal = None
            dificultad = None
            return 
        elif (respuesta != decimal and respuesta != -1):
            print("Alto salame, intentalo nuevamente")
        else:
            print("Saliendo...")
    return

def subir_nivel(dificultad, nivel):
    if (nivel<3 and dificultad=='1'):
        nivel+=1
    elif (nivel <5 and dificultad=='2'):
        nivel+=1
    elif (nivel <8 and dificultad=='3'):
        nivel+=1
    elif (nivel == 8):
        print("Felicidades has llegado al nivel ANONYMOUS slay")
    else:
        print("Has alcanzado el limite de nivel para estas dificultades, avanza en los siguientes desafios para subir de nivel.")
        return nivel
    print("Has subido un nivel!")
    return nivel

#-------------------------------
# MENU DE OPCIONES
#-------------------------------

def menu():
    global dificultad, decimal, codigo
    dificultad = None
    decimal = None
    codigo = None
    while True:
        print("\nBienvenido al menu de opciones")
        print("1) Generar Codigo 🐈")
        print("2) Descifrar el Codigo 🤓")
        print("3) Salir")
        print("Tu nivel actual es: ", nivel)
        option = input("Selecciona lo que quieres hacer: ").strip()

        if option == '1':
            dificultad=elegir_dificultad(nivel)
            decimal=generar_decimal(dificultad)
            codigo=generar_codigo(decimal, dificultad)
            print ("El codigo generado es:", codigo)
        elif option == '2':
            if codigo is None or decimal is None or dificultad is None:
                print("\nPrimero debes generar un codigo antes de descifralo, no seas pillo!")
            else:
                print("\nHas elegido descifrar el código, buena suerte hacker.")
                descifrar_codigo()
        elif option == '3':
            break # aqui se sale del programa nomas, kaboom
        else:
            print("Opcion no valida, porfavor intenta denuevo\n")



#-------------------------------
# MAIN
#-------------------------------
nivel = 1
menu()

#Niveles arreglado yippie
#Menu lowkey no se como hacerlo mas bonito, la vrd no soy bueno diseñandolols pero sabes q iwal se ve weno
#pasable, yo creo q si