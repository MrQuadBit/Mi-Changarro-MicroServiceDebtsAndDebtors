# Mi-Changarro-MicroServiceDebtsAndDebtors
Microservice biuld in python with flask

Universidad Autónoma Metropolitana
Unidad Cuajimalpa

Tecnologías y Sistemas de la Información
Trimestre 20-I

Integración de Sistemas
Christian Sánchez Sánchez

Proyecto Final
Microservicio con XML

Ayala De La Rosa José Daniel
2173071015

Contenido:

Título
Resumen
Introducción
Metodología
Propuesta
Conclusiones
Referencias bibliográficas














Introducción: 
En la UEA Integración de Sistemas vimos la importancia y dificultad que tiene crear un sistema pensando en que este mismo podría comunicarse con otros sistemas, que no necesariamente están escritos en el mismo lenguaje o se ejecutan en las misma plataformas, para estos problemas se crearon 2 técnicas importantes:
-La filosofía de no hacer programas gigantes que manejen todas las características de un problema a resolver en un sólo sistema, si no que se piense en dividir y vencer, así se podría partir el problema en pequeños sistemas o servicios donde cada uno de estos resuelve una particularidad del problema inicial.
-La forma en la cual se comunican los sistemas debe de ser una forma homogénea, donde todos los integrantes de la comunicación (sistemas intercambiando mensajes) hablen el mismo idioma, algo así como el inglés en nuestra época contemporánea, donde no importa a qué parte del mundo vayas, siempre podrás comunicarte siempre y cuando manejes el idioma.

La implementación de estas técnicas o filosofías las hicimos con una REST API para la parte de los microservicios y usamos XML como lenguaje de comunicación.

Para representar de una manera más clara el problema, usé la temática de mi proyecto de Interacción Humano Computadora (“Mi Changarro”)  el cual es un sistema que pretende ayudar a gestionar y administrar las finanzas de pequeños negocios.
(Si se quiere ver a fondo la idea del proyecto puede hacer click AQUÍ)

No es necesario profundizar en la temática así que explicaré por encima el funcionamiento y en la parte con la que nos enfocamos para la UEA de Integración de Sistemas:

“Mi changarro” ayuda a gestionar y administrar las finanzas de un un negocio por medio de registrar las actividades que se tienen durante el día, crea una lista de deudas / deudores y al finalizar el día se genera un reporte de cómo le fué al negocio de acuerdo a los datos ingresados.
Para esta UEA sólo usaremos la parte de deudas / deudores.

El servicio se basa en 4 Métodos HTTP:
GET: devuelve la lista entera de las personas que deben o les debes.
POST: recibe una nueva persona para agregar a la lista.
PATCH: recibe 2 personas, una persona que existe en la lista de personas y la persona con la que será reemplazada
DELETE: recibe la persona que será eliminada de la lista.

Este microservicio se hizo en Python usando el framework Flask y el cliente se hizo con las 3 tecnologías de la web (HTML, CSS y JavaScript) pero como es un microservicio, el cliente y su tecnología no son relevantes ya que debe de funcionar independientemente la plataforma o tecnología.

La interacción entre el microservicio y cualquier sistema que hable verbos / peticiones HTTP es la siguiente:

Siguiendo el siguiente proceso:
El cliente (cliente.html) hace una petición al servicio (debts_and_debtors.py), indicando el Método y enviando el debido archivo XML.
El servicio recibirá el XML y lo validará por medio de un DTD (persons.dtd), una vez validado regresará al cliente una respuesta si es que fue o no valido su XML (si está bien escrito o no de acuerdo al DTD).
De acuerdo al tipo de Método HTTP se hará lo siguiente:

GET: El servicio recibe una petición GET del cliente con o sin XML (es ignorado si se envía), abre el XML de almacenamiento (persons.xml), extrae todas las personas y lo envía como respuesta al cliente.

POST: El servicio recibe una petición POST con un XML, el servicio extrae sólo la etiqueta y su contenido de la persona (<person>), abre el XML de almacenamiento, lo agrega como último elemento y sobre escribe el XML de almacenamiento.

PATCH: El servicio recibe una petición PATCH con un XML que tenga al menos 2 personas, la primera debe de ser una persona ya existente y la segunda una con los datos que quieren ser actualizados, el servicio abre el XML de almacenamiento, verifica que existe la primer persona y cuando la encuentre, reemplazará todos los datos de la primer persona con los de la segunda persona, por último el servicio sobre escribirá el xml de almacenamiento.

DELETE: El servicio recibe una petición DELETE con un XML, abre el XML de almacenamiento, verifica que exista la persona proporcionada por el cliente, elimina la etiqueta que lo contenga junto con su contenido y sobre escribe el XML de almacenamiento.

Cómo ejecutar el proyecto:
Para obtener el proyecto puede descargarlo de github

