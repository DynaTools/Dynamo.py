import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Developed by Paulo Augusto Giavoni
# Contact: paulo.giavoni@gmail.com
# LinkedIn: https://www.linkedin.com/in/paulogiavoni/

# Inputs
curve1 = IN[0]  # First curve (horizontal)
curve2 = IN[1]  # Second curve (vertical)
divisions1 = IN[2]  # Number of internal divisions for the first curve
divisions2 = IN[3]  # Number of internal divisions for the second curve

def get_curve(curve):
    """Ensure the input is a single curve."""
    if isinstance(curve, list):
        return curve[0]
    return curve

def get_points(curve, divisions, margin=1):
    """Generate points along the curve, considering margins and spacing rules."""
    points = []
    total_divisions = (divisions - 1) * 2 + margin * 2  # Calculate total divisions considering margins
    for i in range(total_divisions + 1):
        param = i / float(total_divisions)
        point = curve.PointAtParameter(param)
        # Add points within the margin and following the spacing rule
        if margin <= i <= total_divisions - margin:
            if (i - margin) % 2 == 0:
                points.append(point)
    return points

def find_intersections(points1, points2):
    """Find intersection points based on X and Y coordinates of points from two curves."""
    intersections = []
    for pt1 in points1:
        for pt2 in points2:
            intersection_point = Point.ByCoordinates(pt1.X, pt2.Y, pt1.Z)
            intersections.append(intersection_point)
    return intersections

# Verify input curves
curve1 = get_curve(curve1)
curve2 = get_curve(curve2)

# Validate division inputs
error_message = None
if divisions1 <= 0 or divisions2 <= 0:
    error_message = "Error: The number of divisions must be greater than 0."
elif divisions1 < 0 or divisions2 < 0:
    error_message = "Error: The number of divisions cannot be negative."

if error_message:
    OUT = [error_message]
else:
    # Obtain points along the curves
    pointsCurve1 = get_points(curve1, divisions1)
    pointsCurve2 = get_points(curve2, divisions2)

    # Find intersection points
    intersectionPoints = find_intersections(pointsCurve1, pointsCurve2)

    # Output
    OUT = intersectionPoints
