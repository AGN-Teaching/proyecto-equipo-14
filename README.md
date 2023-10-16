<div align="center">
  <h1>UNIVERSIDAD AUTÓNOMA METROPOLITANA</h1>
  <h2>UNIDAD CUAJIMALPA</h2>
  <hr>
  
  <h2>Informe del Proyecto</h2>
  
  <h3>LICENCIATURA EN INGENIERÍA EN COMPUTACIÓN</h3>
  
  <p><strong>Tema:</strong> Programa de Recompensas</p>
  
  <h3>Equipo de trabajo:</h3>
  <p>Erik Muñoz Rodríguez</p>
  <p>Luis Fernando Fabián Guzmán</p>
  
  <h3>UEA:</h3>
  <p>PROGRAMACIÓN ORIENTADA A OBJETOS</p>
  
  <h3>PROFESOR:</h3>
  <p>Abel García Nájera</p>
</div>

# ANALISIS DEL PROBLEMA


# DESCRIPCION DEL PROBLEMA


El problema se centra en la implementación de un programa de recompensas que permite a los clientes obtener beneficios de compañías asociadas según sus hábitos de compra. Además, se establece un criterio para otorgar la categoría VIP a los clientes que son miembros de cinco o más compañías, lo que les permite transferir beneficios entre compañías.


# REQUISITOS CLAVE


Los clientes pueden ser miembros de múltiples compañías socias.
Los beneficios se basan en los hábitos de compra de los clientes, donde mayores compras significan mayores beneficios.
Los clientes VIP pueden transferir beneficios entre compañías.
Debe haber un mecanismo para agregar nuevas compañías socias y clientes.


# ENTIDADES CLAVE


Cliente: Representa a los clientes que son miembros del programa de recompensas. Pueden ser clientes normales o VIP.
Compañía Socia: Representa a las compañías que participan en el programa de recompensas y ofrecen beneficios a los clientes.
Beneficio: Los beneficios ofrecidos por las compañías a los clientes en función de sus hábitos de compra.
Programa de Recompensas: El sistema que gestiona a los clientes, las compañías socias y los beneficios.


# DISEÑO DE LA SOLUCION


# CLASE CLIENTE


La clase Cliente representa a un cliente del programa de recompensas. Un cliente tiene un nombre y una lista de afiliaciones que indican a qué compañías está asociado. El constructor __init__ inicializa un nuevo objeto Cliente con un nombre y una lista de afiliaciones (que se inicializa como una lista vacía por defecto). La clase también tiene un método agregar_compania_afiliada para permitir la adición de compañías afiliadas a la lista del cliente. El método __str__ proporciona una representación en cadena del objeto, mostrando el nombre del cliente y las compañías a las que está afiliado.

![1](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/3dfdb09c-33e5-4ef1-9bf8-c8caaf3c7fb2)


# CLASE CLIENTEVIP

La clase ClienteVIP hereda de la clase Cliente y agrega la funcionalidad adicional para clientes que alcanzan la categoría VIP al ser miembros de cinco o más compañías socias del programa. Además, los clientes VIP tienen la capacidad de transferir beneficios entre compañías. Esto se logra a través de los métodos agregar_beneficio_transferible y quitar_beneficio_transferible para agregar o eliminar beneficios transferibles, y el método transferir_beneficios para transferir un beneficio de una compañía a otra.

![2](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/4700dd71-e753-477a-bd0c-f17e87ce1ff2)


# CLASE COMPANIASOCIA


La clase CompaniaSocia representa a una compañía socia del programa de recompensas. Cada compañía tiene un nombre y ofrece una lista de beneficios a sus clientes, los cuales están asociados a la compañía. Los beneficios incluyen una descripción y un requisito de gasto. La compañía permite agregar beneficios a través del método agregar_beneficio, y transferir beneficios a otras compañías a través del método transferir_beneficio.

![3](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/dadfa2a3-e612-4935-9e0b-b22faa971885)


# CLASE PROGRAMARECOMPENSAS


La clase ProgramaRecompensas interactúa con todas las demás clases para gestionar el programa de recompensas, permitiendo a los clientes registrarse, obtener beneficios, transferir beneficios y realizar operaciones de guardado y carga de información. También tiene una relación de agregación con las clases Cliente y ClienteVIP, ya que contiene listas de clientes y clientes VIP registrados en el programa.

![4](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/954aab66-fbbe-4473-a0c8-aa61a351a213)


# CLASE MAIN


Sirve como punto de entrada para el programa de recompensas. La clase Main instancia un objeto de ProgramaRecompensas y proporciona un menú principal que permite a los usuarios (clientes o administradores) seleccionar diferentes opciones. Los usuarios pueden gestionar sus cuentas, autenticarse como administradores, ver información y salir del programa. La funcionalidad del programa se basa en el uso de métodos y clases previamente definidos, proporcionando una interfaz de usuario intuitiva y fácil de usar.

![5](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/d79c5ee1-809f-4ded-8d01-23e18e97af43)


# CLASE MENUS


La clase Menu proporciona un sistema de menús que permite a los usuarios (clientes y administradores) seleccionar diferentes opciones. Contiene submenús para trabajar con clientes, beneficios, compañías y clientes VIP, así como un menú principal para el administrador. Estos menús facilitan la interacción de los usuarios con las funciones del programa.
 
