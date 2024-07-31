
# Selected Views

The Selection class will also allow obtaining the views selected in the project browser. The `GetElementIds()` method is used to perform this task. In the following example, this process will be packed into a function.

```python
actuiapp = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

def ActualSelection():
    def output(x):
        if len(x) == 1: return x[0]
        else: return x

    selectID = actuiapp.Selection.GetElementIds()
    return output([doc.GetElement(id).ToDSType(True) for id in selectID])
```

## Select Points

The `PickPoint()` method may be used to select a specific snap point of any object in the model. The enumerated `ObjectSnapTypes` value shall be used to identify the type of snap point and shall allow selection from the following possibilities:

- **None**: It is not attached to anything.
- **EndPoints**: The end point of an element or component.
- **MidPoints**: Midpoint of an element or component.
- **Nearest**: Closest element or component.
- **WorkPlaneGrid**: Work plane grid.
- **Intersections**: Intersections.
- **Centers**: Centre of an arc.
- **Perpendicular**: Perpendicular elements or components.
- **Tangents**: Tangent to an arc.
- **Quadrants**: Points of the quadrant.
- **Points**: Site points.

In case the `ObjectSnapType` is not specified, any point in the model can be selected.

Here is an example of how to implement this selection method.

```python
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
point = uidoc.Selection.PickPoint(ObjectSnapTypes.EndPoints, "End Point")
OUT = point
```

## Application Views

The `UIView` class represents all the views of the model that are open within Revit. To collect them, you can use the `GetOpenUIViews()` method.
