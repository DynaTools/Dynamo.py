def setup():
    size(800, 800)  # Window size
    background(255)  # White background
    textSize(16)  # Set text size for displaying information

def draw():
    # Display current and previous mouse positions
    background(255)  # Clear background
    fill(0)  # Black text color
    text(f"mouseX: {mouseX}, mouseY: {mouseY}", 10, 20)
    text(f"pmouseX: {pmouseX}, pmouseY: {pmouseY}", 10, 40)

    # Check if mouse is pressed
    if mousePressed:
        text("Mouse is pressed", 10, 60)
    else:
        text("Mouse is not pressed", 10, 60)

def mouseClicked():
    # Called when the mouse is clicked
    fill(0, 255, 0)  # Green fill color
    ellipse(mouseX, mouseY, 50, 50)  # Draw a circle at the mouse position

def mouseDragged():
    # Called when the mouse is dragged
    fill(255, 0, 0)  # Red fill color
    rect(mouseX, mouseY, 50, 50)  # Draw a rectangle at the mouse position

def mouseMoved():
    # Called when the mouse is moved
    fill(0, 0, 255)  # Blue fill color
    ellipse(mouseX, mouseY, 25, 25)  # Draw a small circle at the mouse position

def mousePressed():
    # Called once when the mouse button is pressed
    fill(255, 255, 0)  # Yellow fill color
    ellipse(mouseX, mouseY, 30, 30)  # Draw a circle at the mouse position

def mouseReleased():
    # Called once when the mouse button is released
    fill(255, 0, 255)  # Magenta fill color
    ellipse(mouseX, mouseY, 30, 30)  # Draw a circle at the mouse position

def mouseWheel(event):
    # Called when the mouse wheel is scrolled
    fill(0)  # Black fill color
    ellipse(mouseX, mouseY, 10 + event.getCount() * 10, 10 + event.getCount() * 10)  # Draw a circle with size based on scroll

