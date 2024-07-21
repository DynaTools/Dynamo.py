# Filter Items According to a Specific Level

## Overview
To filter items hosted in a level, use the `ElementLevelFilter()` constructor.

## Example
1. **Apply the filter:**
    ```python
    Level = UnwrapElement(IN[0])
    Filter = ElementLevelFilter(Level.Id)
    Elements = FilteredElementCollector(doc).WherePasses(Filter).WhereElementIsNotElementType().ToElements()
    ```
