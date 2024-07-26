def setup():
    size(800, 800)  # Window size
    background(255)  # White background

def draw():
    # arc
    fill(255, 0, 0)  # Red fill color
    arc(100, 100, 80, 80, 0, PI + QUARTER_PI)  # Draws an arc
    
    # circle
    fill(0, 255, 0)  # Green fill color
    circle(250, 100, 80)  # Draws a circle
    
    # ellipse
    fill(0, 0, 255)  # Blue fill color
    ellipse(400, 100, 80, 120)  # Draws an ellipse
    
    # line
    stroke(0)  # Black line color
    line(500, 60, 580, 140)  # Draws a line
    
    # point
    stroke(0)  # Black point color
    point(650, 100)  # Draws a point
    
    # quad
    fill(255, 255, 0)  # Yellow fill color
    quad(100, 200, 150, 150, 200, 200, 150, 250)  # Draws a quadrilateral
    
    # rect
    fill(0, 255, 255)  # Cyan fill color
    rect(250, 150, 100, 50)  # Draws a rectangle
    
    # square
    fill(255, 0, 255)  # Magenta fill color
    square(400, 150, 80)  # Draws a square
    
    # triangle
    fill(128, 128, 128)  # Gray fill color
    triangle(550, 200, 600, 150, 650, 200)  # Draws a triangle
    
    noLoop()  # Stops the draw loop

run()

