def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # print() - Prints a message to the console without a newline
    print("This is a message printed using print() ")

    # println() - Prints a message to the console with a newline
    println("This is a message printed using println()")

def draw():
    background(255)  # Clear background
    fill(0)  # Black text color

    # Displaying messages on the canvas
    textSize(16)
    text("Check the console for print() and println() messages.", 10, 20)

    # Using print() and println() in draw for continuous updates
    print("Frame count: ")
    println(frameCount)


