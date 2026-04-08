from PIL import Image, ImageDraw
import random
import math

def generate_body_bg(filename="body_bg.png", size=256):
    img = Image.new('RGBA', (size, size), (20, 29, 38, 255))
    draw = ImageDraw.Draw(img)

    # Draw subtle grid
    grid_spacing = 32
    for x in range(0, size, grid_spacing):
        draw.line([(x, 0), (x, size)], fill=(255, 255, 255, 5), width=1)
    for y in range(0, size, grid_spacing):
        draw.line([(0, y), (size, y)], fill=(255, 255, 255, 5), width=1)

    # Add noise
    pixels = img.load()
    for x in range(size):
        for y in range(size):
            r, g, b, a = pixels[x, y]
            noise = random.randint(-8, 8)
            pixels[x, y] = (max(0, min(255, r + noise)),
                            max(0, min(255, g + noise)),
                            max(0, min(255, b + noise)), 255)
    img.save(filename)

def generate_overlay(filename="game_overlay.png", size=256):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    pixels = img.load()
    for x in range(size):
        for y in range(size):
            # random noise for overlay
            v = random.randint(0, 255)
            # make it very subtle, low alpha
            a = random.randint(0, 15)
            pixels[x, y] = (v, v, v, a)
    img.save(filename)

def generate_vignette(filename="vignette.png", size=800):
    # This won't be seamless, just a large overlay
    img = Image.new('RGBA', (size, 600), (0, 0, 0, 0))
    pixels = img.load()
    cx, cy = size / 2, 600 / 2
    max_dist = math.hypot(cx, cy)
    for x in range(size):
        for y in range(600):
            dist = math.hypot(x - cx, y - cy)
            # intensity increases towards edges
            intensity = (dist / max_dist) ** 2.5
            a = int(min(255, intensity * 200))
            pixels[x, y] = (0, 0, 0, a)
    img.save(filename)

generate_body_bg()
generate_overlay()
generate_vignette()
