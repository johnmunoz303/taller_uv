def main():
    nombre = input("Ingrese su nombre: ")
    edad_actual = int(input("Ingrese su edad actual: "))

    edad_futura = edad_actual + 5

    print(f"\nHola {nombre}, actualmente tienes {edad_actual} años y dentro de 5 años tendrás {edad_futura} años.")

if __name__ == "__main__":
    main()
