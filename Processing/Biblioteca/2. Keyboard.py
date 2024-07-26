def setup():
    size(800, 800)  # Window size
    background(255)  # White background
    textSize(16)  # Set text size for displaying information

def draw():
    background(255)  # Clear background
    fill(0)  # Black text color

    # Display the last key pressed
    text(f"Last key pressed: {key}", 10, 20)

    # Display the keyCode of the last key pressed
    text(f"keyCode: {keyCode}", 10, 40)

    # Check if any key is pressed
    if keyPressed:
        text("A key is pressed", 10, 60)
    else:
        text("No key is pressed", 10, 60)

def keyPressed():
    # Called once when a key is pressed
    fill(255, 0, 0)  # Red fill color
    ellipse(random(width), random(height), 50, 50)  # Draw a circle at a random position

def keyReleased():
    # Called once when a key is released
    fill(0, 255, 0)  # Green fill color
    rect(random(width), random(height), 50, 50)  # Draw a rectangle at a random position

def keyTyped():
    # Called once when a key is typed
    fill(0, 0, 255)  # Blue fill color
    textSize(32)
    text(key, random(width), random(height))  # Draw the character at a random position


