def main():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    area = base * altura

    print(f"\nMedidas ingresadas -> Base: {base}, Altura: {altura}")
    print(f"El área del rectángulo es: {area}")

if __name__ == "__main__":
    main()
