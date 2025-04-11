"""
Script para generar imágenes para la Animación 1 del Módulo 3: Integración con Google Sheets
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/materiales_visuales/modulo3/animacion1'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_google = '#0F9D58'       # Verde Google
color_n8n = '#FF6D00'          # Naranja n8n
color_sheets = '#0F9D58'       # Verde para Sheets
color_docs = '#4285F4'         # Azul para Docs
color_gmail = '#D14836'        # Rojo para Gmail
color_drive = '#FFBA00'        # Amarillo para Drive
color_conexion = '#9E9E9E'     # Gris para conexiones

# Función para crear imagen base
def crear_imagen_base(width=1200, height=800):
    img = Image.new('RGB', (width, height), color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Título
    try:
        font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    except OSError:
        font_title = ImageFont.load_default()
    
    draw.text((width//2, 50), "Integración con Google Sheets", fill=color_texto, font=font_title, anchor="mm")
    
    return img, draw, width, height

# Escena 1: Introducción a la Integración
img1, draw1, width, height = crear_imagen_base()

# Cargar fuentes
try:
    font_subtitle = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    font_text = ImageFont.truetype("DejaVuSans.ttf", 18)
except OSError:
    font_subtitle = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Subtítulo
draw1.text((width//2, 100), "Conectando n8n con Google Sheets", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar logos
logo_size = 120
logo_y = 250

# Logo n8n (representado como un cuadrado naranja con "n8n")
n8n_x = width//3
draw1.rounded_rectangle([(n8n_x-logo_size//2, logo_y-logo_size//2), 
                        (n8n_x+logo_size//2, logo_y+logo_size//2)], 
                       radius=15, fill=color_n8n, outline=color_texto)
draw1.text((n8n_x, logo_y), "n8n", fill='white', font=font_subtitle, anchor="mm")

# Logo Google Sheets (representado como un cuadrado verde con ícono de tabla)
sheets_x = 2*width//3
draw1.rounded_rectangle([(sheets_x-logo_size//2, logo_y-logo_size//2), 
                        (sheets_x+logo_size//2, logo_y+logo_size//2)], 
                       radius=15, fill=color_sheets, outline=color_texto)

# Dibujar ícono de tabla simplificado
table_size = 60
table_x = sheets_x - table_size//2
table_y = logo_y - table_size//2
# Fondo blanco para la tabla
draw1.rectangle([(table_x, table_y), (table_x+table_size, table_y+table_size)], fill='white')
# Líneas horizontales
draw1.line([(table_x, table_y+table_size//3), (table_x+table_size, table_y+table_size//3)], fill='black', width=2)
draw1.line([(table_x, table_y+2*table_size//3), (table_x+table_size, table_y+2*table_size//3)], fill='black', width=2)
# Líneas verticales
draw1.line([(table_x+table_size//3, table_y), (table_x+table_size//3, table_y+table_size)], fill='black', width=2)
draw1.line([(table_x+2*table_size//3, table_y), (table_x+2*table_size//3, table_y+table_size)], fill='black', width=2)

# Flecha bidireccional entre logos
arrow_y = logo_y
draw1.line([(n8n_x+logo_size//2+10, arrow_y), (sheets_x-logo_size//2-10, arrow_y)], fill=color_texto, width=3)
# Puntas de flecha
arrow_size = 10
draw1.polygon([(sheets_x-logo_size//2-10, arrow_y), 
              (sheets_x-logo_size//2-10-arrow_size, arrow_y-arrow_size//2), 
              (sheets_x-logo_size//2-10-arrow_size, arrow_y+arrow_size//2)], 
             fill=color_texto)
draw1.polygon([(n8n_x+logo_size//2+10, arrow_y), 
              (n8n_x+logo_size//2+10+arrow_size, arrow_y-arrow_size//2), 
              (n8n_x+logo_size//2+10+arrow_size, arrow_y+arrow_size//2)], 
             fill=color_texto)

# Texto explicativo
draw1.text((width//2, 400), "n8n puede conectarse con Google Sheets para:", 
          fill=color_texto, font=font_text, anchor="mm")

# Lista de capacidades
capacidades = [
    "Leer datos de hojas de cálculo",
    "Escribir información en celdas",
    "Actualizar registros existentes",
    "Eliminar filas",
    "Crear nuevas hojas"
]

for i, capacidad in enumerate(capacidades):
    y_pos = 450 + i*40
    # Punto de viñeta
    draw1.ellipse([(width//2-200, y_pos-5), (width//2-190, y_pos+5)], fill=color_n8n)
    # Texto
    draw1.text((width//2-170, y_pos), capacidad, fill=color_texto, font=font_text, anchor="lm")

# Guardar la primera escena
img1.save(os.path.join(output_dir, 'escena1_introduccion.png'))

# Escena 2: Configuración de Credenciales
img2, draw2, width, height = crear_imagen_base()

# Subtítulo
draw2.text((width//2, 100), "Configuración de Credenciales OAuth", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar proceso de configuración
# Paso 1: Google Cloud Console
paso1_x = 200
paso1_y = 200
draw2.rounded_rectangle([(paso1_x-100, paso1_y-50), (paso1_x+100, paso1_y+50)], 
                       radius=10, fill='white', outline=color_texto)
draw2.text((paso1_x, paso1_y-20), "Google Cloud", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso1_x, paso1_y+10), "Console", fill=color_texto, font=font_text, anchor="mm")

# Paso 2: Crear Credenciales
paso2_x = width//2
paso2_y = 200
draw2.rounded_rectangle([(paso2_x-100, paso2_y-50), (paso2_x+100, paso2_y+50)], 
                       radius=10, fill='white', outline=color_texto)
draw2.text((paso2_x, paso2_y-20), "Crear", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso2_x, paso2_y+10), "Credenciales", fill=color_texto, font=font_text, anchor="mm")

# Paso 3: Configurar en n8n
paso3_x = width-200
paso3_y = 200
draw2.rounded_rectangle([(paso3_x-100, paso3_y-50), (paso3_x+100, paso3_y+50)], 
                       radius=10, fill='white', outline=color_texto)
draw2.text((paso3_x, paso3_y-20), "Configurar en", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso3_x, paso3_y+10), "n8n", fill=color_texto, font=font_text, anchor="mm")

# Flechas entre pasos
draw2.line([(paso1_x+100, paso1_y), (paso2_x-100, paso2_y)], fill=color_texto, width=2)
draw2.polygon([(paso2_x-100, paso2_y), (paso2_x-110, paso2_y-5), (paso2_x-110, paso2_y+5)], fill=color_texto)

draw2.line([(paso2_x+100, paso2_y), (paso3_x-100, paso3_y)], fill=color_texto, width=2)
draw2.polygon([(paso3_x-100, paso3_y), (paso3_x-110, paso3_y-5), (paso3_x-110, paso3_y+5)], fill=color_texto)

# Detalles de configuración
# Google Cloud Console
detalles_y_start = 300
draw2.text((paso1_x, detalles_y_start), "1. Crear proyecto", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso1_x, detalles_y_start+30), "2. Activar APIs:", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso1_x, detalles_y_start+60), "   - Google Sheets", fill=color_sheets, font=font_text, anchor="mm")
draw2.text((paso1_x, detalles_y_start+90), "   - Google Drive", fill=color_drive, font=font_text, anchor="mm")

# Crear Credenciales
draw2.text((paso2_x, detalles_y_start), "1. Tipo: OAuth 2.0", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso2_x, detalles_y_start+30), "2. Configurar pantalla", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso2_x, detalles_y_start+60), "   de consentimiento", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso2_x, detalles_y_start+90), "3. Obtener Client ID", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso2_x, detalles_y_start+120), "   y Client Secret", fill=color_texto, font=font_text, anchor="mm")

# Configurar en n8n
draw2.text((paso3_x, detalles_y_start), "1. Ir a Credentials", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso3_x, detalles_y_start+30), "2. Crear nueva", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso3_x, detalles_y_start+60), "3. Seleccionar", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso3_x, detalles_y_start+90), "   Google Sheets", fill=color_sheets, font=font_text, anchor="mm")
draw2.text((paso3_x, detalles_y_start+120), "4. Pegar credenciales", fill=color_texto, font=font_text, anchor="mm")
draw2.text((paso3_x, detalles_y_start+150), "5. Autorizar", fill=color_texto, font=font_text, anchor="mm")

# Resultado final
resultado_y = 600
draw2.rounded_rectangle([(width//2-200, resultado_y-40), (width//2+200, resultado_y+40)], 
                       radius=10, fill='#E8F5E9', outline=color_google)
draw2.text((width//2, resultado_y), "¡Conexión establecida con Google Sheets!", 
          fill=color_google, font=font_subtitle, anchor="mm")

# Guardar la segunda escena
img2.save(os.path.join(output_dir, 'escena2_credenciales.png'))

# Escena 3: Operaciones CRUD
img3, draw3, width, height = crear_imagen_base()

# Subtítulo
draw3.text((width//2, 100), "Operaciones CRUD con Google Sheets", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar tabla de Google Sheets
table_width = 600
table_height = 300
table_x = (width - table_width) // 2
table_y = 180
cell_height = 50
header_height = 60

# Fondo de la tabla
draw3.rectangle([(table_x, table_y), (table_x+table_width, table_y+table_height)], 
               fill='white', outline=color_texto)

# Encabezado
draw3.rectangle([(table_x, table_y), (table_x+table_width, table_y+header_height)], 
               fill='#E8F5E9', outline=color_texto)

# Columnas
col_width = table_width // 4
for i in range(1, 4):
    col_x = table_x + i * col_width
    draw3.line([(col_x, table_y), (col_x, table_y+table_height)], fill=color_texto, width=1)

# Filas
for i in range(1, 5):
    row_y = table_y + header_height + (i-1) * cell_height
    draw3.line([(table_x, row_y), (table_x+table_width, row_y)], fill=color_texto, width=1)

# Títulos de columnas
draw3.text((table_x+col_width//2, table_y+header_height//2), "ID", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((table_x+col_width+col_width//2, table_y+header_height//2), "Nombre", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((table_x+2*col_width+col_width//2, table_y+header_height//2), "Email", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((table_x+3*col_width+col_width//2, table_y+header_height//2), "Teléfono", 
          fill=color_texto, font=font_text, anchor="mm")

# Datos de ejemplo
datos = [
    ["1", "Ana García", "ana@ejemplo.com", "555-1234"],
    ["2", "Carlos López", "carlos@ejemplo.com", "555-5678"],
    ["3", "Elena Martín", "elena@ejemplo.com", "555-9012"],
    ["4", "David Sánchez", "david@ejemplo.com", "555-3456"]
]

for i, fila in enumerate(datos):
    row_y_center = table_y + header_height + i * cell_height + cell_height//2
    for j, valor in enumerate(fila):
        col_x_center = table_x + j * col_width + col_width//2
        draw3.text((col_x_center, row_y_center), valor, 
                  fill=color_texto, font=font_text, anchor="mm")

# Operaciones CRUD alrededor de la tabla
# CREATE
create_x = table_x - 150
create_y = table_y + 50
draw3.rounded_rectangle([(create_x-70, create_y-30), (create_x+70, create_y+30)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw3.text((create_x, create_y), "CREATE", fill='white', font=font_text, anchor="mm")
# Flecha
draw3.line([(create_x+70, create_y), (table_x-10, create_y)], fill=color_texto, width=2)
draw3.polygon([(table_x-10, create_y), (table_x-20, create_y-5), (table_x-20, create_y+5)], fill=color_texto)

# READ
read_x = table_x + table_width + 150
read_y = table_y + 50
draw3.rounded_rectangle([(read_x-70, read_y-30), (read_x+70, read_y+30)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw3.text((read_x, read_y), "READ", fill='white', font=font_text, anchor="mm")
# Flecha
draw3.line([(table_x+table_width+10, read_y), (read_x-70, read_y)], fill=color_texto, width=2)
draw3.polygon([(read_x-70, read_y), (read_x-60, read_y-5), (read_x-60, read_y+5)], fill=color_texto)

# UPDATE
update_x = table_x - 150
update_y = table_y + 150
draw3.rounded_rectangle([(update_x-70, update_y-30), (update_x+70, update_y+30)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw3.text((update_x, update_y), "UPDATE", fill='white', font=font_text, anchor="mm")
# Flecha bidireccional
draw3.line([(update_x+70, update_y), (table_x-10, update_y)], fill=color_texto, width=2)
draw3.polygon([(table_x-10, update_y), (table_x-20, update_y-5), (table_x-20, update_y+5)], fill=color_texto)
draw3.polygon([(update_x+70, update_y), (update_x+60, update_y-5), (update_x+60, update_y+5)], fill=color_texto)

# DELETE
delete_x = table_x - 150
delete_y = table_y + 250
draw3.rounded_rectangle([(delete_x-70, delete_y-30), (delete_x+70, delete_y+30)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw3.text((delete_x, delete_y), "DELETE", fill='white', font=font_text, anchor="mm")
# Flecha
draw3.line([(delete_x+70, delete_y), (table_x-10, delete_y)], fill=color_texto, width=2)
draw3.polygon([(table_x-10, delete_y), (table_x-20, delete_y-5), (table_x-20, delete_y+5)], fill=color_texto)

# Texto explicativo
draw3.text((width//2, 550), "n8n permite realizar todas las operaciones CRUD", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((width//2, 580), "(Crear, Leer, Actualizar, Eliminar) en Google Sheets", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((width//2, 610), "facilitando la gestión completa de datos", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la tercera escena
img3.save(os.path.join(output_dir, 'escena3_operaciones_crud.png'))

# Escena 4: Transformación de Datos
img4, draw4, width, height = crear_imagen_base()

# Subtítulo
draw4.text((width//2, 100), "Transformación de Datos", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar flujo de transformación
# Datos originales (Google Sheets)
original_x = 250
original_y = 250
draw4.rounded_rectangle([(original_x-150, original_y-100), (original_x+150, original_y+100)], 
                       radius=10, fill='white', outline=color_sheets)
draw4.text((original_x, original_y-80), "Datos en Google Sheets", 
          fill=color_sheets, font=font_text, anchor="mm")

# Tabla simple
table_width = 200
table_height = 120
table_x = original_x - table_width//2
table_y = original_y - 50
cell_height = 30

# Fondo de la tabla
draw4.rectangle([(table_x, table_y), (table_x+table_width, table_y+table_height)], 
               fill='white', outline=color_texto)

# Encabezado
draw4.rectangle([(table_x, table_y), (table_x+table_width, table_y+cell_height)], 
               fill='#E8F5E9', outline=color_texto)

# Columnas
col_width = table_width // 2
draw4.line([(table_x+col_width, table_y), (table_x+col_width, table_y+table_height)], 
          fill=color_texto, width=1)

# Filas
for i in range(1, 4):
    row_y = table_y + i * cell_height
    draw4.line([(table_x, row_y), (table_x+table_width, row_y)], fill=color_texto, width=1)

# Datos de ejemplo
draw4.text((table_x+col_width//2, table_y+cell_height//2), "fecha", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((table_x+col_width+col_width//2, table_y+cell_height//2), "ventas", 
          fill=color_texto, font=font_text, anchor="mm")

draw4.text((table_x+col_width//2, table_y+cell_height+cell_height//2), "2025-01-15", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((table_x+col_width+col_width//2, table_y+cell_height+cell_height//2), "1500", 
          fill=color_texto, font=font_text, anchor="mm")

draw4.text((table_x+col_width//2, table_y+2*cell_height+cell_height//2), "2025-02-20", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((table_x+col_width+col_width//2, table_y+2*cell_height+cell_height//2), "2300", 
          fill=color_texto, font=font_text, anchor="mm")

draw4.text((table_x+col_width//2, table_y+3*cell_height+cell_height//2), "2025-03-10", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((table_x+col_width+col_width//2, table_y+3*cell_height+cell_height//2), "1800", 
          fill=color_texto, font=font_text, anchor="mm")

# Nodo de transformación (n8n)
transform_x = width//2
transform_y = 250
draw4.rounded_rectangle([(transform_x-100, transform_y-60), (transform_x+100, transform_y+60)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw4.text((transform_x, transform_y-30), "Nodo Function", 
          fill='white', font=font_text, anchor="mm")
draw4.text((transform_x, transform_y), "en n8n", 
          fill='white', font=font_text, anchor="mm")
draw4.text((transform_x, transform_y+30), "Transformación", 
          fill='white', font=font_text, anchor="mm")

# Datos transformados
transformed_x = width - 250
transformed_y = 250
draw4.rounded_rectangle([(transformed_x-150, transformed_y-100), (transformed_x+150, transformed_y+100)], 
                       radius=10, fill='white', outline=color_n8n)
draw4.text((transformed_x, transformed_y-80), "Datos Transformados", 
          fill=color_n8n, font=font_text, anchor="mm")

# JSON transformado
json_width = 250
json_height = 140
json_x = transformed_x - json_width//2
json_y = transformed_y - 50

# Fondo del JSON
draw4.rectangle([(json_x, json_y), (json_x+json_width, json_y+json_height)], 
               fill='#FFFDE7', outline=color_texto)

# Texto del JSON
try:
    mono_font = ImageFont.truetype("DejaVuSans-Mono.ttf", 14)
except OSError:
    mono_font = ImageFont.load_default()

json_text = [
    '{',
    '  "resumen": {',
    '    "total": 5600,',
    '    "promedio": 1866.67,',
    '    "meses": 3,',
    '    "tendencia": "positiva"',
    '  }',
    '}'
]

for i, line in enumerate(json_text):
    draw4.text((json_x+10, json_y+10+i*15), line, fill=color_texto, font=mono_font)

# Flechas de flujo
# De datos originales a transformación
draw4.line([(original_x+150, original_y), (transform_x-100, transform_y)], 
          fill=color_texto, width=2)
draw4.polygon([(transform_x-100, transform_y), 
              (transform_x-110, transform_y-5), 
              (transform_x-110, transform_y+5)], 
             fill=color_texto)

# De transformación a datos transformados
draw4.line([(transform_x+100, transform_y), (transformed_x-150, transformed_y)], 
          fill=color_texto, width=2)
draw4.polygon([(transformed_x-150, transformed_y), 
              (transformed_x-140, transformed_y-5), 
              (transformed_x-140, transformed_y+5)], 
             fill=color_texto)

# Código de ejemplo
code_x = transform_x
code_y = transform_y + 150
code_width = 400
code_height = 120

# Fondo del código
draw4.rectangle([(code_x-code_width//2, code_y-code_height//2), 
                (code_x+code_width//2, code_y+code_height//2)], 
               fill='#263238', outline=color_texto)

# Texto del código
code_text = [
    'const ventas = $input.all.map(item => parseInt(item.json.ventas));',
    'const total = ventas.reduce((sum, val) => sum + val, 0);',
    'const promedio = total / ventas.length;',
    '',
    'return {',
    '  json: {',
    '    resumen: { total, promedio, meses: ventas.length,',
    '               tendencia: promedio > 1500 ? "positiva" : "negativa" }',
    '  }',
    '};'
]

for i, line in enumerate(code_text):
    draw4.text((code_x-code_width//2+10, code_y-code_height//2+10+i*12), 
              line, fill='#FFFFFF', font=mono_font)

# Texto explicativo
draw4.text((width//2, 450), "n8n permite transformar los datos de Google Sheets", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((width//2, 480), "mediante código JavaScript o nodos especializados", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((width//2, 510), "para obtener exactamente el formato que necesitas", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la cuarta escena
img4.save(os.path.join(output_dir, 'escena4_transformacion_datos.png'))

# Escena 5: Casos de Uso Prácticos
img5, draw5, width, height = crear_imagen_base()

# Subtítulo
draw5.text((width//2, 100), "Casos de Uso Prácticos", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar casos de uso
caso_width = 220
caso_height = 150
caso_y = 250
padding = 30

# Caso 1: CRM
caso1_x = width//4
draw5.rounded_rectangle([(caso1_x-caso_width//2, caso_y-caso_height//2), 
                        (caso1_x+caso_width//2, caso_y+caso_height//2)], 
                       radius=10, fill='white', outline=color_sheets)
draw5.text((caso1_x, caso_y-caso_height//2+padding), "CRM Simple", 
          fill=color_sheets, font=font_text, anchor="mm")

# Iconos simplificados para CRM
# Persona
person_x = caso1_x - 50
person_y = caso_y
draw5.ellipse([(person_x-15, person_y-15), (person_x+15, person_y+15)], 
             fill=color_sheets)
draw5.rectangle([(person_x-20, person_y+20), (person_x+20, person_y+50)], 
               fill=color_sheets)

# Documento
doc_x = caso1_x + 50
doc_y = caso_y
draw5.rectangle([(doc_x-20, doc_y-30), (doc_x+20, doc_y+30)], 
               fill='white', outline=color_sheets)
# Líneas de texto
draw5.line([(doc_x-15, doc_y-20), (doc_x+15, doc_y-20)], fill=color_sheets, width=2)
draw5.line([(doc_x-15, doc_y-5), (doc_x+15, doc_y-5)], fill=color_sheets, width=2)
draw5.line([(doc_x-15, doc_y+10), (doc_x+15, doc_y+10)], fill=color_sheets, width=2)

# Texto descriptivo
draw5.text((caso1_x, caso_y+caso_height//2-padding), "Gestión de clientes", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((caso1_x, caso_y+caso_height//2-padding+20), "y seguimiento", 
          fill=color_texto, font=font_text, anchor="mm")

# Caso 2: Inventario
caso2_x = width//2
draw5.rounded_rectangle([(caso2_x-caso_width//2, caso_y-caso_height//2), 
                        (caso2_x+caso_width//2, caso_y+caso_height//2)], 
                       radius=10, fill='white', outline=color_sheets)
draw5.text((caso2_x, caso_y-caso_height//2+padding), "Control de Inventario", 
          fill=color_sheets, font=font_text, anchor="mm")

# Iconos simplificados para Inventario
# Caja
box_x = caso2_x - 50
box_y = caso_y
draw5.rectangle([(box_x-25, box_y-25), (box_x+25, box_y+25)], 
               fill='white', outline=color_sheets, width=2)
# Líneas de la caja
draw5.line([(box_x-25, box_y-10), (box_x+25, box_y-10)], fill=color_sheets, width=1)
draw5.line([(box_x, box_y-25), (box_x, box_y+25)], fill=color_sheets, width=1)

# Gráfico
graph_x = caso2_x + 50
graph_y = caso_y
# Ejes
draw5.line([(graph_x-20, graph_y+20), (graph_x-20, graph_y-20)], fill=color_sheets, width=2)
draw5.line([(graph_x-20, graph_y+20), (graph_x+20, graph_y+20)], fill=color_sheets, width=2)
# Barras
draw5.rectangle([(graph_x-15, graph_y), (graph_x-5, graph_y+19)], fill=color_sheets)
draw5.rectangle([(graph_x, graph_y-10), (graph_x+10, graph_y+19)], fill=color_sheets)

# Texto descriptivo
draw5.text((caso2_x, caso_y+caso_height//2-padding), "Seguimiento de stock", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((caso2_x, caso_y+caso_height//2-padding+20), "y pedidos", 
          fill=color_texto, font=font_text, anchor="mm")

# Caso 3: Reportes
caso3_x = 3*width//4
draw5.rounded_rectangle([(caso3_x-caso_width//2, caso_y-caso_height//2), 
                        (caso3_x+caso_width//2, caso_y+caso_height//2)], 
                       radius=10, fill='white', outline=color_sheets)
draw5.text((caso3_x, caso_y-caso_height//2+padding), "Reportes Automáticos", 
          fill=color_sheets, font=font_text, anchor="mm")

# Iconos simplificados para Reportes
# Gráfico circular
pie_x = caso3_x - 50
pie_y = caso_y
draw5.ellipse([(pie_x-25, pie_y-25), (pie_x+25, pie_y+25)], 
             fill='white', outline=color_sheets, width=2)
# Divisiones del gráfico
draw5.pieslice([(pie_x-25, pie_y-25), (pie_x+25, pie_y+25)], 
              start=0, end=90, fill=color_sheets, outline=color_sheets)
draw5.pieslice([(pie_x-25, pie_y-25), (pie_x+25, pie_y+25)], 
              start=180, end=270, fill=color_sheets, outline=color_sheets)

# Email
email_x = caso3_x + 50
email_y = caso_y
# Sobre
draw5.rectangle([(email_x-25, email_y-15), (email_x+25, email_y+15)], 
               fill='white', outline=color_sheets, width=2)
# Línea diagonal del sobre
draw5.line([(email_x-25, email_y-15), (email_x, email_y)], fill=color_sheets, width=1)
draw5.line([(email_x+25, email_y-15), (email_x, email_y)], fill=color_sheets, width=1)

# Texto descriptivo
draw5.text((caso3_x, caso_y+caso_height//2-padding), "Generación y envío", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((caso3_x, caso_y+caso_height//2-padding+20), "automático de informes", 
          fill=color_texto, font=font_text, anchor="mm")

# Flujo de trabajo general
workflow_y = 500
# n8n en el centro
n8n_x = width//2
draw5.rounded_rectangle([(n8n_x-80, workflow_y-40), (n8n_x+80, workflow_y+40)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw5.text((n8n_x, workflow_y), "n8n", fill='white', font=font_subtitle, anchor="mm")

# Google Sheets a la izquierda
sheets_x = n8n_x - 250
draw5.rounded_rectangle([(sheets_x-100, workflow_y-40), (sheets_x+100, workflow_y+40)], 
                       radius=10, fill=color_sheets, outline=color_texto)
draw5.text((sheets_x, workflow_y), "Google Sheets", fill='white', font=font_text, anchor="mm")

# Aplicaciones a la derecha
apps_x = n8n_x + 250
draw5.rounded_rectangle([(apps_x-100, workflow_y-40), (apps_x+100, workflow_y+40)], 
                       radius=10, fill=color_texto, outline=color_texto)
draw5.text((apps_x, workflow_y), "Aplicaciones", fill='white', font=font_text, anchor="mm")

# Flechas bidireccionales
# Entre Sheets y n8n
draw5.line([(sheets_x+100, workflow_y), (n8n_x-80, workflow_y)], fill=color_texto, width=2)
draw5.polygon([(n8n_x-80, workflow_y), (n8n_x-90, workflow_y-5), (n8n_x-90, workflow_y+5)], fill=color_texto)
draw5.polygon([(sheets_x+100, workflow_y), (sheets_x+110, workflow_y-5), (sheets_x+110, workflow_y+5)], fill=color_texto)

# Entre n8n y aplicaciones
draw5.line([(n8n_x+80, workflow_y), (apps_x-100, workflow_y)], fill=color_texto, width=2)
draw5.polygon([(apps_x-100, workflow_y), (apps_x-110, workflow_y-5), (apps_x-110, workflow_y+5)], fill=color_texto)
draw5.polygon([(n8n_x+80, workflow_y), (n8n_x+90, workflow_y-5), (n8n_x+90, workflow_y+5)], fill=color_texto)

# Texto explicativo
draw5.text((width//2, 600), "Google Sheets combinado con n8n permite crear", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((width//2, 630), "soluciones completas para múltiples casos de uso", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((width//2, 660), "sin necesidad de programación compleja", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la quinta escena
img5.save(os.path.join(output_dir, 'escena5_casos_uso.png'))

print(f"Imágenes generadas en {output_dir}")
