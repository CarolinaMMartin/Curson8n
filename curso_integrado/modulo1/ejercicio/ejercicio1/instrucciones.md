# Ejercicio 1: Creación de un flujo "Hola Mundo"

## Objetivo
Crear tu primer flujo de trabajo en n8n que muestre el mensaje "¡Hola Mundo!" cuando se active manualmente.

## Tiempo estimado
10-15 minutos

## Requisitos previos
- Acceso a una instancia de n8n (local o en la nube)
- Conocimientos básicos de navegación web

## Pasos a seguir

### Paso 1: Crear un nuevo flujo de trabajo
1. Inicia sesión en tu instancia de n8n
2. En el panel de navegación izquierdo, haz clic en "Flujos de trabajo"
3. Haz clic en el botón "+ Nuevo" en la esquina superior derecha
4. Se abrirá un nuevo flujo de trabajo en blanco
5. Haz clic en "Guardar" y asigna un nombre: "Hola Mundo"

### Paso 2: Añadir un nodo de activación manual
1. Haz clic en el botón "+" en el centro del área de trabajo
2. En el panel de búsqueda, escribe "manual"
3. Selecciona el nodo "Manual Trigger"
4. El nodo se añadirá al área de trabajo

### Paso 3: Añadir un nodo Set
1. Haz clic en el botón "+" que aparece a la derecha del nodo Manual Trigger
2. En el panel de búsqueda, escribe "set"
3. Selecciona el nodo "Set"
4. El nodo se añadirá y se conectará automáticamente

### Paso 4: Configurar el nodo Set
1. Haz clic en el nodo "Set" para abrir su panel de configuración
2. En la sección "Valores a establecer", haz clic en "Añadir valor"
3. En "Nombre", escribe "mensaje"
4. En "Valor", escribe "¡Hola Mundo!"
5. Haz clic en "Cerrar" para guardar la configuración

### Paso 5: Ejecutar el flujo
1. Haz clic en el botón "Ejecutar" en la barra superior
2. Selecciona el nodo "Manual Trigger" para activar el flujo
3. Observa cómo se ejecuta el flujo y los datos pasan de un nodo a otro
4. Haz clic en el nodo "Set" para ver el resultado final

## Resultado esperado
Al ejecutar el flujo, deberías ver que el nodo Set produce un objeto JSON con la propiedad "mensaje" que contiene el texto "¡Hola Mundo!".

## Variaciones y experimentos
- Modifica el mensaje para que diga algo diferente
- Añade más valores al nodo Set (por ejemplo, "fecha", "autor", etc.)
- Intenta añadir un tercer nodo que utilice el mensaje (como un nodo "Respond to Webhook")

## Puntos de reflexión
- ¿Qué representa cada nodo en el flujo de trabajo?
- ¿Cómo fluyen los datos de un nodo a otro?
- ¿Qué otros tipos de nodos podrías utilizar para ampliar este flujo?

## Solución de problemas
- Si no ves el resultado esperado, verifica que hayas configurado correctamente el nodo Set
- Asegúrate de que los nodos estén conectados correctamente
- Comprueba que no haya errores en la ejecución del flujo
