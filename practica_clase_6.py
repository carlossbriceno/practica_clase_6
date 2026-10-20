# parte_A
def agregar_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado con éxito.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def listar_productos(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- LISTA DE PRODUCTOS ---")
        for nombre, datos in inventario.items():
            print(f"- {nombre}: Precio: ${datos['precio']}, Cantidad: {datos['cantidad']}")
 # parte_B
def stock_bajo(inventario, limite):
    return [nombre for nombre, datos in inventario.items() if datos["cantidad"] < limite]

def valor_total(inventario):
    return sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())

def nombres_en_mayuscula(inventario):
    return sorted([nombre.upper() for nombre in inventario.keys()])
# parte_Cfrom inventario import agregar_producto, eliminar_producto, listar_productosfrom reportes import stock_bajo, valor_total, nombres_en_mayuscula

def main():
    # Diccionario inicial con datos base
    inventario = {
        "Manzana": {"precio": 1.5, "cantidad": 25},
        "Arroz": {"precio": 2.0, "cantidad": 4},
        "Leche": {"precio": 1.2, "cantidad": 10}
    }

    while True:
        print("\n===== MENÚ DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Listar productos")
        print("4. Ver productos con stock bajo")
        print("5. Ver valor total")
        print("6. Ver nombres en mayúscula")
        print("7. Salir")

        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ").strip()
            try:
                precio = float(input("Ingrese el precio: "))
                cantidad = int(input("Ingrese la cantidad: "))
                agregar_producto(inventario, nombre, precio, cantidad)
                print(f"Producto '{nombre}' procesado correctamente.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido para el precio y la cantidad.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
            eliminar_producto(inventario, nombre)

        elif opcion == "3":
            listar_productos(inventario)

        elif opcion == "4":
            try:
                limite = int(input("Ingrese el límite de stock: "))
                productos_bajos = stock_bajo(inventario, limite)
                print(f"Productos con stock menor a {limite}: {productos_bajos}")
            except ValueError:
                print("Error: El límite debe ser un número entero.")

        elif opcion == "5":
            total = valor_total(inventario)
            print(f"El valor total del inventario es: ${total:.2f}")

        elif opcion == "6":
            mayusculas = nombres_en_mayuscula(inventario)
            print(f"Nombres en mayúscula ordenados: {mayusculas}")

        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
