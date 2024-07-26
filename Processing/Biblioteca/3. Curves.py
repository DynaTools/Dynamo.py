def setup():
    size(800, 800)  # Window size
    background(255)  # White background

    # bezier() - Draws a Bezier curve using control points
    stroke(0)  # Black stroke color
    noFill()  # No fill color
    bezier(100, 200, 150, 100, 250, 300, 300, 200)  # Control points for the Bezier curve

    # bezierDetail() - Sets the resolution at which Bezier curves display
    bezierDetail(20)
    stroke(0)
    noFill()
    bezier(100, 400, 150, 300, 250, 500, 300, 400)  # Bezier curve with higher detail

    # bezierPoint() - Calculates a point along a Bezier curve
    stroke(0)
    noFill()
    bezier(400, 200, 450, 100, 550, 300, 600, 200)
    t = 0.5  # Position along the curve (0.0 - 1.0)
    x = bezierPoint(400, 450, 550, 600, t)
    y = bezierPoint(200, 100, 300, 200, t)
    fill(255, 0, 0)
    ellipse(x, y, 10, 10)  # Red ellipse at the calculated point

    # bezierTangent() - Calculates the tangent of a Bezier curve at a point
    stroke(0)
    noFill()
    bezier(400, 400, 450, 300, 550, 500, 600, 400)
    t = 0.5  # Position along the curve (0.0 - 1.0)
    tx = bezierTangent(400, 450, 550, 600, t)
    ty = bezierTangent(400, 300, 500, 400, t)
    fill(0, 0, 255)
    line(650, 400, 650 + tx, 400 + ty)  # Line representing the tangent

    # curve() - Draws a Catmull-Rom spline curve
    stroke(0)
    noFill()
    curve(50, 600, 150, 600, 250, 700, 350, 700)  # Control points

    # curveDetail() - Sets the resolution at which curves display
    curveDetail(20)
    stroke(0)
    noFill()
    curve(50, 700, 150, 700, 250, 800, 350, 800)  # Curve with higher detail

    # curvePoint() - Calculates a point along a curve
    stroke(0)
    noFill()
    curve(50, 500, 150, 500, 250, 600, 350, 600)
    t = 0.5  # Position along the curve (0.0 - 1.0)
    x = curvePoint(50, 150, 250, 350, t)
    y = curvePoint(500, 500, 600, 600, t)
    fill(255, 0, 0)
    ellipse(x, y, 10, 10)  # Red ellipse at the calculated point

    # curveTangent() - Calculates the tangent of a curve at a point
    stroke(0)
    noFill()
    curve(50, 400, 150, 400, 250, 500, 350, 500)
    t = 0.5  # Position along the curve (0.0 - 1.0)
    tx = curveTangent(50, 150, 250, 350, t)
    ty = curveTangent(400, 400, 500, 500, t)
    fill(0, 0, 255)
    line(650, 500, 650 + tx, 500 + ty)  # Line representing the tangent

    # curveTightness() - Sets the tightness of the curves
    curveTightness(5)  # Increase tightness
    stroke(0)
    noFill()
    curve(400, 600, 500, 600, 600, 700, 700, 700)

    noLoop()  # Stops the draw loop

run()
