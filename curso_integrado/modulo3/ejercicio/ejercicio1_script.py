"""
Script para generar materiales para el Ejercicio 1 del Módulo 3: Configuración de credenciales para Google Sheets
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/ejercicios_interactivos/modulo3/ejercicio1'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_n8n = '#FF6D00'          # Naranja n8n
color_google = '#0F9D58'       # Verde Google
color_sheets = '#0F9D58'       # Verde para Sheets
color_conexion = '#9E9E9E'     # Gris para conexiones
color_resaltado = '#FFC107'    # Amarillo para resaltados
color_exito = '#4CAF50'        # Verde para éxito
color_error = '#F44336'        # Rojo para error

# Función para crear imagen base
def crear_imagen_base(width=1200, height=800, titulo="Ejercicio 1: Configuración de credenciales para Google Sheets"):
    img = Image.new('RGB', (width, height), color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Título
    try:
        font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    except OSError:
        font_title = ImageFont.load_default()
    
    draw.text((width//2, 50), titulo, fill=color_texto, font=font_title, anchor="mm")
    
    return img, draw, width, height

# Cargar fuentes
try:
    font_subtitle = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    font_text = ImageFont.truetype("DejaVuSans.ttf", 18)
    font_small = ImageFont.truetype("DejaVuSans.ttf", 14)
except OSError:
    font_subtitle = ImageFont.load_default()
    font_text = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Paso 1: Introducción al ejercicio
img1, draw1, width, height = crear_imagen_base(titulo="Ejercicio 1: Configuración de credenciales para Google Sheets")

# Subtítulo
draw1.text((width//2, 100), "Objetivo: Configurar credenciales OAuth para conectar n8n con Google Sheets", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Descripción del ejercicio
descripcion = [
    "En este ejercicio, configurarás las credenciales OAuth necesarias para conectar n8n",
    "con Google Sheets. Aprenderás a:",
    "",
    "• Crear un proyecto en Google Cloud Console",
    "• Activar las APIs necesarias",
    "• Configurar la pantalla de consentimiento OAuth",
    "• Crear credenciales OAuth 2.0",
    "• Configurar las credenciales en n8n"
]

y_pos = 160
for linea in descripcion:
    draw1.text((width//2, y_pos), linea, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 30

# Diagrama del proceso
proceso_y = 400
box_width = 180
box_height = 80
spacing = 50

# Paso 1: Google Cloud Console
paso1_x = width//4
draw1.rounded_rectangle([(paso1_x-box_width//2, proceso_y-box_height//2), 
                        (paso1_x+box_width//2, proceso_y+box_height//2)], 
                       radius=10, fill='white', outline=color_google)
draw1.text((paso1_x, proceso_y-15), "Google Cloud", fill=color_google, font=font_text, anchor="mm")
draw1.text((paso1_x, proceso_y+15), "Console", fill=color_google, font=font_text, anchor="mm")

# Paso 2: Crear Credenciales
paso2_x = width//2
draw1.rounded_rectangle([(paso2_x-box_width//2, proceso_y-box_height//2), 
                        (paso2_x+box_width//2, proceso_y+box_height//2)], 
                       radius=10, fill='white', outline=color_google)
draw1.text((paso2_x, proceso_y-15), "Crear", fill=color_google, font=font_text, anchor="mm")
draw1.text((paso2_x, proceso_y+15), "Credenciales", fill=color_google, font=font_text, anchor="mm")

# Paso 3: Configurar en n8n
paso3_x = 3*width//4
draw1.rounded_rectangle([(paso3_x-box_width//2, proceso_y-box_height//2), 
                        (paso3_x+box_width//2, proceso_y+box_height//2)], 
                       radius=10, fill='white', outline=color_n8n)
draw1.text((paso3_x, proceso_y-15), "Configurar en", fill=color_n8n, font=font_text, anchor="mm")
draw1.text((paso3_x, proceso_y+15), "n8n", fill=color_n8n, font=font_text, anchor="mm")

# Flechas entre pasos
draw1.line([(paso1_x+box_width//2, proceso_y), (paso2_x-box_width//2, proceso_y)], 
          fill=color_conexion, width=3)
draw1.polygon([(paso2_x-box_width//2, proceso_y), 
              (paso2_x-box_width//2-10, proceso_y-5), 
              (paso2_x-box_width//2-10, proceso_y+5)], 
             fill=color_conexion)

draw1.line([(paso2_x+box_width//2, proceso_y), (paso3_x-box_width//2, proceso_y)], 
          fill=color_conexion, width=3)
draw1.polygon([(paso3_x-box_width//2, proceso_y), 
              (paso3_x-box_width//2-10, proceso_y-5), 
              (paso3_x-box_width//2-10, proceso_y+5)], 
             fill=color_conexion)

# Resultado final
resultado_y = 550
draw1.rounded_rectangle([(width//2-250, resultado_y-50), (width//2+250, resultado_y+50)], 
                       radius=10, fill='#E8F5E9', outline=color_exito)
draw1.text((width//2, resultado_y-20), "Resultado:", fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, resultado_y+20), "¡Conexión establecida con Google Sheets!", 
          fill=color_exito, font=font_text, anchor="mm")

# Instrucciones para comenzar
draw1.text((width//2, 650), "Para comenzar, necesitarás una cuenta de Google y acceso a n8n", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, 680), "Tiempo estimado: 20-30 minutos", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la primera imagen
img1.save(os.path.join(output_dir, 'paso1_introduccion.png'))

# Paso 2: Crear un proyecto en Google Cloud Console
img2, draw2, width, height = crear_imagen_base(titulo="Paso 2: Crear un proyecto en Google Cloud Console")

# Instrucciones
draw2.text((width//2, 100), "Crea un nuevo proyecto en Google Cloud Console", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Ve a console.cloud.google.com e inicia sesión con tu cuenta de Google",
    "2. En la barra superior, haz clic en el selector de proyectos",
    "3. Haz clic en 'Nuevo proyecto'",
    "4. Asigna un nombre al proyecto (por ejemplo, 'n8n-integration')",
    "5. Haz clic en 'Crear'"
]

y_pos = 160
for paso in pasos:
    draw2.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de Google Cloud Console
interfaz_y = 400
interfaz_width = 700
interfaz_height = 300

# Fondo de la interfaz
draw2.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='white', outline=color_texto)

# Barra superior
draw2.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#4285F4', outline=color_texto)
draw2.text((width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+20), 
          "Google Cloud Console", fill='white', font=font_text, anchor="mm")

# Selector de proyectos (resaltado)
selector_x = width//2-interfaz_width//2+300
selector_y = interfaz_y-interfaz_height//2+20
draw2.rounded_rectangle([(selector_x-100, selector_y-15), 
                        (selector_x+100, selector_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw2.text((selector_x, selector_y), "Seleccionar proyecto ▼", 
          fill=color_texto, font=font_text, anchor="mm")

# Menú desplegable
menu_y = selector_y + 50
draw2.rounded_rectangle([(selector_x-100, menu_y-40), 
                        (selector_x+100, menu_y+40)], 
                       radius=5, fill='white', outline=color_texto)
draw2.text((selector_x, menu_y-20), "Mi Proyecto", 
          fill=color_texto, font=font_small, anchor="mm")
draw2.line([(selector_x-90, menu_y), (selector_x+90, menu_y)], 
          fill=color_texto, width=1)
draw2.text((selector_x, menu_y+20), "Nuevo proyecto", 
          fill=color_resaltado, font=font_small, anchor="mm")

# Diálogo de nuevo proyecto
dialogo_x = width//2
dialogo_y = interfaz_y + 50
dialogo_width = 400
dialogo_height = 200
draw2.rounded_rectangle([(dialogo_x-dialogo_width//2, dialogo_y-dialogo_height//2), 
                        (dialogo_x+dialogo_width//2, dialogo_y+dialogo_height//2)], 
                       radius=10, fill='white', outline=color_texto)

# Título del diálogo
draw2.rectangle([(dialogo_x-dialogo_width//2, dialogo_y-dialogo_height//2), 
                (dialogo_x+dialogo_width//2, dialogo_y-dialogo_height//2+40)], 
               fill='#4285F4', outline=color_texto)
draw2.text((dialogo_x, dialogo_y-dialogo_height//2+20), "Nuevo proyecto", 
          fill='white', font=font_text, anchor="mm")

# Contenido del diálogo
draw2.text((dialogo_x-dialogo_width//2+30, dialogo_y-dialogo_height//2+70), "Nombre del proyecto:", 
          fill=color_texto, font=font_small, anchor="lm")
draw2.rectangle([(dialogo_x-dialogo_width//2+30, dialogo_y-dialogo_height//2+90), 
                (dialogo_x+dialogo_width//2-30, dialogo_y-dialogo_height//2+120)], 
               fill='white', outline=color_texto)
draw2.text((dialogo_x-dialogo_width//2+40, dialogo_y-dialogo_height//2+105), "n8n-integration", 
          fill=color_texto, font=font_small, anchor="lm")

# Botón de crear (resaltado)
boton_crear_x = dialogo_x + dialogo_width//2 - 80
boton_crear_y = dialogo_y + dialogo_height//2 - 30
draw2.rounded_rectangle([(boton_crear_x-50, boton_crear_y-15), 
                        (boton_crear_x+50, boton_crear_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw2.text((boton_crear_x, boton_crear_y), "Crear", 
          fill=color_texto, font=font_text, anchor="mm")

# Consejos
draw2.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw2.text((width//2, 675), "Consejo: Anota el ID del proyecto, lo necesitarás más adelante", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la segunda imagen
img2.save(os.path.join(output_dir, 'paso2_crear_proyecto.png'))

# Paso 3: Activar las APIs necesarias
img3, draw3, width, height = crear_imagen_base(titulo="Paso 3: Activar las APIs necesarias")

# Instrucciones
draw3.text((width//2, 100), "Activa las APIs de Google Sheets y Google Drive", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. En el menú de navegación izquierdo, selecciona 'APIs y servicios' > 'Biblioteca'",
    "2. Busca 'Google Sheets API' y selecciónala",
    "3. Haz clic en 'Habilitar'",
    "4. Regresa a la biblioteca y busca 'Google Drive API'",
    "5. Haz clic en 'Habilitar'"
]

y_pos = 160
for paso in pasos:
    draw3.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de Google Cloud Console - Biblioteca de APIs
interfaz_y = 400
interfaz_width = 700
interfaz_height = 300

# Fondo de la interfaz
draw3.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='white', outline=color_texto)

# Barra superior
draw3.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#4285F4', outline=color_texto)
draw3.text((width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+20), 
          "Google Cloud Console", fill='white', font=font_text, anchor="mm")
draw3.text((width//2+100, interfaz_y-interfaz_height//2+20), 
          "Proyecto: n8n-integration", fill='white', font=font_small, anchor="mm")

# Panel izquierdo
draw3.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw3.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "APIs y servicios", fill=color_resaltado, font=font_small, anchor="mm")
draw3.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+100), 
          "Biblioteca", fill=color_resaltado, font=font_small, anchor="mm")

# Área principal - Biblioteca de APIs
draw3.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Barra de búsqueda
busqueda_y = interfaz_y-interfaz_height//2+70
draw3.rectangle([(width//2-interfaz_width//2+170, busqueda_y-15), 
                (width//2+interfaz_width//2-20, busqueda_y+15)], 
               fill='white', outline=color_texto)
draw3.text((width//2-interfaz_width//2+190, busqueda_y), "Google Sheets API", 
          fill=color_texto, font=font_small, anchor="lm")

# Resultados de búsqueda - Google Sheets API
api_sheets_y = interfaz_y
draw3.rounded_rectangle([(width//2-150, api_sheets_y-50), 
                        (width//2+150, api_sheets_y+50)], 
                       radius=5, fill='white', outline=color_sheets)
draw3.text((width//2, api_sheets_y-25), "Google Sheets API", 
          fill=color_sheets, font=font_text, anchor="mm")
draw3.text((width//2, api_sheets_y+10), "Accede y modifica hojas de cálculo", 
          fill=color_texto, font=font_small, anchor="mm")

# Botón de habilitar (resaltado)
boton_habilitar_x = width//2 + 100
boton_habilitar_y = api_sheets_y + 30
draw3.rounded_rectangle([(boton_habilitar_x-50, boton_habilitar_y-15), 
                        (boton_habilitar_x+50, boton_habilitar_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw3.text((boton_habilitar_x, boton_habilitar_y), "Habilitar", 
          fill=color_texto, font=font_text, anchor="mm")

# Consejos
draw3.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw3.text((width//2, 675), "Consejo: Necesitas habilitar ambas APIs para que funcione correctamente", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la tercera imagen
img3.save(os.path.join(output_dir, 'paso3_activar_apis.png'))

# Paso 4: Configurar la pantalla de consentimiento OAuth
img4, draw4, width, height = crear_imagen_base(titulo="Paso 4: Configurar la pantalla de consentimiento OAuth")

# Instrucciones
draw4.text((width//2, 100), "Configura la pantalla de consentimiento OAuth", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. En el menú de navegación, selecciona 'APIs y servicios' > 'Pantalla de consentimiento'",
    "2. Selecciona 'Externo' como tipo de usuario y haz clic en 'Crear'",
    "3. Completa la información requerida:",
    "   • Nombre de la aplicación: 'n8n Integration'",
    "   • Correo electrónico de soporte: tu dirección de correo",
    "4. Haz clic en 'Guardar y continuar'"
]

y_pos = 160
for paso in pasos:
    draw4.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de Google Cloud Console - Pantalla de consentimiento
interfaz_y = 400
interfaz_width = 700
interfaz_height = 300

# Fondo de la interfaz
draw4.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='white', outline=color_texto)

# Barra superior
draw4.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#4285F4', outline=color_texto)
draw4.text((width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+20), 
          "Google Cloud Console", fill='white', font=font_text, anchor="mm")
draw4.text((width//2+100, interfaz_y-interfaz_height//2+20), 
          "Proyecto: n8n-integration", fill='white', font=font_small, anchor="mm")

# Panel izquierdo
draw4.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw4.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "APIs y servicios", fill=color_resaltado, font=font_small, anchor="mm")
draw4.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+100), 
          "Pantalla de consentimiento", fill=color_resaltado, font=font_small, anchor="mm")

# Área principal - Formulario de consentimiento
draw4.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Título del formulario
draw4.text((width//2, interfaz_y-interfaz_height//2+70), 
          "Configurar pantalla de consentimiento OAuth", 
          fill=color_texto, font=font_text, anchor="mm")

# Selección de tipo de usuario
tipo_usuario_y = interfaz_y-interfaz_height//2+110
draw4.text((width//2-200, tipo_usuario_y), "Tipo de usuario:", 
          fill=color_texto, font=font_small, anchor="lm")

# Opción Interno
draw4.rectangle([(width//2-180, tipo_usuario_y+20), (width//2-160, tipo_usuario_y+40)], 
               fill='white', outline=color_texto)
draw4.text((width//2-150, tipo_usuario_y+30), "Interno", 
          fill=color_texto, font=font_small, anchor="lm")

# Opción Externo (seleccionada)
draw4.rectangle([(width//2+20, tipo_usuario_y+20), (width//2+40, tipo_usuario_y+40)], 
               fill=color_resaltado, outline=color_texto)
draw4.text((width//2+50, tipo_usuario_y+30), "Externo", 
          fill=color_texto, font=font_small, anchor="lm")

# Campos del formulario
form_y = interfaz_y
draw4.text((width//2-200, form_y), "Nombre de la aplicación:", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.rectangle([(width//2-200, form_y+20), (width//2+200, form_y+40)], 
               fill='white', outline=color_texto)
draw4.text((width//2-190, form_y+30), "n8n Integration", 
          fill=color_texto, font=font_small, anchor="lm")

draw4.text((width//2-200, form_y+60), "Correo electrónico de soporte:", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.rectangle([(width//2-200, form_y+80), (width//2+200, form_y+100)], 
               fill='white', outline=color_texto)
draw4.text((width//2-190, form_y+90), "tu.correo@ejemplo.com", 
          fill=color_texto, font=font_small, anchor="lm")

# Botón de guardar y continuar (resaltado)
boton_guardar_x = width//2
boton_guardar_y = interfaz_y+interfaz_height//2-30
draw4.rounded_rectangle([(boton_guardar_x-100, boton_guardar_y-15), 
                        (boton_guardar_x+100, boton_guardar_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw4.text((boton_guardar_x, boton_guardar_y), "Guardar y continuar", 
          fill=color_texto, font=font_text, anchor="mm")

# Consejos
draw4.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw4.text((width//2, 675), "Consejo: No necesitas añadir dominios ni ámbitos adicionales para este ejercicio", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la cuarta imagen
img4.save(os.path.join(output_dir, 'paso4_pantalla_consentimiento.png'))

# Paso 5: Crear credenciales OAuth 2.0
img5, draw5, width, height = crear_imagen_base(titulo="Paso 5: Crear credenciales OAuth 2.0")

# Instrucciones
draw5.text((width//2, 100), "Crea las credenciales OAuth 2.0", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. En el menú de navegación, selecciona 'APIs y servicios' > 'Credenciales'",
    "2. Haz clic en '+ Crear credenciales' y selecciona 'ID de cliente de OAuth'",
    "3. Selecciona 'Aplicación web' como tipo de aplicación",
    "4. Asigna un nombre (por ejemplo, 'n8n Client')",
    "5. En 'URI de redirección autorizados', añade: https://tu-instancia-n8n.com/oauth2/callback",
    "6. Haz clic en 'Crear'"
]

y_pos = 160
for paso in pasos:
    draw5.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de Google Cloud Console - Credenciales
interfaz_y = 400
interfaz_width = 700
interfaz_height = 300

# Fondo de la interfaz
draw5.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='white', outline=color_texto)

# Barra superior
draw5.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#4285F4', outline=color_texto)
draw5.text((width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+20), 
          "Google Cloud Console", fill='white', font=font_text, anchor="mm")
draw5.text((width//2+100, interfaz_y-interfaz_height//2+20), 
          "Proyecto: n8n-integration", fill='white', font=font_small, anchor="mm")

# Panel izquierdo
draw5.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw5.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "APIs y servicios", fill=color_resaltado, font=font_small, anchor="mm")
draw5.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+100), 
          "Credenciales", fill=color_resaltado, font=font_small, anchor="mm")

# Área principal - Formulario de credenciales
draw5.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Título del formulario
draw5.text((width//2, interfaz_y-interfaz_height//2+70), 
          "Crear ID de cliente de OAuth", 
          fill=color_texto, font=font_text, anchor="mm")

# Campos del formulario
form_y = interfaz_y-80
draw5.text((width//2-200, form_y), "Tipo de aplicación:", 
          fill=color_texto, font=font_small, anchor="lm")
draw5.rounded_rectangle([(width//2-200, form_y+20), (width//2+200, form_y+40)], 
                       radius=5, fill='white', outline=color_texto)
draw5.text((width//2-190, form_y+30), "Aplicación web", 
          fill=color_texto, font=font_small, anchor="lm")

draw5.text((width//2-200, form_y+60), "Nombre:", 
          fill=color_texto, font=font_small, anchor="lm")
draw5.rectangle([(width//2-200, form_y+80), (width//2+200, form_y+100)], 
               fill='white', outline=color_texto)
draw5.text((width//2-190, form_y+90), "n8n Client", 
          fill=color_texto, font=font_small, anchor="lm")

draw5.text((width//2-200, form_y+120), "URI de redirección autorizados:", 
          fill=color_texto, font=font_small, anchor="lm")
draw5.rectangle([(width//2-200, form_y+140), (width//2+200, form_y+160)], 
               fill='white', outline=color_texto)
draw5.text((width//2-190, form_y+150), "https://tu-instancia-n8n.com/oauth2/callback", 
          fill=color_texto, font=font_small, anchor="lm")

# Botón de crear (resaltado)
boton_crear_x = width//2
boton_crear_y = interfaz_y+interfaz_height//2-30
draw5.rounded_rectangle([(boton_crear_x-50, boton_crear_y-15), 
                        (boton_crear_x+50, boton_crear_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw5.text((boton_crear_x, boton_crear_y), "Crear", 
          fill=color_texto, font=font_text, anchor="mm")

# Consejos
draw5.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw5.text((width//2, 675), "Consejo: Reemplaza la URL con la dirección real de tu instancia de n8n", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la quinta imagen
img5.save(os.path.join(output_dir, 'paso5_crear_credenciales.png'))

# Paso 6: Obtener Client ID y Client Secret
img6, draw6, width, height = crear_imagen_base(titulo="Paso 6: Obtener Client ID y Client Secret")

# Instrucciones
draw6.text((width//2, 100), "Obtén y guarda el Client ID y Client Secret", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Después de crear las credenciales, se mostrará una ventana con el Client ID y Client Secret",
    "2. Copia y guarda ambos valores en un lugar seguro",
    "3. También puedes acceder a estos valores más tarde desde la sección 'Credenciales'",
    "4. Necesitarás estos valores para configurar la conexión en n8n"
]

y_pos = 160
for paso in pasos:
    draw6.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de Google Cloud Console - Credenciales creadas
interfaz_y = 400
interfaz_width = 600
interfaz_height = 250

# Fondo de la interfaz (diálogo de credenciales)
draw6.rounded_rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                        (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
                       radius=10, fill='white', outline=color_texto)

# Título del diálogo
draw6.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#4285F4', outline=color_texto)
draw6.text((width//2, interfaz_y-interfaz_height//2+20), "Credenciales OAuth creadas", 
          fill='white', font=font_text, anchor="mm")

# Contenido del diálogo
draw6.text((width//2, interfaz_y-interfaz_height//2+70), 
          "Tus credenciales OAuth 2.0 han sido creadas", 
          fill=color_texto, font=font_text, anchor="mm")

# Client ID
client_id_y = interfaz_y-20
draw6.text((width//2-interfaz_width//2+50, client_id_y), "Client ID:", 
          fill=color_texto, font=font_text, anchor="lm")
draw6.rounded_rectangle([(width//2-interfaz_width//2+150, client_id_y-20), 
                        (width//2+interfaz_width//2-50, client_id_y+20)], 
                       radius=5, fill='#f0f0f0', outline=color_texto)
draw6.text((width//2-interfaz_width//2+160, client_id_y), 
          "123456789012-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com", 
          fill=color_texto, font=font_small, anchor="lm")

# Client Secret
client_secret_y = interfaz_y+30
draw6.text((width//2-interfaz_width//2+50, client_secret_y), "Client Secret:", 
          fill=color_texto, font=font_text, anchor="lm")
draw6.rounded_rectangle([(width//2-interfaz_width//2+150, client_secret_y-20), 
                        (width//2+interfaz_width//2-50, client_secret_y+20)], 
                       radius=5, fill='#f0f0f0', outline=color_texto)
draw6.text((width//2-interfaz_width//2+160, client_secret_y), 
          "GOCSPX-abcdefghijklmnopqrstuvwxyz", 
          fill=color_texto, font=font_small, anchor="lm")

# Botón de cerrar
boton_cerrar_x = width//2
boton_cerrar_y = interfaz_y+interfaz_height//2-30
draw6.rounded_rectangle([(boton_cerrar_x-50, boton_cerrar_y-15), 
                        (boton_cerrar_x+50, boton_cerrar_y+15)], 
                       radius=5, fill='#4285F4', outline=color_texto)
draw6.text((boton_cerrar_x, boton_cerrar_y), "Cerrar", 
          fill='white', font=font_text, anchor="mm")

# Consejos
draw6.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw6.text((width//2, 675), "Consejo: Nunca compartas tu Client Secret con nadie", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la sexta imagen
img6.save(os.path.join(output_dir, 'paso6_obtener_credenciales.png'))

# Paso 7: Configurar credenciales en n8n
img7, draw7, width, height = crear_imagen_base(titulo="Paso 7: Configurar credenciales en n8n")

# Instrucciones
draw7.text((width//2, 100), "Configura las credenciales en n8n", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Inicia sesión en tu instancia de n8n",
    "2. Haz clic en el icono de usuario en la esquina superior derecha",
    "3. Selecciona 'Credenciales' en el menú desplegable",
    "4. Haz clic en '+ Añadir nueva credencial'",
    "5. Selecciona 'Google Sheets' como tipo de credencial",
    "6. Introduce el Client ID y Client Secret que obtuviste anteriormente",
    "7. Haz clic en 'Crear' y luego en 'Conectar'"
]

y_pos = 160
for paso in pasos:
    draw7.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 30

# Interfaz simplificada de n8n - Configuración de credenciales
interfaz_y = 400
interfaz_width = 700
interfaz_height = 300

# Fondo de la interfaz
draw7.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='white', outline=color_texto)

# Barra superior
draw7.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#333333', outline=color_texto)
draw7.text((width//2-interfaz_width//2+100, interfaz_y-interfaz_height//2+20), 
          "n8n - Credenciales", fill='white', font=font_text, anchor="mm")

# Formulario de credenciales
form_y = interfaz_y-50
draw7.text((width//2-250, form_y), "Tipo de credencial:", 
          fill=color_texto, font=font_text, anchor="lm")
draw7.rounded_rectangle([(width//2-250, form_y+20), (width//2+250, form_y+50)], 
                       radius=5, fill='white', outline=color_texto)
draw7.text((width//2-240, form_y+35), "Google Sheets", 
          fill=color_texto, font=font_text, anchor="lm")

# Client ID
client_id_y = form_y+80
draw7.text((width//2-250, client_id_y), "Client ID:", 
          fill=color_texto, font=font_text, anchor="lm")
draw7.rounded_rectangle([(width//2-250, client_id_y+20), (width//2+250, client_id_y+50)], 
                       radius=5, fill='white', outline=color_texto)
draw7.text((width//2-240, client_id_y+35), 
          "123456789012-abcdefg...apps.googleusercontent.com", 
          fill=color_texto, font=font_small, anchor="lm")

# Client Secret
client_secret_y = client_id_y+80
draw7.text((width//2-250, client_secret_y), "Client Secret:", 
          fill=color_texto, font=font_text, anchor="lm")
draw7.rounded_rectangle([(width//2-250, client_secret_y+20), (width//2+250, client_secret_y+50)], 
                       radius=5, fill='white', outline=color_texto)
draw7.text((width//2-240, client_secret_y+35), 
          "GOCSPX-abcdefghijklmnopqrstuvwxyz", 
          fill=color_texto, font=font_small, anchor="lm")

# Botones
boton_y = interfaz_y+interfaz_height//2-30

# Botón de crear
boton_crear_x = width//2-80
draw7.rounded_rectangle([(boton_crear_x-60, boton_y-15), 
                        (boton_crear_x+60, boton_y+15)], 
                       radius=5, fill=color_n8n, outline=color_texto)
draw7.text((boton_crear_x, boton_y), "Crear", 
          fill='white', font=font_text, anchor="mm")

# Botón de conectar
boton_conectar_x = width//2+80
draw7.rounded_rectangle([(boton_conectar_x-60, boton_y-15), 
                        (boton_conectar_x+60, boton_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw7.text((boton_conectar_x, boton_y), "Conectar", 
          fill=color_texto, font=font_text, anchor="mm")

# Consejos
draw7.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw7.text((width//2, 675), "Consejo: Al hacer clic en 'Conectar', se abrirá una ventana de Google para autorizar el acceso", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la séptima imagen
img7.save(os.path.join(output_dir, 'paso7_configurar_n8n.png'))

# Paso 8: Autorizar el acceso
img8, draw8, width, height = crear_imagen_base(titulo="Paso 8: Autorizar el acceso")

# Instrucciones
draw8.text((width//2, 100), "Autoriza el acceso a tu cuenta de Google", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Después de hacer clic en 'Conectar', se abrirá una ventana de Google",
    "2. Inicia sesión con tu cuenta de Google si aún no lo has hecho",
    "3. Revisa los permisos solicitados",
    "4. Haz clic en 'Permitir' para autorizar a n8n a acceder a tus hojas de cálculo",
    "5. Serás redirigido de vuelta a n8n con la conexión establecida"
]

y_pos = 160
for paso in pasos:
    draw8.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de Google - Pantalla de autorización
interfaz_y = 400
interfaz_width = 500
interfaz_height = 350

# Fondo de la interfaz
draw8.rounded_rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                        (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
                       radius=10, fill='white', outline=color_texto)

# Encabezado de Google
draw8.text((width//2, interfaz_y-interfaz_height//2+30), "Google", 
          fill='#4285F4', font=font_subtitle, anchor="mm")

# Título de la autorización
draw8.text((width//2, interfaz_y-interfaz_height//2+70), 
          "n8n Integration quiere acceder a tu cuenta de Google", 
          fill=color_texto, font=font_text, anchor="mm")

# Cuenta de Google
cuenta_y = interfaz_y-interfaz_height//2+120
draw8.text((width//2, cuenta_y), 
          "tu.correo@gmail.com", 
          fill=color_texto, font=font_text, anchor="mm")

# Permisos solicitados
permisos_y = interfaz_y
draw8.text((width//2-interfaz_width//2+50, permisos_y-50), "Esta aplicación podrá:", 
          fill=color_texto, font=font_text, anchor="lm")

# Lista de permisos
permisos = [
    "• Ver y administrar tus hojas de cálculo en Google Drive",
    "• Ver y administrar los archivos en tu Google Drive"
]

for i, permiso in enumerate(permisos):
    draw8.text((width//2-interfaz_width//2+50, permisos_y-20+i*30), permiso, 
              fill=color_texto, font=font_small, anchor="lm")

# Botones
boton_y = interfaz_y+interfaz_height//2-50

# Botón de cancelar
boton_cancelar_x = width//2-80
draw8.rounded_rectangle([(boton_cancelar_x-60, boton_y-15), 
                        (boton_cancelar_x+60, boton_y+15)], 
                       radius=5, fill='white', outline=color_texto)
draw8.text((boton_cancelar_x, boton_y), "Cancelar", 
          fill=color_texto, font=font_text, anchor="mm")

# Botón de permitir (resaltado)
boton_permitir_x = width//2+80
draw8.rounded_rectangle([(boton_permitir_x-60, boton_y-15), 
                        (boton_permitir_x+60, boton_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw8.text((boton_permitir_x, boton_y), "Permitir", 
          fill=color_texto, font=font_text, anchor="mm")

# Consejos
draw8.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw8.text((width//2, 675), "Consejo: Si recibes un aviso de 'App no verificada', haz clic en 'Avanzado' y luego en 'Ir a n8n Integration'", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la octava imagen
img8.save(os.path.join(output_dir, 'paso8_autorizar_acceso.png'))

# Paso 9: Verificar la conexión
img9, draw9, width, height = crear_imagen_base(titulo="Paso 9: Verificar la conexión")

# Instrucciones
draw9.text((width//2, 100), "Verifica que la conexión se ha establecido correctamente", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Después de autorizar el acceso, serás redirigido a n8n",
    "2. Deberías ver un mensaje de 'Conexión establecida con éxito'",
    "3. La credencial aparecerá en tu lista de credenciales",
    "4. Ahora puedes usar esta credencial en cualquier nodo de Google Sheets"
]

y_pos = 160
for paso in pasos:
    draw9.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n - Credenciales
interfaz_y = 400
interfaz_width = 700
interfaz_height = 300

# Fondo de la interfaz
draw9.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='white', outline=color_texto)

# Barra superior
draw9.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#333333', outline=color_texto)
draw9.text((width//2-interfaz_width//2+100, interfaz_y-interfaz_height//2+20), 
          "n8n - Credenciales", fill='white', font=font_text, anchor="mm")

# Mensaje de éxito
mensaje_y = interfaz_y-interfaz_height//2+70
draw9.rounded_rectangle([(width//2-300, mensaje_y-20), (width//2+300, mensaje_y+20)], 
                       radius=5, fill='#E8F5E9', outline=color_exito)
draw9.text((width//2, mensaje_y), "✓ Conexión establecida con éxito", 
          fill=color_exito, font=font_text, anchor="mm")

# Lista de credenciales
lista_y = interfaz_y+20
draw9.rectangle([(width//2-300, lista_y-40), (width//2+300, lista_y+40)], 
               fill='#f9f9f9', outline=color_texto)

# Credencial de Google Sheets
draw9.text((width//2-280, lista_y), "Google Sheets", 
          fill=color_texto, font=font_text, anchor="lm")
draw9.text((width//2-280, lista_y+25), "Nombre: Google Sheets Account", 
          fill=color_texto, font=font_small, anchor="lm")
draw9.text((width//2+280, lista_y), "✓", 
          fill=color_exito, font=font_text, anchor="rm")

# Botón de añadir nueva credencial
boton_y = interfaz_y+100
draw9.rounded_rectangle([(width//2-150, boton_y-20), (width//2+150, boton_y+20)], 
                       radius=5, fill=color_n8n, outline=color_texto)
draw9.text((width//2, boton_y), "+ Añadir nueva credencial", 
          fill='white', font=font_text, anchor="mm")

# Consejos
draw9.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw9.text((width//2, 675), "Consejo: Puedes crear múltiples credenciales para diferentes cuentas de Google", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la novena imagen
img9.save(os.path.join(output_dir, 'paso9_verificar_conexion.png'))

# Paso 10: Completado
img10, draw10, width, height = crear_imagen_base(titulo="¡Ejercicio Completado!")

# Mensaje de felicitación
draw10.text((width//2, 100), "¡Felicidades! Has configurado correctamente las credenciales para Google Sheets", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Resumen
draw10.text((width//2, 160), "En este ejercicio has aprendido:", 
          fill=color_texto, font=font_text, anchor="mm")

aprendizajes = [
    "• Crear un proyecto en Google Cloud Console",
    "• Activar las APIs necesarias para Google Sheets",
    "• Configurar la pantalla de consentimiento OAuth",
    "• Crear credenciales OAuth 2.0",
    "• Configurar las credenciales en n8n"
]

y_pos = 200
for aprendizaje in aprendizajes:
    draw10.text((width//2, y_pos), aprendizaje, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 30

# Diagrama del proceso completo
proceso_y = 400
box_width = 180
box_height = 80
spacing = 50

# Paso 1: Google Cloud Console (completado)
paso1_x = width//4
draw10.rounded_rectangle([(paso1_x-box_width//2, proceso_y-box_height//2), 
                        (paso1_x+box_width//2, proceso_y+box_height//2)], 
                       radius=10, fill='white', outline=color_exito, width=3)
draw10.text((paso1_x, proceso_y-15), "Google Cloud", fill=color_google, font=font_text, anchor="mm")
draw10.text((paso1_x, proceso_y+15), "Console", fill=color_google, font=font_text, anchor="mm")
draw10.text((paso1_x-box_width//2+20, proceso_y-box_height//2+20), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Paso 2: Crear Credenciales (completado)
paso2_x = width//2
draw10.rounded_rectangle([(paso2_x-box_width//2, proceso_y-box_height//2), 
                        (paso2_x+box_width//2, proceso_y+box_height//2)], 
                       radius=10, fill='white', outline=color_exito, width=3)
draw10.text((paso2_x, proceso_y-15), "Crear", fill=color_google, font=font_text, anchor="mm")
draw10.text((paso2_x, proceso_y+15), "Credenciales", fill=color_google, font=font_text, anchor="mm")
draw10.text((paso2_x-box_width//2+20, proceso_y-box_height//2+20), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Paso 3: Configurar en n8n (completado)
paso3_x = 3*width//4
draw10.rounded_rectangle([(paso3_x-box_width//2, proceso_y-box_height//2), 
                        (paso3_x+box_width//2, proceso_y+box_height//2)], 
                       radius=10, fill='white', outline=color_exito, width=3)
draw10.text((paso3_x, proceso_y-15), "Configurar en", fill=color_n8n, font=font_text, anchor="mm")
draw10.text((paso3_x, proceso_y+15), "n8n", fill=color_n8n, font=font_text, anchor="mm")
draw10.text((paso3_x-box_width//2+20, proceso_y-box_height//2+20), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Flechas entre pasos
draw10.line([(paso1_x+box_width//2, proceso_y), (paso2_x-box_width//2, proceso_y)], 
          fill=color_conexion, width=3)
draw10.polygon([(paso2_x-box_width//2, proceso_y), 
              (paso2_x-box_width//2-10, proceso_y-5), 
              (paso2_x-box_width//2-10, proceso_y+5)], 
             fill=color_conexion)

draw10.line([(paso2_x+box_width//2, proceso_y), (paso3_x-box_width//2, proceso_y)], 
          fill=color_conexion, width=3)
draw10.polygon([(paso3_x-box_width//2, proceso_y), 
              (paso3_x-box_width//2-10, proceso_y-5), 
              (paso3_x-box_width//2-10, proceso_y+5)], 
             fill=color_conexion)

# Resultado final
resultado_y = 550
draw10.rounded_rectangle([(width//2-250, resultado_y-50), (width//2+250, resultado_y+50)], 
                       radius=10, fill='#E8F5E9', outline=color_exito)
draw10.text((width//2, resultado_y-20), "Resultado:", fill=color_texto, font=font_text, anchor="mm")
draw10.text((width//2, resultado_y+20), "¡Conexión establecida con Google Sheets!", 
          fill=color_exito, font=font_text, anchor="mm")

# Próximos pasos
draw10.rounded_rectangle([(width//2-300, 650), (width//2+300, 700)], 
                       radius=10, fill='#E8F5E9', outline=color_exito)
draw10.text((width//2, 675), "Ahora puedes usar Google Sheets en tus flujos de trabajo de n8n", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la décima imagen
img10.save(os.path.join(output_dir, 'paso10_completado.png'))

# Crear un archivo de instrucciones
instrucciones_path = os.path.join(output_dir, 'instrucciones.md')
with open(instrucciones_path, 'w') as f:
    f.write("""# Ejercicio 1: Configuración de credenciales para Google Sheets

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
""")

print(f"Materiales para el Ejercicio 1 del Módulo 3 generados en {output_dir}")
