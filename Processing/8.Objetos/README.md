
## Resumo

Este documento aprofunda-se na programação orientada a objetos (OOP) no Processing. Ele explica como definir classes e criar objetos, encapsulando dados e funcionalidades em componentes reutilizáveis.

10/Objects
Object-oriented programming
(OOP) is a
di‡erent
way to think about your pro-
grams. Although the term …object-
oriented programming— may sound
intimidating, there•s good news: you•ve
been working with objects since
Chap-
ter 7
, when you started using
PImage
,
PFont
,
String
, and
PShape
. Unlike the
primitive data types
boolean
,
int
, and
float
, which can store only one value, an
object can store many. But that•s only a
part of the story. Objects are also a way
to group variables with related functions.
Because you already know how to work
with variables and functions, objects sim-
ply combine what you•ve already learned
into a more understandable package.
Objects are important , because they break up ideas into smaller
building blocks. This mirrors the natural world where, for
instance, organs are made of tissue, tissue is made of cells, and
so on. Similarly, as your code becomes more complicated, you
must think in terms of smaller structures that form more com-
plicated ones. It†s easier to write and maintain smaller, under-
standable pieces of code that work together than it is to write
one large piece of code that does ever y thing at once.
129




Fields and Methods
A software object is a collection of related variables and func-
tions. In the context of objects, a variable is called a
®eld
(some-
times known as an
instance variable
or
data attribute
in Py thon)
and a function is called a
method
. Fields and methods work in a
manner similar to the variables and functions covered in earlier
chapters, but we†ll use the new terms to emphasize that they
are a part of an object . To say it another way, an object com-
bines related data
(®elds)
with related actions and behaviors
(methods). The idea is to group together related data with
related methods that act on that data.
For instance, to model a radio, think about what parameters can
be adjusted and the actions that can
a‚ect
those parameters:
Fields
volume
,
frequency
,
band
(FM, AM),
power
(on,
o‚)
Methods
setVolume
,
setFrequency
,
setBand
Modeling a simple mechanical device is easy compared to mod-
eling an organism like an ant or a person. It†s not possible to
reduce such complex organisms to a few
®elds
and methods,
but it is possible to model enough to create an interesting simu-
lation.
The Sims
video game is a clear example. This game is
played by managing the daily activities of simulated people. The
characters have enough personality to make a playable, addic-
tive game, but no more. In fact , they have only
®ve
personality
attributes: neat , outgoing, active, playful, and nice. With the
knowledge that it†s possible to make a highly
simpli®ed
model of
complex organisms, we could start programming an ant with
only a few
®elds
and methods:
Fields
type
(worker, soldier),
weight
,
length
Methods
walk
,
pinch
,
releasePheromones
,
eat
If you made a list of an ant†s
®elds
and methods, you might
choose to focus on
di‚erent
aspects of the ant to model.




There†s no right way to make a model, as long as you make it
appropriate for the purpose of your program†s goals.
De®ne
a Class
Before you can create an object , you must
de®ne
a class. A
class
is the
speci®cation
for an object . Using an architectural analogy,
a class is like a blueprint for a house, and the object is like the
house itself. Each house made from the blueprint can have var-
iations, and the blueprint is only the
speci®cation,
not a built
structure. For example, one house can be blue and another red;
one house might come with a
®replace
and another without .
Likewise with objects, the class
de®nes
the data types and
behaviors, but each object (house) made from a single class
(blueprint) has variables (color,
®replace)
that are set to
di‚er-
ent
values. To use a more technical term, each object is an
instance
of a class and each instance has its own set of
®elds
and methods.
Before you write a class, we recommend a little planning. Think
about what
®elds
and methods your class should have. Do a lit-
tle brainstorming to imagine all the possible options and then
prioritize and make your best guess about what will work. You†ll
make changes during the programming process, but it†s impor-
tant to have a good start .
The
®elds
inside a class can be any type of data. A class can
simultaneously hold many booleans,
¯oats,
images, strings, and
so on. Keep in mind that one reason to make a class is to group
together related data elements. For your methods, select clear
names and decide the return values (if any). The methods are
used to change the values of the
®elds
and to perform actions
based on the
®elds†
values.
For our
®rst
class, we†ll convert one of our earlier examples
(
Example 8-9 on page 106
). We start by making a list of the
®elds
from the example:
x
y
diameter
speed
131




The next step is to
®gure
out what methods might be useful for
the class. In looking at the
draw()
function from the example
we†re adapting, we see two primar y components. The position
of the shape is updated and drawn to the screen. Let†s create
two methods for our class, one for each task:
def


move()
def


display()
When we next write the class based on the lists of
®elds
and
methods, we†ll follow these steps:
1.Write the class
de®nition.
2. Write an
__init__
method (explained shortly) to initialize the
object and assign values to the
®elds.
3. Add the methods.
First , we write the class
de®nition:
class


