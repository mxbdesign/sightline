from PIL import Image, ImageDraw
import random
import math

def create_concrete(filename, size=256):
    img = Image.new('RGBA', (size, size))
    pixels = img.load()

    # Generate base noise
    for x in range(size):
        for y in range(size):
            # Base brightness
            v = random.randint(180, 220)

            # Subtle low frequency variation
            lf = math.sin(x/10) * math.cos(y/10) * 10
            v = int(v + lf)

            # Clamp
            v = max(0, min(255, v))

            # Transparency
            a = random.randint(150, 200)

            # Make some pixels darker (pitting/pores)
            if random.random() < 0.05:
                v = max(0, v - random.randint(30, 80))

            pixels[x, y] = (v, v, v, a)

    img.save(filename)

def create_grass_texture(filename, size=128):
    img = Image.new('RGBA', (size, size))
    pixels = img.load()

    # Base green variations
    colors = [(39, 174, 96), (46, 204, 113), (30, 130, 76), (25, 105, 60)]

    for x in range(size):
        for y in range(size):
            # Choose a base color with some noise
            base = random.choice(colors)
            r = min(255, max(0, base[0] + random.randint(-15, 15)))
            g = min(255, max(0, base[1] + random.randint(-15, 15)))
            b = min(255, max(0, base[2] + random.randint(-15, 15)))

            # Add some dark blades
            if random.random() < 0.08:
                r = max(0, r - 30)
                g = max(0, g - 30)
                b = max(0, b - 30)

            pixels[x, y] = (r, g, b, 255)

    # Add vertical streaks for grass blades
    draw = ImageDraw.Draw(img)
    for _ in range(80):
        x = random.randint(0, size-1)
        y1 = random.randint(0, size-10)
        length = random.randint(4, 12)
        c = random.choice(colors)
        c = (max(0, c[0]-20), max(0, c[1]-20), max(0, c[2]-20), 200)
        draw.line([(x, y1), (x, y1+length)], fill=c, width=1)

    img.save(filename)

create_concrete("textures/concrete.png")
create_grass_texture("textures/grass.png")
