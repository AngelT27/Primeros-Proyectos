personas=input("Ingrese el número de personas: \n")
personas=int(personas)
if personas==1:
    total=input("Ingrese el total de la cuenta: \n")
    porcentaje=input("Ingrese el porcentaje de propina: \n20%, 22%, 25%:")
    total=float(total)
    porcentaje=float(porcentaje)
    if porcentaje==25 or porcentaje==22 or porcentaje==20:
        tip=float(total*float(porcentaje)/100)
        pagar=total+tip
        print(f"El total a pagar es: {pagar:.2f} con una propina de {tip:.2f}. Muchas gracias por su preferencia.")
    else:
        print("Por favor, ingrese un porcentaje válido (20%, 22% o 25%)")
elif personas>1:
    total=input("Ingrese el total de la cuenta: \n")
    porcentaje=input("Ingrese el porcentaje de propina: \n20%, 22%, 25%:")
    total=float(total)
    porcentaje=float(porcentaje)
    if porcentaje==25 or porcentaje==22 or porcentaje==20:
        tip=float(total*float(porcentaje)/100)
        pagar=total+tip
        dividir=pagar/personas
        print(f"El total a pagar es: {pagar:.2f} con una propina de {tip:.2f}.\n Cada persona debe pagar: {dividir:.2f}.\n Muchas gracias por su preferencia.")