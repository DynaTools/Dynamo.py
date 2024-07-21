# Elements Intersecting a BoundingBox with Tolerance

## Overview
This filter allows you to define a tolerance (Double) as an argument and also provides the option to invert the filter with a Boolean value.

## Example
1. **Filter elements intersecting a bounding box:**
    ```python
    Filter = BoundingBoxIntersectsFilter(outline)
    elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(Filter).ToElements()
    ```

2. **Filter with tolerance:**
    ```python
    Filter = BoundingBoxIntersectsFilter(outline, tolerance, False)
    elems = FilteredElementCollector(doc, doc.ActiveView.Id).WherePasses(Filter).ToElements()
    ```

## Note
When using tolerances, remember to convert the units. The filter returns a list of elements that intersect the bounding box considering the defined tolerance.
