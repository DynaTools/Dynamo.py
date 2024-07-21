
# Elements Intersecting a BoundingBox with Tolerance

## Overview
The `BoundingBoxIntersectsFilter` is a powerful tool within the Dynamo environment that allows users to filter elements that intersect a specified bounding box. Additionally, it supports the definition of a tolerance (Double) and provides an option to invert the filter using a Boolean value.

### Key Features
- **Filter elements intersecting a bounding box**: Basic usage without tolerance.
- **Filter with tolerance**: Adds an additional layer of precision.
- **Invert filter**: Option to invert the filter logic.

## Examples

### Basic Filter
This example demonstrates how to filter elements that intersect a bounding box.
```python
Filter = BoundingBoxIntersectsFilter(outline)
elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(Filter).ToElements()
```

### Filter with Tolerance
This example includes a tolerance parameter, which adjusts the precision of the filtering process.
```python
Filter = BoundingBoxIntersectsFilter(outline, tolerance, False)
elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(Filter).ToElements()
```

### Inverted Filter
To invert the filter, set the Boolean parameter to `True`.
```python
Filter = BoundingBoxIntersectsFilter(outline, tolerance, True)
elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(Filter).ToElements()
```

## Detailed Explanation
### Outline Parameter
The `outline` parameter defines the bounding box within which the filtering will occur. It typically consists of two points representing the minimum and maximum extents of the box.

### Tolerance Parameter
The `tolerance` parameter is a double value that specifies the allowable deviation when checking for intersections. This can be particularly useful in cases where elements are close to the boundary of the bounding box.

### Inversion Parameter
The Boolean `invert` parameter allows the logic of the filter to be inverted. When set to `True`, elements that do not intersect the bounding box (considering the tolerance) will be returned.

### Unit Conversion
It's essential to ensure that the units of the `tolerance` parameter match the units used in the bounding box and the elements being filtered. This typically involves converting between metric and imperial units if necessary.

## Project: Exercises for Students

### Exercise 1: Basic Intersection Filtering
#### Objective
Filter and list all elements intersecting a predefined bounding box in the active view.
#### Steps
1. Define the bounding box using two points.
2. Create a `BoundingBoxIntersectsFilter` with the outline.
3. Collect and list the elements that intersect the bounding box.

#### Code Example
```python
outline = Outline(minPoint, maxPoint)
filter = BoundingBoxIntersectsFilter(outline)
elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(filter).ToElements()
for elem in elems:
    print(elem.Id)
```

### Exercise 2: Intersection Filtering with Tolerance
#### Objective
Include a tolerance value in the filtering process and list the resulting elements.
#### Steps
1. Define the bounding box and the tolerance value.
2. Create a `BoundingBoxIntersectsFilter` with the outline and tolerance.
3. Collect and list the elements that intersect the bounding box considering the tolerance.

#### Code Example
```python
outline = Outline(minPoint, maxPoint)
tolerance = 0.5  # Example tolerance value
filter = BoundingBoxIntersectsFilter(outline, tolerance, False)
elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(filter).ToElements()
for elem in elems:
    print(elem.Id)
```

### Exercise 3: Inverted Intersection Filtering
#### Objective
Filter elements that do not intersect the bounding box and list them.
#### Steps
1. Define the bounding box, tolerance value, and set the inversion parameter to `True`.
2. Create a `BoundingBoxIntersectsFilter` with the outline, tolerance, and inversion.
3. Collect and list the elements that do not intersect the bounding box.

#### Code Example
```python
outline = Outline(minPoint, maxPoint)
tolerance = 0.5  # Example tolerance value
filter = BoundingBoxIntersectsFilter(outline, tolerance, True)
elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(filter).ToElements()
for elem in elems:
    print(elem.Id)
```

### Conclusion
These exercises provide a practical introduction to using the `BoundingBoxIntersectsFilter` in Dynamo for Revit. By working through these examples, students will gain hands-on experience with filtering elements based on geometric criteria and understanding the impact of tolerance and inversion parameters.

## Dynamo Version
The examples and explanations provided are based on the latest version of Dynamo, which at the time of writing is Dynamo Core 2.13.
