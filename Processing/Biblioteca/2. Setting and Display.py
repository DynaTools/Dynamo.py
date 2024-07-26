def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # loadImage() - Loads an image from a file
    global img
    img = loadImage('example.jpg')  # Ensure you have an 'example.jpg' file in your sketch folder

    # imageMode() - Sets the mode for drawing images
    imageMode(CENTER)  # Draw images from their center

    # requestImage() - Requests an image from a URL or filename (asynchronous loading)
    global requested_img
    requested_img = requestImage('example.jpg')  # Request an image

def draw():
    background(255)  # Clear background

    # image() - Displays the loaded image on the screen
    if img is not None:
        image(img, width / 2, height / 2, img.width / 2, img.height / 2)  # Draw image at center, scaled to half size

    # tint() - Applies a tint to images
    tint(255, 0, 0, 128)  # Apply a red tint with 50% opacity
    if img is not None:
        image(img, width / 4, height / 4, img.width / 4, img.height / 4)  # Draw tinted image

    # noTint() - Disables tinting
    noTint()  # Disable tint
    if img is not None:
        image(img, 3 * width / 4, height / 4, img.width / 4, img.height / 4)  # Draw image without tint

    # Display the requested image (if loaded)
    if requested_img is not None and requested_img.width > 0:
        image(requested_img, width / 2, 3 * height / 4, requested_img.width / 4, requested_img.height / 4)

def mousePressed():
    # Refresh the display with new tint when mouse is pressed
    tint(random(255), random(255), random(255), 128)  # Random tint color with 50% opacity

run()
