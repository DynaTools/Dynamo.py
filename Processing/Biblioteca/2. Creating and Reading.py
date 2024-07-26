def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # color() - Creates a color object
    c1 = color(255, 0, 0)  # Red color
    c2 = color(0, 255, 0)  # Green color
    c3 = color(0, 0, 255)  # Blue color

    # alpha() - Gets the alpha (opacity) value from a color
    a = alpha(c1)  # Alpha of c1
    textSize(16)
    fill(0)
    text(f"Alpha of c1: {a}", 10, 20)

    # blendColor() - Blends two colors together
    bc = blendColor(c1, c2, BLEND)
    fill(bc)
    rect(10, 40, 50, 50)

    # blue() - Extracts the blue component from a color
    b = blue(c3)
    fill(0)
    text(f"Blue component of c3: {b}", 10, 110)

    # brightness() - Gets the brightness of a color
    br = brightness(c3)
    text(f"Brightness of c3: {br}", 10, 140)

    # green() - Extracts the green component from a color
    g = green(c2)
    text(f"Green component of c2: {g}", 10, 170)

    # hue() - Gets the hue of a color
    h = hue(c1)
    text(f"Hue of c1: {h}", 10, 200)

    # lerpColor() - Linearly interpolates between two colors
    lc = lerpColor(c1, c3, 0.5)
    fill(lc)
    rect(10, 220, 50, 50)
    text(f"lerpColor between c1 and c3 at 0.5: {lc}", 70, 250)

    # red() - Extracts the red component from a color
    r = red(c1)
    text(f"Red component of c1: {r}", 10, 290)

    # saturation() - Gets the saturation of a color
    s = saturation(c2)
    text(f"Saturation of c2: {s}", 10, 320)

def draw():
    pass


