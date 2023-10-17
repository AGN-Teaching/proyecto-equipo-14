# Define una clase llamada Cliente
class Cliente:
    def __init__(self, nombre, companias_afiliadas):

        # Inicializa un nuevo objeto Cliente con un nombre y una lista de afiliaciones vacía por defecto

        self.nombre = nombre
        self.companias_afiliadas = companias_afiliadas

    def agregar_compania_afiliada(self, compania):

        # Permite agregar una compañía a la lista de compañías afiliadas del cliente

        self.companias_afiliadas.append(compania)

    def __str__(self):

        # Define una representación en cadena del objeto Cliente

        return f"Cliente: {self.nombre}, Compañías Afiliadas: {', '.join(self.companias_afiliadas)}"

