from abc import ABC, abstractmethod
from datetime import datetime

#CLASES ABSTRACTAS

class Persona(ABC):
    def __init__(self, nombre, contacto, direccion ):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas = []

    @abstractmethod
    def agregar_historial(self, detalles_servicio):
        pass

class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.servicio = servicio
        self.hora = hora
        self.veterinario = veterinario

        @abstractmethod
        def actualizar(self, **kwargs):
            pass

# DEFINICION DE LAS SUBCLASES

class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion )
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, Contacto{self.contacto}, Direccion {self.direccion}"

class registroMascota(Mascota):
    def agregar_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)

    def obtener_historial(self):
        return self.historial_citas

class citaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)

class sistemaVeterinaria:
    def __init__(self):
        self.clientes = []

    def registrar_clientes(self):
        try:
            nombre = input("Ingrese el nombre del cliente:").strip()
            contacto = input("Ingrese el contacto:").strip()
            direccion = input("Ingrese la direccion:").strip()

            if not nombre or not contacto or not direccion:
                raise ValueError("Todos los campos son obligatorios")

            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print("¡Cliente registrado con exito!")

        except ValueError as e:
            print(f"Error: {e}")

    def registrar_mascota(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente:").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)

            if not cliente:
                raise ValueError("Cliente no encontrado")

            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie: ").strip()
            raza = input("Ingrese la raza: ").strip()
            edad = int(input("Ingrese la edad: ").strip())

            if not nombre_mascota or not especie or not raza or edad <= 0:
                raise ValueError("Informacion de la mascota invalidada")

            mascota = registroMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("¡Mascota registrada con exito!")

        except ValueError as e:
            print(f"Error: {e}")

    def programar_cita(self):

        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            if not cliente:
                raise ValueError("Cliente no encontrado")
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)
            if not mascota:
                raise ValueError("Mascota no encontrada")
            
            fecha = input("Ingrese la fecha de la cita (AAAA-MM-DD): ").strip()
            hora = input("Ingrese la hora (HH:MM):").strip()
            servicio = input("Ingrese el servicio(Consulta, vacunacion, etc)").strip()
            veterinario = input("Ingrese el nombre del veterinario: ").strip()
            
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            
            if not servicio or not veterinario:
                raise ValueError("Detalles invalidos")
            
            cita = citaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_historial(cita)
            print("¡Cita programada con exito!")

        except ValueError as e:
            print(f"Error: {e}")
    
    def actualizar_cita(self):
        
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("Cliente no encontrado")
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)
            
            if not mascota:
                raise ValueError("Mascota no encontrada")
            
            if not mascota.historial_citas:
                raise ValueError("No hay citas registradas")
            
            print("Citas disponibles para actualizar")
            for i, cita in enumerate(mascota.historial_citas):
                print(f"{i+1}. Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}")
                
            indice = int(input("Seleccione el numero de las citas a actualizar: ").strip()) -1 
            if indice < 0 or indice >= len(mascota.historial_citas):
                raise ValueError("Seleccion invalida")
            
            cita = mascota.historial_citas[indice]
            
            print("Dejar en blanco los campos que no se quieren actualizar")
            nueva_fecha = input("Nueva fecha (AAAA-MM-DD): ").strip()
            nueva_horas = input("Nueva hora (HH:MM): ").strip()
            nuevo_servicio = input("Nuevo servicio: ").strip()
            nuevo_veterinario = input("Nuevo veterinario: ").strip()
            
            if nueva_fecha:
                datetime.strptime(nueva_fecha, "%Y-%m-%d")
                cita.actualizar(fecha = nueva_fecha)
                
            if nueva_horas:
                datetime.strptime(nueva_horas, "%H:%M")
                cita.actualizar(hora = nueva_horas)
            
            if nuevo_servicio:
                cita.actualizar(servicio = nuevo_servicio)
                
            if nuevo_veterinario:
                cita.actualizar(veterinario = nuevo_veterinario)
                
            print("¡Cita actualizada con exito!")     
        except ValueError as e:
            print(f"Error: {e}")
            
    def consultar_historial(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            if not cliente:
                raise ValueError("Cliente no encontrado")
            
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)
            if not mascota:
                raise ValueError("Mascota no encontrada")
    
            historial = mascota.obtener_historial()
            if not historial:
                print("No hay historial disponible para la mascota.")
            else:
                for entrada in historial:
                    print(f"Fecha: {entrada.fecha}, Hora: {entrada.hora}, Servicio: {entrada.servicio}, Veterinario: {entrada.veterinario}")
        
        except ValueError as e:
            print(f"Error: {e}")
            
    def iniciar(self):
        while True:
            print("\n *** SISTEMA DE GESTION ***")
            print("1. Registrar cliente.")
            print("2. Registrar mascota.")
            print("3. Programar cita.")
            print("4. Actualizar cita.")
            print("5. Consultar historial.")
            print("6. Salir.")
            
            opcion = input("Seleccione una opcion: ").strip()
            
            if opcion == "1":
                self.registrar_clientes()
            elif opcion == "2":
                self.registrar_mascota()
            elif opcion == "3":
                self.programar_cita()
            elif opcion == "4":
                self.actualizar_cita()
            elif opcion == "5":
                self.consultar_historial()
            elif opcion == "6":
                print("¡...Saliendo del sistema...")
                break
            else:
                print("Opcion invalida")
                
if __name__ == "__main__":
    sistema = sistemaVeterinaria()
    sistema.iniciar()
        