JitterBug(
object
):
Notice that the keyword
class
is lowercase and the name
Jitter
Bug
is uppercase. Naming the class with an uppercase letter
isn†t required, but it is a convention (that we strongly encour-
age) used to denote that it†s a class. (The keyword
class
, how-
ever, must be lowercase because it†s a rule of the programming
language.)
Second, we add an
__init__
method (that†s two underscore
characters before
init
and two underscore characters after
it). Py thon automatically calls this method whenever an object
(an instance of the class) is created. The purpose of the
__init__
method is to assign the initial values to the object†s
®elds.
You can use the parameters passed to
__init__
to initial-
ize
®elds
in the object , or you can initialize
®elds
to a value that
doesn†t change from one object to the next . For the
JitterBug
class, we† ve decided that the values for
x
,
y
, and
diameter
will be
passed in, but the value for
speed
will be the same for ever y
object that belongs to the class.
The code inside the
__init__
method is run once when the
object is
®rst
created. As discussed earlier, we†re passing in
three parameters to this method when the object is initialized.




Each of the values passed in is assigned to a temporar y variable
that exists only while the code inside the
__init__
method is
run. To clarif y this, we† ve added the name
temp
to each of these
variables, but they can be named with any terms that you prefer.
In this example, these variables are used only to assign the val-
ues to the
®elds
that are a part of the class. Also note that the
__init__
method never returns a value and therefore doesn†t
have a
return
statement in it .
After adding the
__init__
method, the class looks like this:
class


JitterBug(
object
):


def


__init__(
self
,


tempX,


tempY,


tempDiameter):


self
.
x


=


tempX


self
.
y


=


tempY


self
.
diameter


=


tempDiameter


self
.
speed


=


0.5
The
®rst
parameter to any method in Py thon, including
the
__init__
method, is the word
self
. This is a special parame-
ter that Py thon automatically passes to methods. Its value is the
object that the method is being called on. The
self
parameter is
what allows you to set the value for a
®eld
(e. g., the expression
self.x = tempX
in the preceding example) or to use the value of
that
®eld
in an expression.
Figure 10-1
shows another example of a class
de®nition:
a
ﬁTrainﬂ class that has
®elds
for the train†s name and distance.
The illustration highlights how values
¯ow
from the main pro-
gram to the
®elds
of the newly created object via the
__init__
method.
133




Figure 10-1.
Passing values into the __init__ method to set the
values for an object†s
®elds
The last step in creating a class is to add the other methods.
This part is straightfor ward; it†s just like writing functions, but
here they are contained within the class. Also, note the code
spacing. Ever y line within the class is indented a few spaces to
show that it†s inside the block. Within the methods, the code is
spaced again to clearly show the hierarchy:




class


JitterBug(
object
):




def


__init__(
self
,


tempX,


tempY,


tempDiameter):








self
.
x


=


tempX








self
.
y


=


tempY








self
.
diameter


=


tempDiameter








self
.
speed


=


0.5


def


move(
self
):


self
.
x


+=


random
(
-
self
.
speed,


self
.
speed)


self
.
y


+=


random
(
-
self
.
speed,


self
.
speed)


def


display(
self
):


ellipse
(
self
.
x,


self
.
y,


self
.
diameter,


self
.
diameter)
Create Objects
Now that you have
de®ned
a class, to use it in a program you
must
de®ne
an object from that class. There are two steps to
create an object:
1.Create a variable to store the object .
2. Create (initialize) the object by ﬁcalling ﬂ the name of the
class as though it were a function.
Example 10-1: Make an Object
To make your
®rst
object , we†ll start by showing how this works
within a Processing sketch and then continue by explaining each
part in depth:
class


JitterBug(
object
):




def


__init__(
self
,


tempX,


tempY,


tempDiameter):








self
.
x


=


tempX








self
.
y


=


tempY








self
.
diameter


=


tempDiameter








self
.
speed


=


0.5
135






def


move(
self
):


self
.
x


+=


random
(
-
self
.
speed,


self
.
speed)


self
.
y


+=


random
(
-
self
.
speed,


self
.
speed)


def


display(
self
):


ellipse
(
self
.
x,


self
.
y,


self
.
diameter,


self
.
diameter)
bug


=


JitterBug(240,


60,


20)
def


setup
():


size
(480,


120)
def


draw
():


bug
.
move()


bug
.
display()
Once we† ve created a variable to store the object , the second
step is to initialize the object . The syntax for accomplishing this
in Py thon is to write the name of the class that you want to
instantiate, followed by a pair of parentheses with parameters
inside them. It looks just like you†re ﬁcalling ﬂ the name of the
class, as though it were a function:
bug


=


