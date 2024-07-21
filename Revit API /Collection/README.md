# Revit API Collectors for Dynamo

In the context of Revit API for Dynamo, collectors are essential tools used to retrieve elements from a Revit document based on specific criteria. These collectors, known as `FilteredElementCollector` in the Revit API, allow users to filter elements by various parameters, such as category, type, parameter values, and more.

This README provides a comprehensive guide to understanding and using collectors in Dynamo with Revit API, referencing each explanation with the corresponding `.md` file.

## Table of Contents

1. [Element Conversion Methods](#element-conversion-methods)
2. [Elements Intersecting a BoundingBox](#elements-intersecting-a-boundingbox)
3. [Elements within a BoundingBox](#elements-within-a-boundingbox)
4. [Exclusive Filter](#exclusive-filter)
5. [FamilySymbols Filtering](#familysymbols-filtering)
6. [Filter by Class](#filter-by-class)
7. [Filter Items According to the Current View](#filter-items-according-to-the-current-view)
8. [Filter by Family Instance](#filter-by-family-instance)
9. [Filter by Level](#filter-by-level)
10. [Filter by Parameter Values](#filter-by-parameter-values)
11. [Filter by Workset](#filter-by-workset)
12. [Filter Intersecting Elements](#filter-intersecting-elements)
13. [Filter Selectable Items](#filter-selectable-items)
14. [Filter Space Tags](#filter-space-tags)
15. [Filtering by Design Options](#filtering-by-design-options)
16. [Filtering Elements Controlled by a Linked Model](#filtering-elements-controlled-by-a-linked-model)
17. [Filtering Elements Visible in View](#filtering-elements-visible-in-view)
18. [Filtering of Types and Instances](#filtering-of-types-and-instances)
19. [Filtering View-Dependent Elements](#filtering-view-dependent-elements)
20. [Insertion Point within a BoundingBox](#insertion-point-within-a-boundingbox)
21. [Logic Filters](#logic-filters)
22. [MultiClass Filtering](#multiclass-filtering)
23. [Other FilteredElementCollector Methods](#other-filteredelementcollector-methods)
24. [Quick Filter Concatenation](#quick-filter-concatenation)
25. [Slow Filters](#slow-filters)
26. [Structural Element Filtering](#structural-element-filtering)
27. [BoundingBox Tolerance](#boundingbox-tolerance)
28. [Collecting Worksets](#collecting-worksets)

## Element Conversion Methods
Detailed explanation of methods to convert elements.
![Element_Conversion_Methods.md](Revit%20API%20/Collection/Element_Conversion_Methods.md)

## Elements Intersecting a BoundingBox
How to collect elements intersecting a bounding box.
![Elements_Intersecting_a_BoundingBox.md](Revit%20API%20/Collection/Elements_Intersecting_a_BoundingBox.md)

## Elements within a BoundingBox
Collecting elements within a specified bounding box.
![Elements_within_a_BoundingBox.md](Revit%20API%20/Collection/Elements_within_a_BoundingBox.md)

## Exclusive Filter
Using exclusive filters to refine collections.
![Exclusive_Filter.md](Revit%20API%20/Collection/Exclusive_Filter.md)

## FamilySymbols Filtering
Filtering elements based on family symbols.
![FamilySymbols_Filtering.md](Revit%20API%20/Collection/FamilySymbols_Filtering.md)

## Filter by Class
Collecting elements based on their class.
![Filter_by_Class.md](Revit%20API%20/Collection/Filter_by_Class.md)

## Filter Items According to the Current View
Filtering elements visible in the current view.
![Filter_Items_According_to_the_Current_View.md](Revit%20API%20/Collection/Filter_Items_According_to_the_Current_View.md)

## Filter by Family Instance
Collecting family instances.
![Filter_by_Family_Instance.md](Revit%20API%20/Collection/Filter_by_Family_Instance.md)

## Filter by Level
Filtering elements by level.
![Filter_by_Level.md](Revit%20API%20/Collection/Filter_by_Level.md)

## Filter by Parameter Values
Using parameter values to filter elements.
![Filter_by_Parameter_Values.md](Revit%20API%20/Collection/Filter_by_Parameter_Values.md)

## Filter by Workset
Collecting elements by workset.
![Filter_by_Workset.md](Revit%20API%20/Collection/Filter_by_Workset.md)

## Filter Intersecting Elements
How to filter elements that intersect.
![Filter_Intersecting_Elements.md](Revit%20API%20/Collection/Filter_Intersecting_Elements.md)

## Filter Selectable Items
Filtering selectable elements.
![Filter_Selectable_Items.md](Revit%20API%20/Collection/Filter_Selectable_Items.md)

## Filter Space Tags
Filtering space tags.
![Filter_Space_Tags.md](Revit%20API%20/Collection/Filter_Space_Tags.md)

## Filtering by Design Options
Using design options to filter elements.
![Filtering_by_Design_Options.md](Revit%20API%20/Collection/Filtering_by_Design_Options.md)

## Filtering Elements Controlled by a Linked Model
Filtering elements in linked models.
![Filtering_Elements_Controlled_by_a_Linked_Model.md](Revit%20API%20/Collection/Filtering_Elements_Controlled_by_a_Linked_Model.md)

## Filtering Elements Visible in View
Collecting elements visible in the current view.
![Filtering Elements Visible in View](https://github.com/DynaTools/Dynamo.py/blob/main/Revit%20API%20/Collection/Filtering%20Elements%20Visible%20in%20View.md))

## Filtering of Types and Instances
Filtering elements by types and instances.
![Filtering_of_Types_and_Instances.md](Revit%20API%20/Collection/Filtering_of_Types_and_Instances.md)

## Filtering View-Dependent Elements
Collecting view-dependent elements.
![Filtering_View-Dependent_Elements.md](Revit%20API%20/Collection/Filtering_View-Dependent_Elements.md)

## Insertion Point within a BoundingBox
Finding insertion points within a bounding box.
![Insertion_Point_within_a_BoundingBox.md](Revit%20API%20/Collection/Insertion_Point_within_a_BoundingBox.md)

## Logic Filters
Using logical operations for filtering.
![Logic_Filters.md](Revit%20API%20/Collection/Logic_Filters.md)

## MultiClass Filtering
Filtering elements by multiple classes.
![MultiClass_Filtering.md](Revit%20API%20/Collection/MultiClass_Filtering.md)

## Other FilteredElementCollector Methods
Additional methods for element collection.
![Other_FilteredElementCollector_Methods.md](Revit%20API%20/Collection/Other_FilteredElementCollector_Methods.md)

## Quick Filter Concatenation
Concatenating multiple filters quickly.
![Quick_Filter_Concatenation.md](Revit%20API%20/Collection/Quick_Filter_Concatenation.md)

## Slow Filters
Using slow filters for element collection.
![Slow_Filters.md](Revit%20API%20/Collection/Slow_Filters.md)

## Structural Element Filtering
Filtering structural elements.
![Structural_Element_Filtering.md](Revit%20API%20/Collection/Structural_Element_Filtering.md)

## BoundingBox Tolerance
Using bounding box tolerance in filters.
![BoundingBox_Tolerance.md](Revit%20API%20/Collection/BoundingBox_Tolerance.md)

## Collecting Worksets
Collecting elements by worksets.
![Collecting_Worksets.md](Revit%20API%20/Collection/Collecting_Worksets.md)

---

Happy Designing! 🎨

