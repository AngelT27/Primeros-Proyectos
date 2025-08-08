from Tip_calculator import tip_calculator

# Función para solicitar productos y sus precios
def solicitar_productos():
    repid = []
    productos = []
    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): \n")
        reps=0
        if producto.lower() == 'salir':
            break
        try:
            repid.append(producto)
            if producto in repid:
                reps = repid.count(producto)
            if reps > 1:
                print(f"Producto {producto} agregado {reps} veces.")
                pr_prev = [p for (prod, p, _) in productos if prod == producto]
                if pr_prev:
                     precio = pr_prev[-1]
                else:
                    precio = float(input(f"Ingrese el precio de {producto}:\n"))
            else:
                precio = float(input(f"Ingrese el precio de {producto}:\n"))
            productos.append((producto, precio, reps))
        except ValueError:
            print("Precio inválido. Intente de nuevo.")
            reps = 0
    return productos

# Función para mostrar el resumen del pedido
def mostrar_resumen(productos):
    total = sum(precio for _, precio, _ in productos)
    print("\nResumen del pedido:\n")
    lin_resumen = []
    agregado = {}
    lin_resumen.append("Resumen del pedido:\n")
    for nom, pre, _ in productos:
        if nom not in agregado:
            agregado[nom] = [0, 0.0]
            agregado[nom][0] += 1
            agregado[nom][1] += float(pre)
        else:
            agregado[nom][0] += 1
            agregado[nom][1] += float(pre) 
    
    filas = []
    for nom, (rep, cant) in agregado.items():
        izq = f"{rep} {nom}" if rep>1 else nom
        der = f"{cant:.2f}"
        filas.append((izq, der))

    wi = max(len(i) for i, _ in filas)+2
    wd = max(len(d) for _, d in filas)
    for i, d in filas:
        print(f"{i:<{wi}}{d:>{wd}}")
        lin_resumen.append(f"{i:<{wi}}{d:>{wd}}")

    print(f"\nTotal de la cuenta: {total:.2f}")
    lin_resumen.append(f"\nTotal de la cuenta: {total:.2f}")
    return (total, lin_resumen)
    
# Función para exportar el resumen a un archivo
def exportar_resumen(lista, nom):
    try:
        from pathlib import Path
        from datetime import datetime

        nombre = f"{nom}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        p = Path(nombre)
        carp = Path("exports")
        carp.mkdir(exist_ok=True)
        p = carp/nombre
        with p.open("w", encoding="utf-8") as file:
            for linea in lista:
                file.write(f"{linea}\n")
        return str(p)
    except Exception as e:
        print("Error al exportar:", e)

# Función principal para organizar el pedido
def order_organizer():
    productos = solicitar_productos()
    if not productos:
        print("No se han agregado productos.")
        return

    total, lista = mostrar_resumen(productos)

    agregar = input("¿Desea agregar propina? (si/no):\n").strip().lower()
    ja = (agregar == "si")
    lista = tip_calculator(total, lista, ja)
    res = input("¿Desea exportar el resumen? (si/no):\n").strip().lower()
    if res == "si":
        nom = input("Ingrese el nombre del archivo para exportar:\n")
        rut = exportar_resumen(lista, nom)
        print(f"Resumen exportado exitosamente en: {rut}.")
    else:
        print("Resumen no exportado.")




# Función para identificar productos repetidos en una tupla de productos
# Esta función no se usa en el flujo principal, pero puede ser útil para análisis adicionales futuros.
def lista_repetidos(productos):
    repid = {}
    for producto, _, _ in productos:
        if producto in repid:
            repid[producto] += 1
        else:
            repid[producto] = 1
    repetidos = [(producto, reps) for producto, reps in repid.items() if reps > 1]
    return repetidos