JitterBug(200.0,


250.0,


30)
The three numbers within the parentheses are the parameters
that are passed into the
__init__
method
de®ned
in the
Jitter
Bug
class. Because Py thon automatically inserts
self
as the
®rst
parameter to any method (including
__init__
), the number of
parameters inside the parentheses should be exactly one
fewe r
than the number
de®ned
in
__init__
.
Example 10-2: Make Multiple Objects
In
Example 10-1 on page 135
, we see something else new: the
period (dot) that†s used to access the object†s methods inside of
draw()
. The dot operator is used to join the name of the object
with its
®elds
and methods. This becomes clearer in this exam-
ple, where two objects are made from the same class. The
jit.move()
command refers to the
move()
method that belongs
to the object named
jit
, and
bug.move()
refers to the
move()
method that belongs to the object named
bug
:




# Put a copy of the Jitterbug class here
jit


=


JitterBug(160,


60,


50)
bug


=


JitterBug(320,


60,


10)
def


setup
():


size
(480,


120)
def


draw
():


jit
.
move()


jit
.
display()


bug
.
move()


bug
.
display()
Now that the class exists as its own module of code, any
changes will modif y the objects made from it . For instance, you
could add a
®eld
to the
JitterBug
class that controls the color,
or another that determines its size. These values can be passed
in using the
__init__
method or assigned using additional
methods, such as
setColor()
or
setSize()
. And because it†s a
self-contained unit , you can also use the
JitterBug
class in
another sketch.
Code in Tabs
Now is a good time to learn about the tab feature of the Pro-
cessing Development Environment (
Figure 10-2
). Tabs allow you
to spread your code across more than one
®le.
This makes
longer code easier to edit and more manageable in general. A
new tab is usually created for each class, which reinforces the
modularity of working with classes and makes the code easy to
®nd.
To create a new tab, click on the arrow at the righthand side of
the tab bar. When you select New Tab from the menu, you will
be prompted to name the tab within the message window. Using
137




this technique, modif y this example†s code to tr y to make a new
tab for the
JitterBug
class.
Figure 10-2.
Code can be split into
di…erent
tabs to make it eas-
ier to manage




Robot 8: Objects
A software object combines methods (functions) and
®elds
(variables) into one unit . The
Robot
class in this example
de®nes
all of the robot objects that will be created from it . Each
Robot
object has its own set of
®elds
to store a position and the illus-
tration that will draw to the screen. Each has methods to update
the position and display the illustration.
The parameters for
bot1
and
bot2


de®ne
the
x
and
y
coordinates
and the
.svg


®le
that will be used to depict the robot . The
tempX
and
tempY
parameters are passed into the
__init__
method and
assigned to the
xpos
and
ypos


®elds.
The
svgName
parameter is
stored in the
®eld


svgName
, and the
®le
named in the
®eld
is
loaded later in
setup()
by calling the
loadSvg()
method. The
objects (
bot1
and
bot2
) draw at their own location and with a dif-
ferent illustration because they each have unique values passed
into the objects through their
__init__
methods:
class


Robot(
object
):




def


__init__(
self
,


tempSvgName,


tempX,


tempY):








self
.
svgName


=


tempSvgName








self
.
xpos


=


tempX








self
.
ypos


=


tempY








self
.
angle


=


random
(0,


TWO_PI
)
139








self
.
yoffset


=


0




def


loadSvg(
self
):




self
.
botShape


=


loadShape
(
self
.
svgName)




def


update(
self
):








self
.
angle


+=


0.05








self
.
yoffset


=


sin
(
self
.
angle)


*


20




def


display(
self
):








shape
(
self
.
botShape,


self
.
xpos,


self
.
ypos


+


self
.
yoffset);
bot1


=


Robot(
"robot1.svg"
,


90,


80)
bot2


=


Robot(
"robot2.svg"
,


440,


30)
def


setup
():


size
(720,


480)




bot1
.
loadSvg()




bot2
.
loadSvg()
def


draw
():


background
(0,


153,


204)


# Update and display first robot


bot1
.
update()


bot1
.
display()


# Update and display second robot


bot2
.
update()


bot2
.
display()







## Exercícios

1. **Definindo Classes**:
   - Defina uma classe simples que representa uma forma geométrica.
   - Crie várias instâncias da classe e exiba-as na tela.

2. **Usando Métodos**:
   - Escreva métodos para sua classe para controlar seu comportamento, como mover ou mudar de cor.
   - Chame esses métodos em seu esboço para animar os objetos.

3. **Encapsulamento**:
   - Encapsule as propriedades de seus objetos tornando variáveis privadas e usando métodos getter e setter.
   - Certifique-se de que o estado interno dos objetos só possa ser modificado através de métodos.

4. **Herança**:
   - Crie uma subclasse que herda da sua classe principal e adiciona recursos adicionais.
   - Use polimorfismo para gerenciar diferentes tipos de objetos em uma única lista.
