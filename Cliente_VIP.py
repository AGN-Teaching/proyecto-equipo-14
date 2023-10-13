from Cliente import Cliente  # Importar la clase Cliente

# Define una clase ClienteVIP que hereda de Cliente
class ClienteVIP(Cliente):

    def __init__(self, nombre, afiliaciones=[]):

        # Llama al constructor de la clase base (Cliente) con el nombre y afiliaciones

        super().__init__(nombre, afiliaciones)

        # Crea un diccionario para llevar el registro de beneficios transferibles

        self.beneficios_transferibles = {}

    def agregar_beneficio_transferible(self, beneficio_nombre, cantidad):

        # Verifica si el beneficio ya existe en el diccionario

        if beneficio_nombre in self.beneficios_transferibles:

            # Si existe, incrementa la cantidad

            self.beneficios_transferibles[beneficio_nombre] += cantidad

        else:

            # Si no existe, crea una nueva entrada en el diccionario

            self.beneficios_transferibles[beneficio_nombre] = cantidad

    def quitar_beneficio_transferible(self, beneficio_nombre, cantidad):

        # Verifica si el beneficio existe en el diccionario

        if beneficio_nombre in self.beneficios_transferibles:

            # Comprueba si la cantidad especificada es mayor o igual a la cantidad existente

            if cantidad >= self.beneficios_transferibles[beneficio_nombre]:
                # Si es mayor o igual, elimina el beneficio del diccionario

                del self.beneficios_transferibles[beneficio_nombre]

            else:

                # Si no es mayor o igual, reduce la cantidad del beneficio

                self.beneficios_transferibles[beneficio_nombre] -= cantidad






