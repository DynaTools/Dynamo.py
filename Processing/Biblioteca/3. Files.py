def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # Draw some graphics
    fill(255, 0, 0)  # Red fill color
    ellipse(400, 400, 200, 200)  # Draw a red circle

    # Save the current canvas as raw data using beginRaw() and endRaw()
    beginRaw(PDF, "output.pdf")
    ellipse(400, 400, 200, 200)
    endRaw()  # Ends the recording of the raw data

    # Create a writer to write text to a file using createWriter()
    global writer
    writer = createWriter("output.txt")
    writer.println("This is a line of text.")
    writer.println("This is another line of text.")
    writer.close()  # Close the writer

    # Save data as bytes using saveBytes()
    data = bytearray("This is some byte data.", "utf-8")
    saveBytes("outputBytes.dat", data)

    # Save data as strings using saveStrings()
    lines = ["Line 1", "Line 2", "Line 3"]
    saveStrings("outputStrings.txt", lines)

    # Save data as XML using saveXML()
    xml = createXML("root")
    child = xml.addChild("child")
    child.setString("name", "example")
    saveXML(xml, "output.xml")

    # Select output file using selectOutput()
    selectOutput("Select a file to save output", "outputSelected")

def outputSelected(selection):
    if selection:
        # Write some data to the selected output file
        with createWriter(selection) as output:
            output.println("This is a line of text saved to the selected file.")
        print(f"Output file selected: {selection}")
    else:
        print("File selection was canceled.")

def draw():
    pass


