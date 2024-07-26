# background() - Used to set the background color of the canvas.
def setup():
    size(800, 800)
    background(100, 150, 200)  # Light blue background color
run()

# clear() - Clears the canvas to a transparent state.
def setup():
    size(800, 800)
    background(100, 150, 200)
    
def draw():
    clear()  # Clears the canvas
    fill(255, 0, 0)
    ellipse(mouseX, mouseY, 50, 50)
run()

# colorMode() - Sets the color mode for the following color functions.
def setup():
    size(800, 800)
    colorMode(HSB, 360, 100, 100)  # HSB color mode
    background(200, 50, 100)  # Background color in HSB mode
run()

# fill() - Sets the color used to fill shapes.
def setup():
    size(800, 800)
    background(255)
    fill(255, 0, 0)  # Red fill color
    rect(100, 100, 200, 100)
run()

# noFill() - Disables the fill color for shapes.
def setup():
    size(800, 800)
    background(255)
    fill(255, 0, 0)
    rect(100, 100, 200, 100)
    noFill()  # Disable fill color
    ellipse(400, 150, 100, 100)
run()

# noStroke() - Disables the stroke (outline) for shapes.
def setup():
    size(800, 800)
    background(255)
    fill(0, 255, 0)
    rect(100, 100, 200, 100)
    noStroke()  # Disable outline
    ellipse(400, 150, 100, 100)
run()

# stroke() - Sets the color used to draw lines and borders around shapes.
def setup():
    size(800, 800)
    background(255)
    fill(255, 255, 0)
    rect(100, 100, 200, 100)
    stroke(0, 0, 255)  # Blue stroke color
    strokeWeight(5)  # Stroke weight (thickness)
    ellipse(400, 150, 100, 100)
run()
