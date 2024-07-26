def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # loadShape() - Loads an SVG or OBJ file as a PShape object
    global s
    s = loadShape('example.svg')  # Make sure you have an 'example.svg' file in your sketch folder

    # shapeMode() - Sets the location from which shapes draw
    shapeMode(CENTER)  # Draw shapes from the center

def draw():
    background(255)  # Clear background
    # shape() - Draws the loaded shape on the screen
    fill(0, 0, 255)  # Blue fill color
    shape(s, width / 2, height / 2, 400, 400)  # Draw the shape in the center of the canvas
