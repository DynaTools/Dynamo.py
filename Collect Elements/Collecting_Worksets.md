# Collecting Worksets

## Overview
Revit worksets have their own collector represented by the `FilteredWorksetCollector` class and their own filtering methods. 

## Example
1. **Collect all worksets:**
    ```python
    FW = FilteredWorksetCollector(doc).OfKind(WorksetKind.FamilyWorkset).ToWorksets()
    VW = FilteredWorksetCollector(doc).OfKind(WorksetKind.ViewWorkset).ToWorksets()
    SW = FilteredWorksetCollector(doc).OfKind(WorksetKind.StandardWorkset).ToWorksets()
    ```

2. **Filter worksets by type:**
    ```python
    Filter = WorksetKindFilter(WorksetKind.UserWorkset)
    Elements = FilteredWorksetCollector(doc).WherePasses(Filter).ToWorksets()
    ```
