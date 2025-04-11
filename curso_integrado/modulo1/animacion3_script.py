"""
Script para generar imágenes para la Animación 3: Flujo de Datos entre Nodos
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/materiales_visuales/modulo1/animacion3'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_trigger = '#4CAF50'      # Verde
color_set = '#2196F3'          # Azul
color_email = '#FF5722'        # Naranja
color_datos = '#FFC107'        # Amarillo
color_conexion = '#9E9E9E'     # Gris

# Función para crear imagen base
def crear_imagen_base(width=1200, height=800):
    img = Image.new('RGB', (width, height), color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Título
    try:
        font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    except OSError:
        font_title = ImageFont.load_default()
    
    draw.text((width//2, 50), "Flujo de Datos entre Nodos", fill=color_texto, font=font_title, anchor="mm")
    
    return img, draw, width, height

# Función para dibujar un nodo
def dibujar_nodo(draw, x, y, width, height, texto, color, font):
    # Dibujar rectángulo redondeado
    draw.rounded_rectangle([(x, y), (x+width, y+height)], radius=10, fill=color, outline=color_texto)
    
    # Añadir texto
    draw.text((x+width//2, y+height//2), texto, fill='white', font=font, anchor="mm")

# Función para dibujar partículas de datos
def dibujar_particulas(draw, x1, y1, x2, y2, num_particulas, color, radio=5):
    # Calcular puntos a lo largo de la línea
    for i in range(num_particulas):
        t = i / (num_particulas - 1) if num_particulas > 1 else 0.5
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        
        # Dibujar círculo
        draw.ellipse([(x-radio, y-radio), (x+radio, y+radio)], fill=color)

# Escena 1: Workflow Simple
img1, draw1, width, height = crear_imagen_base()

# Cargar fuentes
try:
    font_subtitle = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    font_text = ImageFont.truetype("DejaVuSans.ttf", 18)
    font_node = ImageFont.truetype("DejaVuSans-Bold.ttf", 20)
except OSError:
    font_subtitle = ImageFont.load_default()
    font_text = ImageFont.load_default()
    font_node = ImageFont.load_default()

# Subtítulo
draw1.text((width//2, 100), "Workflow Simple de 3 Nodos", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar los tres nodos
nodo_width = 150
nodo_height = 80
y_nodos = 300

# Nodo 1: Manual Trigger
x1 = 200
dibujar_nodo(draw1, x1, y_nodos, nodo_width, nodo_height, "Manual Trigger", color_trigger, font_node)

# Nodo 2: Set
x2 = width//2 - nodo_width//2
dibujar_nodo(draw1, x2, y_nodos, nodo_width, nodo_height, "Set", color_set, font_node)

# Nodo 3: Send Email
x3 = width - 200 - nodo_width
dibujar_nodo(draw1, x3, y_nodos, nodo_width, nodo_height, "Send Email", color_email, font_node)

# Conexiones entre nodos
# Línea de Trigger a Set
draw1.line([(x1+nodo_width, y_nodos+nodo_height//2), (x2, y_nodos+nodo_height//2)], fill=color_conexion, width=3)
# Línea de Set a Email
draw1.line([(x2+nodo_width, y_nodos+nodo_height//2), (x3, y_nodos+nodo_height//2)], fill=color_conexion, width=3)

# Texto explicativo
draw1.text((width//2, 500), "Un workflow en n8n conecta nodos que procesan y transmiten datos", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, 530), "Cada nodo recibe datos, los procesa y envía el resultado al siguiente", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la primera escena
img1.save(os.path.join(output_dir, 'escena1_workflow_simple.png'))

# Escena 2: Inicio del Flujo
img2, draw2, width, height = crear_imagen_base()

# Subtítulo
draw2.text((width//2, 100), "Inicio del Flujo: El Disparador", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar los tres nodos (el primero resaltado)
# Nodo 1: Manual Trigger (resaltado)
dibujar_nodo(draw2, x1, y_nodos, nodo_width, nodo_height, "Manual Trigger", color_trigger, font_node)
# Borde adicional para resaltar
draw2.rounded_rectangle([(x1-5, y_nodos-5), (x1+nodo_width+5, y_nodos+nodo_height+5)], 
                       radius=15, fill=None, outline=color_trigger, width=3)

# Nodos 2 y 3 (atenuados)
dibujar_nodo(draw2, x2, y_nodos, nodo_width, nodo_height, "Set", color_set, font_node)
dibujar_nodo(draw2, x3, y_nodos, nodo_width, nodo_height, "Send Email", color_email, font_node)

# Conexiones entre nodos
draw2.line([(x1+nodo_width, y_nodos+nodo_height//2), (x2, y_nodos+nodo_height//2)], fill=color_conexion, width=3)
draw2.line([(x2+nodo_width, y_nodos+nodo_height//2), (x3, y_nodos+nodo_height//2)], fill=color_conexion, width=3)

# Botón de ejecución
boton_x = x1 + nodo_width//2
boton_y = y_nodos - 80
draw2.ellipse([(boton_x-30, boton_y-30), (boton_x+30, boton_y+30)], fill='#E0E0E0', outline=color_texto)
# Triángulo de play
draw2.polygon([(boton_x-10, boton_y-15), (boton_x+15, boton_y), (boton_x-10, boton_y+15)], fill=color_trigger)

# Flecha de clic
flecha_start_x = boton_x - 80
flecha_start_y = boton_y - 50
draw2.line([(flecha_start_x, flecha_start_y), (boton_x-20, boton_y-10)], fill=color_texto, width=2)
# Punta de flecha
draw2.polygon([(boton_x-25, boton_y-20), (boton_x-20, boton_y-10), (boton_x-30, boton_y-5)], fill=color_texto)

# Texto "Clic"
draw2.text((flecha_start_x-10, flecha_start_y-10), "Clic", fill=color_texto, font=font_text, anchor="mm")

# Partículas saliendo del nodo Trigger
dibujar_particulas(draw2, x1+nodo_width, y_nodos+nodo_height//2, x2, y_nodos+nodo_height//2, 8, color_datos)

# Texto explicativo
draw2.text((width//2, 500), "El flujo comienza con un disparador (trigger)", 
          fill=color_texto, font=font_text, anchor="mm")
draw2.text((width//2, 530), "Al hacer clic en ejecutar, el nodo trigger inicia el proceso", 
          fill=color_texto, font=font_text, anchor="mm")
draw2.text((width//2, 560), "y envía datos iniciales al siguiente nodo", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la segunda escena
img2.save(os.path.join(output_dir, 'escena2_inicio_flujo.png'))

# Escena 3: Transformación de Datos
img3, draw3, width, height = crear_imagen_base()

# Subtítulo
draw3.text((width//2, 100), "Transformación de Datos", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar los tres nodos (el segundo resaltado)
# Nodo 1: Manual Trigger (atenuado)
dibujar_nodo(draw3, x1, y_nodos, nodo_width, nodo_height, "Manual Trigger", color_trigger, font_node)

# Nodo 2: Set (resaltado)
dibujar_nodo(draw3, x2, y_nodos, nodo_width, nodo_height, "Set", color_set, font_node)
# Borde adicional para resaltar
draw3.rounded_rectangle([(x2-5, y_nodos-5), (x2+nodo_width+5, y_nodos+nodo_height+5)], 
                       radius=15, fill=None, outline=color_set, width=3)

# Nodo 3: Send Email (atenuado)
dibujar_nodo(draw3, x3, y_nodos, nodo_width, nodo_height, "Send Email", color_email, font_node)

# Conexiones entre nodos
draw3.line([(x1+nodo_width, y_nodos+nodo_height//2), (x2, y_nodos+nodo_height//2)], fill=color_conexion, width=3)
draw3.line([(x2+nodo_width, y_nodos+nodo_height//2), (x3, y_nodos+nodo_height//2)], fill=color_conexion, width=3)

# Partículas entrando al nodo Set (color datos)
dibujar_particulas(draw3, x1+nodo_width, y_nodos+nodo_height//2, x2, y_nodos+nodo_height//2, 4, color_datos)

# Partículas saliendo del nodo Set (color diferente)
dibujar_particulas(draw3, x2+nodo_width, y_nodos+nodo_height//2, x3, y_nodos+nodo_height//2, 4, color_set)

# Visualización de JSON
json_x = x2 + nodo_width//2
json_y = y_nodos - 100
json_width = 200
json_height = 80

# Fondo del JSON
draw3.rectangle([(json_x-json_width//2, json_y-json_height//2), 
                (json_x+json_width//2, json_y+json_height//2)], 
               fill='white', outline=color_texto)

# Texto del JSON
try:
    mono_font = ImageFont.truetype("DejaVuSans-Mono.ttf", 14)
except OSError:
    mono_font = ImageFont.load_default()

json_text = [
    '{',
    '  "mensaje": "Hola Mundo",',
    '  "fecha": "2025-04-11"',
    '}'
]

for i, line in enumerate(json_text):
    draw3.text((json_x-json_width//2+10, json_y-json_height//2+15+i*15), 
              line, fill=color_texto, font=mono_font)

# Línea conectora del JSON al nodo
draw3.line([(json_x, json_y+json_height//2), (json_x, y_nodos)], 
          fill=color_set, width=2)

# Texto explicativo
draw3.text((width//2, 500), "El nodo Set transforma los datos según su configuración", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((width//2, 530), "En este caso, crea un objeto con un mensaje y una fecha", 
          fill=color_texto, font=font_text, anchor="mm")
draw3.text((width//2, 560), "Los datos transformados fluyen hacia el siguiente nodo", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la tercera escena
img3.save(os.path.join(output_dir, 'escena3_transformacion_datos.png'))

# Escena 4: Acción Final
img4, draw4, width, height = crear_imagen_base()

# Subtítulo
draw4.text((width//2, 100), "Acción Final", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar los tres nodos (el tercero resaltado)
# Nodo 1: Manual Trigger (atenuado)
dibujar_nodo(draw4, x1, y_nodos, nodo_width, nodo_height, "Manual Trigger", color_trigger, font_node)

# Nodo 2: Set (atenuado)
dibujar_nodo(draw4, x2, y_nodos, nodo_width, nodo_height, "Set", color_set, font_node)

# Nodo 3: Send Email (resaltado)
dibujar_nodo(draw4, x3, y_nodos, nodo_width, nodo_height, "Send Email", color_email, font_node)
# Borde adicional para resaltar
draw4.rounded_rectangle([(x3-5, y_nodos-5), (x3+nodo_width+5, y_nodos+nodo_height+5)], 
                       radius=15, fill=None, outline=color_email, width=3)

# Conexiones entre nodos
draw4.line([(x1+nodo_width, y_nodos+nodo_height//2), (x2, y_nodos+nodo_height//2)], fill=color_conexion, width=3)
draw4.line([(x2+nodo_width, y_nodos+nodo_height//2), (x3, y_nodos+nodo_height//2)], fill=color_conexion, width=3)

# Partículas entrando al nodo Email
dibujar_particulas(draw4, x2+nodo_width, y_nodos+nodo_height//2, x3, y_nodos+nodo_height//2, 4, color_set)

# Sobre de email saliendo
email_x = x3 + nodo_width//2
email_y = y_nodos + nodo_height + 80

# Dibujar sobre
sobre_width = 60
sobre_height = 40
draw4.rectangle([(email_x-sobre_width//2, email_y-sobre_height//2), 
                (email_x+sobre_width//2, email_y+sobre_height//2)], 
               fill='white', outline=color_texto)

# Línea diagonal del sobre
draw4.line([(email_x-sobre_width//2, email_y-sobre_height//2), 
           (email_x, email_y)], 
          fill=color_texto, width=1)
draw4.line([(email_x+sobre_width//2, email_y-sobre_height//2), 
           (email_x, email_y)], 
          fill=color_texto, width=1)

# Línea conectora del nodo al sobre
draw4.line([(email_x, y_nodos+nodo_height), (email_x, email_y-sobre_height//2)], 
          fill=color_email, width=2)

# Mensaje de éxito
draw4.rounded_rectangle([(email_x+sobre_width//2+10, email_y-10), 
                        (email_x+sobre_width//2+160, email_y+10)], 
                       radius=5, fill='#E8F5E9', outline=color_trigger)
draw4.text((email_x+sobre_width//2+85, email_y), "¡Email enviado!", 
          fill=color_trigger, font=font_text, anchor="mm")

# Texto explicativo
draw4.text((width//2, 500), "El nodo Send Email utiliza los datos recibidos", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((width//2, 530), "para realizar una acción: enviar un correo electrónico", 
          fill=color_texto, font=font_text, anchor="mm")
draw4.text((width//2, 560), "El flujo completa su ejecución con éxito", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la cuarta escena
img4.save(os.path.join(output_dir, 'escena4_accion_final.png'))

# Escena 5: Ciclo Completo
img5, draw5, width, height = crear_imagen_base()

# Subtítulo
draw5.text((width//2, 100), "Ciclo Completo del Flujo de Datos", fill=color_texto, font=font_subtitle, anchor="mm")

# Dibujar los tres nodos
# Nodo 1: Manual Trigger
dibujar_nodo(draw5, x1, y_nodos, nodo_width, nodo_height, "Manual Trigger", color_trigger, font_node)

# Nodo 2: Set
dibujar_nodo(draw5, x2, y_nodos, nodo_width, nodo_height, "Set", color_set, font_node)

# Nodo 3: Send Email
dibujar_nodo(draw5, x3, y_nodos, nodo_width, nodo_height, "Send Email", color_email, font_node)

# Conexiones entre nodos
draw5.line([(x1+nodo_width, y_nodos+nodo_height//2), (x2, y_nodos+nodo_height//2)], fill=color_conexion, width=3)
draw5.line([(x2+nodo_width, y_nodos+nodo_height//2), (x3, y_nodos+nodo_height//2)], fill=color_conexion, width=3)

# Flechas de secuencia numeradas
# Flecha 1: Inicio
flecha1_x = x1 + nodo_width//2
flecha1_y = y_nodos - 50
draw5.ellipse([(flecha1_x-20, flecha1_y-20), (flecha1_x+20, flecha1_y+20)], 
             fill=color_trigger, outline=color_texto)
draw5.text((flecha1_x, flecha1_y), "1", fill='white', font=font_node, anchor="mm")

# Flecha 2: Transformación
flecha2_x = x2 + nodo_width//2
flecha2_y = y_nodos - 50
draw5.ellipse([(flecha2_x-20, flecha2_y-20), (flecha2_x+20, flecha2_y+20)], 
             fill=color_set, outline=color_texto)
draw5.text((flecha2_x, flecha2_y), "2", fill='white', font=font_node, anchor="mm")

# Flecha 3: Acción
flecha3_x = x3 + nodo_width//2
flecha3_y = y_nodos - 50
draw5.ellipse([(flecha3_x-20, flecha3_y-20), (flecha3_x+20, flecha3_y+20)], 
             fill=color_email, outline=color_texto)
draw5.text((flecha3_x, flecha3_y), "3", fill='white', font=font_node, anchor="mm")

# Líneas conectoras de las flechas
draw5.line([(flecha1_x+20, flecha1_y), (flecha2_x-20, flecha2_y)], 
          fill=color_texto, width=2)
draw5.line([(flecha2_x+20, flecha2_y), (flecha3_x-20, flecha3_y)], 
          fill=color_texto, width=2)

# Partículas a lo largo de todo el flujo
dibujar_particulas(draw5, x1+nodo_width, y_nodos+nodo_height//2, x2, y_nodos+nodo_height//2, 4, color_datos)
dibujar_particulas(draw5, x2+nodo_width, y_nodos+nodo_height//2, x3, y_nodos+nodo_height//2, 4, color_set)

# Texto explicativo
draw5.text((width//2, 500), "Cada nodo recibe, procesa y pasa datos al siguiente", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((width//2, 530), "formando un flujo completo de información", 
          fill=color_texto, font=font_text, anchor="mm")
draw5.text((width//2, 580), "¡Así fluye la información en n8n!", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Guardar la quinta escena
img5.save(os.path.join(output_dir, 'escena5_ciclo_completo.png'))

print(f"Imágenes generadas en {output_dir}")
