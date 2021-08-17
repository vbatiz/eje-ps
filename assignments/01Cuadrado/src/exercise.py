import math
import os

def main():
    #escribe tu código abajo de esta línea

    os.system('clear')
    lado=int(input("Dame el valor del lado del cuadrado: "))

    perimetro = 4 * lado
    area = math.pow(lado,2)

    print("El perimetro del cuadrado de lado " + str(lado) + " es: " + str(perimetro))
    print(f"El area del cuadrado de lado {lado} es: {area}")

if __name__=='__main__':
    main()