![6](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/6e5b2d62-29ca-4163-80d5-0f2a745757bd)


# RELACIONES ENTRE CLASES 


La clase Cliente tiene una relación de asociación con la clase CompaniaSocia a través de la lista de afiliaciones, ya que un cliente está afiliado a una o más compañías.


La clase ClienteVIP hereda de la clase Cliente, lo que indica una relación de herencia. Además, tiene una relación de asociación con la clase CompaniaSocia para gestionar los beneficios transferibles.


La clase CompaniaSocia tiene una relación de asociación con la clase Cliente, ya que cada compañía tiene una lista de clientes afiliados. También tiene una relación de asociación con la clase ClienteVIP para transferir beneficios.


La clase ProgramaRecompensas interactúa con todas las demás clases para gestionar el programa de recompensas, permitiendo a los clientes registrarse, obtener beneficios, transferir beneficios y realizar operaciones de guardado y carga de información. También tiene una relación de agregación con las clases Cliente y ClienteVIP, ya que contiene listas de clientes y clientes VIP registrados en el programa.


La clase Main tiene una relación de asociación con la clase ProgramaRecompensas debido a que Main necesita interactuar con ProgramaRecompensas para llevar a cabo su funcionalidad. Esta asociación se debe a que Main crea una instancia de ProgramaRecompensas en su constructor y utiliza esta instancia para acceder a los métodos y atributos de ProgramaRecompensas.


La clase Menu tiene una relación de asociación con la clase ProgramaRecompensas y la clase Main. La relación con la clase ProgramaRecompensas se debe a que Menu utiliza una instancia de ProgramaRecompensas para interactuar con los datos y realizar operaciones basadas en las opciones seleccionadas por el usuario. Además, la relación con la clase Main se debe a que Menu es una parte fundamental de la lógica de Main y se utiliza para proporcionar opciones de menú y gestionar las interacciones del usuario dentro de la aplicación global.

![ultproyecto](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/0e93a459-96bf-4241-bef5-4b473b95b42a)


# MANEJO DE ERRORES


![97120fea-be73-4610-a9dd-509468054a9a](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/0cd0af57-feb0-494f-a8bb-ce307f85ec18)


En este caso, el error radica en que al agregar un beneficio en la función "agregar compañía," solo se habían definido las variables "nombre_compañia" y "beneficios," en la que solo se especificaba la descripción del beneficio. Sin embargo, al momento de agregar el beneficio, faltaba una variable que no estaba definida, que era el requisito del gasto para el beneficio.


Este error se corrigió agregando en la variable "beneficio" las dos definiciones, es decir, la descripción y el requisito de gastos.


![3ad3d162-169c-455a-9091-417faa792812](https://github.com/AGN-Teaching/proyecto-equipo-14/assets/141948025/7f612069-b751-45b3-8e1f-77cc58fbb88b)


Este error ocurrió ya que en la función mostrar información no se había definido el atributo compañias lo cual generaba el error al seleccionar mostrar información en el menú administrador esto se corrigió definiendo el atributo en el objeto para que no sucediera el error.


DEL SIGUIENTE ERROR, NO SE CUENTA CON IMAGEN, PERO TRATABA DE LO SIGUIENTE:


Al momento de guardar o cargar un archivo ocurría el error de que no  se guardaba la información esto ocurría porque para guardar objetos personalizados en un archivo de texto se necesitaban serializar y deserializar esos objetos se solucionó utilizando el módulo "pickle" lo cual si permitía la serializacion y deserializacion de las listas, diccionarios u otro

# PRUEBAS



# CONCLUSIONES


# Luis Fernado Fabián Guzmán


En conclusión, el diseño del programa de recompensas se estructura de manera efectiva, aprovechando las relaciones de herencia y composición para ofrecer una gestión flexible de clientes, compañías socias y beneficios. Esta estructura proporciona una base sólida para adaptarse a futuras necesidades y garantiza una experiencia versátil y eficiente para los usuarios. El programa se enfoca en recompensar a los clientes en función de sus hábitos de compra y ofrece una categoría VIP con la capacidad de transferir beneficios, lo que mejora la satisfacción del cliente y promueve la fidelidad a las compañías socias.


# Erik Muñoz Rodríguez

En conclusión, este proyecto ha logrado diseñar e implementar con éxito un programa de recompensas que cumple con el objetivo planteado. Este sistema de gestión de recompensas se basa en un enfoque orientado a objetos que ha demostrado ser altamente efectivo en la gestión de clientes, compañías asociadas y beneficios. La estructura de clases y sus relaciones permiten una gestión flexible y escalable, mientras que la incorporación de herencia y composición ha sido fundamental para construir un sistema robusto y adaptable. Además, la capacidad de agregar nuevas funciones garantiza que el programa pueda evolucionar según las necesidades cambiantes. Este enfoque orientado a objetos está diseñado para mejorar la retención de clientes y fomentar la lealtad de una manera innovadora. El análisis del problema, el diseño UML y las contribuciones individuales han enriquecido de manera significativa este proyecto.
