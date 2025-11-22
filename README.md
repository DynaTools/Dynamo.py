# Parametric Modeling Course with Python and Revit

## INTRODUCTION

Building Information Modeling (BIM) is increasingly present and has brought significant changes to architecture, engineering, and construction (AEC), as it represents a faithful three-dimensional representation of a building.

When complete, the computationally generated model contains precise geometry and relevant data necessary to support construction, manufacturing, and supply of materials needed for construction (EASTMAN et al., 2018, our translation).

BIM models are developed through platforms known as parametric, object-based systems. They possess a type of intelligence or design behavior (EASTMAN et al., 2018). For example, when modeling a wall element, it will be automatically identified in the quantity list and associated sections. Another parametric characteristic is in the insertion of elements: a door can only be inserted in a wall element, which in turn will have its material area immediately removed from the metadata.

This type of parametric intelligence is absent in CAD modeling programs. These require the designer to identify the element by filling in the associated property. In the example cited above, the door can be inserted at any point in the CAD model without generating any error identification, just as sections will need to be updated when changes occur in the floor plan.

The limits and usability of CAD and BIM programs can vary in a project, and the benefits should be evaluated by the involved team. Despite the availability of various CAD and BIM tools, the designer may eventually be confronted with a need to seek programming support as a solution for expanding software functionality. Visual programming or visual programming language (VPL) is the name given to any type of programming language that can be manipulated in a graphical format. One of the positive characteristics of this way of programming is the instant visual feedback of the result to the designer, without the need to compile complex codes with mastery of programming concepts and algorithm creation.

Research indicates that the use of VPL presents benefits to the designer in relation to textual programming, especially for those who need more visual feedback from their process. VPL improves the ability to see parametrization options within projects. This way of thinking is classified as parametric thinking. The designer, when developing this reasoning, begins abstractly to conceive connections between project elements that can be translated into algorithms.

Algorithms are the set of defined, ordered rules, operations, and procedures used in solving a problem in a finite number of steps. Therefore, the order and organization of information are crucial for the designer to produce good results. It is important that the designer has knowledge about the types and classifications of the tools they use in the project, as they can make more informed decisions about when to use a particular software, technology, or programming language during project development.

## RESEARCH PROBLEM AND METHODOLOGY

Existing courses that aim to teach the use of visual programming interfaces like Grasshopper and Dynamo are excellent means of introducing the designer to parametric design tools. We find several quick courses on these tools available on platforms like LinkedIn Learning and Udemy, for example. These courses have content that teaches the designer to use the program interfaces. We observe that the content is directed at teaching through practical examples that complement functionalities that are not present in BIM programs by default.

As the figure below illustrates, courses have focused on teaching students the syntax of the language, that is, the rules that determine which combinations of nodes generate useful functions, how constructors operate with data types, which symbols and punctuations are accepted to declare variables and data lists, etc. In this way, courses have been configured as a set of ready-made routines that can be taught so that students begin to understand the interface's functioning through these examples.

In a practical way, this makes the course content objective and functional. However, keeping the student focused on the tool or learning the interface does not guarantee that they understand a theoretical-practical framework that provides autonomy to think about project flows.

### Figure 01 - LinkedIn Learning Course - Dynamo Essential Training

