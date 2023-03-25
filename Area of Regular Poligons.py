while True:
    n_Lados = int(input("Ingresa el # de lados del poligono: "))
    if n_Lados < 3:
        print("No hay poligonos con menos de 3 lados")

    if n_Lados == 3:
        b = float(input("Ingresa la medida de la base: "))
        h = float(input("Ingresa la medida de la altura: "))
        A = b * h / 2
        print("El área del poligono es: " + str(A))
    elif n_Lados == 4:
        b = float(input("Ingresa la medida de la base: "))
        h = float(input("Ingresa la medida de la altura: "))
        A = b * h
        print("El área del poligono es: " + str(A))
    elif n_Lados > 4:
        med_lado = float(input("Cuanto mide un lado del poligono: "))
        P = n_Lados * med_lado
        a = float(input("Ingresa el valor de la apotema: "))
        A = P * a / 2
        print("El área del poligono es: " + str(A))

    opciones = ("s", "n")
    de_nuevo = input("Otro cálculo (s/n): ")
    while de_nuevo not in opciones:
        de_nuevo = input("Otro cálculo (s/n): ")
    if de_nuevo == "n":
        break
