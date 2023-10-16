# Importa el módulo 'pickle' para guardar y cargar datos en formato binario.
import pickle
# Importa las clases necesarias desde otros archivos.
from Cliente import Cliente
from Cliente_VIP import ClienteVIP
from Compania_Socia import CompaniaSocia

# Define la clase ProgramaRecompensas.
class ProgramaRecompensas:
    def __init__(self):
        # Inicializa las listas para almacenar clientes normales, clientes VIP y compañías afiliadas.
        self.clientes = []
        self.clientes_vip = []
        self.companias = []
        # Inicializa la variable cliente_actual como None (ningún cliente en sesión).
        self.cliente_actual = None
        # Define un nombre de usuario y contraseña para el administrador.
        self.usuario_admin = "Admin"
        self.contrasena_admin = "1234"

        try:
            # Intenta cargar datos desde el archivo "Projecto.pkl" si existe.
            with open("Projecto.pkl", "rb") as archivo:
                datos = pickle.load(archivo)
                self.companias = datos['companias']
                self.clientes = datos['clientes']
                self.clientes_vip = datos['clientes_vip']
                # Otros datos que hayas guardado.

        except FileNotFoundError:
            # El archivo no existe, se inician las listas vacías.
            self.companias = []
            self.clientes = []
            self.clientes_vip = []

    # Método para ingresar como un cliente normal.
    def ingresar_cliente(self):
        nombre_cliente = input("Ingrese su nombre de cliente: ")
        cliente_existente = self.buscar_cliente(nombre_cliente)
        if cliente_existente:
            self.cliente_actual = cliente_existente
            self.menu_cliente()
        else:
            self.cliente_actual = None
            print("Cliente no encontrado. Debes Registrarte.")

    # Método para ingresar como un cliente VIP.
    def ingresar_cliente_vip(self):
        nombre_cliente = input("Ingrese su nombre de cliente: ")
        cliente_vip_existente = self.buscar_cliente_vip(nombre_cliente)
        if cliente_vip_existente:
            self.cliente_actual = cliente_vip_existente
            self.menu_cliente_vip()
        else:
            self.cliente_actual = None
            print("No eres cliente vip, continua con la opcion cliente o registrate.")

    # Método para buscar un cliente por nombre.
    def buscar_cliente(self, nombre_cliente):
        for cliente in self.clientes + self.clientes_vip:
            if cliente.nombre == nombre_cliente:
                return cliente
        return None

    # Menú para elegir entre Cliente Normal, Cliente VIP o Registrarse.
    def menu_clientes(self):
        while True:
            print("1. Cliente")
            print("2. Cliente VIP")
            print("3. Registrarse")
            print("4. Volver al Menú Principal ")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ingresar_cliente()
            elif opcion == "2":
                self.ingresar_cliente_vip()
            elif opcion == "3":
                self.agregar_cliente()
            elif opcion == "4":
                self.guardar_informacion()
                break
            else:
                print("Opcion incorrecta vuelva a intentar")

    # Menú principal para Cliente Normal.
    def menu_cliente(self):
        while True:
            print("\nMenú Cliente:")
            print("1. Obtener Beneficio")
            print("2. Mostrar Catálogo de Beneficios")
            print("3. Eliminar compañia")
            print("4. Agregar Compañia ")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.mostrar_companias_relacionadas_y_elegir_beneficio()
            elif opcion == "2":
                self.mostrar_catalogo_beneficios_cliente()
            elif opcion == "3":
                self.eliminar_empresa_afiliada(self.cliente_actual)
            elif opcion == "4":
                self.agregar_compania_afiliada(self.cliente_actual)
            elif opcion == "5":
                self.guardar_informacion()
                break
            else:
                print("Opcion incorrecta vuelva a intentar")

    # Menú principal para Cliente VIP.
    def menu_cliente_vip(self):
        while True:
            print("\nMenú Cliente VIP:")
            print("1. Transferir Beneficios")
            print("2. Mostrar Catálogo de Beneficios")
            print("3. Obtener un beneficio ")
            print("4. Eliminar una compañia")
            print("5. Agregar Compañia")
            print("6. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Mostrar una lista de compañías de las que es cliente VIP
                print("Compañías en las que eres Cliente VIP:")
                for i, compania in enumerate(self.cliente_actual.companias_afiliadas, 1):
                    print(f"{i}. {compania.nombre}")

                # Ingresar el número de la compañía de origen
                numero_compania_origen = int(input("Ingrese el número de la compañía de origen: ")) - 1

                if 0 <= numero_compania_origen < len(self.cliente_actual.companias_afiliadas):
                    compania_origen = self.cliente_actual.companias_afiliadas[numero_compania_origen]

                    # Ingresar el número de la compañía de destino
                    numero_compania_destino = int(input("Ingrese el número de la compañía de destino: ")) - 1

                    if 0 <= numero_compania_destino < len(self.cliente_actual.companias_afiliadas):
                        compania_destino = self.cliente_actual.companias_afiliadas[numero_compania_destino]

                        # Mostrar los beneficios de la compañía de origen
                        print(f"Beneficios de {compania_origen.nombre}:")
                        for i, (beneficio, info) in enumerate(compania_origen.beneficios.items(), 1):
                            print(f"{i}. {beneficio}")

                        # Ingresar el número del beneficio a transferir
                        numero_beneficio = int(input("Ingrese el número del beneficio a transferir: ")) - 1

                        if 0 <= numero_beneficio < len(compania_origen.beneficios):
                            beneficio_transferir = list(compania_origen.beneficios.keys())[numero_beneficio]
                            self.transferir_beneficios(compania_origen, compania_destino, beneficio_transferir)
                        else:
                            print("Número de beneficio no válido.")
                    else:
                        print("Número de compañía de destino no válido.")
                else:
                    print("Número de compañía de origen no válido.")
            elif opcion == "2":
                self.mostrar_catalogo_beneficios_cliente()
            elif opcion == "3":
                self.mostrar_companias_relacionadas_y_elegir_beneficio()
            elif opcion == "4":
                self.eliminar_empresa_afiliada(self.cliente_actual)
            elif opcion == "5":
                self.agregar_compania_afiliada_cliente_vip(self.cliente_actual)
            elif opcion == "6":
                self.guardar_informacion()
                break
            else:
                print("Opción incorrecta. Por favor, vuelva a intentar.")

    # Método para transferir un beneficio entre compañías.
    def transferir_beneficios(self, origen, destino, beneficio):
        if origen in self.companias and destino in self.companias:
            if beneficio in origen.beneficios:
                beneficio_info = origen.beneficios[beneficio]
                # Agrega el beneficio al destino marcándolo como transferido
                destino.agregar_beneficio(f"Transferido - {beneficio}", beneficio_info['descripcion'],
                                          beneficio_info['requisito_gasto'])
                print(f"Beneficio '{beneficio}' transferido de {origen.nombre} a {destino.nombre}")
                # No se elimina el beneficio de la compañía de origen
                print(f"Beneficio '{beneficio}' ahora está disponible en {destino.nombre}.")
            else:
                print(f"El beneficio '{beneficio}' no está disponible en {origen.nombre}")
        else:
            print("Una de las compañías no está en la lista de compañías afiliadas.")

    # Método para mostrar el catálogo de beneficios disponibles.
    def mostrar_catalogo_beneficios_cliente(self):
        print("\nCatálogo de Beneficios Disponibles:")
        print("Compañías en las que eres cliente:")

        # Mostrar las empresas en las que el cliente es cliente
        for compania in self.cliente_actual.companias_afiliadas:
            print(f"Compañía: {compania.nombre}")
            print("Beneficios:")
            for beneficio, info in compania.beneficios.items():
                descripcion = info['descripcion']
                requisito_gasto = info['requisito_gasto']
                print(f"- Beneficio: {beneficio}")
                print(f"  Descripción: {descripcion}")
                print(f"  Requisito de Gasto: ${requisito_gasto}")
                print("---------------")

    # Método para agregar una compañía socia.
    def agregar_compania_socia(self):
        nombre_compania = input("Nombre de la Compañía: ")
        beneficios = {}
        while True:
            beneficio_nombre = input("Nombre del Beneficio (o '0' para terminar): ")
            if beneficio_nombre == '0':
                break
            beneficio_descripcion = input("Descripción del Beneficio: ")
            beneficio_requisito_gasto = float(input("Requisito de Gasto para el Beneficio: $"))
            beneficios[beneficio_nombre] = {
                'descripcion': beneficio_descripcion,
                'requisito_gasto': beneficio_requisito_gasto
            }
        nueva_compania = CompaniaSocia(nombre_compania, beneficios)
        self.companias.append(nueva_compania)
        print(f"Compañía '{nombre_compania}' agregada con éxito.")

    # Método para agregar un cliente (tanto normal como VIP).
    def agregar_cliente(self):
        nombre_cliente = input("Nombre del Cliente: ")

        # Mostrar la lista de compañías disponibles para que el cliente elija
        print("\nLista de Compañías Disponibles:")
        for i, compania in enumerate(self.companias):
            print(f"{i + 1}. {compania.nombre}")

        seleccion_companias = input("Seleccione las compañías a las que el cliente pertenece (separadas por comas): ")
        seleccion_companias = [int(index) for index in seleccion_companias.split(",") if index.isdigit()]

        companias_cliente = []
        for index in seleccion_companias:
            if 0 < index <= len(self.companias):
                companias_cliente.append(self.companias[index - 1])

        nuevo_cliente = Cliente(nombre_cliente, companias_cliente)
        self.clientes.append(nuevo_cliente)

        if len(companias_cliente) >= 5:
            nuevo_cliente_vip = ClienteVIP(nombre_cliente, companias_cliente)
            self.clientes_vip.append(nuevo_cliente_vip)
            print(f"El cliente '{nombre_cliente}' se ha agregado como Cliente VIP.")
        else:
            print(f"El cliente '{nombre_cliente}' se ha agregado como Cliente Normal.")

    def guardar_informacion(self):
        # Implementación para guardar la información en el archivo "Projecto.pkl"
        datos = {
            'companias': self.companias,
            'clientes': self.clientes,
            'clientes_vip': self.clientes_vip,
        }
        with open("Projecto.pkl", "wb") as archivo:
            pickle.dump(datos, archivo)

    # Método para mostrar la información de las compañías y clientes.
    def mostrar_informacion(self):
        print("\nInformación de Compañías:")
        for compania in self.companias:
            print(f"Nombre de la Compañía: {compania.nombre}")
            print("Beneficios:")
            for beneficio, info in compania.beneficios.items():
                descripcion = info['descripcion']
                requisito_gasto = info['requisito_gasto']
                print(f"- Beneficio: {beneficio}")
                print(f"  Descripción: {descripcion}")
                print(f"  Requisito de Gasto: ${requisito_gasto}")
            print("\n")

        print("\nInformación de Clientes:")
        for cliente in self.clientes + self.clientes_vip:
            print(f"Nombre del Cliente: {cliente.nombre}")
            print("Compañías afiliadas:")
            for compania in cliente.companias_afiliadas:
                print(f"- {compania.nombre}")
            print("\n")

    # Método para mostrar la lista de compañías y permitir al usuario elegir una.
    def mostrar_companias_relacionadas_y_elegir_beneficio(self):
        print("\nSelecciona una compañía:")
        for i, compania in enumerate(self.cliente_actual.companias_afiliadas):
            print(f"{i + 1}. {compania.nombre}")

        seleccion_compania = input("Seleccione una compañía por número o '0' para volver: ")
        if seleccion_compania == '0':
            return

        if seleccion_compania.isdigit() and 0 < int(seleccion_compania) <= len(self.cliente_actual.companias_afiliadas):
            compania_elegida = self.cliente_actual.companias_afiliadas[int(seleccion_compania) - 1]
            print(f"Compañía seleccionada: {compania_elegida.nombre}")

            print("\nSelecciona un beneficio:")
            beneficios_disponibles = [(i + 1, nombre, info["descripcion"], info["requisito_gasto"]) for
                                      i, (nombre, info) in
                                      enumerate(compania_elegida.beneficios.items())]
            for num, nombre, descripcion, requisito in beneficios_disponibles:
                print(f"{num}. {nombre} - {descripcion} (Requisito de gasto: ${requisito})")

            seleccion_beneficio = input("Seleccione un beneficio por número o '0' para volver: ")
            if seleccion_beneficio == '0':
                return

            if seleccion_beneficio.isdigit() and 0 < int(seleccion_beneficio) <= len(beneficios_disponibles):
                num_seleccionado, beneficio_nombre, _, requisito_gasto = beneficios_disponibles[
                    int(seleccion_beneficio) - 1]
                print(f"Beneficio seleccionado: {beneficio_nombre}")
                gasto_cliente = float(input("Ingrese su gasto actual en la compañía: "))
                self.obtener_beneficio(compania_elegida, beneficio_nombre, gasto_cliente, requisito_gasto)
            else:
                print("Selección de beneficio inválida.")
        else:
            print("Selección de compañía inválida.")

    # Método para verificar si el cliente cumple con el requisito de gasto para obtener un beneficio.
    def obtener_beneficio(self, compania, beneficio_nombre, gasto_cliente, requisito_gasto):
        if gasto_cliente >= requisito_gasto:
            print(
                f"Has gastado ${gasto_cliente} y cumples con el requisito de gasto para obtener el beneficio '{beneficio_nombre}' de la compañía '{compania.nombre}'.")
        else:
            print(
                f"No cumples con el requisito de gasto para obtener el beneficio '{beneficio_nombre}' de la compañía '{compania.nombre}'.")

    # Método para buscar un cliente VIP por nombre.
    def buscar_cliente_vip(self, nombre_cliente):
        for cliente_vip in self.clientes_vip:
            if cliente_vip.nombre == nombre_cliente:
                return cliente_vip
        return None

    # Método para autenticar al administrador con usuario y contraseña.
    def autenticar_admin(self, usuario, contrasena):
        return usuario == self.usuario_admin and contrasena == self.contrasena_admin

    # Método para mostrar la lista de compañías afiliadas.
    def mostrar_lista_companias(self):
        print("\nCompañías Afiliadas:")
        for i, compania in enumerate(self.companias, 1):
            print(f"{i}. {compania.nombre}")

    # Métodos para eliminación de clientes o compañías.
    def menu_eliminar_compania(self):
        self.mostrar_lista_companias()
        nombre_compania = input("Ingrese el nombre de la compañía que desea eliminar: ")
        self.eliminar_compania(nombre_compania)

    def eliminar_compania(self, nombre_compania):
        for compania in self.companias:
            if compania.nombre == nombre_compania:
                # Solicitar confirmación
                if self.confirmar_accion(f"¿Desea eliminar la compañía '{nombre_compania}'?"):
                    self.companias.remove(compania)
                    print(f"Compañía '{nombre_compania}' eliminada con éxito.")
                else:
                    print("No se eliminó la compañía.")
                return
        print(f"La compañía '{nombre_compania}' no se encontró en la lista de compañías.")

    def confirmar_accion(self, mensaje):
        confirmacion = input(f"{mensaje} (Sí/No): ").strip().lower()
        return confirmacion == "si"

    def mostrar_lista_clientes(self):
        print("\nLista de Clientes:")
        print("Clientes Normales:")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i}. {cliente.nombre}")

        print("\nClientes VIP:")
        for i, cliente in enumerate(self.clientes_vip, len(self.clientes) + 1):
            print(f"{i}. {cliente.nombre} (VIP)")

    def menu_eliminar_cliente(self):
        self.mostrar_lista_clientes()
        numero_cliente = int(input("Ingrese el número del cliente que desea eliminar: "))
        self.eliminar_cliente(numero_cliente)

    def eliminar_cliente(self, numero_cliente):
        if 1 <= numero_cliente <= len(self.clientes) + len(self.clientes_vip):
            if numero_cliente <= len(self.clientes):
                cliente = self.clientes[numero_cliente - 1]
                es_vip = isinstance(cliente, ClienteVIP)
            else:
                cliente = self.clientes_vip[numero_cliente - 1 - len(self.clientes)]
                es_vip = True

            # Solicitar confirmación
            if self.confirmar_accion(f"¿Desea eliminar al cliente '{cliente.nombre}'?"):
                if es_vip:
                    self.clientes_vip.remove(cliente)
                else:
                    self.clientes.remove(cliente)
                print(f"Cliente '{cliente.nombre}' eliminado con éxito.")
            else:
                print("No se eliminó al cliente.")
        else:
            print("Número de cliente no válido.")

    # Metodo para eliminar beneficios de las compañias
    def eliminar_beneficio(self):
        # Mostrar una lista de compañías disponibles para que el usuario elija
        print("Compañías Disponibles:")
        for i, compania in enumerate(self.companias, 1):
            print(f"{i}. {compania.nombre}")

        seleccion_compania = input("Seleccione el número de la compañía de la que desea eliminar un beneficio: ")

        if seleccion_compania.isdigit() and 1 <= int(seleccion_compania) <= len(self.companias):
            # Obtener la compañía seleccionada
            compania = self.companias[int(seleccion_compania) - 1]

            # Mostrar una lista de beneficios disponibles para la compañía
            print(f"Beneficios disponibles en {compania.nombre}:")
            for i, (beneficio, info) in enumerate(compania.beneficios.items(), 1):
                print(f"{i}. {beneficio}")

            seleccion_beneficio = input("Seleccione el número del beneficio que desea eliminar: ")

            if seleccion_beneficio.isdigit() and 1 <= int(seleccion_beneficio) <= len(compania.beneficios):
                beneficios = list(compania.beneficios.keys())
                beneficio = beneficios[int(seleccion_beneficio) - 1]

                # Eliminar el beneficio de la compañía
                del compania.beneficios[beneficio]
                print(f"Beneficio '{beneficio}' eliminado de la compañía '{compania.nombre}'.")
            else:
                print("Selección de beneficio no válida.")
        else:
            print("Selección de compañía no válida.")

    # Metodo para agregar beneficios a las compañias
    def agregar_beneficio(self):
        # Mostrar una lista de compañías disponibles para que el usuario elija
        print("Compañías Disponibles:")
        for i, compania in enumerate(self.companias, 1):
            print(f"{i}. {compania.nombre}")

        seleccion_compania = input("Seleccione el número de la compañía a la que desea agregar un beneficio: ")

        if seleccion_compania.isdigit() and 1 <= int(seleccion_compania) <= len(self.companias):
            # Obtener la compañía seleccionada
            compania = self.companias[int(seleccion_compania) - 1]

            # Solicitar información del nuevo beneficio
            beneficio = input("Nombre del nuevo beneficio: ")
            descripcion = input("Descripción del beneficio: ")
            requisito_gasto = float(input("Requisito de gasto para el beneficio: $"))

            # Agregar el beneficio a la compañía
            compania.agregar_beneficio(beneficio, descripcion, requisito_gasto)
            print(f"Beneficio '{beneficio}' agregado a la compañía '{compania.nombre}'.")
        else:
            print("Selección de compañía no válida.")

    # Metodo para eliminar una compañia de la que ya no eres cliente
    def eliminar_empresa_afiliada(self, cliente):
        print(f"Empresas afiliadas de {cliente.nombre}:")
        for i, empresa in enumerate(cliente.companias_afiliadas, 1):
            print(f"{i}. {empresa.nombre}")

        numero_empresa = int(input("Seleccione el número de la empresa que desea eliminar: "))

        if 1 <= numero_empresa <= len(cliente.companias_afiliadas):
            empresa_eliminada = cliente.companias_afiliadas.pop(numero_empresa - 1)
            print(
                f"La empresa '{empresa_eliminada.nombre}' ha sido eliminada de las empresas afiliadas de {cliente.nombre}.")

            # Verificar si el cliente se ha convertido en cliente normal
            if len(cliente.companias_afiliadas) < 5 and isinstance(cliente, ClienteVIP):
                cliente_vip = cliente
                self.clientes_vip.remove(cliente_vip)
                cliente_normal = Cliente(cliente_vip.nombre, cliente_vip.companias_afiliadas)
                self.clientes.append(cliente_normal)
                print(f"{cliente.nombre} ya no es cliente VIP y se ha convertido en cliente normal.")
        else:
            print("Número de empresa no válido.")

    # Metodo para convertir un cliente Vip en cliente normal por no tener los requerimientos
    def convertir_a_cliente_normal(self, cliente_vip):
        if cliente_vip in self.clientes_vip:
            self.clientes_vip.remove(cliente_vip)
            nuevo_cliente_normal = Cliente(cliente_vip.nombre, cliente_vip.companias_afiliadas)
            self.clientes.append(nuevo_cliente_normal)
            print(f"El cliente VIP '{cliente_vip.nombre}' se ha convertido en cliente normal.")
        else:
            print("El cliente VIP no existe en la lista de clientes VIP.")

    # Metodo para agregar una compañia de la que vas a ser cliente
    def agregar_compania_afiliada(self, cliente):
        if cliente in self.clientes:
            limite_companias = 5  # Límite de compañías para convertirse en Cliente VIP
            if len(cliente.companias_afiliadas) < limite_companias:
                print("Compañías Disponibles para Afiliarse:")
                for i, compania in enumerate(self.companias, 1):
                    print(f"{i}. {compania.nombre}")

                seleccion_companias = input(
                    "Seleccione las compañías a las que deseas afiliarte (separadas por comas): ")
                seleccion_companias = [int(index) for index in seleccion_companias.split(",") if index.isdigit()]

                companias_cliente = []
                for index in seleccion_companias:
                    if 0 < index <= len(self.companias):
                        companias_cliente.append(self.companias[index - 1])

                cliente.companias_afiliadas.extend(companias_cliente)
                print("Compañías afiliadas actualizadas con éxito.")
                if len(cliente.companias_afiliadas) >= limite_companias:
                    print("Has alcanzado el límite de compañías afiliadas y te has convertido en Cliente VIP.")
                    # Crear un objeto ClienteVIP y reemplazar el cliente normal en la lista
                    nuevo_cliente_vip = ClienteVIP(cliente.nombre, cliente.companias_afiliadas)
                    self.clientes_vip.append(nuevo_cliente_vip)
                    self.clientes.remove(cliente)
                    cliente = nuevo_cliente_vip
            else:
                print("Has alcanzado el límite de compañías afiliadas como Cliente Normal.")

    # Metodo para agregar una compañia de la que vas a ser cliente siendo vip
    def agregar_compania_afiliada_cliente_vip(self, cliente_vip):
        if cliente_vip in self.clientes_vip:
            print("Compañías Disponibles para Afiliarse:")
            for i, compania in enumerate(self.companias, 1):
                print(f"{i}. {compania.nombre}")

            seleccion_companias = input("Seleccione las compañías a las que deseas afiliarte (separadas por comas): ")
            seleccion_companias = [int(index) for index in seleccion_companias.split(",") if index.isdigit()]

            companias_cliente = []
            for index in seleccion_companias:
                if 0 < index <= len(self.companias):
                    companias_cliente.append(self.companias[index - 1])

            cliente_vip.companias_afiliadas.extend(companias_cliente)
            print("Compañías afiliadas actualizadas con éxito para Cliente VIP.")

    # Metodo para ver la informacion de un cliente o compaia en especifico
    def ver_informacion_cliente(self):
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cliente_encontrado = self.buscar_cliente(nombre_cliente)
        if cliente_encontrado:
            print("Información del Cliente:")
            print(f"Nombre: {cliente_encontrado.nombre}")
            print("Compañías Afiliadas:")
            for compania in cliente_encontrado.companias_afiliadas:
                print(f"- {compania.nombre}")
        else:
            print(f"Cliente con nombre '{nombre_cliente}' no encontrado.")

    def ver_informacion_compania(self, nombre_compania):
        compania = next((c for c in self.companias if c.nombre == nombre_compania), None)
        if compania:
            print(f"Información de la Compañía '{nombre_compania}':")
            for beneficio, info in compania.beneficios.items():
                descripcion = info['descripcion']
                requisito_gasto = info['requisito_gasto']
                print(f"- Beneficio: {beneficio}")
                print(f"  Descripción: {descripcion}")
                print(f"  Requisito de Gasto: ${requisito_gasto}")
        else:
            print(f"No se encontró una compañía con el nombre '{nombre_compania}'.")

