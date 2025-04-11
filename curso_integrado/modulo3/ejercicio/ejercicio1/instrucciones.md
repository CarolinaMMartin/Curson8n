# Ejercicio 1: Configuración de credenciales para Google Sheets

## Objetivo
Configurar las credenciales OAuth necesarias para conectar n8n con Google Sheets, permitiendo la integración con hojas de cálculo de Google.

## Tiempo estimado
20-30 minutos

## Requisitos previos
- Acceso a una instancia de n8n (local o en la nube)
- Una cuenta de Google
- Conocimientos básicos de navegación web

## Pasos a seguir

### Paso 1: Crear un proyecto en Google Cloud Console
1. Ve a console.cloud.google.com e inicia sesión con tu cuenta de Google
2. En la barra superior, haz clic en el selector de proyectos
3. Haz clic en "Nuevo proyecto"
4. Asigna un nombre al proyecto (por ejemplo, "n8n-integration")
5. Haz clic en "Crear"

### Paso 2: Activar las APIs necesarias
1. En el menú de navegación izquierdo, selecciona "APIs y servicios" > "Biblioteca"
2. Busca "Google Sheets API" y selecciónala
3. Haz clic en "Habilitar"
4. Regresa a la biblioteca y busca "Google Drive API"
5. Haz clic en "Habilitar"

### Paso 3: Configurar la pantalla de consentimiento OAuth
1. En el menú de navegación, selecciona "APIs y servicios" > "Pantalla de consentimiento"
2. Selecciona "Externo" como tipo de usuario y haz clic en "Crear"
3. Completa la información requerida:
   - Nombre de la aplicación: "n8n Integration"
   - Correo electrónico de soporte: tu dirección de correo
4. Haz clic en "Guardar y continuar"
5. En la sección de ámbitos, haz clic en "Guardar y continuar" sin añadir ámbitos adicionales
6. En la sección de usuarios de prueba, haz clic en "Guardar y continuar" sin añadir usuarios
7. Revisa la configuración y haz clic en "Volver al panel"

### Paso 4: Crear credenciales OAuth 2.0
1. En el menú de navegación, selecciona "APIs y servicios" > "Credenciales"
2. Haz clic en "+ Crear credenciales" y selecciona "ID de cliente de OAuth"
3. Selecciona "Aplicación web" como tipo de aplicación
4. Asigna un nombre (por ejemplo, "n8n Client")
5. En "URI de redirección autorizados", añade: https://tu-instancia-n8n.com/oauth2/callback
   (Reemplaza "tu-instancia-n8n.com" con la URL real de tu instancia de n8n)
6. Haz clic en "Crear"

### Paso 5: Obtener Client ID y Client Secret
1. Después de crear las credenciales, se mostrará una ventana con el Client ID y Client Secret
2. Copia y guarda ambos valores en un lugar seguro
3. También puedes acceder a estos valores más tarde desde la sección "Credenciales"

### Paso 6: Configurar credenciales en n8n
1. Inicia sesión en tu instancia de n8n
2. Haz clic en el icono de usuario en la esquina superior derecha
3. Selecciona "Credenciales" en el menú desplegable
4. Haz clic en "+ Añadir nueva credencial"
5. Selecciona "Google Sheets" como tipo de credencial
6. Introduce el Client ID y Client Secret que obtuviste anteriormente
7. Haz clic en "Crear" y luego en "Conectar"

### Paso 7: Autorizar el acceso
1. Después de hacer clic en "Conectar", se abrirá una ventana de Google
2. Inicia sesión con tu cuenta de Google si aún no lo has hecho
3. Revisa los permisos solicitados
4. Haz clic en "Permitir" para autorizar a n8n a acceder a tus hojas de cálculo
5. Serás redirigido de vuelta a n8n con la conexión establecida

## Resultado esperado
Al completar este ejercicio, deberías tener configuradas las credenciales de Google Sheets en n8n, lo que te permitirá acceder y manipular hojas de cálculo de Google en tus flujos de trabajo.

## Solución de problemas

### Error "App no verificada"
Si recibes un aviso de "App no verificada", haz clic en "Avanzado" y luego en "Ir a n8n Integration (no seguro)". Esto es normal para aplicaciones en desarrollo.

### Error de redirección
Si recibes un error de redirección, asegúrate de que la URI de redirección en Google Cloud Console coincida exactamente con la URL de tu instancia de n8n, incluyendo el protocolo (http/https) y la ruta "/oauth2/callback".

### Error de ámbitos
Si recibes un error relacionado con los ámbitos, asegúrate de haber habilitado correctamente tanto la API de Google Sheets como la API de Google Drive.

## Próximos pasos
Una vez configuradas las credenciales, puedes:
- Crear un flujo de trabajo que lea datos de una hoja de cálculo de Google
- Crear un flujo de trabajo que escriba datos en una hoja de cálculo de Google
- Explorar las diferentes operaciones disponibles en el nodo de Google Sheets
