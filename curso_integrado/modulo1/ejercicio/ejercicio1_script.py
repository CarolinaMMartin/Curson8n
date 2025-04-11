"""
Script para generar materiales para el Ejercicio 1 del Módulo 1: Creación de un flujo "Hola Mundo"
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/ejercicios_interactivos/modulo1/ejercicio1'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_n8n = '#FF6D00'          # Naranja n8n
color_nodo1 = '#4CAF50'        # Verde para nodo trigger
color_nodo2 = '#2196F3'        # Azul para nodo set
color_conexion = '#9E9E9E'     # Gris para conexiones
color_resaltado = '#FFC107'    # Amarillo para resaltados
color_exito = '#4CAF50'        # Verde para éxito
color_error = '#F44336'        # Rojo para error

# Función para crear imagen base
def crear_imagen_base(width=1200, height=800, titulo="Ejercicio 1: Creación de un flujo 'Hola Mundo'"):
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
img1, draw1, width, height = crear_imagen_base(titulo="Ejercicio 1: Creación de un flujo 'Hola Mundo'")

# Subtítulo
draw1.text((width//2, 100), "Objetivo: Crear tu primer flujo de trabajo en n8n", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Descripción del ejercicio
descripcion = [
    "En este ejercicio, crearás un flujo de trabajo simple que muestre el mensaje 'Hola Mundo'",
    "cuando se active manualmente. Aprenderás a:",
    "",
    "• Crear un nuevo flujo de trabajo",
    "• Añadir un nodo de activación manual",
    "• Configurar un nodo para establecer datos",
    "• Conectar nodos entre sí",
    "• Ejecutar el flujo y ver los resultados"
]

y_pos = 160
for linea in descripcion:
    draw1.text((width//2, y_pos), linea, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 30

# Imagen de ejemplo del resultado final
resultado_y = 400
nodo_size = 80
nodo_spacing = 200

# Nodo 1: Manual Trigger
nodo1_x = width//2 - nodo_spacing//2
draw1.rounded_rectangle([(nodo1_x-nodo_size//2, resultado_y-nodo_size//2), 
                        (nodo1_x+nodo_size//2, resultado_y+nodo_size//2)], 
                       radius=15, fill=color_nodo1, outline=color_texto)
draw1.text((nodo1_x, resultado_y-15), "Manual", fill='white', font=font_text, anchor="mm")
draw1.text((nodo1_x, resultado_y+15), "Trigger", fill='white', font=font_text, anchor="mm")

# Nodo 2: Set
nodo2_x = width//2 + nodo_spacing//2
draw1.rounded_rectangle([(nodo2_x-nodo_size//2, resultado_y-nodo_size//2), 
                        (nodo2_x+nodo_size//2, resultado_y+nodo_size//2)], 
                       radius=15, fill=color_nodo2, outline=color_texto)
draw1.text((nodo2_x, resultado_y), "Set", fill='white', font=font_text, anchor="mm")

# Conexión entre nodos
draw1.line([(nodo1_x+nodo_size//2, resultado_y), (nodo2_x-nodo_size//2, resultado_y)], 
          fill=color_conexion, width=3)
draw1.polygon([(nodo2_x-nodo_size//2, resultado_y), 
              (nodo2_x-nodo_size//2-10, resultado_y-5), 
              (nodo2_x-nodo_size//2-10, resultado_y+5)], 
             fill=color_conexion)

# Resultado del flujo
resultado_box_y = resultado_y + 150
draw1.rounded_rectangle([(width//2-200, resultado_box_y-50), (width//2+200, resultado_box_y+50)], 
                       radius=10, fill='white', outline=color_exito, width=3)
draw1.text((width//2, resultado_box_y-20), "Resultado:", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, resultado_box_y+20), "¡Hola Mundo!", 
          fill=color_n8n, font=font_subtitle, anchor="mm")

# Flecha de resultado
draw1.line([(nodo2_x, resultado_y+nodo_size//2), (nodo2_x, resultado_box_y-50)], 
          fill=color_conexion, width=2)
draw1.polygon([(nodo2_x, resultado_box_y-50), 
              (nodo2_x-5, resultado_box_y-60), 
              (nodo2_x+5, resultado_box_y-60)], 
             fill=color_conexion)

# Instrucciones para comenzar
draw1.text((width//2, 600), "Para comenzar, abre n8n en tu navegador y sigue los pasos de este ejercicio", 
          fill=color_texto, font=font_text, anchor="mm")
draw1.text((width//2, 640), "Tiempo estimado: 10-15 minutos", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la primera imagen
img1.save(os.path.join(output_dir, 'paso1_introduccion.png'))

# Paso 2: Crear un nuevo flujo de trabajo
img2, draw2, width, height = crear_imagen_base(titulo="Paso 2: Crear un nuevo flujo de trabajo")

# Instrucciones
draw2.text((width//2, 100), "Crea un nuevo flujo de trabajo en n8n", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Inicia sesión en tu instancia de n8n",
    "2. En el panel de navegación izquierdo, haz clic en 'Flujos de trabajo'",
    "3. Haz clic en el botón '+ Nuevo' en la esquina superior derecha",
    "4. Se abrirá un nuevo flujo de trabajo en blanco",
    "5. Haz clic en 'Guardar' y asigna un nombre: 'Hola Mundo'"
]

y_pos = 160
for paso in pasos:
    draw2.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n
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
draw2.text((width//2-interfaz_width//2+100, interfaz_y-interfaz_height//2+20), 
          "Hola Mundo", fill='white', font=font_text, anchor="mm")

# Botón de guardar (resaltado)
boton_guardar_x = width//2+interfaz_width//2-100
boton_guardar_y = interfaz_y-interfaz_height//2+20
draw2.rounded_rectangle([(boton_guardar_x-50, boton_guardar_y-15), 
                        (boton_guardar_x+50, boton_guardar_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw2.text((boton_guardar_x, boton_guardar_y), "Guardar", 
          fill=color_texto, font=font_text, anchor="mm")

# Panel izquierdo
draw2.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw2.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Flujos de trabajo", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw2.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)
draw2.text((width//2, interfaz_y), "Área de trabajo vacía", 
          fill='#999999', font=font_text, anchor="mm")

# Consejos
draw2.rounded_rectangle([(width//2-300, 650), (width//2+300, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw2.text((width//2, 675), "Consejo: Guarda tu flujo de trabajo regularmente", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la segunda imagen
img2.save(os.path.join(output_dir, 'paso2_crear_flujo.png'))

# Paso 3: Añadir un nodo de activación manual
img3, draw3, width, height = crear_imagen_base(titulo="Paso 3: Añadir un nodo de activación manual")

# Instrucciones
draw3.text((width//2, 100), "Añade un nodo de activación manual", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Haz clic en el botón '+' en el centro del área de trabajo",
    "2. En el panel de búsqueda, escribe 'manual'",
    "3. Selecciona el nodo 'Manual Trigger'",
    "4. El nodo se añadirá al área de trabajo"
]

y_pos = 160
for paso in pasos:
    draw3.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n con nodo añadido
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
draw3.text((width//2-interfaz_width//2+100, interfaz_y-interfaz_height//2+20), 
          "Hola Mundo", fill='white', font=font_text, anchor="mm")

# Panel izquierdo
draw3.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw3.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Flujos de trabajo", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw3.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Nodo Manual Trigger
nodo_x = width//2 - 100
nodo_y = interfaz_y
nodo_size = 80
draw3.rounded_rectangle([(nodo_x-nodo_size//2, nodo_y-nodo_size//2), 
                        (nodo_x+nodo_size//2, nodo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo1, outline=color_texto)
draw3.text((nodo_x, nodo_y-15), "Manual", fill='white', font=font_text, anchor="mm")
draw3.text((nodo_x, nodo_y+15), "Trigger", fill='white', font=font_text, anchor="mm")

# Panel de búsqueda (resaltado)
panel_busqueda_x = width//2 + 150
panel_busqueda_y = interfaz_y - 50
draw3.rounded_rectangle([(panel_busqueda_x-120, panel_busqueda_y-30), 
                        (panel_busqueda_x+120, panel_busqueda_y+30)], 
                       radius=5, fill='white', outline=color_resaltado, width=3)
draw3.text((panel_busqueda_x-100, panel_busqueda_y), "Buscar: manual", 
          fill=color_texto, font=font_text, anchor="lm")

# Resultado de búsqueda
resultado_y = panel_busqueda_y + 70
draw3.rounded_rectangle([(panel_busqueda_x-120, resultado_y-20), 
                        (panel_busqueda_x+120, resultado_y+20)], 
                       radius=5, fill='white', outline=color_texto)
draw3.text((panel_busqueda_x-100, resultado_y), "Manual Trigger", 
          fill=color_texto, font=font_text, anchor="lm")

# Flecha de selección
draw3.line([(panel_busqueda_x, resultado_y+20), (panel_busqueda_x, resultado_y+50)], 
          fill=color_resaltado, width=2)
draw3.line([(panel_busqueda_x, resultado_y+50), (nodo_x+nodo_size//2, nodo_y)], 
          fill=color_resaltado, width=2)
draw3.polygon([(nodo_x+nodo_size//2, nodo_y), 
              (nodo_x+nodo_size//2-10, nodo_y-5), 
              (nodo_x+nodo_size//2-10, nodo_y+5)], 
             fill=color_resaltado)

# Consejos
draw3.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw3.text((width//2, 675), "Consejo: El nodo Manual Trigger es el punto de inicio de tu flujo", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la tercera imagen
img3.save(os.path.join(output_dir, 'paso3_nodo_manual.png'))

# Paso 4: Añadir un nodo Set
img4, draw4, width, height = crear_imagen_base(titulo="Paso 4: Añadir un nodo Set")

# Instrucciones
draw4.text((width//2, 100), "Añade un nodo Set para crear el mensaje", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Haz clic en el botón '+' que aparece a la derecha del nodo Manual Trigger",
    "2. En el panel de búsqueda, escribe 'set'",
    "3. Selecciona el nodo 'Set'",
    "4. El nodo se añadirá y se conectará automáticamente"
]

y_pos = 160
for paso in pasos:
    draw4.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n con ambos nodos
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
draw4.text((width//2-interfaz_width//2+100, interfaz_y-interfaz_height//2+20), 
          "Hola Mundo", fill='white', font=font_text, anchor="mm")

# Panel izquierdo
draw4.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw4.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Flujos de trabajo", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw4.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Nodo Manual Trigger
nodo1_x = width//2 - 100
nodo_y = interfaz_y
nodo_size = 80
draw4.rounded_rectangle([(nodo1_x-nodo_size//2, nodo_y-nodo_size//2), 
                        (nodo1_x+nodo_size//2, nodo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo1, outline=color_texto)
draw4.text((nodo1_x, nodo_y-15), "Manual", fill='white', font=font_text, anchor="mm")
draw4.text((nodo1_x, nodo_y+15), "Trigger", fill='white', font=font_text, anchor="mm")

# Nodo Set
nodo2_x = width//2 + 100
draw4.rounded_rectangle([(nodo2_x-nodo_size//2, nodo_y-nodo_size//2), 
                        (nodo2_x+nodo_size//2, nodo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo2, outline=color_texto)
draw4.text((nodo2_x, nodo_y), "Set", fill='white', font=font_text, anchor="mm")

# Conexión entre nodos
draw4.line([(nodo1_x+nodo_size//2, nodo_y), (nodo2_x-nodo_size//2, nodo_y)], 
          fill=color_conexion, width=3)
draw4.polygon([(nodo2_x-nodo_size//2, nodo_y), 
              (nodo2_x-nodo_size//2-10, nodo_y-5), 
              (nodo2_x-nodo_size//2-10, nodo_y+5)], 
             fill=color_conexion)

# Panel de búsqueda (resaltado)
panel_busqueda_x = width//2 + 200
panel_busqueda_y = interfaz_y - 50
draw4.rounded_rectangle([(panel_busqueda_x-120, panel_busqueda_y-30), 
                        (panel_busqueda_x+120, panel_busqueda_y+30)], 
                       radius=5, fill='white', outline=color_resaltado, width=3)
draw4.text((panel_busqueda_x-100, panel_busqueda_y), "Buscar: set", 
          fill=color_texto, font=font_text, anchor="lm")

# Resultado de búsqueda
resultado_y = panel_busqueda_y + 70
draw4.rounded_rectangle([(panel_busqueda_x-120, resultado_y-20), 
                        (panel_busqueda_x+120, resultado_y+20)], 
                       radius=5, fill='white', outline=color_texto)
draw4.text((panel_busqueda_x-100, resultado_y), "Set", 
          fill=color_texto, font=font_text, anchor="lm")

# Flecha de selección
draw4.line([(panel_busqueda_x, resultado_y+20), (panel_busqueda_x, resultado_y+50)], 
          fill=color_resaltado, width=2)
draw4.line([(panel_busqueda_x, resultado_y+50), (nodo2_x, nodo_y-nodo_size//2)], 
          fill=color_resaltado, width=2)
draw4.polygon([(nodo2_x, nodo_y-nodo_size//2), 
              (nodo2_x-5, nodo_y-nodo_size//2-10), 
              (nodo2_x+5, nodo_y-nodo_size//2-10)], 
             fill=color_resaltado)

# Consejos
draw4.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw4.text((width//2, 675), "Consejo: El nodo Set permite definir valores para usar en el flujo", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la cuarta imagen
img4.save(os.path.join(output_dir, 'paso4_nodo_set.png'))

# Paso 5: Configurar el nodo Set
img5, draw5, width, height = crear_imagen_base(titulo="Paso 5: Configurar el nodo Set")

# Instrucciones
draw5.text((width//2, 100), "Configura el nodo Set para mostrar 'Hola Mundo'", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Haz clic en el nodo 'Set' para abrir su panel de configuración",
    "2. En la sección 'Valores a establecer', haz clic en 'Añadir valor'",
    "3. En 'Nombre', escribe 'mensaje'",
    "4. En 'Valor', escribe '¡Hola Mundo!'",
    "5. Haz clic en 'Cerrar' para guardar la configuración"
]

y_pos = 160
for paso in pasos:
    draw5.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n con panel de configuración
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
               fill='#333333', outline=color_texto)
draw5.text((width//2-interfaz_width//2+100, interfaz_y-interfaz_height//2+20), 
          "Hola Mundo", fill='white', font=font_text, anchor="mm")

# Panel izquierdo
draw5.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw5.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Flujos de trabajo", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw5.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Nodo Manual Trigger
nodo1_x = width//2 - 200
nodo_y = interfaz_y
nodo_size = 80
draw5.rounded_rectangle([(nodo1_x-nodo_size//2, nodo_y-nodo_size//2), 
                        (nodo1_x+nodo_size//2, nodo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo1, outline=color_texto)
draw5.text((nodo1_x, nodo_y-15), "Manual", fill='white', font=font_text, anchor="mm")
draw5.text((nodo1_x, nodo_y+15), "Trigger", fill='white', font=font_text, anchor="mm")

# Nodo Set (resaltado)
nodo2_x = width//2
draw5.rounded_rectangle([(nodo2_x-nodo_size//2, nodo_y-nodo_size//2), 
                        (nodo2_x+nodo_size//2, nodo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo2, outline=color_resaltado, width=3)
draw5.text((nodo2_x, nodo_y), "Set", fill='white', font=font_text, anchor="mm")

# Conexión entre nodos
draw5.line([(nodo1_x+nodo_size//2, nodo_y), (nodo2_x-nodo_size//2, nodo_y)], 
          fill=color_conexion, width=3)
draw5.polygon([(nodo2_x-nodo_size//2, nodo_y), 
              (nodo2_x-nodo_size//2-10, nodo_y-5), 
              (nodo2_x-nodo_size//2-10, nodo_y+5)], 
             fill=color_conexion)

# Panel de configuración
config_x = width//2 + 200
config_y = interfaz_y
config_width = 250
config_height = 200
draw5.rounded_rectangle([(config_x-config_width//2, config_y-config_height//2), 
                        (config_x+config_width//2, config_y+config_height//2)], 
                       radius=10, fill='white', outline=color_resaltado, width=3)

# Título del panel
draw5.rectangle([(config_x-config_width//2, config_y-config_height//2), 
                (config_x+config_width//2, config_y-config_height//2+30)], 
               fill=color_nodo2, outline=color_texto)
draw5.text((config_x, config_y-config_height//2+15), "Configuración del nodo Set", 
          fill='white', font=font_small, anchor="mm")

# Contenido del panel
draw5.text((config_x-config_width//2+20, config_y-config_height//2+50), "Valores a establecer:", 
          fill=color_texto, font=font_small, anchor="lm")

# Campo de nombre
draw5.text((config_x-config_width//2+20, config_y-config_height//2+80), "Nombre:", 
          fill=color_texto, font=font_small, anchor="lm")
draw5.rectangle([(config_x-config_width//2+80, config_y-config_height//2+70), 
                (config_x+config_width//2-20, config_y-config_height//2+90)], 
               fill='white', outline=color_texto)
draw5.text((config_x-config_width//2+90, config_y-config_height//2+80), "mensaje", 
          fill=color_texto, font=font_small, anchor="lm")

# Campo de valor
draw5.text((config_x-config_width//2+20, config_y-config_height//2+110), "Valor:", 
          fill=color_texto, font=font_small, anchor="lm")
draw5.rectangle([(config_x-config_width//2+80, config_y-config_height//2+100), 
                (config_x+config_width//2-20, config_y-config_height//2+120)], 
               fill='white', outline=color_texto)
draw5.text((config_x-config_width//2+90, config_y-config_height//2+110), "¡Hola Mundo!", 
          fill=color_texto, font=font_small, anchor="lm")

# Botón de cerrar
draw5.rounded_rectangle([(config_x-50, config_y+config_height//2-40), 
                        (config_x+50, config_y+config_height//2-10)], 
                       radius=5, fill=color_nodo2, outline=color_texto)
draw5.text((config_x, config_y+config_height//2-25), "Cerrar", 
          fill='white', font=font_small, anchor="mm")

# Flecha de conexión
draw5.line([(nodo2_x+nodo_size//2, nodo_y), (config_x-config_width//2, config_y)], 
          fill=color_resaltado, width=2)

# Consejos
draw5.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw5.text((width//2, 675), "Consejo: Puedes añadir múltiples valores en un solo nodo Set", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la quinta imagen
img5.save(os.path.join(output_dir, 'paso5_configurar_set.png'))

# Paso 6: Ejecutar el flujo
img6, draw6, width, height = crear_imagen_base(titulo="Paso 6: Ejecutar el flujo")

# Instrucciones
draw6.text((width//2, 100), "Ejecuta el flujo y observa el resultado", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Pasos a seguir
pasos = [
    "1. Haz clic en el botón 'Ejecutar' en la barra superior",
    "2. Selecciona el nodo 'Manual Trigger' para activar el flujo",
    "3. Observa cómo se ejecuta el flujo y los datos pasan de un nodo a otro",
    "4. Haz clic en el nodo 'Set' para ver el resultado final"
]

y_pos = 160
for paso in pasos:
    draw6.text((width//2, y_pos), paso, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 40

# Interfaz simplificada de n8n con flujo ejecutado
interfaz_y = 400
interfaz_width = 700
interfaz_height = 300

# Fondo de la interfaz
draw6.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='white', outline=color_texto)

# Barra superior
draw6.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2), 
                (width//2+interfaz_width//2, interfaz_y-interfaz_height//2+40)], 
               fill='#333333', outline=color_texto)
draw6.text((width//2-interfaz_width//2+100, interfaz_y-interfaz_height//2+20), 
          "Hola Mundo", fill='white', font=font_text, anchor="mm")

# Botón de ejecutar (resaltado)
boton_ejecutar_x = width//2
boton_ejecutar_y = interfaz_y-interfaz_height//2+20
draw6.rounded_rectangle([(boton_ejecutar_x-50, boton_ejecutar_y-15), 
                        (boton_ejecutar_x+50, boton_ejecutar_y+15)], 
                       radius=5, fill=color_resaltado, outline=color_texto)
draw6.text((boton_ejecutar_x, boton_ejecutar_y), "Ejecutar", 
          fill=color_texto, font=font_text, anchor="mm")

# Panel izquierdo
draw6.rectangle([(width//2-interfaz_width//2, interfaz_y-interfaz_height//2+40), 
                (width//2-interfaz_width//2+150, interfaz_y+interfaz_height//2)], 
               fill='#f0f0f0', outline=color_texto)
draw6.text((width//2-interfaz_width//2+75, interfaz_y-interfaz_height//2+70), 
          "Flujos de trabajo", fill=color_texto, font=font_small, anchor="mm")

# Área de trabajo (canvas)
draw6.rectangle([(width//2-interfaz_width//2+150, interfaz_y-interfaz_height//2+40), 
                (width//2+interfaz_width//2, interfaz_y+interfaz_height//2)], 
               fill='#f9f9f9', outline=color_texto)

# Nodo Manual Trigger (ejecutado)
nodo1_x = width//2 - 100
nodo_y = interfaz_y
nodo_size = 80
draw6.rounded_rectangle([(nodo1_x-nodo_size//2, nodo_y-nodo_size//2), 
                        (nodo1_x+nodo_size//2, nodo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo1, outline=color_exito, width=3)
draw6.text((nodo1_x, nodo_y-15), "Manual", fill='white', font=font_text, anchor="mm")
draw6.text((nodo1_x, nodo_y+15), "Trigger", fill='white', font=font_text, anchor="mm")

# Nodo Set (ejecutado)
nodo2_x = width//2 + 100
draw6.rounded_rectangle([(nodo2_x-nodo_size//2, nodo_y-nodo_size//2), 
                        (nodo2_x+nodo_size//2, nodo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo2, outline=color_exito, width=3)
draw6.text((nodo2_x, nodo_y), "Set", fill='white', font=font_text, anchor="mm")

# Conexión entre nodos (animada)
for i in range(5):
    x = nodo1_x + nodo_size//2 + i * ((nodo2_x - nodo_size//2) - (nodo1_x + nodo_size//2)) // 4
    y = nodo_y
    draw6.ellipse([(x-5, y-5), (x+5, y+5)], fill=color_exito)

# Panel de resultado
resultado_x = width//2 + 200
resultado_y = interfaz_y + 50
resultado_width = 250
resultado_height = 150
draw6.rounded_rectangle([(resultado_x-resultado_width//2, resultado_y-resultado_height//2), 
                        (resultado_x+resultado_width//2, resultado_y+resultado_height//2)], 
                       radius=10, fill='white', outline=color_exito, width=3)

# Título del panel
draw6.rectangle([(resultado_x-resultado_width//2, resultado_y-resultado_height//2), 
                (resultado_x+resultado_width//2, resultado_y-resultado_height//2+30)], 
               fill=color_nodo2, outline=color_texto)
draw6.text((resultado_x, resultado_y-resultado_height//2+15), "Resultado del nodo Set", 
          fill='white', font=font_small, anchor="mm")

# Contenido del panel
draw6.text((resultado_x-resultado_width//2+20, resultado_y-resultado_height//2+60), "Output:", 
          fill=color_texto, font=font_small, anchor="lm")

# JSON resultado
json_text = [
    "{",
    "  \"json\": {",
    "    \"mensaje\": \"¡Hola Mundo!\"",
    "  }",
    "}"
]

for i, line in enumerate(json_text):
    draw6.text((resultado_x-resultado_width//2+40, resultado_y-resultado_height//2+90+i*15), line, 
              fill=color_texto, font=font_small, anchor="lm")

# Flecha de conexión
draw6.line([(nodo2_x+nodo_size//2, nodo_y), (resultado_x-resultado_width//2, resultado_y)], 
          fill=color_exito, width=2)

# Consejos
draw6.rounded_rectangle([(width//2-350, 650), (width//2+350, 700)], 
                       radius=10, fill='#E3F2FD', outline='#2196F3')
draw6.text((width//2, 675), "Consejo: Puedes hacer clic en cualquier nodo para ver sus datos de entrada y salida", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la sexta imagen
img6.save(os.path.join(output_dir, 'paso6_ejecutar_flujo.png'))

# Paso 7: Completado
img7, draw7, width, height = crear_imagen_base(titulo="¡Ejercicio Completado!")

# Mensaje de felicitación
draw7.text((width//2, 100), "¡Felicidades! Has creado tu primer flujo de trabajo en n8n", 
          fill=color_texto, font=font_subtitle, anchor="mm")

# Resumen
draw7.text((width//2, 160), "En este ejercicio has aprendido:", 
          fill=color_texto, font=font_text, anchor="mm")

aprendizajes = [
    "• Crear un nuevo flujo de trabajo en n8n",
    "• Añadir y conectar nodos",
    "• Configurar un nodo para establecer datos",
    "• Ejecutar un flujo y ver los resultados"
]

y_pos = 200
for aprendizaje in aprendizajes:
    draw7.text((width//2, y_pos), aprendizaje, fill=color_texto, font=font_text, anchor="mm")
    y_pos += 30

# Flujo completo
flujo_y = 350
nodo_size = 80
nodo_spacing = 200

# Nodo 1: Manual Trigger
nodo1_x = width//2 - nodo_spacing//2
draw7.rounded_rectangle([(nodo1_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (nodo1_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo1, outline=color_exito, width=3)
draw7.text((nodo1_x, flujo_y-15), "Manual", fill='white', font=font_text, anchor="mm")
draw7.text((nodo1_x, flujo_y+15), "Trigger", fill='white', font=font_text, anchor="mm")

# Nodo 2: Set
nodo2_x = width//2 + nodo_spacing//2
draw7.rounded_rectangle([(nodo2_x-nodo_size//2, flujo_y-nodo_size//2), 
                        (nodo2_x+nodo_size//2, flujo_y+nodo_size//2)], 
                       radius=15, fill=color_nodo2, outline=color_exito, width=3)
draw7.text((nodo2_x, flujo_y), "Set", fill='white', font=font_text, anchor="mm")

# Conexión entre nodos
draw7.line([(nodo1_x+nodo_size//2, flujo_y), (nodo2_x-nodo_size//2, flujo_y)], 
          fill=color_conexion, width=3)
draw7.polygon([(nodo2_x-nodo_size//2, flujo_y), 
              (nodo2_x-nodo_size//2-10, flujo_y-5), 
              (nodo2_x-nodo_size//2-10, flujo_y+5)], 
             fill=color_conexion)

# Resultado del flujo
resultado_box_y = flujo_y + 150
draw7.rounded_rectangle([(width//2-200, resultado_box_y-50), (width//2+200, resultado_box_y+50)], 
                       radius=10, fill='white', outline=color_exito, width=3)
draw7.text((width//2, resultado_box_y-20), "Resultado:", 
          fill=color_texto, font=font_text, anchor="mm")
draw7.text((width//2, resultado_box_y+20), "¡Hola Mundo!", 
          fill=color_n8n, font=font_subtitle, anchor="mm")

# Flecha de resultado
draw7.line([(nodo2_x, flujo_y+nodo_size//2), (nodo2_x, resultado_box_y-50)], 
          fill=color_conexion, width=2)
draw7.polygon([(nodo2_x, resultado_box_y-50), 
              (nodo2_x-5, resultado_box_y-60), 
              (nodo2_x+5, resultado_box_y-60)], 
             fill=color_conexion)

# Próximos pasos
draw7.rounded_rectangle([(width//2-300, 600), (width//2+300, 700)], 
                       radius=10, fill='#E8F5E9', outline=color_exito)
draw7.text((width//2, 620), "Próximos pasos:", 
          fill=color_texto, font=font_text, anchor="mm")
draw7.text((width//2, 650), "Intenta modificar el mensaje o añadir más valores al nodo Set", 
          fill=color_texto, font=font_text, anchor="mm")
draw7.text((width//2, 680), "Explora otros nodos disponibles en n8n", 
          fill=color_texto, font=font_text, anchor="mm")

# Guardar la séptima imagen
img7.save(os.path.join(output_dir, 'paso7_completado.png'))

# Crear un archivo de instrucciones
instrucciones_path = os.path.join(output_dir, 'instrucciones.md')
with open(instrucciones_path, 'w') as f:
    f.write("""# Ejercicio 1: Creación de un flujo "Hola Mundo"

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
""")

print(f"Materiales para el Ejercicio 1 del Módulo 1 generados en {output_dir}")
