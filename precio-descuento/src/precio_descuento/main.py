def main():
    precio_original = float(input("Ingrese el precio original del producto: "))

    descuento = precio_original * 0.10
    precio_final = precio_original - descuento

    print(f"\nPrecio original: ${precio_original:,.2f}")
    print(f"Descuento (10%):  ${descuento:,.2f}")
    print(f"Precio final:     ${precio_final:,.2f}")

if __name__ == "__main__":
    main()
