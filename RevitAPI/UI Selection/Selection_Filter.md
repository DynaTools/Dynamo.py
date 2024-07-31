
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
