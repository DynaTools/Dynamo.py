def setup():
    size(800, 800)  # Window size
    background(255)  # White background
    noLoop()  # Stop draw loop for static demonstration

def draw():
    background(255)  # Clear background

    # Draw original rectangle
    fill(0, 0, 255)
    rect(100, 100, 100, 100)

    # pushMatrix() and popMatrix() - Save and restore the transformation state
    pushMatrix()
    translate(300, 100)  # Move origin to (300, 100)
    rotate(radians(45))  # Rotate by 45 degrees
    fill(0, 255, 0)
    rect(0, 0, 100, 100)  # Draw rectangle at new origin
    popMatrix()  # Restore original transformation state

    # printMatrix() - Print the current transformation matrix
    printMatrix()

    # resetMatrix() - Reset the transformation matrix to the identity matrix
    resetMatrix()
    fill(255, 0, 0)
    rect(500, 100, 100, 100)  # Draw rectangle with no transformations

    # rotateX(), rotateY(), rotateZ() - Rotate around x, y, and z axes
    pushMatrix()
    translate(100, 300)  # Move origin to (100, 300)
    rotateX(radians(45))
    rotateY(radians(45))
    rotateZ(radians(45))
    fill(255, 255, 0)
    box(100)  # Draw a box at new origin
    popMatrix()  # Restore original transformation state

    # scale() - Scale the size of objects
    pushMatrix()
    translate(300, 300)  # Move origin to (300, 300)
    scale(2, 1)  # Scale x by 2 and y by 1
    fill(0, 255, 255)
    rect(0, 0, 100, 100)  # Draw scaled rectangle
    popMatrix()  # Restore original transformation state

    # shearX() - Shear along the x axis
    pushMatrix()
    translate(500, 300)  # Move origin to (500, 300)
    shearX(radians(45))  # Shear along x axis
    fill(255, 0, 255)
    rect(0, 0, 100, 100)  # Draw sheared rectangle
    popMatrix()  # Restore original transformation state

    # shearY() - Shear along the y axis
    pushMatrix()
    translate(700, 300)  # Move origin to (700, 300)
    shearY(radians(45))  # Shear along y axis
    fill(128, 0, 128)
    rect(0, 0, 100, 100)  # Draw sheared rectangle
    popMatrix()  # Restore original transformation state

    # applyMatrix() - Apply a custom transformation matrix
    pushMatrix()
    translate(100, 500)  # Move origin to (100, 500)
    m = [[1, 0.5, 0, 0], [0.5, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    applyMatrix(m[0][0], m[0][1], m[1][0], m[1][1], m[3][0], m[3][1])
    fill(0, 128, 128)
    rect(0, 0, 100, 100)  # Draw rectangle with custom matrix
    popMatrix()  # Restore original transformation state

    # translate() - Move the origin to a new position
    pushMatrix()
    translate(300, 500)  # Move origin to (300, 500)
    fill(128, 128, 0)
    rect(0, 0, 100, 100)  # Draw rectangle at new origin
    popMatrix()  # Restore original transformation state

