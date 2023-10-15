#ANALISIS DEL PROBLEMA


#DESCRIPCION DEL PROBLEMA


El problema se centra en la implementación de un programa de recompensas que permite a los clientes obtener beneficios de compañías asociadas según sus hábitos de compra. Además, se establece un criterio para otorgar la categoría VIP a los clientes que son miembros de cinco o más compañías, lo que les permite transferir beneficios entre compañías.


#REQUISITOS CLAVE


Los clientes pueden ser miembros de múltiples compañías socias.
Los beneficios se basan en los hábitos de compra de los clientes, donde mayores compras significan mayores beneficios.
Los clientes VIP pueden transferir beneficios entre compañías.
Debe haber un mecanismo para agregar nuevas compañías socias y clientes.


#ENTIDADES CLAVE


Cliente: Representa a los clientes que son miembros del programa de recompensas. Pueden ser clientes normales o VIP.
Compañía Socia: Representa a las compañías que participan en el programa de recompensas y ofrecen beneficios a los clientes.
Beneficio: Los beneficios ofrecidos por las compañías a los clientes en función de sus hábitos de compra.
Programa de Recompensas: El sistema que gestiona a los clientes, las compañías socias y los beneficios.


#DISEÑO DE LA SOLUCION


#CLASE CLIENTE


La clase Cliente representa a un cliente del programa de recompensas. Un cliente tiene un nombre y una lista de afiliaciones que indican a qué compañías está asociado. El constructor __init__ inicializa un nuevo objeto Cliente con un nombre y una lista de afiliaciones (que se inicializa como una lista vacía por defecto). La clase también tiene un método agregar_compania_afiliada para permitir la adición de compañías afiliadas a la lista del cliente. El método __str__ proporciona una representación en cadena del objeto, mostrando el nombre del cliente y las compañías a las que está afiliado.

Img1


#CLASE CLIENTEVIP

La clase ClienteVIP hereda de la clase Cliente y agrega la funcionalidad adicional para clientes que alcanzan la categoría VIP al ser miembros de cinco o más compañías socias del programa. Además, los clientes VIP tienen la capacidad de transferir beneficios entre compañías. Esto se logra a través de los métodos agregar_beneficio_transferible y quitar_beneficio_transferible para agregar o eliminar beneficios transferibles, y el método transferir_beneficios para transferir un beneficio de una compañía a otra.

IMG_2


#CLASE COMPANIASOCIA


La clase CompaniaSocia representa a una compañía socia del programa de recompensas. Cada compañía tiene un nombre y ofrece una lista de beneficios a sus clientes, los cuales están asociados a la compañía. Los beneficios incluyen una descripción y un requisito de gasto. La compañía permite agregar beneficios a través del método agregar_beneficio, y transferir beneficios a otras compañías a través del método transferir_beneficio.

IMG_3



#CLASE PROGRAMARECOMPENSAS


La clase ProgramaRecompensas interactúa con todas las demás clases para gestionar el programa de recompensas, permitiendo a los clientes registrarse, obtener beneficios, transferir beneficios y realizar operaciones de guardado y carga de información. También tiene una relación de agregación con las clases Cliente y ClienteVIP, ya que contiene listas de clientes y clientes VIP registrados en el programa.

IMG_4


#CLASE MAIN


Sirve como punto de entrada para el programa de recompensas. La clase Main instancia un objeto de ProgramaRecompensas y proporciona un menú principal que permite a los usuarios (clientes o administradores) seleccionar diferentes opciones. Los usuarios pueden gestionar sus cuentas, autenticarse como administradores, ver información y salir del programa. La funcionalidad del programa se basa en el uso de métodos y clases previamente definidos, proporcionando una interfaz de usuario intuitiva y fácil de usar.

IMG_5

#CLASE MENUS


La clase Menu proporciona un sistema de menús que permite a los usuarios (clientes y administradores) seleccionar diferentes opciones. Contiene submenús para trabajar con clientes, beneficios, compañías y clientes VIP, así como un menú principal para el administrador. Estos menús facilitan la interacción de los usuarios con las funciones del programa.
 
IMG_6


#RELACIONES ENTRE CLASES 


La clase Cliente tiene una relación de asociación con la clase CompaniaSocia a través de la lista de afiliaciones, ya que un cliente está afiliado a una o más compañías.


La clase ClienteVIP hereda de la clase Cliente, lo que indica una relación de herencia. Además, tiene una relación de asociación con la clase CompaniaSocia para gestionar los beneficios transferibles.


La clase CompaniaSocia tiene una relación de asociación con la clase Cliente, ya que cada compañía tiene una lista de clientes afiliados. También tiene una relación de asociación con la clase ClienteVIP para transferir beneficios.


La clase ProgramaRecompensas interactúa con todas las demás clases para gestionar el programa de recompensas, permitiendo a los clientes registrarse, obtener beneficios, transferir beneficios y realizar operaciones de guardado y carga de información. También tiene una relación de agregación con las clases Cliente y ClienteVIP, ya que contiene listas de clientes y clientes VIP registrados en el programa.


La clase Main tiene una relación de asociación con la clase ProgramaRecompensas debido a que Main necesita interactuar con ProgramaRecompensas para llevar a cabo su funcionalidad. Esta asociación se debe a que Main crea una instancia de ProgramaRecompensas en su constructor y utiliza esta instancia para acceder a los métodos y atributos de ProgramaRecompensas.


La clase Menu tiene una relación de asociación con la clase ProgramaRecompensas y la clase Main. La relación con la clase ProgramaRecompensas se debe a que Menu utiliza una instancia de ProgramaRecompensas para interactuar con los datos y realizar operaciones basadas en las opciones seleccionadas por el usuario. Además, la relación con la clase Main se debe a que Menu es una parte fundamental de la lógica de Main y se utiliza para proporcionar opciones de menú y gestionar las interacciones del usuario dentro de la aplicación global.

IMG_7


#CONCLUSIONES


Luis Fernado Fabián Guzmán


En conclusión, el diseño del programa de recompensas se estructura de manera efectiva, aprovechando las relaciones de herencia y composición para ofrecer una gestión flexible de clientes, compañías socias y beneficios. Esta estructura proporciona una base sólida para adaptarse a futuras necesidades y garantiza una experiencia versátil y eficiente para los usuarios. El programa se enfoca en recompensar a los clientes en función de sus hábitos de compra y ofrece una categoría VIP con la capacidad de transferir beneficios, lo que mejora la satisfacción del cliente y promueve la fidelidad a las compañías socias.


Erik Muñoz Rodríguez

En conclusión, este proyecto ha logrado diseñar e implementar con éxito un programa de recompensas que cumple con el objetivo planteado. Este sistema de gestión de recompensas se basa en un enfoque orientado a objetos que ha demostrado ser altamente efectivo en la gestión de clientes, compañías asociadas y beneficios. La estructura de clases y sus relaciones permiten una gestión flexible y escalable, mientras que la incorporación de herencia y composición ha sido fundamental para construir un sistema robusto y adaptable. Además, la capacidad de agregar nuevas funciones garantiza que el programa pueda evolucionar según las necesidades cambiantes. Este enfoque orientado a objetos está diseñado para mejorar la retención de clientes y fomentar la lealtad de una manera innovadora. El análisis del problema, el diseño UML y las contribuciones individuales han enriquecido de manera significativa este proyecto.
