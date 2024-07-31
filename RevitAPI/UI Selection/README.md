
# Create TaskDialog

This option involves first creating the TaskDialog using its constructor, setting its properties individually and then using the `Show()` method to display it. This approach will allow access to more settings. For this reason, in cases where you want to interact with the user, it will be the most recommendable option.

Here is an example of how to perform this task.

First, the instance of the `TaskDialog` class is constructed, defining the title, header and body of the pop-up window.

```python
dialog = TaskDialog("Title")
dialog.MainInstruction = "Header"
dialog.MainContent = "Body"
```

## Buttons

Once the base structure of the window is created, the buttons can be created through the `CommonButtons` property. You can add as many as the values defined in the enumerated `TaskDialogCommonButtons`. It simply has to be separated with the "|" symbol.

Possible Buttons:

- `TaskDialogCommonButtons.Ok`
- `TaskDialogCommonButtons.Yes`
- `TaskDialogCommonButtons.No`
- `TaskDialogCommonButtons.Cancel`
- `TaskDialogCommonButtons.Retry`
- `TaskDialogCommonButtons.Close`

The following is an example of how to create the "Yes" and "No" buttons:

```python
dialog.CommonButtons = TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No
```

It is also possible to add a selectable field of type Yes/No. The `VerificationText` property shall be used for this purpose.

```python
dialog.VerificationText = "Yes/No"
```

Alternatively, to the `VerificationText` you can create an `ExtraCheckBoxText` which has identical behavior. Only one of them can be created, but never at the same time.

```python
dialog.ExtraCheckBoxText = "Another selection"
```

## Progress Bar

The `EnableMarqueeProgressBar` property will allow a progress bar to be displayed while all the options available in the pop-up window are configured.

```python
dialog.EnableMarqueeProgressBar = True
```

A progress bar is a window that an application can use to indicate the progress of a long operation. It consists of a rectangle that shows a progress bar that animates as an operation progresses. The animation continues until the TaskDialog is closed.



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



# User Interface Selection Request

From the API it is possible to activate Revit’s selection mode, forcing the user to select the elements with which he/she wishes to work. It is also possible to condition this choice to a specific type of element or filter those that may have been selected by mistake.

Within the API structure there is a namespace called UI.Selection that is exclusively dedicated to this task, specifically, the Selection() class that is detailed in this section.

To guarantee the correct functioning of the code, the following libraries must be imported.

```python
import clr
clr.AddReference('RevitAPIUI')
import Autodesk
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
```




# Select elements by rectangle

This method asks the user to select several elements by drawing a rectangle.

```python
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
selection = uidoc.Selection.PickElementsByRectangle()
```

Users will be able to manipulate the Revit view (zoom, frame and rotate the view), but will not be allowed to click on other elements of the user interface. They will not be able to change the active view, close the active document or the Revit application in the selection session, otherwise an exception will be thrown.



## Select filtered elements

This method will also allow the creation of an object of type user interface for filtering the selected elements. These interfaces cannot be instantiated, so it will be mandatory to create an object directly inheriting its methods and properties.

This will open the possibility of keeping the desired objects regardless of the set of elements that have been selected. Here is an instance where only the walls of a selected set of elements will be selected.



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



# Selection Filter

```python
class Filter(ISelectionFilter):
    def __init__(self):
        pass
    
    def AllowElement(self, element):
        bip = element.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
        if bip.AsString() == "select":
            return True
        else:
            return False
    
    def AllowReference(self, element):
        return False

elems = uidoc.Selection.PickObjects(ObjectType.Element, Filter(), "Select elements")
OUT = [doc.GetElement(x.ElementId) for x in elems]
```

Note: These lines of code will only select items that meet the filtering characteristics set in the `SelectionFilter`.


## Select elements

To invoke the different methods of the Selection() class, the User Interface application of the active document must first be obtained. All selections are made against it.

```python
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
```

Below are the different selection methods.

- **Pick a box**

The PickBox method executes a rectangle based on two clicks. It allows to delimit an area on the screen.

The type of the box is determined by the enumerated PickBoxStyle value which allows to choose between the following values.

- **Crossing**: Used when selecting objects wholly or partially within the frame
- **Enclosing**: Used when selecting objects that are completely enclosed by the frame
- **Directional**: The frame style depends on the direction in which the frame is drawn. Use the Crossing style when drawing from right to left, or the Enclosing style when drawing in the opposite direction

Example:

```python
box = uidoc.Selection.PickBox(PickBoxStyle.Crossing, "Points to define the floor")
```

This will return a PickedBox reference that can be used for a variety of purposes.

---

This is the same selection method used in AutoCAD.


