# Ejercicio 1: Automatización de seguimiento de clientes potenciales

## Objetivo
Crear un sistema automatizado que capture datos de clientes potenciales (leads) desde un formulario web, los almacene en Google Sheets y envíe emails de seguimiento personalizados.

## Tiempo estimado
45-60 minutos

## Requisitos previos
- Acceso a una instancia de n8n (local o en la nube)
- Credenciales de Google configuradas en n8n (ver ejercicio anterior)
- Credenciales de email configuradas en n8n (SMTP)
- Conocimientos básicos de HTML para el formulario web

## Pasos a seguir

### Paso 1: Configurar el formulario web
1. En n8n, crea un nuevo flujo de trabajo y nómbralo "Seguimiento de Leads"
2. Añade un nodo "Webhook" como disparador
3. Configura el webhook para recibir datos de un formulario web (método POST)
4. Haz clic en "Ejecutar flujo de trabajo" para activar el webhook
5. Copia la URL del webhook generada
6. Crea un formulario HTML simple que envíe datos a esta URL:

```html
<form action="https://tu-instancia-n8n.com/webhook/abc123" method="POST">
  <input type="text" name="nombre" placeholder="Nombre">
  <input type="email" name="email" placeholder="Email">
  <input type="submit" value="Enviar">
</form>
```

### Paso 2: Configurar Google Sheets
1. Crea una nueva hoja de cálculo en Google Sheets
2. Configura las siguientes columnas: ID, Nombre, Email, Fecha, Estado
3. En n8n, añade un nodo "Google Sheets" después del nodo Webhook
4. Configura el nodo para usar tus credenciales de Google
5. Selecciona la operación "Append" para añadir filas a la hoja
6. Configura los siguientes campos:
   - Hoja de cálculo: Selecciona tu hoja de cálculo creada
   - Hoja: Nombre de la hoja (por defecto "Hoja 1")
   - Datos: Mapea los datos del webhook a las columnas correspondientes
     - ID: Puedes usar una expresión como `{{$now}}` para generar un ID único
     - Nombre: `{{$node.Webhook.json.nombre}}`
     - Email: `{{$node.Webhook.json.email}}`
     - Fecha: `{{$now.toISOString().split('T')[0]}}`
     - Estado: "Nuevo"

### Paso 3: Configurar el email automático
1. En n8n, añade un nodo "IF" después del nodo Google Sheets
2. Configura la condición para verificar si el email es válido:
   - Condición: `{{$node.Webhook.json.email.includes('@')}}`
3. En la rama "true", añade un nodo "Send Email"
4. Configura el nodo con tus credenciales de email
5. Personaliza el mensaje de bienvenida:
   - Para: `{{$node.Webhook.json.email}}`
   - Asunto: "Bienvenido a nuestra lista"
   - Contenido: 
     ```
     Hola {{$node.Webhook.json.nombre}},

     Gracias por registrarte en nuestra lista. Pronto recibirás más información sobre nuestros productos y servicios.

     Saludos cordiales,
     El equipo
     ```

### Paso 4: Probar el flujo completo
1. Asegúrate de que todos los nodos estén correctamente configurados
2. Activa el flujo de trabajo haciendo clic en "Activar"
3. Envía datos de prueba al webhook usando el formulario web
4. Verifica que los datos se hayan añadido a Google Sheets
5. Comprueba que el email de bienvenida se haya enviado correctamente

## Resultado esperado
Al completar este ejercicio, tendrás un sistema automatizado que:
1. Captura datos de leads desde un formulario web
2. Almacena la información en Google Sheets para su seguimiento
3. Envía automáticamente un email de bienvenida personalizado
4. Filtra entradas inválidas mediante una condición

## Variaciones y experimentos
- Añade más campos al formulario (teléfono, intereses, etc.)
- Implementa una clasificación de leads basada en criterios específicos
- Configura diferentes plantillas de email según el tipo de lead
- Añade un nodo de notificación para alertar al equipo de ventas sobre nuevos leads
- Programa seguimientos automáticos después de cierto tiempo

## Solución de problemas
- Si el webhook no recibe datos, verifica que la URL sea correcta y que el formulario esté bien configurado
- Si los datos no se añaden a Google Sheets, comprueba las credenciales y los permisos
- Si los emails no se envían, verifica la configuración SMTP y las credenciales
- Utiliza los nodos "Debug" para ver el contenido de los datos en cada paso del flujo
