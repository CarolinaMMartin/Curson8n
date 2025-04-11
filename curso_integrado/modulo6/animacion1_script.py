"""
Script para generar imágenes para la Animación 1 del Módulo 6: Caso Práctico de Marketing Automatizado
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/materiales_visuales/modulo6/animacion1'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_n8n = '#FF6D00'          # Naranja n8n
color_email = '#D14836'        # Rojo para Email
color_ecommerce = '#4CAF50'    # Verde para E-commerce
color_analytics = '#2196F3'    # Azul para Analytics
color_crm = '#9C27B0'          # Púrpura para CRM
color_conexion = '#9E9E9E'     # Gris para conexiones
color_cliente = '#FFC107'      # Amarillo para clientes

# Función para crear imagen base
def crear_imagen_base(width=1200, height=800):
    img = Image.new('RGB', (width, height), color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Título
    try:
        font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    except OSError:
        font_title = ImageFont.load_default()
    
    draw.text((width//2, 50), "Caso Práctico: Marketing Automatizado", fill=color_texto, font=font_title, anchor="mm")
    
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

# Escena 1: Visión General del Caso
img1, draw1, width, height = crear_imagen_base()

# Subtítulo
draw1.text((width//2, 100), "Automatización de Email Marketing para E-commerce", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar el flujo general
# E-commerce (Tienda)
ecommerce_x = 200
ecommerce_y = 250
draw1.rounded_rectangle([(ecommerce_x-80, ecommerce_y-50), (ecommerce_x+80, ecommerce_y+50)], 
                       radius=10, fill=color_ecommerce, outline=color_texto)
draw1.text((ecommerce_x, ecommerce_y), "Tienda Online", fill='white', font=font_text, anchor="mm")

# n8n (Centro)
n8n_x = width//2
n8n_y = 250
draw1.rounded_rectangle([(n8n_x-80, n8n_y-50), (n8n_x+80, n8n_y+50)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw1.text((n8n_x, n8n_y), "n8n", fill='white', font=font_text, anchor="mm")

# Email Marketing
email_x = width - 200
email_y = 250
draw1.rounded_rectangle([(email_x-80, email_y-50), (email_x+80, email_y+50)], 
                       radius=10, fill=color_email, outline=color_texto)
draw1.text((email_x, email_y), "Email Marketing", fill='white', font=font_text, anchor="mm")

# Conexiones
# E-commerce a n8n
draw1.line([(ecommerce_x+80, ecommerce_y), (n8n_x-80, n8n_y)], fill=color_conexion, width=2)
draw1.polygon([(n8n_x-80, n8n_y), (n8n_x-90, n8n_y-5), (n8n_x-90, n8n_y+5)], fill=color_conexion)

# n8n a Email
draw1.line([(n8n_x+80, n8n_y), (email_x-80, email_y)], fill=color_conexion, width=2)
draw1.polygon([(email_x-80, email_y), (email_x-90, email_y-5), (email_x-90, email_y+5)], fill=color_conexion)

# Clientes (abajo)
cliente_x = width//2
cliente_y = 450
draw1.rounded_rectangle([(cliente_x-100, cliente_y-50), (cliente_x+100, cliente_y+50)], 
                       radius=10, fill=color_cliente, outline=color_texto)
draw1.text((cliente_x, cliente_y), "Clientes", fill=color_texto, font=font_text, anchor="mm")

# Conexión bidireccional entre n8n y Clientes
draw1.line([(n8n_x, n8n_y+50), (cliente_x, cliente_y-50)], fill=color_conexion, width=2)
draw1.polygon([(cliente_x, cliente_y-50), (cliente_x-5, cliente_y-60), (cliente_x+5, cliente_y-60)], fill=color_conexion)
draw1.polygon([(n8n_x, n8n_y+50), (n8n_x-5, n8n_y+60), (n8n_x+5, n8n_y+60)], fill=color_conexion)

# Analytics (arriba)
analytics_x = width//2
analytics_y = 100
draw1.rounded_rectangle([(analytics_x-80, analytics_y-40), (analytics_x+80, analytics_y+40)], 
                       radius=10, fill=color_analytics, outline=color_texto)
draw1.text((analytics_x, analytics_y), "Analytics", fill='white', font=font_text, anchor="mm")

# Conexión bidireccional entre n8n y Analytics
draw1.line([(n8n_x, n8n_y-50), (analytics_x, analytics_y+40)], fill=color_conexion, width=2)
draw1.polygon([(analytics_x, analytics_y+40), (analytics_x-5, analytics_y+30), (analytics_x+5, analytics_y+30)], fill=color_conexion)
draw1.polygon([(n8n_x, n8n_y-50), (n8n_x-5, n8n_y-40), (n8n_x+5, n8n_y-40)], fill=color_conexion)

# Texto explicativo
draw1.text((width//2, 550), "Este caso práctico muestra cómo automatizar el marketing por email", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, 580), "para una tienda online, segmentando clientes y enviando", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, 610), "campañas personalizadas según su comportamiento", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la primera escena
img1.save(os.path.join(output_dir, 'escena1_vision_general.png'))

# Escena 2: Captura de Leads
img2, draw2, width, height = crear_imagen_base()

# Subtítulo
draw2.text((width//2, 100), "Captura de Leads desde Múltiples Fuentes", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar fuentes de leads
fuentes_y = 200
fuente_height = 60
fuente_width = 160
spacing = 50

# Fuente 1: Formulario Web
fuente1_x = 200
draw2.rounded_rectangle([(fuente1_x-fuente_width//2, fuentes_y-fuente_height//2), 
                        (fuente1_x+fuente_width//2, fuentes_y+fuente_height//2)], 
                       radius=10, fill='white', outline=color_texto)
draw2.text((fuente1_x, fuentes_y), "Formulario Web", fill=color_texto, font=font_text, anchor="mm")

# Fuente 2: Compras en Tienda
fuente2_x = width//2
draw2.rounded_rectangle([(fuente2_x-fuente_width//2, fuentes_y-fuente_height//2), 
                        (fuente2_x+fuente_width//2, fuentes_y+fuente_height//2)], 
                       radius=10, fill='white', outline=color_texto)
draw2.text((fuente2_x, fuentes_y), "Compras en Tienda", fill=color_texto, font=font_text, anchor="mm")

# Fuente 3: Redes Sociales
fuente3_x = width - 200
draw2.rounded_rectangle([(fuente3_x-fuente_width//2, fuentes_y-fuente_height//2), 
                        (fuente3_x+fuente_width//2, fuentes_y+fuente_height//2)], 
                       radius=10, fill='white', outline=color_texto)
draw2.text((fuente3_x, fuentes_y), "Redes Sociales", fill=color_texto, font=font_text, anchor="mm")

# n8n en el centro
n8n_y = 350
draw2.rounded_rectangle([(width//2-100, n8n_y-60), (width//2+100, n8n_y+60)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw2.text((width//2, n8n_y-20), "n8n", fill='white', font=font_text, anchor="mm")
draw2.text((width//2, n8n_y+20), "Captura de Leads", fill='white', font=font_text, anchor="mm")

# Conexiones desde fuentes a n8n
# Desde Formulario
draw2.line([(fuente1_x, fuentes_y+fuente_height//2), (fuente1_x, n8n_y-60)], fill=color_conexion, width=2)
draw2.line([(fuente1_x, n8n_y-60), (width//2-100, n8n_y)], fill=color_conexion, width=2)
draw2.polygon([(width//2-100, n8n_y), (width//2-110, n8n_y-5), (width//2-110, n8n_y+5)], fill=color_conexion)

# Desde Compras
draw2.line([(fuente2_x, fuentes_y+fuente_height//2), (fuente2_x, n8n_y-60)], fill=color_conexion, width=2)
draw2.polygon([(fuente2_x, n8n_y-60), (fuente2_x-5, n8n_y-70), (fuente2_x+5, n8n_y-70)], fill=color_conexion)

# Desde Redes
draw2.line([(fuente3_x, fuentes_y+fuente_height//2), (fuente3_x, n8n_y-60)], fill=color_conexion, width=2)
draw2.line([(fuente3_x, n8n_y-60), (width//2+100, n8n_y)], fill=color_conexion, width=2)
draw2.polygon([(width//2+100, n8n_y), (width//2+110, n8n_y-5), (width//2+110, n8n_y+5)], fill=color_conexion)

# Base de datos de clientes
db_y = 500
draw2.rounded_rectangle([(width//2-120, db_y-60), (width//2+120, db_y+60)], 
                       radius=10, fill=color_crm, outline=color_texto)
draw2.text((width//2, db_y-20), "Base de Datos", fill='white', font=font_text, anchor="mm")
draw2.text((width//2, db_y+20), "de Clientes", fill='white', font=font_text, anchor="mm")

# Conexión de n8n a base de datos
draw2.line([(width//2, n8n_y+60), (width//2, db_y-60)], fill=color_conexion, width=2)
draw2.polygon([(width//2, db_y-60), (width//2-5, db_y-70), (width//2+5, db_y-70)], fill=color_conexion)

# Datos capturados (a la derecha)
datos_x = width - 200
datos_y = 400
datos_width = 200
datos_height = 200

# Fondo para los datos
draw2.rounded_rectangle([(datos_x-datos_width//2, datos_y-datos_height//2), 
                        (datos_x+datos_width//2, datos_y+datos_height//2)], 
                       radius=10, fill='white', outline=color_texto)

# Título de los datos
draw2.text((datos_x, datos_y-datos_height//2+20), "Datos Capturados:", 
          fill=color_texto, font=font_text, anchor="mm")

# Lista de datos
datos = [
    "Nombre",
    "Email",
    "Teléfono",
    "Fuente",
    "Intereses",
    "Historial de compras",
    "Comportamiento web"
]

for i, dato in enumerate(datos):
    y_pos = datos_y - datos_height//2 + 50 + i*20
    draw2.text((datos_x-datos_width//2+20, y_pos), "• " + dato, 
              fill=color_texto, font=font_small, anchor="lm")

# Conexión de n8n a datos
draw2.line([(width//2+100, n8n_y), (datos_x-datos_width//2, datos_y)], fill=color_conexion, width=2)
draw2.polygon([(datos_x-datos_width//2, datos_y), 
              (datos_x-datos_width//2-10, datos_y-5), 
              (datos_x-datos_width//2-10, datos_y+5)], 
             fill=color_conexion)

# Texto explicativo
draw2.text((width//2, 650), "n8n captura leads de múltiples fuentes y los almacena", 
          fill=color_texto, font=font_text, anchor="mm")
draw2.text((width//2, 680), "en una base de datos centralizada para su posterior segmentación", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la segunda escena
img2.save(os.path.join(output_dir, 'escena2_captura_leads.png'))

# Escena 3: Segmentación Automática
img3, draw3, width, height = crear_imagen_base()

# Subtítulo
draw3.text((width//2, 100), "Segmentación Automática por Comportamiento", fill=color_texto, font=font_subtitle, anchor="mm")

# Base de datos de clientes (arriba)
db_y = 200
draw3.rounded_rectangle([(width//2-120, db_y-60), (width//2+120, db_y+60)], 
                       radius=10, fill=color_crm, outline=color_texto)
draw3.text((width//2, db_y-20), "Base de Datos", fill='white', font=font_text, anchor="mm")
draw3.text((width//2, db_y+20), "de Clientes", fill='white', font=font_text, anchor="mm")

# n8n en el centro
n8n_y = 350
draw3.rounded_rectangle([(width//2-100, n8n_y-60), (width//2+100, n8n_y+60)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw3.text((width//2, n8n_y-20), "n8n", fill='white', font=font_text, anchor="mm")
draw3.text((width//2, n8n_y+20), "Segmentación", fill='white', font=font_text, anchor="mm")

# Conexión de base de datos a n8n
draw3.line([(width//2, db_y+60), (width//2, n8n_y-60)], fill=color_conexion, width=2)
draw3.polygon([(width//2, n8n_y-60), (width//2-5, n8n_y-70), (width//2+5, n8n_y-70)], fill=color_conexion)

# Segmentos de clientes (abajo)
segment_y = 500
segment_width = 150
segment_height = 80
spacing = 50

# Segmento 1: Nuevos Clientes
segment1_x = width//4
draw3.rounded_rectangle([(segment1_x-segment_width//2, segment_y-segment_height//2), 
                        (segment1_x+segment_width//2, segment_y+segment_height//2)], 
                       radius=10, fill=color_cliente, outline=color_texto)
draw3.text((segment1_x, segment_y), "Nuevos Clientes", fill=color_texto, font=font_text, anchor="mm")

# Segmento 2: Clientes Activos
segment2_x = width//2
draw3.rounded_rectangle([(segment2_x-segment_width//2, segment_y-segment_height//2), 
                        (segment2_x+segment_width//2, segment_y+segment_height//2)], 
                       radius=10, fill=color_cliente, outline=color_texto)
draw3.text((segment2_x, segment_y), "Clientes Activos", fill=color_texto, font=font_text, anchor="mm")

# Segmento 3: Clientes Inactivos
segment3_x = 3*width//4
draw3.rounded_rectangle([(segment3_x-segment_width//2, segment_y-segment_height//2), 
                        (segment3_x+segment_width//2, segment_y+segment_height//2)], 
                       radius=10, fill=color_cliente, outline=color_texto)
draw3.text((segment3_x, segment_y), "Clientes Inactivos", fill=color_texto, font=font_text, anchor="mm")

# Conexiones de n8n a segmentos
# A Nuevos Clientes
draw3.line([(width//2-50, n8n_y+60), (segment1_x, segment_y-segment_height//2)], fill=color_conexion, width=2)
draw3.polygon([(segment1_x, segment_y-segment_height//2), 
              (segment1_x-5, segment_y-segment_height//2-10), 
              (segment1_x+5, segment_y-segment_height//2-10)], 
             fill=color_conexion)

# A Clientes Activos
draw3.line([(width//2, n8n_y+60), (segment2_x, segment_y-segment_height//2)], fill=color_conexion, width=2)
draw3.polygon([(segment2_x, segment_y-segment_height//2), 
              (segment2_x-5, segment_y-segment_height//2-10), 
              (segment2_x+5, segment_y-segment_height//2-10)], 
             fill=color_conexion)

# A Clientes Inactivos
draw3.line([(width//2+50, n8n_y+60), (segment3_x, segment_y-segment_height//2)], fill=color_conexion, width=2)
draw3.polygon([(segment3_x, segment_y-segment_height//2), 
              (segment3_x-5, segment_y-segment_height//2-10), 
              (segment3_x+5, segment_y-segment_height//2-10)], 
             fill=color_conexion)

# Criterios de segmentación (a la derecha)
criterios_x = width - 150
criterios_y = 350
criterios_width = 250
criterios_height = 250

# Fondo para los criterios
draw3.rounded_rectangle([(criterios_x-criterios_width//2, criterios_y-criterios_height//2), 
                        (criterios_x+criterios_width//2, criterios_y+criterios_height//2)], 
                       radius=10, fill='white', outline=color_texto)

# Título de los criterios
draw3.text((criterios_x, criterios_y-criterios_height//2+20), "Criterios de Segmentación:", 
          fill=color_texto, font=font_text, anchor="mm")

# Lista de criterios
criterios = [
    "Tiempo desde registro",
    "Última compra",
    "Frecuencia de compras",
    "Valor promedio",
    "Categorías visitadas",
    "Emails abiertos",
    "Enlaces clicados",
    "Carrito abandonado"
]

for i, criterio in enumerate(criterios):
    y_pos = criterios_y - criterios_height//2 + 50 + i*22
    draw3.text((criterios_x-criterios_width//2+20, y_pos), "• " + criterio, 
              fill=color_texto, font=font_small, anchor="lm")

# Conexión de n8n a criterios
draw3.line([(width//2+100, n8n_y), (criterios_x-criterios_width//2, criterios_y)], fill=color_conexion, width=2)
draw3.polygon([(criterios_x-criterios_width//2, criterios_y), 
              (criterios_x-criterios_width//2-10, criterios_y-5), 
              (criterios_x-criterios_width//2-10, criterios_y+5)], 
             fill=color_conexion)

# Texto explicativo
draw3.text((width//2, 620), "n8n analiza automáticamente el comportamiento de los clientes", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((width//2, 650), "y los segmenta en diferentes grupos para enviar", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((width//2, 680), "comunicaciones personalizadas y relevantes", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la tercera escena
img3.save(os.path.join(output_dir, 'escena3_segmentacion.png'))

# Escena 4: Secuencias de Emails Personalizados
img4, draw4, width, height = crear_imagen_base()

# Subtítulo
draw4.text((width//2, 100), "Secuencias de Emails Personalizados", fill=color_texto, font=font_subtitle, anchor="mm")

# n8n en el centro
n8n_y = 250
draw4.rounded_rectangle([(width//2-100, n8n_y-60), (width//2+100, n8n_y+60)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw4.text((width//2, n8n_y-20), "n8n", fill='white', font=font_text, anchor="mm")
draw4.text((width//2, n8n_y+20), "Automatización", fill='white', font=font_text, anchor="mm")

# Plataforma de Email
email_x = width - 200
email_y = 250
draw4.rounded_rectangle([(email_x-100, email_y-60), (email_x+100, email_y+60)], 
                       radius=10, fill=color_email, outline=color_texto)
draw4.text((email_x, email_y-20), "Plataforma de", fill='white', font=font_text, anchor="mm")
draw4.text((email_x, email_y+20), "Email Marketing", fill='white', font=font_text, anchor="mm")

# Conexión de n8n a plataforma de email
draw4.line([(width//2+100, n8n_y), (email_x-100, email_y)], fill=color_conexion, width=2)
draw4.polygon([(email_x-100, email_y), (email_x-110, email_y-5), (email_x-110, email_y+5)], fill=color_conexion)

# Secuencias de emails (abajo)
sequence_y_start = 400
sequence_height = 80
sequence_width = 180
sequence_spacing = 100

# Secuencia 1: Bienvenida
sequence1_y = sequence_y_start
draw4.rounded_rectangle([(width//2-sequence_width//2, sequence1_y-sequence_height//2), 
                        (width//2+sequence_width//2, sequence1_y+sequence_height//2)], 
                       radius=10, fill='white', outline=color_email)
draw4.text((width//2, sequence1_y-20), "Secuencia de", fill=color_email, font=font_text, anchor="mm")
draw4.text((width//2, sequence1_y+20), "Bienvenida", fill=color_email, font=font_text, anchor="mm")

# Secuencia 2: Reactivación
sequence2_y = sequence1_y + sequence_spacing
draw4.rounded_rectangle([(width//2-sequence_width//2, sequence2_y-sequence_height//2), 
                        (width//2+sequence_width//2, sequence2_y+sequence_height//2)], 
                       radius=10, fill='white', outline=color_email)
draw4.text((width//2, sequence2_y-20), "Secuencia de", fill=color_email, font=font_text, anchor="mm")
draw4.text((width//2, sequence2_y+20), "Reactivación", fill=color_email, font=font_text, anchor="mm")

# Conexiones de n8n a secuencias
draw4.line([(width//2, n8n_y+60), (width//2, sequence1_y-sequence_height//2)], fill=color_conexion, width=2)
draw4.polygon([(width//2, sequence1_y-sequence_height//2), 
              (width//2-5, sequence1_y-sequence_height//2-10), 
              (width//2+5, sequence1_y-sequence_height//2-10)], 
             fill=color_conexion)

draw4.line([(width//2, sequence1_y+sequence_height//2), (width//2, sequence2_y-sequence_height//2)], 
          fill=color_conexion, width=2)
draw4.polygon([(width//2, sequence2_y-sequence_height//2), 
              (width//2-5, sequence2_y-sequence_height//2-10), 
              (width//2+5, sequence2_y-sequence_height//2-10)], 
             fill=color_conexion)

# Emails de la secuencia (a la derecha)
email_template_x = width - 200
email_template_y = 450
email_width = 120
email_height = 80
email_spacing = 40

# Email 1
draw4.rectangle([(email_template_x-email_width//2, email_template_y-email_height//2), 
                (email_template_x+email_width//2, email_template_y+email_height//2)], 
               fill='white', outline=color_email)
draw4.text((email_template_x, email_template_y-20), "Email #1", fill=color_email, font=font_small, anchor="mm")
draw4.text((email_template_x, email_template_y+10), "Día 1", fill=color_email, font=font_small, anchor="mm")

# Email 2
email2_y = email_template_y + email_height + email_spacing//2
draw4.rectangle([(email_template_x-email_width//2, email2_y-email_height//2), 
                (email_template_x+email_width//2, email2_y+email_height//2)], 
               fill='white', outline=color_email)
draw4.text((email_template_x, email2_y-20), "Email #2", fill=color_email, font=font_small, anchor="mm")
draw4.text((email_template_x, email2_y+10), "Día 3", fill=color_email, font=font_small, anchor="mm")

# Email 3
email3_y = email2_y + email_height + email_spacing//2
draw4.rectangle([(email_template_x-email_width//2, email3_y-email_height//2), 
                (email_template_x+email_width//2, email3_y+email_height//2)], 
               fill='white', outline=color_email)
draw4.text((email_template_x, email3_y-20), "Email #3", fill=color_email, font=font_small, anchor="mm")
draw4.text((email_template_x, email3_y+10), "Día 7", fill=color_email, font=font_small, anchor="mm")

# Conexión de secuencia a emails
draw4.line([(width//2+sequence_width//2, sequence1_y), (email_template_x-email_width//2, email_template_y)], 
          fill=color_conexion, width=2)
draw4.polygon([(email_template_x-email_width//2, email_template_y), 
              (email_template_x-email_width//2-10, email_template_y-5), 
              (email_template_x-email_width//2-10, email_template_y+5)], 
             fill=color_conexion)

# Personalización (a la izquierda)
personalizacion_x = 200
personalizacion_y = 450
personalizacion_width = 250
personalizacion_height = 200

# Fondo para personalización
draw4.rounded_rectangle([(personalizacion_x-personalizacion_width//2, personalizacion_y-personalizacion_height//2), 
                        (personalizacion_x+personalizacion_width//2, personalizacion_y+personalizacion_height//2)], 
                       radius=10, fill='white', outline=color_texto)

# Título de personalización
draw4.text((personalizacion_x, personalizacion_y-personalizacion_height//2+20), "Personalización:", 
          fill=color_texto, font=font_text, anchor="mm")

# Lista de elementos personalizados
personalizaciones = [
    "Nombre del cliente",
    "Productos vistos",
    "Última compra",
    "Recomendaciones",
    "Cupones personalizados",
    "Contenido según intereses",
    "Horario óptimo de envío"
]

for i, personalizacion in enumerate(personalizaciones):
    y_pos = personalizacion_y - personalizacion_height//2 + 50 + i*20
    draw4.text((personalizacion_x-personalizacion_width//2+20, y_pos), "• " + personalizacion, 
              fill=color_texto, font=font_small, anchor="lm")

# Conexión de n8n a personalización
draw4.line([(width//2-100, n8n_y), (personalizacion_x+personalizacion_width//2, personalizacion_y)], 
          fill=color_conexion, width=2)
draw4.polygon([(personalizacion_x+personalizacion_width//2, personalizacion_y), 
              (personalizacion_x+personalizacion_width//2+10, personalizacion_y-5), 
              (personalizacion_x+personalizacion_width//2+10, personalizacion_y+5)], 
             fill=color_conexion)

# Texto explicativo
draw4.text((width//2, 650), "n8n automatiza el envío de secuencias de emails personalizados", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((width//2, 680), "adaptados al perfil y comportamiento de cada cliente", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la cuarta escena
img4.save(os.path.join(output_dir, 'escena4_secuencias_emails.png'))

# Escena 5: Seguimiento y Optimización
img5, draw5, width, height = crear_imagen_base()

# Subtítulo
draw5.text((width//2, 100), "Seguimiento de Resultados y Optimización", fill=color_texto, font=font_subtitle, anchor="mm")

# Plataforma de Email (izquierda)
email_x = 200
email_y = 250
draw5.rounded_rectangle([(email_x-100, email_y-60), (email_x+100, email_y+60)], 
                       radius=10, fill=color_email, outline=color_texto)
draw5.text((email_x, email_y-20), "Plataforma de", fill='white', font=font_text, anchor="mm")
draw5.text((email_x, email_y+20), "Email Marketing", fill='white', font=font_text, anchor="mm")

# n8n en el centro
n8n_x = width//2
n8n_y = 250
draw5.rounded_rectangle([(n8n_x-100, n8n_y-60), (n8n_x+100, n8n_y+60)], 
                       radius=10, fill=color_n8n, outline=color_texto)
draw5.text((n8n_x, n8n_y-20), "n8n", fill='white', font=font_text, anchor="mm")
draw5.text((n8n_x, n8n_y+20), "Análisis y Mejora", fill='white', font=font_text, anchor="mm")

# Analytics (derecha)
analytics_x = width - 200
analytics_y = 250
draw5.rounded_rectangle([(analytics_x-100, analytics_y-60), (analytics_x+100, analytics_y+60)], 
                       radius=10, fill=color_analytics, outline=color_texto)
draw5.text((analytics_x, analytics_y-20), "Plataforma de", fill='white', font=font_text, anchor="mm")
draw5.text((analytics_x, analytics_y+20), "Analytics", fill='white', font=font_text, anchor="mm")

# Conexiones bidireccionales
# Entre Email y n8n
draw5.line([(email_x+100, email_y), (n8n_x-100, n8n_y)], fill=color_conexion, width=2)
draw5.polygon([(n8n_x-100, n8n_y), (n8n_x-110, n8n_y-5), (n8n_x-110, n8n_y+5)], fill=color_conexion)
draw5.polygon([(email_x+100, email_y), (email_x+110, email_y-5), (email_x+110, email_y+5)], fill=color_conexion)

# Entre n8n y Analytics
draw5.line([(n8n_x+100, n8n_y), (analytics_x-100, analytics_y)], fill=color_conexion, width=2)
draw5.polygon([(analytics_x-100, analytics_y), (analytics_x-110, analytics_y-5), (analytics_x-110, analytics_y+5)], fill=color_conexion)
draw5.polygon([(n8n_x+100, n8n_y), (n8n_x+110, n8n_y-5), (n8n_x+110, n8n_y+5)], fill=color_conexion)

# Dashboard de métricas (abajo)
dashboard_y = 450
draw5.rounded_rectangle([(width//2-300, dashboard_y-120), (width//2+300, dashboard_y+120)], 
                       radius=10, fill='white', outline=color_analytics)
draw5.text((width//2, dashboard_y-100), "Dashboard de Métricas", 
          fill=color_analytics, font=font_subtitle, anchor="mm")

# Gráficos simplificados
# Gráfico de barras (izquierda)
bar_x = width//2 - 150
bar_y = dashboard_y + 20
bar_width = 150
bar_height = 100

# Ejes
draw5.line([(bar_x-bar_width//2, bar_y+bar_height//2), (bar_x+bar_width//2, bar_y+bar_height//2)], 
          fill=color_texto, width=2)  # Eje X
draw5.line([(bar_x-bar_width//2, bar_y-bar_height//2), (bar_x-bar_width//2, bar_y+bar_height//2)], 
          fill=color_texto, width=2)  # Eje Y

# Barras
bar_count = 4
bar_individual_width = bar_width / (bar_count * 2)
for i in range(bar_count):
    bar_height_val = np.random.randint(30, 80)
    x_pos = bar_x - bar_width//2 + bar_individual_width + i * (bar_width / bar_count)
    draw5.rectangle([(x_pos, bar_y+bar_height//2-bar_height_val), (x_pos+bar_individual_width, bar_y+bar_height//2)], 
                   fill=color_analytics)

# Gráfico circular (derecha)
pie_x = width//2 + 150
pie_y = dashboard_y + 20
pie_radius = 50

# Círculo base
draw5.ellipse([(pie_x-pie_radius, pie_y-pie_radius), (pie_x+pie_radius, pie_y+pie_radius)], 
             fill='white', outline=color_texto)

# Sectores
draw5.pieslice([(pie_x-pie_radius, pie_y-pie_radius), (pie_x+pie_radius, pie_y+pie_radius)], 
              start=0, end=120, fill=color_analytics)
draw5.pieslice([(pie_x-pie_radius, pie_y-pie_radius), (pie_x+pie_radius, pie_y+pie_radius)], 
              start=120, end=240, fill=color_email)
draw5.pieslice([(pie_x-pie_radius, pie_y-pie_radius), (pie_x+pie_radius, pie_y+pie_radius)], 
              start=240, end=360, fill=color_n8n)

# Conexión de n8n a dashboard
draw5.line([(n8n_x, n8n_y+60), (n8n_x, dashboard_y-120)], fill=color_conexion, width=2)
draw5.polygon([(n8n_x, dashboard_y-120), (n8n_x-5, dashboard_y-130), (n8n_x+5, dashboard_y-130)], fill=color_conexion)

# Métricas clave (a la derecha)
metricas_x = width - 150
metricas_y = 450
metricas_width = 250
metricas_height = 200

# Fondo para métricas
draw5.rounded_rectangle([(metricas_x-metricas_width//2, metricas_y-metricas_height//2), 
                        (metricas_x+metricas_width//2, metricas_y+metricas_height//2)], 
                       radius=10, fill='white', outline=color_texto)

# Título de métricas
draw5.text((metricas_x, metricas_y-metricas_height//2+20), "Métricas Clave:", 
          fill=color_texto, font=font_text, anchor="mm")

# Lista de métricas
metricas = [
    "Tasa de apertura: 28%",
    "Tasa de clics: 12%",
    "Conversiones: 5.2%",
    "Ingresos generados: $12,500",
    "ROI de campaña: 320%",
    "Tasa de rebote: 2.1%",
    "Tasa de cancelación: 0.8%"
]

for i, metrica in enumerate(metricas):
    y_pos = metricas_y - metricas_height//2 + 50 + i*20
    draw5.text((metricas_x-metricas_width//2+20, y_pos), "• " + metrica, 
              fill=color_texto, font=font_small, anchor="lm")

# Texto explicativo
draw5.text((width//2, 620), "n8n recopila y analiza automáticamente los resultados", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((width//2, 650), "de las campañas para optimizar futuras comunicaciones", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((width//2, 680), "y mejorar continuamente el rendimiento del marketing", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la quinta escena
img5.save(os.path.join(output_dir, 'escena5_seguimiento.png'))

print(f"Imágenes generadas en {output_dir}")
