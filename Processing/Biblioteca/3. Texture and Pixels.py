def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # Load an image for texture demonstration
    global img
    img = loadImage('example.jpg')  # Ensure you have an 'example.jpg' file in your sketch folder

    # textureWrap() - Sets the wrapping mode for textures
    textureWrap(REPEAT)

    # Load another image for pixel manipulation demonstration
    global img2
    img2 = loadImage('example2.jpg')  # Ensure you have an 'example2.jpg' file in your sketch folder

def draw():
    background(255)  # Clear background

    # Apply texture and texture wrapping
    beginShape()
    texture(img)
    vertex(100, 100, 0, 0)
    vertex(700, 100, 1, 0)
    vertex(700, 700, 1, 1)
    vertex(100, 700, 0, 1)
    endShape(CLOSE)

    # blend() - Blends a region of pixels with another region
    blend(img2, 0, 0, img2.width, img2.height, 50, 50, img2.width / 2, img2.height / 2, BLEND)

    # copy() - Copies a region of pixels to another region
    copy(img2, 0, 0, img2.width, img2.height, 400, 50, img2.width / 4, img2.height / 4)

    # filter() - Applies a filter to the display window
    filter(GRAY)

    # get() - Reads the color of any pixel or grabs a region of pixels
    c = get(200, 200)  # Gets the color of the pixel at (200, 200)
    fill(c)
    rect(50, 700, 50, 50)  # Draw a rectangle with the color obtained

    # loadPixels() - Loads the pixel data into an array
    loadPixels()

    # Manipulate pixels directly
    for i in range(width):
        for j in range(height):
            if (i+j) % 2 == 0:  # Create a checkerboard pattern
                pixels[j*width + i] = color(0)

    # set() - Sets the color of a specific pixel
    set(400, 400, color(255, 0, 0))  # Set the pixel at (400, 400) to red

    # updatePixels() - Updates the display window with the data in the pixels array
    updatePixels()

def mousePressed():
    # When the mouse is pressed, copy a region of the window to another location
    copy(100, 100, 200, 200, mouseX, mouseY, 200, 200)


