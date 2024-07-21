## SurfacePlacingLighting Node

The `SurfacePlacingLighting` node is designed to insert light fixtures on a selected face of a Revit ceiling according to general lighting spacing criteria. The spacing criteria ensure an even distribution of light fixtures, maintaining a specified distance \(L\) between the fixture and the wall, and \(2L\) between fixtures. The user must select the necessary divisions on each axis to achieve the desired configuration.

### How to Use

1. **Understanding the Custom Node and Its Inputs**:
   ![Custom Node](LAB /Surface Lighting/assets/1.png)  
   This image shows the custom node and its inputs, explaining the required entries:
   - **CeilingSurface**: The face of the Revit ceiling.
   - **FamilyType**: The type of luminaire.
   - **Division_X**: The number of divisions on the X axis.
   - **Division_Y**: The number of divisions on the Y axis.

2. **Lighting Placement Criteria**:
   ![Placement Criteria](LAB /Surface Lighting/assets/2.png)
   The script respects the lighting placement criteria, ensuring that the spacing between the fixture and the wall is \(L\) and the spacing between fixtures is \(2L\), maintaining an even distribution:
   - **X**: Distance from the wall to the first fixture.
   - **2X**: Distance between subsequent fixtures along the X axis.
   - **Y**: Distance from the wall to the first fixture along the Y axis.
   - **2Y**: Distance between subsequent fixtures along the Y axis.

3. **Loading and Searching for a Package in Dynamo**:
   ![Package Search](LAB /Surface Lighting/assets/3.png)
   This image guides you on how to load and search for a package in Dynamo. Search for `SurfacePlacingLighting` to find and install the custom node.

---

Happy Designing! �
