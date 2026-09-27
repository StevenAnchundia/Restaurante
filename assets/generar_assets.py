"""
Genera los íconos PNG necesarios para restaurante_app usando Pillow.
Ejecutar una sola vez: python assets/generar_assets.py
"""
import os

try:
    from PIL import Image, ImageDraw, ImageFont
    PILLOW = True
except ImportError:
    PILLOW = False

DIRECTORIO = os.path.dirname(__file__)


def crear_icono(nombre, emoji, color_fondo, color_texto, tamano=32):
    """Crea un ícono PNG simple con color y texto."""
    img = Image.new("RGBA", (tamano, tamano), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Fondo redondeado (círculo)
    draw.ellipse([0, 0, tamano - 1, tamano - 1], fill=color_fondo)
    # Texto centrado
    font_size = tamano // 2
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), emoji, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((tamano - w) // 2, (tamano - h) // 2), emoji, fill=color_texto, font=font)
    ruta = os.path.join(DIRECTORIO, f"{nombre}.png")
    img.save(ruta)
    print(f"  ✓ {nombre}.png")
    return ruta


def crear_logo(tamano=80):
    """Crea el logo principal del restaurante."""
    img = Image.new("RGBA", (tamano, tamano), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, tamano - 1, tamano - 1], fill=(26, 26, 46, 255))
    draw.ellipse([3, 3, tamano - 4, tamano - 4], outline=(233, 69, 96, 255), width=3)
    font_size = tamano // 3
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size // 2)
    except Exception:
        font = ImageFont.load_default()
        font_sm = font
    texto = "R"
    bbox = draw.textbbox((0, 0), texto, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((tamano - w) // 2, tamano // 5), texto, fill=(233, 69, 96, 255), font=font)
    texto2 = "APP"
    bbox2 = draw.textbbox((0, 0), texto2, font=font_sm)
    w2 = bbox2[2] - bbox2[0]
    draw.text(((tamano - w2) // 2, tamano * 2 // 3), texto2, fill=(255, 255, 255, 255), font=font_sm)
    ruta = os.path.join(DIRECTORIO, "logo.png")
    img.save(ruta)
    print(f"  ✓ logo.png")


if __name__ == "__main__":
    if not PILLOW:
        print("Pillow no disponible. Los íconos se generarán en tiempo de ejecución.")
    else:
        print("Generando assets...")
        crear_logo(80)
        crear_icono("ico_usuarios", "U", (41, 182, 246, 255), (255, 255, 255, 255))
        crear_icono("ico_productos", "P", (102, 187, 106, 255), (255, 255, 255, 255))
        crear_icono("ico_ventas", "V", (233, 69, 96, 255), (255, 255, 255, 255))
        crear_icono("ico_login", "L", (255, 167, 38, 255), (255, 255, 255, 255))
        print("Assets generados correctamente.")
