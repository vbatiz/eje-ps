def main():
    #escribe tu código abajo de esta línea
    nombre=input("Dame tu nombre: ")
    apellido_paterno =input("Dame tu apellido paterno: ")
    apellido_materno =input("Dame tu apellido materno: ")
    nombre_completo =nombre + " " + apellido_paterno + " " + apellido_materno
    print("Es un gusto conocerte " + nombre_completo)

if __name__=='__main__':
    main()
