
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

