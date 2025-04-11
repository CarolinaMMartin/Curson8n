"""
Script para generar materiales para el Ejercicio 1 del Módulo 6: Automatización de seguimiento de clientes potenciales
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/ejercicios_interactivos/modulo6/ejercicio1'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_n8n = '#FF6D00'          # Naranja n8n
color_form = '#4CAF50'         # Verde para formularios
color_sheets = '#0F9D58'       # Verde para Google Sheets
color_email = '#D14836'        # Rojo para Email
color_conexion = '#9E9E9E'     # Gris para conexiones
color_resaltado = '#FFC107'    # Amarillo para resaltados
color_exito = '#4CAF50'        # Verde para éxito
color_error = '#F44336'        # Rojo para error

# Función para crear imagen base
def crear_imagen_base(width=1200, height=800, titulo="Ejercicio 1: Automatización de seguimiento de clientes potenciales"):
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
img1, draw1, width, height = crear_imagen_base(titulo="Ejercicio 1: Automatización de seguimiento de clientes potenciales")

# Subtítulo
draw1.text((width//2, 100), "Objetivo: Crear un sistema automatizado de seguimiento de leads", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Descripción del ejercicio
descripcion = [
    "En este ejercicio, crearás un flujo de trabajo que automatice el proceso de captura",
    "y seguimiento de clientes potenciales (leads). Aprenderás a:",
    "",
    "• Capturar datos de un formulario web",
    "• Almacenar la información en Google Sheets",
    "• Enviar emails de seguimiento automáticos",
    "• Clasificar leads según su interés",
    "• Generar notificaciones para el equipo de ventas"
]

y_pos = 160
for linea in descripcion:
    draw1.text((width//2, y_pos), linea, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 30

# Diagrama del flujo de trabajo
flujo_y = 400
nodo_size = 80
nodo_spacing = 180

# Nodo 1: Formulario Web
nodo1_x = width//2 - nodo_spacing
draw1.rounded_rectangle([(nodo1_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (nodo1_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill=color_form, outline=color_texto)
draw1.text((nodo1_x, flujo_y-15), "Formulario", fill='white', font=font_text, anchor="mm")
draw1.text((nodo1_x, flujo_y+15), "Web", fill='white', font=font_text, anchor="mm")

# Nodo 2: n8n
nodo2_x = width//2
draw1.rounded_rectangle([(nodo2_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (nodo2_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill=color_n8n, outline=color_texto)
draw1.text((nodo2_x, flujo_y), "n8n", fill='white', font=font_text, anchor="mm")

# Nodo 3: Google Sheets
nodo3_x = width//2 + nodo_spacing
draw1.rounded_rectangle([(nodo3_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (nodo3_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill=color_sheets, outline=color_texto)
draw1.text((nodo3_x, flujo_y-15), "Google", fill='white', font=font_text, anchor="mm")
draw1.text((nodo3_x, flujo_y+15), "Sheets", fill='white', font=font_text, anchor="mm")

# Nodo 4: Email
nodo4_x = width//2
nodo4_y = flujo_y + 120
draw1.rounded_rectangle([(nodo4_x-nodo_size//2, nodo4_y-nodo_size//2), 
                        (nodo4_x+nodo_size//2, nodo4_y+nodo_size//2)], 
                       radius=15, fill=color_email, outline=color_texto)
draw1.text((nodo4_x, nodo4_y-15), "Email", fill='white', font=font_text, anchor="mm")
draw1.text((nodo4_x, nodo4_y+15), "Automático", fill='white', font=font_text, anchor="mm")

# Conexiones entre nodos
# Formulario a n8n
draw1.line([(nodo1_x+nodo_size//2, flujo_y), (nodo2_x-nodo_size//2, flujo_y)], 
          fill=color_conexion, width=3)
draw1.polygon([(nodo2_x-nodo_size//2, flujo_y), 
              (nodo2_x-nodo_size//2-10, flujo_y-5), 
              (nodo2_x-nodo_size//2-10, flujo_y+5)], 
             fill=color_conexion)

# n8n a Google Sheets
draw1.line([(nodo2_x+nodo_size//2, flujo_y), (nodo3_x-nodo_size//2, flujo_y)], 
          fill=color_conexion, width=3)
draw1.polygon([(nodo3_x-nodo_size//2, flujo_y), 
              (nodo3_x-nodo_size//2-10, flujo_y-5), 
              (nodo3_x-nodo_size//2-10, flujo_y+5)], 
             fill=color_conexion)

# n8n a Email
draw1.line([(nodo2_x, flujo_y+nodo_size//2), (nodo2_x, nodo4_y-nodo_size//2)], 
          fill=color_conexion, width=3)
draw1.polygon([(nodo2_x, nodo4_y-nodo_size//2), 
              (nodo2_x-5, nodo4_y-nodo_size//2-10), 
              (nodo2_x+5, nodo4_y-nodo_size//2-10)], 
             fill=color_conexion)

# Resultado esperado
resultado_y = 550
draw1.rounded_rectangle([(width//2-300, resultado_y-60), (width//2+300, resultado_y+60)], 
                       radius=10, fill='white', outline=color_exito)
draw1.text((width//2, resultado_y-30), "Resultado esperado:", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, resultado_y), "Sistema automatizado que captura leads, los almacena", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, resultado_y+30), "y envía emails de seguimiento personalizados", 
          fill=color_texto, font=font_text, anchor="mm")

# Instrucciones para comenzar
draw1.text((width//2, 650), "Para comenzar, necesitarás acceso a n8n y una cuenta de Google", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, 680), "Tiempo estimado: 45-60 minutos", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la primera imagen
img1.save(os.path.join(output_dir, 'paso1_introduccion.png'))

# Paso 2: Configurar el formulario web
img2, draw2, width, height = crear_imagen_base(titulo="Paso 2: Configurar el formulario web")

# Instrucciones
draw2.text((width//2, 100), "Configura un formulario web para capturar leads", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. En n8n, crea un nuevo flujo de trabajo y nómbralo 'Seguimiento de Leads'",
    "2. Añade un nodo 'Webhook' como disparador",
    "3. Configura el webhook para recibir datos de un formulario web (método POST)",
    "4. Haz clic en 'Ejecutar flujo de trabajo' para activar el webhook",
    "5. Copia la URL del webhook generada"
]

y_pos = 160
for paso in pasos:
    draw2.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n - Configuración del webhook
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
               fill='#333333', outline=color_texto)
draw2.text((width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+20), 
          "n8n - Seguimiento de Leads", fill='white', font=font_text, anchor="mm")

# Panel izquierdo
draw2.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw2.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Nodos", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw2.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Nodo Webhook
webhook_x = width//2
webhook_y = interfaz_y
webhook_size = 80
draw2.rounded_rectangle([(webhook_x-webhook_size//2, webhook_y-webhook_size//2), 
                        (webhook_x+webhook_size//2, webhook_y+webhook_size//2)], 
                       radius=15, fill='#5096F3', outline=color_texto)
draw2.text((webhook_x, webhook_y), "Webhook", fill='white', font=font_text, anchor="mm")

# Panel de configuración del webhook
config_x = width//2 + 200
config_y = interfaz_y
config_width = 250
config_height = 200
draw2.rounded_rectangle([(config_x-config_width//2, config_y-config_height//2), 
                        (config_x+config_width//2, config_y+config_height//2)], 
                       radius=10, fill='white', outline=color_resaltado, width=2)

# Título del panel
draw2.rectangle([(config_x-config_width//2, config_y-config_height//2), 
                (config_x+config_width//2, config_y-config_height//2+30)], 
               fill='#5096F3', outline=color_texto)
draw2.text((config_x, config_y-config_height//2+15), "Configuración del Webhook", 
          fill='white', font=font_small, anchor="mm")

# Contenido del panel
draw2.text((config_x-config_width//2+20, config_y-config_height//2+50), "Método HTTP:", 
          fill=color_texto, font=font_small, anchor="lm")
draw2.rounded_rectangle([(config_x-config_width//2+120, config_y-config_height//2+40), 
                        (config_x+config_width//2-20, config_y-config_height//2+60)], 
                       radius=5, fill='white', outline=color_texto)
draw2.text((config_x-config_width//2+130, config_y-config_height//2+50), "POST", 
          fill=color_texto, font=font_small, anchor="lm")

draw2.text((config_x-config_width//2+20, config_y-config_height//2+80), "Path:", 
          fill=color_texto, font=font_small, anchor="lm")
draw2.rounded_rectangle([(config_x-config_width//2+120, config_y-config_height//2+70), 
                        (config_x+config_width//2-20, config_y-config_height//2+90)], 
                       radius=5, fill='white', outline=color_texto)
draw2.text((config_x-config_width//2+130, config_y-config_height//2+80), "webhook", 
          fill=color_texto, font=font_small, anchor="lm")

draw2.text((config_x-config_width//2+20, config_y-config_height//2+110), "Respuesta:", 
          fill=color_texto, font=font_small, anchor="lm")
draw2.rounded_rectangle([(config_x-config_width//2+120, config_y-config_height//2+100), 
                        (config_x+config_width//2-20, config_y-config_height//2+120)], 
                       radius=5, fill='white', outline=color_texto)
draw2.text((config_x-config_width//2+130, config_y-config_height//2+110), "JSON", 
          fill=color_texto, font=font_small, anchor="lm")

# URL del webhook
webhook_url_y = config_y+config_height//2-30
draw2.rounded_rectangle([(config_x-config_width//2+20, webhook_url_y-20), 
                        (config_x+config_width//2-20, webhook_url_y+20)], 
                       radius=5, fill='#E8F5E9', outline=color_exito)
draw2.text((config_x, webhook_url_y), "URL generada", 
          fill=color_exito, font=font_small, anchor="mm")

# Flecha de conexión
draw2.line([(webhook_x+webhook_size//2, webhook_y), (config_x-config_width//2, config_y)], 
          fill=color_resaltado, width=2)

# Formulario HTML simplificado
form_x = width//2 - 200
form_y = interfaz_y
form_width = 250
form_height = 200
draw2.rounded_rectangle([(form_x-form_width//2, form_y-form_height//2), 
                        (form_x+form_width//2, form_y+form_height//2)], 
                       radius=10, fill='white', outline=color_form, width=2)

# Título del formulario
draw2.rectangle([(form_x-form_width//2, form_y-form_height//2), 
                (form_x+form_width//2, form_y-form_height//2+30)], 
               fill=color_form, outline=color_texto)
draw2.text((form_x, form_y-form_height//2+15), "Formulario de contacto", 
          fill='white', font=font_small, anchor="mm")

# Campos del formulario
draw2.text((form_x-form_width//2+20, form_y-form_height//2+50), "Nombre:", 
          fill=color_texto, font=font_small, anchor="lm")
draw2.rectangle([(form_x-form_width//2+20, form_y-form_height//2+70), 
                (form_x+form_width//2-20, form_y-form_height//2+90)], 
               fill='white', outline=color_texto)

draw2.text((form_x-form_width//2+20, form_y-form_height//2+110), "Email:", 
          fill=color_texto, font=font_small, anchor="lm")
draw2.rectangle([(form_x-form_width//2+20, form_y-form_height//2+130), 
                (form_x+form_width//2-20, form_y-form_height//2+150)], 
               fill='white', outline=color_texto)

# Botón de enviar
draw2.rounded_rectangle([(form_x-50, form_y+form_height//2-30), 
                        (form_x+50, form_y+form_height//2-10)], 
                       radius=5, fill=color_form, outline=color_texto)
draw2.text((form_x, form_y+form_height//2-20), "Enviar", 
          fill='white', font=font_small, anchor="mm")

# Flecha del formulario al webhook
draw2.line([(form_x+form_width//2, form_y), (webhook_x-webhook_size//2, webhook_y)], 
          fill=color_resaltado, width=2)
draw2.polygon([(webhook_x-webhook_size//2, webhook_y), 
              (webhook_x-webhook_size//2-10, webhook_y-5), 
              (webhook_x-webhook_size//2-10, webhook_y+5)], 
             fill=color_resaltado)

# Código HTML simplificado
codigo_y = 600
draw2.rounded_rectangle([(width//2-350, codigo_y-60), (width//2+350, codigo_y+60)], 
                       radius=10, fill='#263238', outline=color_texto)

codigo_html = [
    '<form action="https://n8n.example.com/webhook/abc123" method="POST">',
    '  <input type="text" name="nombre" placeholder="Nombre">',
    '  <input type="email" name="email" placeholder="Email">',
    '  <input type="submit" value="Enviar">',
    '</form>'
]

for i, linea in enumerate(codigo_html):
    draw2.text((width//2-330, codigo_y-40+i*20), linea, 
              fill='white', font=font_small, anchor="lm")

# Guardar la segunda imagen
img2.save(os.path.join(output_dir, 'paso2_configurar_formulario.png'))

# Paso 3: Configurar Google Sheets
img3, draw3, width, height = crear_imagen_base(titulo="Paso 3: Configurar Google Sheets")

# Instrucciones
draw3.text((width//2, 100), "Configura Google Sheets para almacenar los datos de leads", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Crea una nueva hoja de cálculo en Google Sheets",
    "2. Configura las siguientes columnas: ID, Nombre, Email, Fecha, Estado",
    "3. En n8n, añade un nodo 'Google Sheets' después del nodo Webhook",
    "4. Configura el nodo para usar tus credenciales de Google",
    "5. Selecciona la operación 'Append' para añadir filas a la hoja"
]

y_pos = 160
for paso in pasos:
    draw3.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n con Google Sheets
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
               fill='#333333', outline=color_texto)
draw3.text((width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+20), 
          "n8n - Seguimiento de Leads", fill='white', font=font_text, anchor="mm")

# Panel izquierdo
draw3.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw3.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Nodos", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw3.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Nodo Webhook
webhook_x = width//2 - 150
webhook_y = interfaz_y
webhook_size = 80
draw3.rounded_rectangle([(webhook_x-webhook_size//2, webhook_y-webhook_size//2), 
                        (webhook_x+webhook_size//2, webhook_y+webhook_size//2)], 
                       radius=15, fill='#5096F3', outline=color_texto)
draw3.text((webhook_x, webhook_y), "Webhook", fill='white', font=font_text, anchor="mm")

# Nodo Google Sheets
sheets_x = width//2 + 150
sheets_y = interfaz_y
sheets_size = 80
draw3.rounded_rectangle([(sheets_x-sheets_size//2, sheets_y-sheets_size//2), 
                        (sheets_x+sheets_size//2, sheets_y+sheets_size//2)], 
                       radius=15, fill=color_sheets, outline=color_texto)
draw3.text((sheets_x, sheets_y-15), "Google", fill='white', font=font_text, anchor="mm")
draw3.text((sheets_x, sheets_y+15), "Sheets", fill='white', font=font_text, anchor="mm")

# Conexión entre nodos
draw3.line([(webhook_x+webhook_size//2, webhook_y), (sheets_x-sheets_size//2, sheets_y)], 
          fill=color_conexion, width=3)
draw3.polygon([(sheets_x-sheets_size//2, sheets_y), 
              (sheets_x-sheets_size//2-10, sheets_y-5), 
              (sheets_x-sheets_size//2-10, sheets_y+5)], 
             fill=color_conexion)

# Panel de configuración de Google Sheets
config_x = width//2 + 350
config_y = interfaz_y
config_width = 250
config_height = 250
draw3.rounded_rectangle([(config_x-config_width//2, config_y-config_height//2), 
                        (config_x+config_width//2, config_y+config_height//2)], 
                       radius=10, fill='white', outline=color_resaltado, width=2)

# Título del panel
draw3.rectangle([(config_x-config_width//2, config_y-config_height//2), 
                (config_x+config_width//2, config_y-config_height//2+30)], 
               fill=color_sheets, outline=color_texto)
draw3.text((config_x, config_y-config_height//2+15), "Configuración de Google Sheets", 
          fill='white', font=font_small, anchor="mm")

# Contenido del panel
draw3.text((config_x-config_width//2+20, config_y-config_height//2+50), "Operación:", 
          fill=color_texto, font=font_small, anchor="lm")
draw3.rounded_rectangle([(config_x-config_width//2+120, config_y-config_height//2+40), 
                        (config_x+config_width//2-20, config_y-config_height//2+60)], 
                       radius=5, fill='white', outline=color_texto)
draw3.text((config_x-config_width//2+130, config_y-config_height//2+50), "Append", 
          fill=color_texto, font=font_small, anchor="lm")

draw3.text((config_x-config_width//2+20, config_y-config_height//2+80), "Hoja de cálculo:", 
          fill=color_texto, font=font_small, anchor="lm")
draw3.rounded_rectangle([(config_x-config_width//2+20, config_y-config_height//2+100), 
                        (config_x+config_width//2-20, config_y-config_height//2+120)], 
                       radius=5, fill='white', outline=color_texto)
draw3.text((config_x-config_width//2+30, config_y-config_height//2+110), "Seguimiento de Leads", 
          fill=color_texto, font=font_small, anchor="lm")

draw3.text((config_x-config_width//2+20, config_y-config_height//2+140), "Hoja:", 
          fill=color_texto, font=font_small, anchor="lm")
draw3.rounded_rectangle([(config_x-config_width//2+120, config_y-config_height//2+130), 
                        (config_x+config_width//2-20, config_y-config_height//2+150)], 
                       radius=5, fill='white', outline=color_texto)
draw3.text((config_x-config_width//2+130, config_y-config_height//2+140), "Leads", 
          fill=color_texto, font=font_small, anchor="lm")

draw3.text((config_x-config_width//2+20, config_y-config_height//2+170), "Datos:", 
          fill=color_texto, font=font_small, anchor="lm")
draw3.rounded_rectangle([(config_x-config_width//2+20, config_y-config_height//2+190), 
                        (config_x+config_width//2-20, config_y-config_height//2+210)], 
                       radius=5, fill='white', outline=color_texto)
draw3.text((config_x-config_width//2+30, config_y-config_height//2+200), "{{$node.Webhook.json}}", 
          fill=color_texto, font=font_small, anchor="lm")

# Flecha de conexión
draw3.line([(sheets_x+sheets_size//2, sheets_y), (config_x-config_width//2, config_y)], 
          fill=color_resaltado, width=2)

# Tabla de Google Sheets
tabla_x = width//2 - 250
tabla_y = interfaz_y + 150
tabla_width = 400
tabla_height = 150
draw3.rectangle([(tabla_x-tabla_width//2, tabla_y-tabla_height//2), 
                (tabla_x+tabla_width//2, tabla_y+tabla_height//2)], 
               fill='white', outline=color_sheets)

# Encabezado de la tabla
draw3.rectangle([(tabla_x-tabla_width//2, tabla_y-tabla_height//2), 
                (tabla_x+tabla_width//2, tabla_y-tabla_height//2+30)], 
               fill='#E8F5E9', outline=color_sheets)

# Columnas
col_width = tabla_width / 5
for i in range(1, 5):
    col_x = tabla_x - tabla_width//2 + i * col_width
    draw3.line([(col_x, tabla_y-tabla_height//2), (col_x, tabla_y+tabla_height//2)], 
              fill=color_sheets, width=1)

# Filas
for i in range(1, 4):
    row_y = tabla_y - tabla_height//2 + 30 + i * 30
    draw3.line([(tabla_x-tabla_width//2, row_y), (tabla_x+tabla_width//2, row_y)], 
              fill=color_sheets, width=1)

# Títulos de columnas
col_titles = ["ID", "Nombre", "Email", "Fecha", "Estado"]
for i, title in enumerate(col_titles):
    col_x = tabla_x - tabla_width//2 + i * col_width + col_width//2
    draw3.text((col_x, tabla_y-tabla_height//2+15), title, 
              fill=color_texto, font=font_small, anchor="mm")

# Datos de ejemplo
datos = [
    ["1", "Ana García", "ana@ejemplo.com", "2025-04-10", "Nuevo"],
    ["2", "Carlos López", "carlos@ejemplo.com", "2025-04-11", "Contactado"],
    ["3", "Elena Martín", "elena@ejemplo.com", "2025-04-11", "Nuevo"]
]

for i, fila in enumerate(datos):
    for j, valor in enumerate(fila):
        col_x = tabla_x - tabla_width//2 + j * col_width + col_width//2
        row_y = tabla_y - tabla_height//2 + 30 + (i+1) * 30 - 15
        draw3.text((col_x, row_y), valor, 
                  fill=color_texto, font=font_small, anchor="mm")

# Consejos
draw3.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw3.text((width//2, 675), "Consejo: Asegúrate de tener configuradas las credenciales de Google Sheets en n8n", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la tercera imagen
img3.save(os.path.join(output_dir, 'paso3_configurar_sheets.png'))

# Paso 4: Configurar el email automático
img4, draw4, width, height = crear_imagen_base(titulo="Paso 4: Configurar el email automático")

# Instrucciones
draw4.text((width//2, 100), "Configura el envío automático de emails de seguimiento", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. En n8n, añade un nodo 'IF' después del nodo Google Sheets",
    "2. Configura la condición para verificar si el email es válido",
    "3. En la rama 'true', añade un nodo 'Send Email'",
    "4. Configura el nodo con tus credenciales de email",
    "5. Personaliza el mensaje de bienvenida usando los datos del lead"
]

y_pos = 160
for paso in pasos:
    draw4.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n con flujo completo
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
               fill='#333333', outline=color_texto)
draw4.text((width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+20), 
          "n8n - Seguimiento de Leads", fill='white', font=font_text, anchor="mm")

# Panel izquierdo
draw4.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw4.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Nodos", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw4.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Nodo Webhook
webhook_x = width//2 - 250
webhook_y = interfaz_y
webhook_size = 60
draw4.rounded_rectangle([(webhook_x-webhook_size//2, webhook_y-webhook_size//2), 
                        (webhook_x+webhook_size//2, webhook_y+webhook_size//2)], 
                       radius=15, fill='#5096F3', outline=color_texto)
draw4.text((webhook_x, webhook_y), "Webhook", fill='white', font=font_small, anchor="mm")

# Nodo Google Sheets
sheets_x = width//2 - 100
sheets_y = interfaz_y
sheets_size = 60
draw4.rounded_rectangle([(sheets_x-sheets_size//2, sheets_y-sheets_size//2), 
                        (sheets_x+sheets_size//2, sheets_y+sheets_size//2)], 
                       radius=15, fill=color_sheets, outline=color_texto)
draw4.text((sheets_x, sheets_y-10), "Google", fill='white', font=font_small, anchor="mm")
draw4.text((sheets_x, sheets_y+10), "Sheets", fill='white', font=font_small, anchor="mm")

# Nodo IF
if_x = width//2 + 50
if_y = interfaz_y
if_size = 60
draw4.rounded_rectangle([(if_x-if_size//2, if_y-if_size//2), 
                        (if_x+if_size//2, if_y+if_size//2)], 
                       radius=15, fill='#9C27B0', outline=color_texto)
draw4.text((if_x, if_y), "IF", fill='white', font=font_text, anchor="mm")

# Nodo Send Email
email_x = width//2 + 200
email_y = interfaz_y - 70
email_size = 60
draw4.rounded_rectangle([(email_x-email_size//2, email_y-email_size//2), 
                        (email_x+email_size//2, email_y+email_size//2)], 
                       radius=15, fill=color_email, outline=color_texto)
draw4.text((email_x, email_y-10), "Send", fill='white', font=font_small, anchor="mm")
draw4.text((email_x, email_y+10), "Email", fill='white', font=font_small, anchor="mm")

# Nodo NoOp (rama false)
noop_x = width//2 + 200
noop_y = interfaz_y + 70
noop_size = 60
draw4.rounded_rectangle([(noop_x-noop_size//2, noop_y-noop_size//2), 
                        (noop_x+noop_size//2, noop_y+noop_size//2)], 
                       radius=15, fill='#607D8B', outline=color_texto)
draw4.text((noop_x, noop_y), "NoOp", fill='white', font=font_small, anchor="mm")

# Conexiones entre nodos
# Webhook a Google Sheets
draw4.line([(webhook_x+webhook_size//2, webhook_y), (sheets_x-sheets_size//2, sheets_y)], 
          fill=color_conexion, width=3)
draw4.polygon([(sheets_x-sheets_size//2, sheets_y), 
              (sheets_x-sheets_size//2-10, sheets_y-5), 
              (sheets_x-sheets_size//2-10, sheets_y+5)], 
             fill=color_conexion)

# Google Sheets a IF
draw4.line([(sheets_x+sheets_size//2, sheets_y), (if_x-if_size//2, if_y)], 
          fill=color_conexion, width=3)
draw4.polygon([(if_x-if_size//2, if_y), 
              (if_x-if_size//2-10, if_y-5), 
              (if_x-if_size//2-10, if_y+5)], 
             fill=color_conexion)

# IF a Send Email (true)
draw4.line([(if_x, if_y-if_size//2), (if_x, email_y), (email_x-email_size//2, email_y)], 
          fill=color_conexion, width=3)
draw4.polygon([(email_x-email_size//2, email_y), 
              (email_x-email_size//2-10, email_y-5), 
              (email_x-email_size//2-10, email_y+5)], 
             fill=color_conexion)

# IF a NoOp (false)
draw4.line([(if_x, if_y+if_size//2), (if_x, noop_y), (noop_x-noop_size//2, noop_y)], 
          fill=color_conexion, width=3)
draw4.polygon([(noop_x-noop_size//2, noop_y), 
              (noop_x-noop_size//2-10, noop_y-5), 
              (noop_x-noop_size//2-10, noop_y+5)], 
             fill=color_conexion)

# Panel de configuración del email
config_x = width//2 - 200
config_y = interfaz_y + 150
config_width = 300
config_height = 200
draw4.rounded_rectangle([(config_x-config_width//2, config_y-config_height//2), 
                        (config_x+config_width//2, config_y+config_height//2)], 
                       radius=10, fill='white', outline=color_resaltado, width=2)

# Título del panel
draw4.rectangle([(config_x-config_width//2, config_y-config_height//2), 
                (config_x+config_width//2, config_y-config_height//2+30)], 
               fill=color_email, outline=color_texto)
draw4.text((config_x, config_y-config_height//2+15), "Configuración del Email", 
          fill='white', font=font_small, anchor="mm")

# Contenido del panel
draw4.text((config_x-config_width//2+20, config_y-config_height//2+50), "Para:", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.rounded_rectangle([(config_x-config_width//2+70, config_y-config_height//2+40), 
                        (config_x+config_width//2-20, config_y-config_height//2+60)], 
                       radius=5, fill='white', outline=color_texto)
draw4.text((config_x-config_width//2+80, config_y-config_height//2+50), "{{$node.Webhook.json.email}}", 
          fill=color_texto, font=font_small, anchor="lm")

draw4.text((config_x-config_width//2+20, config_y-config_height//2+80), "Asunto:", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.rounded_rectangle([(config_x-config_width//2+70, config_y-config_height//2+70), 
                        (config_x+config_width//2-20, config_y-config_height//2+90)], 
                       radius=5, fill='white', outline=color_texto)
draw4.text((config_x-config_width//2+80, config_y-config_height//2+80), "Bienvenido a nuestra lista", 
          fill=color_texto, font=font_small, anchor="lm")

draw4.text((config_x-config_width//2+20, config_y-config_height//2+110), "Contenido:", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.rounded_rectangle([(config_x-config_width//2+20, config_y-config_height//2+130), 
                        (config_x+config_width//2-20, config_y-config_height//2+170)], 
                       radius=5, fill='white', outline=color_texto)
draw4.text((config_x-config_width//2+30, config_y-config_height//2+140), "Hola {{$node.Webhook.json.nombre}},", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.text((config_x-config_width//2+30, config_y-config_height//2+160), "Gracias por registrarte...", 
          fill=color_texto, font=font_small, anchor="lm")

# Plantilla de email
email_template_x = width//2 + 200
email_template_y = interfaz_y + 150
email_width = 300
email_height = 200
draw4.rounded_rectangle([(email_template_x-email_width//2, email_template_y-email_height//2), 
                        (email_template_x+email_width//2, email_template_y+email_height//2)], 
                       radius=10, fill='white', outline=color_email, width=2)

# Encabezado del email
draw4.rectangle([(email_template_x-email_width//2, email_template_y-email_height//2), 
                (email_template_x+email_width//2, email_template_y-email_height//2+40)], 
               fill=color_email, outline=color_texto)
draw4.text((email_template_x, email_template_y-email_height//2+20), "Bienvenido a nuestra lista", 
          fill='white', font=font_small, anchor="mm")

# Contenido del email
draw4.text((email_template_x-email_width//2+20, email_template_y-email_height//2+60), "Hola Ana García,", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.text((email_template_x-email_width//2+20, email_template_y-email_height//2+90), "Gracias por registrarte en nuestra lista.", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.text((email_template_x-email_width//2+20, email_template_y-email_height//2+120), "Pronto recibirás más información sobre", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.text((email_template_x-email_width//2+20, email_template_y-email_height//2+140), "nuestros productos y servicios.", 
          fill=color_texto, font=font_small, anchor="lm")
draw4.text((email_template_x-email_width//2+20, email_template_y-email_height//2+170), "Saludos cordiales,", 
          fill=color_texto, font=font_small, anchor="lm")

# Consejos
draw4.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw4.text((width//2, 675), "Consejo: Personaliza el email usando variables dinámicas como {{$node.Webhook.json.nombre}}", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la cuarta imagen
img4.save(os.path.join(output_dir, 'paso4_configurar_email.png'))

# Paso 5: Probar el flujo completo
img5, draw5, width, height = crear_imagen_base(titulo="Paso 5: Probar el flujo completo")

# Instrucciones
draw5.text((width//2, 100), "Prueba el flujo completo de seguimiento de leads", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Asegúrate de que todos los nodos estén correctamente configurados",
    "2. Activa el flujo de trabajo haciendo clic en 'Activar'",
    "3. Envía datos de prueba al webhook usando el formulario web",
    "4. Verifica que los datos se hayan añadido a Google Sheets",
    "5. Comprueba que el email de bienvenida se haya enviado correctamente"
]

y_pos = 160
for paso in pasos:
    draw5.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Diagrama del flujo completo
flujo_y = 400
nodo_size = 60
spacing_h = 120
spacing_v = 80

# Nodo Webhook
webhook_x = width//2 - spacing_h*2
draw5.rounded_rectangle([(webhook_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (webhook_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill='#5096F3', outline=color_exito, width=3)
draw5.text((webhook_x, flujo_y), "Webhook", fill='white', font=font_small, anchor="mm")
draw5.text((webhook_x-nodo_size//2+15, flujo_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo Google Sheets
sheets_x = width//2 - spacing_h
draw5.rounded_rectangle([(sheets_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (sheets_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill=color_sheets, outline=color_exito, width=3)
draw5.text((sheets_x, flujo_y-10), "Google", fill='white', font=font_small, anchor="mm")
draw5.text((sheets_x, flujo_y+10), "Sheets", fill='white', font=font_small, anchor="mm")
draw5.text((sheets_x-nodo_size//2+15, flujo_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo IF
if_x = width//2
draw5.rounded_rectangle([(if_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (if_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill='#9C27B0', outline=color_exito, width=3)
draw5.text((if_x, flujo_y), "IF", fill='white', font=font_text, anchor="mm")
draw5.text((if_x-nodo_size//2+15, flujo_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo Send Email
email_x = width//2 + spacing_h
email_y = flujo_y - spacing_v
draw5.rounded_rectangle([(email_x-nodo_size//2, email_y-nodo_size//2), 
                        (email_x+nodo_size//2, email_y+nodo_size//2)], 
                       radius=15, fill=color_email, outline=color_exito, width=3)
draw5.text((email_x, email_y-10), "Send", fill='white', font=font_small, anchor="mm")
draw5.text((email_x, email_y+10), "Email", fill='white', font=font_small, anchor="mm")
draw5.text((email_x-nodo_size//2+15, email_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo NoOp (rama false)
noop_x = width//2 + spacing_h
noop_y = flujo_y + spacing_v
draw5.rounded_rectangle([(noop_x-nodo_size//2, noop_y-nodo_size//2), 
                        (noop_x+nodo_size//2, noop_y+nodo_size//2)], 
                       radius=15, fill='#607D8B', outline=color_exito, width=3)
draw5.text((noop_x, noop_y), "NoOp", fill='white', font=font_small, anchor="mm")
draw5.text((noop_x-nodo_size//2+15, noop_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Conexiones entre nodos
# Webhook a Google Sheets
draw5.line([(webhook_x+nodo_size//2, flujo_y), (sheets_x-nodo_size//2, flujo_y)], 
          fill=color_conexion, width=3)
draw5.polygon([(sheets_x-nodo_size//2, flujo_y), 
              (sheets_x-nodo_size//2-10, flujo_y-5), 
              (sheets_x-nodo_size//2-10, flujo_y+5)], 
             fill=color_conexion)

# Google Sheets a IF
draw5.line([(sheets_x+nodo_size//2, flujo_y), (if_x-nodo_size//2, flujo_y)], 
          fill=color_conexion, width=3)
draw5.polygon([(if_x-nodo_size//2, flujo_y), 
              (if_x-nodo_size//2-10, flujo_y-5), 
              (if_x-nodo_size//2-10, flujo_y+5)], 
             fill=color_conexion)

# IF a Send Email (true)
draw5.line([(if_x, flujo_y-nodo_size//2), (if_x, email_y), (email_x-nodo_size//2, email_y)], 
          fill=color_conexion, width=3)
draw5.polygon([(email_x-nodo_size//2, email_y), 
              (email_x-nodo_size//2-10, email_y-5), 
              (email_x-nodo_size//2-10, email_y+5)], 
             fill=color_conexion)

# IF a NoOp (false)
draw5.line([(if_x, flujo_y+nodo_size//2), (if_x, noop_y), (noop_x-nodo_size//2, noop_y)], 
          fill=color_conexion, width=3)
draw5.polygon([(noop_x-nodo_size//2, noop_y), 
              (noop_x-nodo_size//2-10, noop_y-5), 
              (noop_x-nodo_size//2-10, noop_y+5)], 
             fill=color_conexion)

# Resultados de la prueba
# Formulario enviado
form_x = width//2 - 300
form_y = flujo_y + 150
form_width = 200
form_height = 100
draw5.rounded_rectangle([(form_x-form_width//2, form_y-form_height//2), 
                        (form_x+form_width//2, form_y+form_height//2)], 
                       radius=10, fill='white', outline=color_form)
draw5.text((form_x, form_y-form_height//2+20), "Formulario enviado", 
          fill=color_form, font=font_small, anchor="mm")
draw5.text((form_x, form_y-form_height//2+50), "Nombre: Ana García", 
          fill=color_texto, font=font_small, anchor="mm")
draw5.text((form_x, form_y-form_height//2+70), "Email: ana@ejemplo.com", 
          fill=color_texto, font=font_small, anchor="mm")

# Datos en Google Sheets
sheets_result_x = width//2
sheets_result_y = flujo_y + 150
sheets_width = 200
sheets_height = 100
draw5.rounded_rectangle([(sheets_result_x-sheets_width//2, sheets_result_y-sheets_height//2), 
                        (sheets_result_x+sheets_width//2, sheets_result_y+sheets_height//2)], 
                       radius=10, fill='white', outline=color_sheets)
draw5.text((sheets_result_x, sheets_result_y-sheets_height//2+20), "Datos almacenados", 
          fill=color_sheets, font=font_small, anchor="mm")
draw5.text((sheets_result_x, sheets_result_y-sheets_height//2+50), "Nueva fila añadida", 
          fill=color_texto, font=font_small, anchor="mm")
draw5.text((sheets_result_x, sheets_result_y-sheets_height//2+70), "ID: 4", 
          fill=color_texto, font=font_small, anchor="mm")

# Email enviado
email_result_x = width//2 + 300
email_result_y = flujo_y + 150
email_width = 200
email_height = 100
draw5.rounded_rectangle([(email_result_x-email_width//2, email_result_y-email_height//2), 
                        (email_result_x+email_width//2, email_result_y+email_height//2)], 
                       radius=10, fill='white', outline=color_email)
draw5.text((email_result_x, email_result_y-email_height//2+20), "Email enviado", 
          fill=color_email, font=font_small, anchor="mm")
draw5.text((email_result_x, email_result_y-email_height//2+50), "Para: ana@ejemplo.com", 
          fill=color_texto, font=font_small, anchor="mm")
draw5.text((email_result_x, email_result_y-email_height//2+70), "Estado: Entregado", 
          fill=color_exito, font=font_small, anchor="mm")

# Flechas de conexión
draw5.line([(webhook_x, flujo_y+nodo_size//2), (form_x, form_y-form_height//2)], 
          fill=color_resaltado, width=2)
draw5.line([(sheets_x, flujo_y+nodo_size//2), (sheets_result_x, sheets_result_y-sheets_height//2)], 
          fill=color_resaltado, width=2)
draw5.line([(email_x, email_y+nodo_size//2), (email_result_x, email_result_y-email_height//2)], 
          fill=color_resaltado, width=2)

# Mensaje de éxito
draw5.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E8F5E9', outline=color_exito)
draw5.text((width//2, 675), "¡Flujo de trabajo probado con éxito! Todos los nodos funcionan correctamente.", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la quinta imagen
img5.save(os.path.join(output_dir, 'paso5_probar_flujo.png'))

# Paso 6: Completado
img6, draw6, width, height = crear_imagen_base(titulo="¡Ejercicio Completado!")

# Mensaje de felicitación
draw6.text((width//2, 100), "¡Felicidades! Has creado un sistema automatizado de seguimiento de leads", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Resumen
draw6.text((width//2, 160), "En este ejercicio has aprendido:", 
          fill=color_texto, font=font_text, anchor="mm")

aprendizajes = [
    "• Configurar un webhook para recibir datos de formularios web",
    "• Almacenar información en Google Sheets de forma automática",
    "• Implementar lógica condicional en tus flujos de trabajo",
    "• Enviar emails personalizados de forma automática",
    "• Crear un sistema completo de seguimiento de leads"
]

y_pos = 200
for aprendizaje in enumerate(aprendizajes):
    draw6.text((width//2, y_pos), aprendizaje[1], fill=color_texto, font=font_text, anchor="mm")
    y_pos += 30

# Diagrama del flujo completo
flujo_y = 400
nodo_size = 60
spacing_h = 120
spacing_v = 80

# Nodo Webhook
webhook_x = width//2 - spacing_h*2
draw6.rounded_rectangle([(webhook_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (webhook_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill='#5096F3', outline=color_exito, width=3)
draw6.text((webhook_x, flujo_y), "Webhook", fill='white', font=font_small, anchor="mm")
draw6.text((webhook_x-nodo_size//2+15, flujo_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo Google Sheets
sheets_x = width//2 - spacing_h
draw6.rounded_rectangle([(sheets_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (sheets_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill=color_sheets, outline=color_exito, width=3)
draw6.text((sheets_x, flujo_y-10), "Google", fill='white', font=font_small, anchor="mm")
draw6.text((sheets_x, flujo_y+10), "Sheets", fill='white', font=font_small, anchor="mm")
draw6.text((sheets_x-nodo_size//2+15, flujo_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo IF
if_x = width//2
draw6.rounded_rectangle([(if_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (if_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill='#9C27B0', outline=color_exito, width=3)
draw6.text((if_x, flujo_y), "IF", fill='white', font=font_text, anchor="mm")
draw6.text((if_x-nodo_size//2+15, flujo_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo Send Email
email_x = width//2 + spacing_h
email_y = flujo_y - spacing_v
draw6.rounded_rectangle([(email_x-nodo_size//2, email_y-nodo_size//2), 
                        (email_x+nodo_size//2, email_y+nodo_size//2)], 
                       radius=15, fill=color_email, outline=color_exito, width=3)
draw6.text((email_x, email_y-10), "Send", fill='white', font=font_small, anchor="mm")
draw6.text((email_x, email_y+10), "Email", fill='white', font=font_small, anchor="mm")
draw6.text((email_x-nodo_size//2+15, email_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Nodo NoOp (rama false)
noop_x = width//2 + spacing_h
noop_y = flujo_y + spacing_v
draw6.rounded_rectangle([(noop_x-nodo_size//2, noop_y-nodo_size//2), 
                        (noop_x+nodo_size//2, noop_y+nodo_size//2)], 
                       radius=15, fill='#607D8B', outline=color_exito, width=3)
draw6.text((noop_x, noop_y), "NoOp", fill='white', font=font_small, anchor="mm")
draw6.text((noop_x-nodo_size//2+15, noop_y-nodo_size//2+15), "✓", 
          fill=color_exito, font=font_text, anchor="mm")

# Conexiones entre nodos
# Webhook a Google Sheets
draw6.line([(webhook_x+nodo_size//2, flujo_y), (sheets_x-nodo_size//2, flujo_y)], 
          fill=color_conexion, width=3)
draw6.polygon([(sheets_x-nodo_size//2, flujo_y), 
              (sheets_x-nodo_size//2-10, flujo_y-5), 
              (sheets_x-nodo_size//2-10, flujo_y+5)], 
             fill=color_conexion)

# Google Sheets a IF
draw6.line([(sheets_x+nodo_size//2, flujo_y), (if_x-nodo_size//2, flujo_y)], 
          fill=color_conexion, width=3)
draw6.polygon([(if_x-nodo_size//2, flujo_y), 
              (if_x-nodo_size//2-10, flujo_y-5), 
              (if_x-nodo_size//2-10, flujo_y+5)], 
             fill=color_conexion)

# IF a Send Email (true)
draw6.line([(if_x, flujo_y-nodo_size//2), (if_x, email_y), (email_x-nodo_size//2, email_y)], 
          fill=color_conexion, width=3)
draw6.polygon([(email_x-nodo_size//2, email_y), 
              (email_x-nodo_size//2-10, email_y-5), 
              (email_x-nodo_size//2-10, email_y+5)], 
             fill=color_conexion)

# IF a NoOp (false)
draw6.line([(if_x, flujo_y+nodo_size//2), (if_x, noop_y), (noop_x-nodo_size//2, noop_y)], 
          fill=color_conexion, width=3)
draw6.polygon([(noop_x-nodo_size//2, noop_y), 
              (noop_x-nodo_size//2-10, noop_y-5), 
              (noop_x-nodo_size//2-10, noop_y+5)], 
             fill=color_conexion)

# Resultado final
resultado_y = 550
draw6.rounded_rectangle([(width//2-300, resultado_y-60), (width//2+300, resultado_y+60)], 
                       radius=10, fill='#E8F5E9', outline=color_exito)
draw6.text((width//2, resultado_y-30), "Sistema de seguimiento de leads completado", 
          fill=color_texto, font=font_text, anchor="mm")
draw6.text((width//2, resultado_y), "Captura de datos → Almacenamiento → Seguimiento automático", 
          fill=color_texto, font=font_text, anchor="mm")
draw6.text((width//2, resultado_y+30), "¡Listo para usar en un entorno real!", 
          fill=color_exito, font=font_text, anchor="mm")

# Próximos pasos
draw6.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw6.text((width//2, 675), "Próximos pasos: Añade más nodos para clasificar leads y enviar notificaciones al equipo", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la sexta imagen
img6.save(os.path.join(output_dir, 'paso6_completado.png'))

# Crear un archivo de instrucciones
instrucciones_path = os.path.join(output_dir, 'instrucciones.md')
with open(instrucciones_path, 'w') as f:
    f.write("""# Ejercicio 1: Automatización de seguimiento de clientes potenciales

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
""")

print(f"Materiales para el Ejercicio 1 del Módulo 6 generados en {output_dir}")
