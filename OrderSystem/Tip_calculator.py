# Este es un script de Python que calcula la propina y el total a pagar en un restaurante.
# Se solicitan el total a pagar, una lista con los productos y un boolean que debe ser True
# si se desea calcular la propina. Si no se desea calcular, se muestra un mensaje de agradecimiento.

def tip_calculator(total, lista, ja):
    try:
        if not ja:
            lista.append("No se ha agregado propina.\n")
            print("Muchas gracias por su preferencia!\n")
            return lista
        personas = int(input("Ingrese el número de personas: \n"))
        porcentaje = float(input("Ingrese el porcentaje de propina (20%, 22%, 25%): \n").replace('%', ''))
        if porcentaje not in [20, 22, 25]:
            mes = "Por favor, ingrese un porcentaje válido (20%, 22% o 25%)\n"
            print(mes)
            lista.append(mes)
            return lista
        tip = total*porcentaje/100
        pagar = total+tip
        if personas == 1:
            mes = f"El total a pagar es: {pagar:.2f} con una propina de {tip:.2f}.\n"
            print(mes); lista.append(mes)
        else:
            dividir = pagar / personas
            mes1 = f"El total a pagar es: {pagar:.2f} con una propina de {tip:.2f}.\n"
            mes2 = f"Cada persona debe pagar: {dividir:.2f}.\n"
            print(mes1); print(mes2)
            lista.extend([mes1, mes2])
        print("Muchas gracias por su preferencia.\n")
        lista.append("Muchas gracias por su preferencia.\n")
        return lista
    except ValueError:
        print("Entrada inválida. Intente de nuevo.\n")
        lista.append("Entrada inválida en la propina.\n")
        return lista