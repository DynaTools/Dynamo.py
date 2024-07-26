def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # cursor() - Sets the cursor to a predefined or custom image
    cursor(CROSS)  # Sets the cursor to a cross

    # delay() - Pauses the program for a specified number of milliseconds
    delay(1000)  # Delay for 1 second

    # displayHeight - System variable that stores the height of the display screen
    textSize(16)
    text(f"displayHeight: {displayHeight}", 10, 20)

    # displayWidth - System variable that stores the width of the display screen
    text(f"displayWidth: {displayWidth}", 10, 40)

    # focused - System variable that is true if the window is in focus
    text(f"focused: {focused}", 10, 60)

    # frameCount - System variable that stores the number of frames displayed since the program started
    text(f"frameCount: {frameCount}", 10, 80)

    # frameRate() - Sets the frame rate of the program
    frameRate(30)  # Set frame rate to 30 frames per second
    text(f"frameRate: {frameRate}", 10, 100)

    # fullScreen() - Sets the display to full-screen mode
    # fullScreen()  # Uncomment to enable full-screen mode

    # height - System variable that stores the height of the display window
    text(f"height: {height}", 10, 120)

    # noCursor() - Hides the cursor from view
    # noCursor()  # Uncomment to hide the cursor

    # size() - Sets the dimensions of the display window
    # size(1024, 768)  # Uncomment to set the window size to 1024x768

    # width - System variable that stores the width of the display window
    text(f"width: {width}", 10, 140)

def draw():
    # Update frameCount display in real-time
    fill(255)  # White background for text
    rect(0, 60, 150, 20)  # Clear previous text
    fill(0)  # Black text
    text(f"frameCount: {frameCount}", 10, 80)

run()
