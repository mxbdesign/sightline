from PIL import Image, ImageDraw
import random

def create_noise(filename, size=128):
    img = Image.new('RGBA', (size, size))
    pixels = img.load()
    for x in range(size):
        for y in range(size):
            a = random.randint(0, 12)
            pixels[x, y] = (255, 255, 255, a)
    img.save(filename)

def create_grid(filename, size=64):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.line([(0, 0), (size, 0)], fill=(255, 255, 255, 8), width=1)
    draw.line([(0, 0), (0, size)], fill=(255, 255, 255, 8), width=1)
    img.save(filename)

def create_scanlines(filename, size=4):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.line([(0, 0), (size, 0)], fill=(0, 0, 0, 30), width=1)
    draw.line([(0, 2), (size, 2)], fill=(255, 255, 255, 5), width=1)
    img.save(filename)

create_noise("textures/noise.png")
create_grid("textures/grid.png")
create_scanlines("textures/scanlines.png")
