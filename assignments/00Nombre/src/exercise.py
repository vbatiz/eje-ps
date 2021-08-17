import math
import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    radio=float(input("Dame el valor del radio: "))
    volumen = 4/3 * math.pi * math.pow(radio,3)
    print(f"El volumen de la esfera de radio {radio} es: {volumen} unidades cúbicas")
if __name__=='__main__':
    main()
