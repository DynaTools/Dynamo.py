# Filter Elements by Class

## Summary

The Revit API allows filtering and collecting specific elements from a document using the `FilteredElementCollector` class. By using the `OfClass()` method, you can specify the class of the elements you want to collect, such as `FamilyInstance`, `WallType`, and others. Additionally, you can apply inverted filters and combine different types of filters to refine the selection of elements. Efficient use of these methods enables the automation of tasks and precise data extraction from Revit models.

## Example

```python
# Importing the necessary libraries
from Autodesk.Revit.DB import FilteredElementCollector, ElementClassFilter, FamilyInstance, Material

# Creating an element collector from the active document
doc = __revit__.ActiveUIDocument.Document

# Collecting all family instances in the document
family_instances = FilteredElementCollector(doc).OfClass(FamilyInstance).ToElements()

# Example of a filter to collect elements of type Material
filter_material = ElementClassFilter(Material)
materials = FilteredElementCollector(doc).WherePasses(filter_material).ToElements()

# Example of an inverted filter to collect all elements that are not of type Material
invert_filter_material = ElementClassFilter(Material, True)
non_materials = FilteredElementCollector(doc).WherePasses(invert_filter_material).ToElements()

# Displaying the number of elements found
print("Number of family instances:", len(family_instances))
print("Number of materials:", len(materials))
print("Number of elements that are not materials:", len(non_materials))

"""
Create a Dynamo script that filters and collects all windows (Window) from a Revit model, and then applies an additional filter to identify which of these windows are in external walls. To achieve this, you will need to use class filters and parameter-based filters for the windows and walls.

Suggested Steps:
1. Use FilteredElementCollector to collect all windows.
2. Apply a filter to check the location parameter of the windows.
3. Combine the results to get only the windows located in external walls.
4. Display or export the results as needed.
"""
