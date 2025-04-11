"""
Script para generar imágenes para la Animación 2: Tour por la Interfaz de n8n
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/materiales_visuales/modulo1/animacion2'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_resaltado = '#FF5722'    # Naranja
color_panel = '#FFFFFF'        # Blanco
color_canvas = '#FAFAFA'       # Gris muy claro
color_nodo = '#4CAF50'         # Verde
color_conexion = '#2196F3'     # Azul
color_etiqueta = '#FFC107'     # Amarillo

# Función para crear imagen base de la interfaz de n8n
def crear_interfaz_base(width=1200, height=800):
    img = Image.new('RGB', (width, height), color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Panel izquierdo
    draw.rectangle([(0, 0), (200, height)], fill=color_panel, outline='#CCCCCC')
    
    # Canvas central
    draw.rectangle([(200, 60), (width-300, height)], fill=color_canvas, outline='#CCCCCC')
    
    # Panel derecho
    draw.rectangle([(width-300, 0), (width, height)], fill=color_panel, outline='#CCCCCC')
    
    # Barra superior
    draw.rectangle([(0, 0), (width, 60)], fill=color_panel, outline='#CCCCCC')
    
    # Panel inferior (ejecución)
    draw.rectangle([(200, height-150), (width-300, height)], fill=color_panel, outline='#CCCCCC')
    
    return img, draw, width, height

# Escena 1: Vista General de la Interfaz
img1, draw1, width, height = crear_interfaz_base()
# Usar fuentes disponibles en el sistema
try:
    font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    font_subtitle = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    font_text = ImageFont.truetype("DejaVuSans.ttf", 18)
except OSError:
    # Usar fuentes por defecto si las específicas no están disponibles
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Título
draw1.text((600, 30), "Exploremos la interfaz de n8n", fill=color_texto, font=font_title, anchor="mm")

# Etiquetas para las secciones principales
draw1.text((100, 100), "Panel de", fill=color_texto, font=font_subtitle, anchor="mm")
draw1.text((100, 130), "Navegación", fill=color_texto, font=font_subtitle, anchor="mm")

draw1.text((550, 200), "Canvas", fill=color_texto, font=font_subtitle, anchor="mm")
draw1.text((550, 230), "Área de Diseño", fill=color_texto, font=font_subtitle, anchor="mm")

draw1.text((1050, 100), "Panel de", fill=color_texto, font=font_subtitle, anchor="mm")
draw1.text((1050, 130), "Configuración", fill=color_texto, font=font_subtitle, anchor="mm")

draw1.text((550, height-120), "Panel de Ejecución", fill=color_texto, font=font_subtitle, anchor="mm")

# Guardar la primera escena
img1.save(os.path.join(output_dir, 'escena1_vista_general.png'))

# Escena 2: Panel Izquierdo Resaltado
img2, draw2, width, height = crear_interfaz_base()
draw2.rectangle([(0, 0), (200, height)], fill=color_panel, outline=color_resaltado, width=3)

# Título
draw2.text((600, 30), "Panel Izquierdo: Navegación", fill=color_texto, font=font_title, anchor="mm")

# Elementos del panel izquierdo
elementos = [
    ("Workflows", 120),
    ("Templates", 170),
    ("Credentials", 220),
    ("Variables", 270),
    ("Settings", 320)
]

for texto, y in elementos:
    draw2.text((100, y), texto, fill=color_texto, font=font_text, anchor="mm")
    # Línea conectora a la descripción
    draw2.line([(150, y), (250, y)], fill=color_resaltado, width=2)
    
# Descripciones
descripciones = [
    ("Gestión de flujos de trabajo", 120),
    ("Plantillas predefinidas", 170),
    ("Conexiones seguras", 220),
    ("Variables globales", 270),
    ("Configuración general", 320)
]

for texto, y in descripciones:
    draw2.text((400, y), texto, fill=color_texto, font=font_text, anchor="mm")

# Guardar la segunda escena
img2.save(os.path.join(output_dir, 'escena2_panel_izquierdo.png'))

# Escena 3: Canvas Central Resaltado
img3, draw3, width, height = crear_interfaz_base()
draw3.rectangle([(200, 60), (width-300, height-150)], fill=color_canvas, outline=color_resaltado, width=3)

# Título
draw3.text((600, 30), "Canvas: Donde construyes tus flujos", fill=color_texto, font=font_title, anchor="mm")

# Añadir algunos nodos de ejemplo en el canvas
# Nodo 1: Trigger
draw3.rounded_rectangle([(300, 200), (400, 250)], radius=10, fill=color_nodo, outline=color_texto)
draw3.text((350, 225), "Trigger", fill='white', font=font_text, anchor="mm")

# Nodo 2: Action
draw3.rounded_rectangle([(500, 200), (600, 250)], radius=10, fill=color_conexion, outline=color_texto)
draw3.text((550, 225), "Action", fill='white', font=font_text, anchor="mm")

# Conexión entre nodos
draw3.line([(400, 225), (500, 225)], fill=color_texto, width=2)
draw3.polygon([(490, 220), (500, 225), (490, 230)], fill=color_texto)

# Texto explicativo
draw3.text((550, 350), "Diseña visualmente tus automatizaciones", fill=color_texto, font=font_subtitle, anchor="mm")
draw3.text((550, 380), "conectando nodos que representan acciones", fill=color_texto, font=font_text, anchor="mm")

# Guardar la tercera escena
img3.save(os.path.join(output_dir, 'escena3_canvas.png'))

# Escena 4: Panel Derecho Resaltado
img4, draw4, width, height = crear_interfaz_base()
draw4.rectangle([(width-300, 0), (width, height)], fill=color_panel, outline=color_resaltado, width=3)

# Título
draw4.text((600, 30), "Panel de Configuración de Nodos", fill=color_texto, font=font_title, anchor="mm")

# Simular panel de configuración
draw4.text((width-150, 100), "Configuración", fill=color_texto, font=font_subtitle, anchor="mm")

# Campos de configuración
campos = [
    ("Nombre:", "Mi Nodo", 150),
    ("Operación:", "Enviar Email", 200),
    ("Destinatario:", "usuario@ejemplo.com", 250),
    ("Asunto:", "Notificación Automática", 300),
    ("Contenido:", "Mensaje personalizado...", 350)
]

for label, valor, y in campos:
    draw4.text((width-250, y), label, fill=color_texto, font=font_text, anchor="mm")
    draw4.rounded_rectangle([(width-230, y+10), (width-50, y+30)], radius=5, fill='white', outline='#CCCCCC')
    draw4.text((width-140, y+20), valor, fill='#666666', font=ImageFont.truetype("DejaVuSans.ttf", 14), anchor="mm")

# Líneas conectoras desde un nodo en el canvas
draw4.rounded_rectangle([(600, 250), (700, 300)], radius=10, fill=color_conexion, outline=color_texto)
draw4.text((650, 275), "Email", fill='white', font=font_text, anchor="mm")
draw4.line([(700, 275), (width-300, 275)], fill=color_resaltado, width=2, joint="curve")
draw4.polygon([(width-310, 270), (width-300, 275), (width-310, 280)], fill=color_resaltado)

# Guardar la cuarta escena
img4.save(os.path.join(output_dir, 'escena4_panel_derecho.png'))

# Escena 5: Barra Superior Resaltada
img5, draw5, width, height = crear_interfaz_base()
draw5.rectangle([(0, 0), (width, 60)], fill=color_panel, outline=color_resaltado, width=3)

# Título
draw5.text((600, 30), "Barra de Herramientas Superior", fill=color_texto, font=font_title, anchor="mm")

# Elementos de la barra superior
elementos_barra = [
    ("Mi Workflow", 150, "Nombre del workflow"),
    ("Guardar", 300, "Guardar cambios"),
    ("Activar", 450, "Activar/desactivar workflow"),
    ("Ejecutar", 600, "Ejecutar workflow")
]

# Dibujar elementos en la barra y sus descripciones
for texto, x, descripcion in elementos_barra:
    # Simular botón o elemento en la barra
    draw5.rounded_rectangle([(x-50, 80), (x+50, 110)], radius=5, fill='white', outline='#CCCCCC')
    draw5.text((x, 95), texto, fill=color_texto, font=font_text, anchor="mm")
    
    # Línea conectora
    draw5.line([(x, 110), (x, 140)], fill=color_resaltado, width=2)
    
    # Descripción
    draw5.text((x, 160), descripcion, fill=color_texto, font=font_text, anchor="mm")

# Guardar la quinta escena
img5.save(os.path.join(output_dir, 'escena5_barra_superior.png'))

# Escena 6: Panel de Ejecución Resaltado
img6, draw6, width, height = crear_interfaz_base()
draw6.rectangle([(200, height-150), (width-300, height)], fill=color_panel, outline=color_resaltado, width=3)

# Título
draw6.text((600, 30), "Panel de Ejecución: Visualiza Resultados", fill=color_texto, font=font_title, anchor="mm")

# Simular datos de ejecución
draw6.text((550, height-120), "Resultados de Ejecución", fill=color_texto, font=font_subtitle, anchor="mm")

# Simular JSON de resultado
json_result = """
{
  "resultado": "éxito",
  "datos": {
    "id": 12345,
    "mensaje": "Operación completada",
    "timestamp": "2025-04-11T14:30:00Z"
  }
}
"""

# Dibujar cuadro de código
draw6.rectangle([(300, height-100), (800, height-20)], fill='#263238', outline='#CCCCCC')
lines = json_result.strip().split('\n')
for i, line in enumerate(lines):
    try:
        mono_font = ImageFont.truetype("DejaVuSans-Mono.ttf", 14)
    except OSError:
        mono_font = ImageFont.load_default()
    draw6.text((310, height-95+i*15), line, fill='#FFFFFF', font=mono_font)

# Texto explicativo
draw6.text((550, 400), "Visualiza los datos que produce cada nodo", fill=color_texto, font=font_text, anchor="mm")
draw6.text((550, 430), "para depurar y verificar tu flujo de trabajo", fill=color_texto, font=font_text, anchor="mm")

# Guardar la sexta escena
img6.save(os.path.join(output_dir, 'escena6_panel_ejecucion.png'))

print(f"Imágenes generadas en {output_dir}")
