from PIL import Image
import random

def create_seamless_noise(filename, size=128, color=(255,255,255), alpha_base=10, alpha_var=10):
    img = Image.new('RGBA', (size, size))
    pixels = img.load()
    for x in range(size):
        for y in range(size):
            a = min(255, max(0, alpha_base + random.randint(-alpha_var, alpha_var)))
            pixels[x, y] = (color[0], color[1], color[2], a)
    img.save(filename)

def create_seamless_grain(filename, size=128, color=(0,0,0), alpha_base=15, alpha_var=15):
    img = Image.new('RGBA', (size, size))
    pixels = img.load()
    for x in range(size):
        for y in range(size):
            a = min(255, max(0, alpha_base + random.randint(-alpha_var, alpha_var)))
            pixels[x, y] = (color[0], color[1], color[2], a)
    img.save(filename)

create_seamless_noise("bg_noise.png", size=128, color=(255,255,255), alpha_base=8, alpha_var=6)
create_seamless_grain("canvas_overlay.png", size=128, color=(0,0,0), alpha_base=15, alpha_var=15)
