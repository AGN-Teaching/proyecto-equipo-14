# Define una clase llamada CompaniaSocia
class CompaniaSocia:
    def __init__(self, nombre, beneficios={}):

        # Constructor de la clase CompaniaSocia que recibe un nombre y una lista de beneficios (diccionario)

        self.nombre = nombre
        self.beneficios = beneficios

    # Método para agregar un beneficio a la compañía
    def agregar_beneficio(self, nombre, descripcion, requisito_gasto):

        self.beneficios[nombre] = {"descripcion": descripcion, "requisito_gasto": requisito_gasto}

    # Método para transferir un beneficio a otra compañía
    def transferir_beneficio(self, destino, beneficio):
        if beneficio in self.beneficios:
            destino.agregar_beneficio(beneficio, self.beneficios[beneficio])
            print(f"Beneficio '{beneficio}' transferido de {self.nombre} a {destino.nombre}")
        else:
            print(f"No se pudo transferir el beneficio '{beneficio}'")

    # Método para proporcionar una representación en cadena de la compañía
    def __str__(self):
        return f"Compañía: {self.nombre}, Beneficios: {', '.join(self.beneficios.keys())}"



