REVIT API - COLLECT ELEMENTS
* Filter by Class
The OfClass shortcut applies a class filter (ElementFilterClass) to the FilteredElementCollector and allows to search for elements of a class matching the specified class.

python
Copy code
ins = FilteredElementCollector(doc).OfClass(FamilyInstance)
The main Revit API classes are:

AssemblyInstance	GridType	ParameterElement	TilePattern
AssemblyType	Group	Phase	View3D
BeamSystemType	ImageType	ProjectInfo	ViewFamilyType
BeamSystemType	ImageView	ProjectLocation	ViewPlan
CADLinkType	IndependentTag	PropertyLine	ViewPlanType
Ceiling	InsertableObject	Revision	ViewSchedule
CeilingAndFloor	Level	RevisionCloud	ViewSection
CeilingType	LevelType	RevitLinkInstance	ViewSheet
CurtainSystem	MEPCurve	RoofType	Viewport
Dimension	MEPCurveType	SharedParameterElement	WallFoundation
DirectShape	MEPSytem	SlabEdge	WallFoundationType
Family	MEPSytemType	SlabEdgeType	WallSweep
FamilyInstance	Material	SpatialElement	WallType
FilledRegion	ModelText	Sweep	WallType
Floor	ModelTextType	SweepType	WallType
FloorType	MullionType	TableView	
Grid	NestedFamilyTypeReference	TextElement	
PanelType	TextElementType	
Note: The vast majority of existing classes in the Revit API will be searchable using this method, as long as the library where they are hosted is imported.

Example: To search for the PipeSegment the library "Plumbing" must be imported.

python
Copy code
from Autodesk.Revit.DB.Plumbing import *
An equally valid way to filter is to construct the filter instance without using the shortcut. This will give the flexibility to invert the filter by passing a boolean value as a second argument.

Whenever the constructor is used, the WherePasses() method must be used in order to apply the instance of the filter to the collector:

python
Copy code
Filter = ElementClassFilter(Material)
allMat = FilteredElementCollector(doc).WherePasses(Filter).ToElements()
The inverse filter will return everything that is not equal to the filter argument.

python
Copy code
InvertFilter = ElementClassFilter(Material, True)
allMat = FilteredElementCollector(doc).WherePasses(InvertFilter).ToElements()
Note: If you do not need to invert the filter, it will be quicker and more elegant to use the shortcut, as discussed at the beginning of this section.
