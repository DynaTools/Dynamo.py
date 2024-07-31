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
