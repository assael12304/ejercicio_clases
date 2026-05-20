class Vehiculo:
    # __init__ es el constructor: se llama automaticamente al crear el objeto
    def __init__(self, marca, modelo):
        self.marca     = marca    # atributo de texto
        self.modelo    = modelo   # atributo de texto
        self.velocidad = 0        # empieza en 0 siempre
        self.encendido = False   # empieza apagado siempre

    def encender(self):
        # Revisamos si ya esta encendido para evitar hacerlo doble
        if self.encendido:
            print("El vehiculo ya esta en marcha.")
        else:
            self.encendido = True
            print(f"{self.marca} {self.modelo} encendido.")

    def acelerar(self, km):
        # Solo podemos acelerar si el motor esta encendido
        if not self.encendido:
            print("Enciende el vehiculo antes de acelerar.")
        else:
            self.velocidad += km
            print(f"Velocidad actual: {self.velocidad} km/h")

    def frenar(self, km):
        # max(0, ...) evita que la velocidad quede negativa
        self.velocidad = max(0, self.velocidad - km)
        print(f"Velocidad actual: {self.velocidad} km/h")

    def apagar(self):
        # No se puede apagar si el vehiculo aun se mueve
        if self.velocidad > 0:
            print(f"Frena antes de apagar (velocidad: {self.velocidad} km/h).")
        else:
            self.encendido = False
            print("Vehiculo apagado.")

    def estado(self):
        # Resumen de todos los atributos actuales del objeto
        estado_str = "Encendido" if self.encendido else "Apagado"
        print("--- Estado ---")
        print(f"Vehiculo : {self.marca} {self.modelo}")
        print(f"Velocidad: {self.velocidad} km/h")
        print(f"Motor    : {estado_str}")


# --- Prueba del codigo ---
moto = Vehiculo("Honda", "CB500")
moto.encender()       # Enciende
moto.acelerar(60)     # 60 km/h
moto.acelerar(40)     # 100 km/h
moto.apagar()         # No puede, aun se mueve
moto.frenar(100)     # 0 km/h
moto.apagar()         # Apagado
moto.estado()         # Resumen final