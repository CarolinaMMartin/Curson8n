"""
Script para generar imágenes para la Animación 1: Comparativa Visual Automatización Tradicional vs. No-Code
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio para las imágenes de salida
output_dir = '/home/ubuntu/curso_automatizacion/materiales_visuales/modulo1/animacion1'
os.makedirs(output_dir, exist_ok=True)

# Configuración de colores
color_tradicional = '#4B5D67'  # Azul grisáceo
color_nocode = '#4CAF50'       # Verde
color_fondo = '#F5F5F5'        # Gris claro
color_texto = '#333333'        # Gris oscuro
color_error = '#F44336'        # Rojo
color_exito = '#2196F3'        # Azul

# Función para crear imagen base con división
def crear_imagen_base(width=1200, height=800):
    img = Image.new('RGB', (width, height), color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Línea divisoria vertical
    draw.line([(width//2, 0), (width//2, height)], fill='#CCCCCC', width=2)
    
    # Títulos
    font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    draw.text((width//4, 50), "Automatización Tradicional", fill=color_tradicional, font=font_title, anchor="mm")
    draw.text((width//4*3, 50), "Automatización No-Code", fill=color_nocode, font=font_title, anchor="mm")
    
    return img, draw

# Escena 1: Comparación de procesos
img1, draw1 = crear_imagen_base()
font_text = ImageFont.truetype("DejaVuSans.ttf", 24)

# Lado izquierdo - Tradicional
draw1.text((300, 150), "Requiere conocimientos de programación", fill=color_texto, font=font_text, anchor="mm")
draw1.text((300, 200), "Desarrollo lento y complejo", fill=color_texto, font=font_text, anchor="mm")
draw1.text((300, 250), "Difícil de modificar", fill=color_texto, font=font_text, anchor="mm")

# Iconos representativos (simulados con formas)
# Código complejo
for i in range(5):
    draw1.rectangle([(150+i*30, 300), (170+i*30, 400)], fill=color_tradicional, outline=color_texto)

# Reloj avanzando rápido (días)
draw1.ellipse([(250, 350), (350, 450)], outline=color_texto, width=2)
draw1.line([(300, 400), (300, 360)], fill=color_texto, width=2)  # Hora
draw1.line([(300, 400), (330, 400)], fill=color_texto, width=2)  # Minuto
draw1.text((300, 480), "Días/Semanas", fill=color_texto, font=font_text, anchor="mm")

# Errores
for i in range(3):
    draw1.text((150+i*100, 550), "ERROR", fill=color_error, font=font_text, anchor="mm")

# Lado derecho - No-Code
draw1.text((900, 150), "Accesible para todos", fill=color_texto, font=font_text, anchor="mm")
draw1.text((900, 200), "Desarrollo rápido e intuitivo", fill=color_texto, font=font_text, anchor="mm")
draw1.text((900, 250), "Fácil de modificar", fill=color_texto, font=font_text, anchor="mm")

# Bloques visuales
for i in range(3):
    draw1.rounded_rectangle([(750+i*100, 300), (850+i*100, 350)], radius=10, fill=color_nocode, outline=color_texto)
    draw1.line([(800+i*100, 350), (800+i*100, 370)], fill=color_texto, width=2)
    if i < 2:
        draw1.line([(800+i*100, 370), (800+(i+1)*100, 370)], fill=color_texto, width=2)

# Reloj avanzando (horas)
draw1.ellipse([(850, 400), (950, 500)], outline=color_texto, width=2)
draw1.line([(900, 450), (900, 420)], fill=color_texto, width=2)  # Hora
draw1.line([(900, 450), (930, 450)], fill=color_texto, width=2)  # Minuto
draw1.text((900, 530), "Horas", fill=color_texto, font=font_text, anchor="mm")

# Éxitos
for i in range(3):
    draw1.text((750+i*100, 550), "✓", fill=color_exito, font=ImageFont.truetype("DejaVuSans.ttf", 48), anchor="mm")

# Guardar la primera escena
img1.save(os.path.join(output_dir, 'escena1_comparacion.png'))

# Escena 2: Resultados
img2, draw2 = crear_imagen_base()

# Título de resultados
font_subtitle = ImageFont.truetype("DejaVuSans-Bold.ttf", 30)
draw2.text((600, 120), "RESULTADOS", fill=color_texto, font=font_subtitle, anchor="mm")

# Comparativa de tiempo
draw2.text((300, 200), "Tiempo de desarrollo:", fill=color_texto, font=font_text, anchor="mm")
draw2.text((300, 240), "3 semanas", fill=color_tradicional, font=font_text, anchor="mm")
draw2.text((900, 240), "3 horas", fill=color_nocode, font=font_text, anchor="mm")

# Comparativa de recursos
draw2.text((300, 320), "Recursos necesarios:", fill=color_texto, font=font_text, anchor="mm")
draw2.text((300, 360), "Equipo de desarrollo", fill=color_tradicional, font=font_text, anchor="mm")
draw2.text((900, 360), "Usuario individual", fill=color_nocode, font=font_text, anchor="mm")

# Comparativa de mantenimiento
draw2.text((300, 440), "Facilidad de modificación:", fill=color_texto, font=font_text, anchor="mm")
draw2.text((300, 480), "Compleja", fill=color_tradicional, font=font_text, anchor="mm")
draw2.text((900, 480), "Sencilla", fill=color_nocode, font=font_text, anchor="mm")

# Comparativa de accesibilidad
draw2.text((300, 560), "Accesibilidad:", fill=color_texto, font=font_text, anchor="mm")
draw2.text((300, 600), "Solo desarrolladores", fill=color_tradicional, font=font_text, anchor="mm")
draw2.text((900, 600), "Cualquier persona", fill=color_nocode, font=font_text, anchor="mm")

# Mensaje final
draw2.text((600, 700), "Mismo resultado, diferente enfoque", fill=color_texto, font=font_subtitle, anchor="mm")

# Guardar la segunda escena
img2.save(os.path.join(output_dir, 'escena2_resultados.png'))

print(f"Imágenes generadas en {output_dir}")