![image](https://github.com/user-attachments/assets/a906a0ce-2eae-4cda-8d2f-45f0fbda94d8)

The course can be rich in examples, but without a logical structure, the student is restricted to the possibilities that were presented in class. Learning about the structure of programming languages beyond a specific language like Dynamo or Grasshopper can help the designer understand what the best computational design strategy might be to solve a particular problem. This also ensures that the knowledge learned along the way can be reused in the long term, as specific VPLs may change or become obsolete.

If the student knows the concepts that structure VPLs in a broader context and in dialogue with textual programming languages, they will be better prepared for these changes and adaptations (LEITÃO, 2013). Furthermore, there are some fundamental differences in the needs that a designer more focused on BIM needs to achieve in workflows based on this technology:

- In BIM, it is not frequent to use the VPL Dynamo to test formal project conception, whether complex, simple, or organic forms. This phase of formal investigation is usually done in other three-dimensional programs or using the VPL Grasshopper, which have functions more adapted for this project phase, and are later connected to BIM workflows.
- BIM tools already have a level of parametrics incorporated by default. Eastman et al. (2018) call this intelligent behavior design behavior:

> The range of rules that can be incorporated into a parametric graph determines the generality of the system. Parametric object families are defined using parameters and the relationships between parameters. Since relationships constrain the design behavior of a parametric model, parametric modeling is also known as constraint modeling (EASTMAN et al., 2018, p.39).

This illustrates that BIM VPL programmers do not need to create codes that restrict the relationships between objects or components of a model, as is usually done by Grasshopper users at first, since the BIM system already brings this solution incorporated.

## TAXONOMY OF PARAMETRIC MODELS

When a computer science course is well-designed and developed, anyone can learn to program. Starting from this principle, we seek to structure the course using the taxonomy proposed by Patrick Janssen and Rudi Stouffs, thus forming the first bibliography we suggest to Visual Parametric Programming (VPL) students at the beginning of their studies. Currently, there are many Building Information Modeling (BIM) software in the market and, sometimes, calling them just BIM program, parametric program, or parametric modeling program may not be sufficient if we want to compare and classify them properly.

In Types of Parametric Modelling, the authors define a General Parametric Model (GPM) as the first classification structure.

The GPM is described using a common mathematical concept in computer science, the directed acyclic graph or directed acyclic graph (DAG). A DAG is a graph that contains directed arcs without any cycle, that is, it is not possible to return to a node once it has already been visited (DIRECTED, 2021). This means it is not possible to traverse the same path multiple times, thus avoiding data recursion.

### Figure 02 - Directed Acyclic Graph

![Directed Acyclic Graph](https://github.com/user-attachments/assets/2b17f4e8-ab94-4962-9aac-dcfadbd9a743)
**Source**: Extracted from Wikipedia¹

Considering that architects, engineers, and designers generally do not have formal training in programming but are being introduced to it through visual programming languages (VPL), the concept of data iteration can become very abstract and hinder student engagement with the content.

The authors classify VPLs (which, in turn, are described as Directed Acyclic Graphs) by the way they iterate data. The types of data iteration are:

1. **Single iteration**: The repetition process occurs directly and linearly.
2. **Implicit multiple iteration**: Repetition happens within data structures like nested lists, in a way not explicitly defined by the user.
3. **Explicit multiple iteration**: Repetition is defined clearly and in detail by the user, allowing greater control over the iterative process.

These types of iteration form the basis for the taxonomy of parametric models described below:

1. **Object Modeling**: Programs that do not allow any type of iteration, such as traditional CAD programs.
2. **Association Modeling**: Programs that allow a single round of iterations, such as Autodesk Revit, where a change in one component can reflect in other associated components.
3. **Data Flow Modeling**: Programs that allow implicit iteration through the use of nested lists, such as Grasshopper for Rhino3D and Bentley's Generative Components.
4. **Procedure-Based Modeling**: Programs that allow explicit iteration, where the user clearly defines how repetition will occur, such as Dynamo BIM.

These types of iteration, and the types of modeling they support, are fundamental to understanding the structure of VPLs used in the area, as well as the types of modeling supported by programs considered parametric. Next, we will focus on the specifics of BIM parametric flows, exploring how these concepts are applied in practice and what their implications are for project development in civil construction.

### Examples of Modeling Software and Their Applications

To better understand how different types of software fit into the concepts of modeling and iteration, here is an explanation of some of the main programs used in the architecture, engineering, and design industry.

- **Revit**: Autodesk Revit is Building Information Modeling (BIM) software. It allows the creation of intelligent 3D models that include important data about construction components. Revit is an example of Association Modeling software, where a modification in one component can automatically update other associated components. This facilitates coordination between different disciplines (architecture, structure, and MEP - mechanical, electrical, and plumbing).

- **Grasshopper**: Grasshopper is a plugin for Rhino3D that allows parametric modeling. It is used to create algorithms that generate complex geometries. Grasshopper exemplifies Data Flow Modeling, where implicit iterations occur through lists and nested data structures, allowing the manipulation and generation of complex forms in a visual way.

- **Dynamo**: Dynamo is visual programming software that integrates with Revit, allowing the creation of scripts to automate tasks and create complex parametric geometries. Dynamo exemplifies Procedure-Based Modeling, where the user explicitly defines how iteration and data manipulation will occur.

- **Rhinoceros (Rhino)**: Rhinoceros, or Rhino, is 3D modeling software based on NURBS (Non-Uniform Rational B-Splines), used primarily to create complex surfaces and geometries. Although Rhino itself is more focused on object modeling, when combined with Grasshopper, it allows advanced parametric modeling.

- **AutoCAD**: AutoCAD is computer-aided design (CAD) software used to create technical drawings and plans. It exemplifies Object Modeling, as it is used primarily to create static geometries without complex iterations or parametrizations.

- **Inventor**: Autodesk Inventor is 3D CAD modeling software used primarily for mechanical design. It allows the creation of parts, assemblies, and simulations. Inventor can be classified as Association Modeling, as it allows changes in one component to reflect in associated assemblies and drawings.

- **SolidWorks**: SolidWorks is 3D CAD software used for product design, mechanical engineering, and simulations. Similar to Inventor, it supports Association Modeling with advanced simulation and analysis capabilities.

- **ArchiCAD**: ArchiCAD is BIM software developed by Graphisoft. It is used primarily for architectural modeling, allowing the creation of detailed building models. ArchiCAD also falls under Association Modeling, where changes in one model element can affect other related elements.

- **Blender**: Blender is open-source 3D modeling software that is widely used in animation, visual effects, 3D art, and game design. Although it is better known for its artistic and animation capabilities, Blender also supports Object Modeling and can be extended for parametric modeling through scripts and plugins.

### Summary

The classification of the above software in terms of their iteration methods and modeling types helps understand their capabilities and specific applications:

- **Object Modeling**: AutoCAD, Blender (with focus on static geometry).
- **Association Modeling**: Revit, Inventor, SolidWorks, ArchiCAD.
- **Data Flow Modeling**: Grasshopper (for Rhino3D).
- **Procedure-Based Modeling**: Dynamo (for Revit).

Understanding these concepts and how they apply to different software is crucial for choosing the right tool for each type of project and for developing efficient workflows in the AEC (Architecture, Engineering, and Construction) industry.

## Integration of Python, Revit, and Dynamo: Enhancing Parametric Design

The combination of Python, Revit, and Dynamo offers a powerful set of tools for parametric modeling and task automation in architecture, engineering, and construction (AEC). Let's explore how each component contributes to this integration and what the benefits of this approach are.

### Revit

Autodesk Revit is Building Information Modeling (BIM) software that allows the creation of detailed 3D models with rich information about construction components. It is widely used for architectural, structural, and MEP (mechanical, electrical, and plumbing) system design. Revit supports Association Modeling, where a change in one component can automatically reflect in related components, facilitating coordination between different disciplines.

### Dynamo

Dynamo is a visual programming environment that integrates seamlessly with Revit. It allows users to create visual scripts to automate repetitive tasks, generate complex geometries, and manipulate data in advanced ways. Dynamo is a Procedure-Based Modeling tool, where the user explicitly defines the processes of iteration and data manipulation.

### Python

Python is a high-level programming language known for its simplicity and versatility. It is widely used in various fields, including task automation, data analysis, and script development for software like Revit and Dynamo. The integration of Python with Dynamo significantly expands Dynamo's capabilities, allowing the creation of more complex and customized scripts.

### Practical Integration

The integration of Python, Revit, and Dynamo can be visualized as a combination of their individual strengths, allowing more efficient and complex workflows. Here are some examples of how this integration can be used:

#### Automation of Repetitive Tasks

- **Revit**: Initial setup and management of BIM models.
- **Dynamo**: Creation of visual scripts to automate repetitive tasks, such as creating standard elements in a project.
- **Python**: Use of scripts to automate even more complex processes, such as importing and manipulating large volumes of external data.

#### Creation of Complex Geometries

- **Revit**: Visualization and documentation of created geometries.
- **Dynamo**: Generation of complex parametric forms through visual nodes.
- **Python**: Programming of advanced algorithms to generate and manipulate geometries that would be difficult to implement with Dynamo alone.

#### Project Analysis and Optimization

- **Revit**: Central repository for project information and visualization of analysis results.
- **Dynamo**: Scripts to execute basic performance analyses and optimization.
- **Python**: Implementation of complex analysis algorithms, such as energy optimization, advanced structural analysis, and workflow simulations.

#### Interoperability and Data Manipulation

- **Revit**: BIM platform that centralizes all project data.
- **Dynamo**: Interaction with Revit data for manipulation and analysis.
- **Python**: Use of external libraries (such as pandas and numpy) for advanced data analysis and manipulation, import and export of data between different formats, and integration with other platforms and services.

### Benefits of Integration

- **Efficiency and Productivity**: Automation of repetitive and complex tasks, reducing the time needed to complete projects.
- **Precision and Consistency**: Reduction of human errors through process automation and data validation.
- **Flexibility and Customization**: Creation of customized solutions that meet the specific needs of each project.
- **Innovation**: Ability to explore new forms of design and analysis that would be difficult or impossible to perform with traditional tools.

### Practical Example

Imagine you are working on a large-scale project that requires the placement of thousands of luminaires in a building. Manually, this would be extremely time-consuming and prone to errors. With the integration of Python, Revit, and Dynamo, you can:

1. Create a script in Dynamo to generate luminaire insertion points based on parametric rules (distance between luminaires, variable heights, etc.).
2. Use Python within Dynamo to read a CSV file containing specific information about each luminaire (type, power, etc.) and apply this data to the model.
3. Automatically update the model in Revit, inserting all luminaires in the correct locations with the appropriate information.

This workflow not only saves time but also ensures that all luminaires are placed according to project specifications, improving the quality and efficiency of the design process.

The combination of Python, Revit, and Dynamo offers a powerful set of tools for any AEC professional, allowing advanced automation, creation of complex geometries, and deep project analysis, all with unparalleled flexibility and customization.

## Parametric Modeling Course Curriculum with Python and Revit

The "Parametric Modeling with Python and Revit" course is a comprehensive journey that integrates visual and textual programming tools and modeling, including Dynamo and Revit. Starting with Python programming using Processing.py, students learn fundamental programming concepts, variable manipulation, control structures, and object orientation in an intuitive visual environment. Next, the course advances to the practical application of these concepts in the Dynamo environment with the Revit API, allowing students to develop complex scripts for automation and parametric modeling. The course is designed to provide a solid foundation in programming and parametric modeling, culminating in final projects that demonstrate the practical application of acquired knowledge.

## Module 01 - Introduction to Visual Programming with Processing.py

**Duration:** 15 hours  
**Objective:** Introduce programming concepts, variables, lists, and object orientation.  
**Project:** Students will present a project at the end of the course.  
**Language:** Python  
**Resources:** 
- [GitHub - Processing](https://github.com/DynaTools/Dynamo.py/tree/main/Processing)
- [Class Materials - Processing Python](https://abav.lugaralgum.com/material-aulas/Processing-Python/)
- [Reference - Processing Python](https://py.processing.org/reference/)

### Module 01 Structure

#### Lesson 1: First Steps with Processing.py
- Basic notions of visual programming
- Installing Processing.py
- First program in Processing.py
- **Exercise:** Simple script that draws a circle on the screen
- **Example:**
```python
def setup():
    size(800, 600)  # Window size
    background(255)  # White background color

def draw():
    # Draw a circle in the center of the screen
    fill(150, 0, 150)  # Purple fill color
    ellipse(width / 2, height / 2, 100, 100)  # Circle with diameter 100
```

#### Lesson 2: Variables and Data Types
- Data types in Python
- Declaration and use of variables in Processing.py
- Basic operations with variables
- **Exercise:** Draw geometric shapes using variables

#### Lesson 3: Control Structures
- Conditionals (if, else, elif)
- Loops (for, while)
- Using control structures to manipulate drawings
- **Exercise:** Draw conditional and repetitive geometric shapes

#### Lesson 4: Functions
- Definition and use of functions
- Built-in functions in Processing.py
- Creating custom functions
- **Exercise:** Using functions to modularize the drawing of complex shapes

#### Lesson 5: Lists and Data Structures
- Introduction to lists in Python
- Manipulating lists to create visual patterns
- **Exercise:** Draw a series of shapes using lists to define positions and sizes

#### Lesson 6: Introduction to Object Orientation
- Basic concepts of object orientation (OO)
- Creating classes and objects in Python
- **Exercise:** Creating a simple class to draw geometric shapes

#### Lesson 7: Methods and Attributes
- Methods and attributes in classes
- Difference between instance methods and class methods
- **Exercise:** Expanding the geometric shapes class to include drawing methods

#### Lesson 8: Inheritance and Polymorphism
- Concepts of inheritance in OO
- Creating subclasses
- Using polymorphism for methods
- **Exercise:** Creating a class hierarchy for different geometric shapes

#### Lesson 9: Interactivity with Objects
- User input to manipulate objects
- Using mouse and keyboard for interaction with objects
- **Exercise:** Interactive script that responds to mouse movements

#### Lesson 10: Object Animation
- Animation concepts in Processing.py applied to objects
- Using loops and variables to create object animations
- **Exercise:** Animation of geometric shapes

#### Lesson 11: Managing Multiple Objects
- Creating and managing multiple objects in a scene
- Using lists to store and manipulate objects
- **Exercise:** Creating a scene with multiple interacting objects

#### Lesson 12: Final Project - Part 1
- Discussion and planning of the final project
- Beginning implementation of the project with object orientation
- **Exercise:** Initial project development

#### Lesson 13: Final Project - Part 2
- Continuation of project implementation
- Application of learned concepts (interactivity, animation, etc.)
- **Exercise:** Intermediate project development

#### Lesson 14: Final Project - Part 3
- Project finalization
- Final tests and adjustments
- **Exercise:** Project completion and preparation for presentation

#### Lesson 15: Project Presentations
- Student project presentations
- Feedback and discussion about presented projects

## Module 02 - Object Orientation with Revit API and Python

**Duration:** 30 hours  
**Objective:** Teach object orientation with the Revit API within the Dynamo environment.  
**Project:** The student chooses a problem to be solved and, with the support of the class and course, presents the solution at the end.  
**Language:** Design Script, Python  
**Resources:** 
- [GitHub - Revit API Collection](https://github.com/DynaTools/Dynamo.py/tree/main/RevitAPI/Collection)
- [GitHub - Library](https://github.com/DynaTools/Dynamo.py/tree/main/Library)
- [Dynamo Python Primer](https://dynamopythonprimer.gitbook.io/dynamo-python-primer)

### Module 02 Structure

#### Lesson 1: Introduction to Python in Dynamo
- Development environment setup
- First steps with Python scripts in Dynamo
- **Exercise:** Simple script using Python in Dynamo

#### Lesson 2: Understanding Dynamo
- Overview of Dynamo and its integration with Revit
- Geometry and data concepts in Dynamo
- **Exercise:** Creating a script that generates basic geometry in Dynamo

#### Lesson 3: Getting Started with the Revit API
- First steps with the Revit API
- Initial setup and basic commands
- **Exercise:** Script to manipulate Revit elements

#### Lesson 4: Specific Revit Topics

##### 4.1 Introduction to the Revit API
- Basic concepts and API structure
- **Exercise:** Accessing basic information from a Revit document

##### 4.2 How to Read the Revit API Documentation
- Navigation and interpretation of API documentation
- **Exercise:** Search in documentation to solve a specific problem

##### 4.3 Doc, UIDoc, App, UIApp
- Differences and uses of Doc, UIDoc, App, and UIApp
- **Exercise:** Using these objects to access and modify data in Revit

##### 4.4 Unwrapping Revit Elements
- Concept of unwrapping in Dynamo
- **Exercise:** Unwrap elements and modify their properties

##### 4.5 The FilteredElementCollector
- Selecting elements in Revit using FilteredElementCollector
- **Exercise:** Script that selects and manipulates a specific set of elements

##### 4.6 Geometry Conversion Methods
- Converting geometry between Dynamo and Revit
- **Exercise:** Convert Dynamo geometry to Revit elements

##### 4.7 Working with Parameters
- Types of parameters in Revit and how to access them
- **Exercise:** Modifying parameters of selected elements

##### 4.8 Working with Transactions
- Concept of transactions in Revit
- **Exercise:** Script that performs multiple operations within a transaction

##### 4.9 Opening and Closing External Files
- Manipulating external files via API
- **Exercise:** Open, modify, and save Revit files

##### 4.10 Selection via User Interface
- Creating interfaces for element selection
- **Exercise:** Script that creates an interface for selecting elements in Revit

##### 4.11 Working with Units
- Manipulating and converting units in Revit
- **Exercise:** Adjust element units to a specific standard

##### 4.12 Built-in Categories
- Using built-in categories in Revit
- **Exercise:** Selection and modification of elements by category

##### 4.13 Family Manipulation
- Creating and modifying families in Revit
- **Exercise:** Script that creates and modifies parametric families

##### 4.14 Task Dialogs for Feedback
- Creating and using task dialogs for user interaction
- **Exercise:** Script that uses task dialogs to interact with the user

#### Lesson 5: Revit Dashboard
- Review of key terms and concepts from the course
- Example: https://revitoverview.streamlit.app/
- **Exercise:** Creating a dashboard with Streamlit and Python

#### Lesson 6: Conclusion and Next Steps
- Reflection on the course and next steps
- **Exercise:** Planning future projects using Dynamo and Revit API
