
motos = 0
autos = 0
bicicletas = 0
camiones = 0

while True:
    entra_salida = input("Elige dependiendo lo que sucede en el estacionamiento \n1. Entrada de vehiculo \n2. Salida de vehiculo \n")
    if  entra_salida == "1":
        Vehiculo =input (" Que vehiculo desea ingresar?  \n1. automovil \n2. motocicletas \n3. biciletas \n4. salida \n-> ")
        if Vehiculo == "1":
            print("Haz ingresado un automóvil.")
            autos += 1
        if Vehiculo == "2":
            print("Haz ingresado una motocicleta.")
            motos += 1
        if Vehiculo == "3":
            print("Haz ingresado una bicicleta.")
            bicicletas += 1
        if Vehiculo == "4":
            print("Haz ingresado un camión.")
            camiones += 1
    if entra_salida == "2":
        Vehiculo =input (" Que vehiculo desea sacar?  \n1. automovil \n2. motocicletas \n3. biciletas \n4. salida \n-> ")
        if Vehiculo == "1":
            print("Haz sacado un automóvil.")
            autos -= 1
            if autos < 0:
                autos = 0
                print("No hay autos para sacar.")
        if Vehiculo == "2":
            print("Haz sacado una motocicleta.")
            motos -= 1
            if motos < 0:
                motos = 0
                print("No hay motocicletas para sacar.")
        if Vehiculo == "3":
            print("Haz sacado una bicicleta.")
            bicicletas -= 1
            if bicicletas < 0:
                bicicletas = 0
                print("No hay bicicletas")
    if Vehiculo == '4':
        Vehiculo = False

