import math
import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    lado=float(input("Dame el valor del lado del cuadrado: "))
    perimetro = 4 * lado
    area = math.pow(lado,2)
    print(f"El perímetro del cuadrado de lado {lado} es: {perimetro}")
    print(f"El área del cuadrado de lado {lado} es: {area}")
if __name__=='__main__':
    main()
