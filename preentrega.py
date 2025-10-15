# Productos = [{nombre: nombre, categoria: categoria, precio: precio}, {nombre: nombre, categoria: categoria, precio: precio}... ]
productos = []

while True:
    print("Sistema de Gestión Básica de Productos")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    while True:
        user_input = input("Digite una opción (1-5): ").strip()
        if user_input not in ["1", "2", "3", "4", "5", ""]:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
        else:
            break

    # 1- Agregar producto
    if user_input == "1":
        while True:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if nombre == "":
                print("El nombre del producto no puede estar vacío. Intente nuevamente.")
            else:
                break
        while True:
            categoria = input("Ingrese la categoria del producto: ").strip()
            if categoria == "":
                print("La categoria del producto no puede estar vacía. Intente nuevamente.")
            else:
                break
        while True:
            precio = input("Ingrese el precio del producto (sin centavos): ").strip()   
            if precio == "":
                print("El precio del producto no puede estar vacío. Intente nuevamente.")
            else:
                break
        productos.append({"nombre": nombre, "categoria": categoria, "precio": precio})
        print("------- Producto añadido con exito! -------")  
        print(f"Nombre: {nombre.capitalize()}, Categoria: {categoria.capitalize()}, Precio: ${precio}.")
        print("-------------------------------------------")
    
    # 2- Mostrar productos:
    if user_input == "2":
        if len(productos) == 0:
            print("--------------------------------")
            print("La lista de productos está vacía :(.")
            print("--------------------------------")
            continue
        print("------- Todos los productos -------")
        for producto in productos:
            print("Nombre:", producto["nombre"].capitalize())
            print("Categoria:", producto["categoria"].capitalize())
            print("Precio: $", producto["precio"])
            print("---------------------------------")

    # 3- Buscar producto
    if user_input == "3":
        while True:
            print("Ingresá el nombre del producto o presioná Enter para volver al menu.")
            busqueda = input("Nombre del producto: ").strip()
            if busqueda == "":
                break
            for producto in productos:
                if  busqueda == producto["nombre"]:
                    print("------- Producto encontrado! -------")
                    print("Nombre:", producto["nombre"].capitalize())
                    print("Categoria:", producto["categoria"].capitalize())
                    print("Precio: $", producto["precio"])
                    print("---------------------------------")
                    break
            else:
                print(f"El producto {busqueda} no existe")
            respuesta = input("Buscar otro producto(s/n)?: ").strip()
            if respuesta in ["s", "si"]:
                continue
            elif respuesta in ["n", "no", ""]:
                break
            else: 
                print("Respuesta invalida.")

    # 4- Eliminar producto
    if user_input == "4":
        while True:
            print("Ingresá el nombre del producto para eliminar o presioná Enter para volver al menu.")
            eliminar = input("Nombre del producto a eliminar: ").strip()
            if eliminar == "":
                break
            for producto in productos:
                if eliminar == producto["nombre"]:
                    productos.remove(producto)
                    print(f"El producto '{eliminar}' fue eliminado de la lista.")
                    break
            else:
                print(f"El producto '{eliminar}' no existe")
                continue
            print("----> Estado actual de la lista de productos:") 
            if len(productos) == 0:
                print("La lista de productos está vacía :(.")
                break
            for producto in productos:    
                print("Nombre:", producto["nombre"].capitalize())
                print("Categoria:", producto["categoria"].capitalize())
                print("Precio: $", producto["precio"])
                print("---------------------------------")  
            respuesta = input("Eliminar otro producto(S/N)?: ").strip()
            if respuesta in ["s", "si"]:
                continue
            elif respuesta in ["n", "no", ""]:
                break
            else:
                print("Ingrese una respuesta valida!")
                continue                        
    
    # 5- Salir del programa
    if user_input in ["5", ""]:
        print("Adios!")
        break

    


        