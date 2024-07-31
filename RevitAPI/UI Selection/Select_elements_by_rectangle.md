
# Select elements by rectangle

This method asks the user to select several elements by drawing a rectangle.

```python
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
selection = uidoc.Selection.PickElementsByRectangle()
```

Users will be able to manipulate the Revit view (zoom, frame and rotate the view), but will not be allowed to click on other elements of the user interface. They will not be able to change the active view, close the active document or the Revit application in the selection session, otherwise an exception will be thrown.
