def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # createImage() - Creates a new PImage object
    img = createImage(400, 400, RGB)  # Create a 400x400 RGB image

    # Set the color of each pixel in the image
    img.loadPixels()  # Load the pixel data of the image
    for i in range(img.width):
        for j in range(img.height):
            # Set pixel color based on position
            img.pixels[j * img.width + i] = color(i % 255, j % 255, (i + j) % 255)
    img.updatePixels()  # Update the pixel data of the image

    # Display the image on the canvas
    image(img, 200, 200)  # Draw the image at position (200, 200)

def draw():
    pass


