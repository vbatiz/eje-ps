import math
import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    radio=float(input("Dame el valor del radio: "))
    volumen = 4/3 * math.pi * math.pow(radio,3)
    area = 4*math.pi*radio ** 2
    print(f"El volumen de la esfera de radio {radio} es: {volumen} unidades cúbicas")
    print(f"El área de la esfera de radio {radio} es: {area} unidades cuadradas")

if __name__=='__main__':
    main()
