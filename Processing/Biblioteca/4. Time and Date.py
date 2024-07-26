def setup():
    size(800, 800)  # Window size
    textSize(16)  # Set text size for displaying information
    background(255)  # White background

def draw():
    background(255)  # Clear background
    fill(0)  # Black text color

    # day() - Gets the current day
    d = day()
    text(f"Day: {d}", 10, 20)

    # hour() - Gets the current hour
    h = hour()
    text(f"Hour: {h}", 10, 40)

    # millis() - Gets the number of milliseconds since the program started
    m = millis()
    text(f"Millis: {m}", 10, 60)

    # minute() - Gets the current minute
    min = minute()
    text(f"Minute: {min}", 10, 80)

    # month() - Gets the current month
    mon = month()
    text(f"Month: {mon}", 10, 100)

    # second() - Gets the current second
    s = second()
    text(f"Second: {s}", 10, 120)

    # year() - Gets the current year
    y = year()
    text(f"Year: {y}", 10, 140)

