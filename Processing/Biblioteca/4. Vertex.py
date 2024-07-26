def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # beginShape() and vertex() - Starts defining a custom shape with vertices
    fill(255, 0, 0)  # Red fill color
    beginShape()
    vertex(100, 100)
    vertex(150, 50)
    vertex(200, 100)
    vertex(150, 150)
    endShape(CLOSE)  # Closes the shape

    # bezierVertex() - Specifies Bezier curve vertices for shapes
    fill(0, 255, 0)  # Green fill color
    beginShape()
    vertex(300, 100)
    bezierVertex(350, 50, 450, 150, 500, 100)
    endShape()

    # curveVertex() - Specifies Catmull-Rom curve vertices for shapes
    fill(0, 0, 255)  # Blue fill color
    beginShape()
    vertex(100, 300)  # Initial vertex
    curveVertex(150, 250)
    curveVertex(200, 350)
    curveVertex(250, 300)
    endShape()

    # quadraticVertex() - Specifies quadratic Bezier curve vertices for shapes
    fill(255, 255, 0)  # Yellow fill color
    beginShape()
    vertex(300, 300)
    quadraticVertex(350, 250, 400, 300)
    endShape()

    # beginContour() and endContour() - Defines a negative space inside a shape
    fill(255, 0, 255)  # Magenta fill color
    beginShape()
    vertex(500, 300)
    vertex(600, 300)
    vertex(600, 400)
    vertex(500, 400)
    beginContour()
    vertex(520, 320)
    vertex(580, 320)
    vertex(580, 380)
    vertex(520, 380)
    endContour()
    endShape(CLOSE)

    # texture() and textureMode() - Applies a texture to a shape
    img = loadImage('example.jpg')  # Load an image
    textureMode(NORMAL)
    beginShape()
    texture(img)
    vertex(100, 500, 0, 0)
    vertex(300, 500, 1, 0)
    vertex(300, 700, 1, 1)
    vertex(100, 700, 0, 1)
    endShape(CLOSE)

def draw():
    pass


