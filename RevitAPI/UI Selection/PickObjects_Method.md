
# The PickObjects() Method

The PickObjects() method shall allow multiple objects to be selected at once.

- **Element**: The entire element.
- **Edge**: Any model edge.
- **Face**: Any face.
- **LinkedElement**: Elements in linked RVT files.
- **Subelement**: The whole element or sub-element.
- **PointOnElement**: Any point on an element (on a face or curve).

Here are some simple examples of how to implement this method:

```python
elem = uidoc.Selection.PickObject(ObjectType.Element, "Select an element")
face = uidoc.Selection.PickObject(ObjectType.Face, "Select a face")
edge = uidoc.Selection.PickObject(ObjectType.Edge, "Select an edge")
link = uidoc.Selection.PickObject(ObjectType.LinkedElement, "Select a linked element")
point = uidoc.Selection.PickObject(ObjectType.PointOnElement, "Select a point")

elems = uidoc.Selection.PickObjects(ObjectType.Element, "Select elements")
faces = uidoc.Selection.PickObjects(ObjectType.Face, "Select faces")
edges = uidoc.Selection.PickObjects(ObjectType.Edge, "Select edges")
links = uidoc.Selection.PickObjects(ObjectType.LinkedElement, "Select linked elements")
points = uidoc.Selection.PickObjects(ObjectType.PointOnElement, "Select points")
```
