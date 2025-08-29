-------------------------------------

Alfonso Pavez 
202373613-9
paralelo:200

-------------------------------------

Hector Chanampe
202304613-2
paralelo:200

-------------------------------------

Algoritmos y funciones:

El algoritmo general para decimal a binario, octal y hexadecimal, 
es tomar un numero entero cualquiera con RANDOM, dividir sucesivamente por 2, 8 o 16
guardar el residuo e invertir el orden para obtener el resultado esperado.

Para el inverso, se recorre la cadena de izquierda a derecha, se multiplica por su potencia correspondiente
y luego se suma todo el resultado.

Para hexadecimal, en ambos casos se considera una variable "simbolos", la cual guarda los simbolos que 
utliza.

def decimal_binario(numero) -> convierte de decimal a binario, requiere de un numero entero
def decimal_octal(numero): -> convierte de decimal a octal, requiere de un numero entero
def decimal_hexa(numero): -> convierte de decimal a hexadecimal, requiere de un numero entero

def binario_decimal(chain): -> convierte de binario a decimal, requiere una cadena de codigo binario
def octal_decimal(chain): -> convierte de octal a decimal, requiere una cadena en codigo octal
def hexa_decimal(chain): -> convierte de hexadecimal a decimal, requiere una cadena de codigo hexadecimal

def elegir_dificultad(nivel): -> logica para elegir la dificultad del codigo, require el nivel actual
                                 para verificar que se puede elegir la dificultad deseada, requiere un numero de nivel base (1)

def generar_decimal(dificultad): -> utlizando la libreria RANDOM, se genera un numero en el rango
                                    de dificultad permitido, requiere un input de dificultad (numero entero entre [1,3])

def generar_codigo(decimal, dificultad): -> se convierte el decimal antes generado en el codigo correspondiente
                                            requiere de un decimal entero, y de un input de dificultad

def descifrar_codigo(): -> loop el cual pregunta por la respuesta del codigo generado
                           si se ingresa mal, se avisa con un mensaje, de lo contrario
                           avisa que fue descifrado correctamente y sube un nivel de dificultad
			   Luego de descifrar correctamente, se reinician los valores de dificultad, codigo y decimal para 
			   evitar que se pueda descifrar dos veces un mismo codigo y hacer "trampa"

def subir_nivel(dificultad, nivel): -> se sube el nivel actual en +1
                                       requiere de un entero de dificultad y un entero de nivel


def menu(): -> loop para el menu
               no requiere entrada

-------------------------------------

Supuestos Utilizados:

1. se asume que los hexadecimal pueden ser ingresados en ambos mayusuclas y minusculas
2. se asume que todos los inputs seran validos, tal como los numeros enteros al momento de elegir en el menu

-------------------------------------

Metodo de ejecucion:
1. ubicar en la consola el archivo "LAB1_202373613-9_202304613-2.py"
2. ejecutar el comando "python3 LAB1_202373613-9_202304613-2.py" o "py LAB1_202373613-9_202304613-2.py"




