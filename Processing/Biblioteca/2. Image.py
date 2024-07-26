def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # Draw some graphics
    fill(255, 0, 0)  # Red fill color
    ellipse(400, 400, 200, 200)  # Draw a red circle

    # Save the current canvas as an image file using save()
    save("savedImage.png")  # Saves the current canvas as 'savedImage.png'

def draw():
    # Draw some additional graphics
    fill(0, 0, 255)  # Blue fill color
    rect(300, 300, 200, 200)  # Draw a blue rectangle

    # Save each frame as an image file using saveFrame()
    saveFrame("frame-####.png")  # Saves each frame as 'frame-0000.png', 'frame-0001.png', etc.

    # Stop the draw loop after a few frames
    if frameCount > 10:
        noLoop()

