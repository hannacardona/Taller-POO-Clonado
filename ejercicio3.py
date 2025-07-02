class DispensadorCafe:
    def __init__(self, maximo=1000, actual=0):
        self.maximo = maximo
        self.actual = min(actual, maximo)

    def llenar(self):
        self.actual = self.maximo

    def servir(self, cantidad):
        if self.actual >= cantidad:
            self.actual -= cantidad
            print(f"Taza servida con {cantidad} cc.")
        else:
            print(f"Solo se sirvieron {self.actual} cc.")
            self.actual = 0

    def vaciar(self):
        self.actual = 0

    def agregar(self, cantidad):
        self.actual = min(self.actual + cantidad, self.maximo)

    def estado(self):
        return f"Nivel: {self.actual}/{self.maximo} cc"

def interfaz_cafetera():
    print("Bienvenido al Sistema de Dispensador de Café ")
    capacidad = input("¿Deseas establecer una capacidad máxima personalizada? (S/N): ").strip().upper()
   
    if capacidad == "S":
        try:
            maximo = int(input("Capacidad máxima (cc): "))
            actual = int(input("Cantidad inicial (cc): "))
            cafetera = DispensadorCafe(maximo, actual)
        except ValueError:
            print("Entrada inválida. Usando valores por defecto.")
            cafetera = DispensadorCafe()
    else:
        cafetera = DispensadorCafe()

    while True:
        print("\n====== MENÚ DE CAFETERA ======")
        print("1. Llenar cafetera")
        print("2. Servir taza")
        print("3. Vaciar cafetera")
        print("4. Agregar café")
        print("5. Mostrar estado")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            cafetera.llenar()
            print("✔ Cafetera llena.")
        elif opcion == "2":
            try:
                cantidad = int(input("Ingrese cantidad para servir (cc): "))
                cafetera.servir(cantidad)
            except ValueError:
                print("Cantidad inválida.")
        elif opcion == "3":
            cafetera.vaciar()
            print("✔ Cafetera vacía.")
        elif opcion == "4":
            try:
                cantidad = int(input("Ingrese cantidad de café a agregar (cc): "))
                cafetera.agregar(cantidad)
                print("✔ Café agregado.")
            except ValueError:
                print("Cantidad inválida.")
        elif opcion == "5":
            print(cafetera.estado())
        elif opcion == "6":
            print("Saliendo del sistema de cafetera. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

