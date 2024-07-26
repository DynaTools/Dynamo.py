
## Resumo

Este documento introduz listas no Processing, uma estrutura de dados que permite armazenar e manipular coleções de valores. Ele explica como criar, acessar e modificar listas, e fornece exemplos de uso de listas para gerenciar múltiplos elementos em um esboço.

11/Lists
A
list
is a group of variables that share a
common name. Lists are useful because
they make it possible to work with more
variables without creating a new name
for each one. This makes the code
shorter, easier to read, and more conve-
nient to update.
From Variables to Lists
When a program needs to keep track of one or two things, it†s
not necessar y to use a list . In fact , adding a list might make the
program more complicated than necessar y. However, when a
program has many elements (for example, a
®eld
of stars in a
space game or multiple data points in a visualization), lists
make the code easier to write.
Example 11-1: Many Variables
To see what we mean, refer to
Example 8-3 on page 101
. This
code works
®ne
if we†re moving around only one shape, but
what if we want to have two? We need to make a new
x
variable
and update it within
draw()
:
141




x1


=


-
20.0
x2


=


20.0
def


setup
():


size
(240,


120)


noStroke
()
def


draw
():




global


x1,


x2


background
(0)


x1


+=


0.5


x2


+=


0.5


arc
(x1,


30,


40,


40,


0.52,


5.76)


arc
(x2,


90,


40,


40,


0.52,


5.76)
Example 11-2: Too Many Variables
The code for the previous example is still manageable, but what
if we want to have
®ve
circles? We need to add three more vari-
ables to the two we already have:
x1


=


-
10.0
x2


=


10.0
x3


=


35.0
x4


=


18.0
x5


=


30.0
def


setup
():


size
(240,


120)


noStroke
()
def


draw
():




global


x1,


x2,


x3,


x4,


x5


background
(0)


x1


+=


0.5


x2


+=


0.5


x3


+=


0.5


x4


+=


0.5






x5


+=


0.5


arc
(x1,


20,


20,


20,


0.52,


5.76)


arc
(x2,


40,


20,


20,


0.52,


5.76)


arc
(x3,


60,


20,


20,


0.52,


5.76)


arc
(x4,


80,


20,


20,


0.52,


5.76)


arc
(x5,


100,


20,


20,


0.52,


5.76)
This code is starting to get out of control.
Example 11-3: Lists, Not Variables
Imagine what would happen if you wanted to have 3,000 circles.
This would mean creating 3,000 individual variables, then
updating each one separately. Could you keep track of that
many variables? Would you want to? Instead, we use a list:
x


=


[]
def


setup
():


size
(240,


120)


noStroke
()


fill
(255,


200)


for


i


in


range
(3000):


x
.
append
(
random
(
-
1000,


200))
def


draw
():


background
(0)


for


i


in


range
(
len
(x)):


x[i]


+=


0.5


y


=


i


*


0.4


arc
(x[i],


y,


12,


12,


0.52,


5.76)
We†ll spend the rest of this chapter talking about the details that
make this example possible.
143




List Operations
Each item in a list is called an
element
, and each has an
index
value to mark its position within the list . Just like coordinates on
the screen, index values for a list start counting from 0. For
instance, the
®rst
element in the list has the index value 0, the
second element in the list has the index value 1, and so on. If
there are 20 values in the list , the index value of the last element
is 19.
Figure 11-1
shows the conceptual structure of a list .
Figure 11-1.
A list is a group of one or more variables that share
the same name
A list value in Py thon looks like a pair of square brackets. This
statement assigns a list to the variable
x
:
x


=


[]
You can also initialize the items in the list by putting comma-
separated values inside the square brackets:
x


=


[5,


10,


15,


20]
Lists in Py thon can contain values of var ying data types. This list
has an integer, a
¯oating-point
number, and a string:
stuff


=


[89,


1.24,


"hello"
]
You can also use the built-in Py thon function
list()
to create a
list value:
x


=


list
()


# creates an empty list
x


=


list
(5,


10,


15,


20)


# creates a list with four initial


# elements
Py thon list values are objects, and support a number of useful
methods. The list method we†ll use most is
append()
, which
adds an item to a list:




x


=


[]


# x is empty
x
.
append
(5)


# now x has one item, the integer value 5
Once there are items in your list , you can access the item at a
particular index using square bracket syntax. Write the name of
the variable that contains your list , followed by a pair of square
brackets with a number between them, like so:
x


=


[5,


10,


15,


20]
print


x[0]


# prints 5
print


x[1]


# prints 10
print


x[2]


# prints 15
print


x[3]


# prints 20
List indices in Py thon are
zero-based
, meaning that the number
you use in square brackets to access the
®rst
element of the list
is 0 (not 1). Likewise, to get the second element , use 1; to get the
third element , use 2; and so forth.
After the list has been created, you can
over write
the value of an
item at a particular index in a list by writing an expression with
the square bracket syntax, followed by an equal sign (
=
) and the
new value for that item:
x


=


[5,


10,


15,


20]
print


x[2]


# prints 15
x[2]


=


789
print


x[2]


# prints 789
To determine the length of a list , use Py thon†s built-
in
len()
function:
x


=


[5,


10,


15,


20]
print


len
(x)


# prints 4
y


=


[]
print


len
(y)


# prints 0
Now that we† ve looked at some of the basic syntax for working
with lists, let†s slow down and talk about common ways to use
lists in our programs. There are a number of steps to working
with a list:
1.Create a list value with square brackets or the
list()
func-
tion.
2.Assign that list value to a variable.
145




3. Optionally, use the list†s
append()
method of the list to add
new items to the list .
Each of the three following examples shows a
di‚erent
techni-
que to create a list called
x
that stores two integers, 12 and 2.
Pay close attention to what happens before
setup()
and what
happens within
setup()
.
Example 11-4: Declare and Append to
a List
First , we†ll declare an empty list outside of
setup()
and then
append values to the list .
x


=


[]


# Create the list
def


setup
():


size
(200,


200)


x
.
append
(12)


# Append the first value


x
.
append
(2)


# Append the second value
Example 11-5: Compact List
Initialization
Here†s a slightly more compact example, in which the list is ini-
tialized with its items when the value is
®rst
created:
x


=


[12,


2]


# Create a new list with two items, assigned to x
def


setup
():


size
(200,


200)


# No further action needed in setup()!
Avoid creating lists within draw(), because creating a
new list on ever y frame will slow down your frame
rate.
Example 11-6: Revisiting the First
Example
As a complete example of how to use lists, here we† ve recoded
Example 11-1
. Although we don†t yet see the full
bene®ts




revealed in
Example 11-3
, we do see some important details of
how lists work:
x


=


[
-
20.0,


20.0]
def


setup
():


size
(240,


120)


noStroke
()
def


draw
():


background
(0)


x[0]


+=


0.5


# Increase the first element


x[1]


+=


0.5


# Increase the second element


arc
(x[0],


30,


40,


40,


0.52,


5.76)


arc
(x[1],


90,


40,


40,


0.52,


5.76)
Note that the
global
keyword is not needed in the
draw()
func-
tion here. See
Appendix D
for more information.
Repetition and Lists
The
for
loop, introduced in
ﬁRepetitionﬂ on page 39
, makes it
easier to work with large lists while keeping the code concise.
The way we use
for
loops to operate on lists is
di‚erent
depend-
ing on exactly what we want to do with the list .
Example 11-7: Filling a List in a for
Loop
A
for
loop can be used to
®ll
a list with values or to read the val-
ues back out . In this example, the list is
®rst


®lled
with random
numbers inside
setup()
, and then these numbers are used to
set the stroke value inside
draw()
. Each time the program is run,
a new set of random numbers is put into the list:
147




gray


=


[]
def


setup
():


size
(240,


120)


for


i


in


range
(
width
):


gray
.
append
(
random
(0,


255))
def


draw
():


for


i


in


range
(
len
(gray)):


stroke
(gray[i])


line
(i,


0,


i,


height
)
Example 11-9: Track Mouse
Movements
In this example, there are two lists to store the position of the
mouseŁone for the
x
coordinate and one for the
y
coordinate.
These lists store the location of the mouse for ever y frame. With
each new frame, the newest coordinate is inserted at the begin-
ning of the list . This example visualizes this action. Also, at each
frame, all coordinates are used to draw a series of ellipses to the
screen:
x


=


[]
y


=


[]
def


setup
():




size
(240,


120)




noStroke
()
def


draw
():




background
(0)




x
.
insert(0,


mouseX
)




y
.
insert(0,


mouseY
)




for


i


in


range
(
len
(x)):








fill
(i


*


4)








ellipse
(x[i],


y[i],


40,


40)




This example demonstrates another method of the list
object ,
insert()
, which takes two parameters: the
®rst
is an
index in the list , and the second is the value to insert into the list
at that index. The code
x.insert(0, mouseX)
inserts the value in
the variable
mouseX
at index 0 of the list (i.e., the beginning of the
list).
The technique for storing coordinates in a list is inef-
ficient . Because there†s no built-in limit to the num-
ber of coordinates the list will store, the list in this
program can quickly grow ver y large in memor y,
causing your sketch to slow down or even crash. For
a more
eŸcient
technique that only stores the
last
n
numbers, see the Examples


Basics


Input


StoringInput example included with Py thon
Mode.
Lists of Objects
The two short examples in this section bring together ever y
major programming concept in this book: variables, iteration,
conditionals, functions, objects, and lists. Making a list of
objects is nearly the same as making the lists we introduced on
the previous pages, but there†s one additional consideration:
because each list element is an object , it must
®rst
be instanti-
ated before it can be appended to the list . (For a built-in Pro-
cessing class such as
PImage
, you need to use the
loadImage()
function to create the object before it†s assigned.)
Example 11-10: Managing Many
Objects
This example creates a list of 33
JitterBug
objects and then
updates and displays each one inside
draw()
. For this example
to work, you need to add the
JitterBug
class (see
Chapter 10
) to
the code:
149




# Copy JitterBug class here
bugs


=


[]
def


setup
():


size
(240,


120)


for


i


in


range
(33):


x


=


random
(
width
)


y


=


random
(
height
)


r


=


i


+


2


bugs
.
append
(JitterBug(x,


y,


r))
def


draw
():


for


i


in


range
(
len
(bugs)):


bugs[i]
.
move()


bugs[i]
.
display()
Example 11-11: A New Way to
Manage Objects
Because iterating over ever y item in a list is a ver y common task
when writing computer programs, Py thon has a shorthand syn-
tax for making it easier. Instead of creating a new counter vari-
able, such as the
i
variable in
Example 11-10 on page 149
, and
iterating over the result of the
range()
function, it†s possible to
iterate over the elements of a list directly. In the following exam-
ple, each object in the
bugs
list of
JitterBug
objects is assigned
to
b
in order to run the
move()
and
display()
methods for all
objects in the list .
This form of the
for
loop is often tidier than looping with a num-
ber, although in this example, we didn†t use it inside
setup()
because
i
was needed inside the loop (to set the size of the
JitterBug
object). This demonstrates how it†s sometimes help-
ful to have the number around:




# Copy JitterBug class here
bugs


=


[]
def


setup
():


size
(240,


120)


for


i


in


range
(33):


x


=


random
(
width
)


y


=


random
(
height
)


r


=


i


+


2


bugs
.
append
(JitterBug(x,


y,


r))
def


draw
():


for


b


in


bugs:


b
.
move()


b
.
display()
The
®nal
list example loads a sequence of images and stores
each as an element within a list of
PImage
objects.
Example 11-12: Sequences of Images
To run this example, get the images from the
media.zip


®le
as
described in
Chapter 7
. The images are named sequentially
(
frame-0000.png
,
frame-0001.png
, etc.), which makes it possi-
ble to create the name of each
®le
within a
for
loop, as seen in
the eighth line of the program:
numFrames


=


12


# The number of frames
images


=


[]


# Make the list
currentFrame


=


0
def


setup
():


size
(240,


120)


for


i


in


range
(numFrames):


imageName


=


"frame-"


+


nf
(i,


4)


+


".png"


images
.
append
(
loadImage
(imageName))


frameRate
(24)
151




def


draw
():




global


currentFrame


image
(images[currentFrame],


0,


0)


currentFrame


+=


1


# Next frame


if


currentFrame


>=


len
(images):


currentFrame


=


0


# Return to first frame
The
nf()
function formats numbers so that
nf(1, 4)
returns the
string ﬁ0001ﬂ and
nf(11, 4)
returns ﬁ0011ﬂ. These values are
concatenated with the beginning of the
®lename
(ﬁframe-ﬂ) and
the end (ﬁ.png ﬂ) to create the complete
®lename
as a string.
The
®les
are appended to the list on the following line. The
images are displayed to the screen one at a time in
draw()
.
When the last image in the list is displayed, the program returns
to the beginning of the list and shows the images again in
sequence.
Robot 9: Lists
Lists make it easier for a program to work with many elements.
In this example, a list intended to contain
Robot
objects is cre-
ated at the top. The list is then
®lled
with
Robot
objects inside
setup()
. In
draw()
, another
for
loop is used to update and dis-
play each element of the
bots
list .




The
for
loop and a list make a powerful combination. Notice the
subtle
di‚erences
between the code for this example and Robot
8 (see
ﬁRobot 8: Objectsﬂ on page 139
) in contrast to the
extreme changes in the visual result . Once a list is created and a
for
loop is put in place, it†s as easy to work with three elements
as it is 3,000.
The decision to load the SVG
®le
within
setup()
rather than in
the
Robot
class is the major change from Robot 8. This choice
was made so the
®le
is loaded only once, rather than as many
times as there are elements in the list (in this case, 20 times).
This change makes the code start faster because loading a
®le
takes time, and it uses less memor y because the
®le
is stored
once. Each element of the
bot
list references the same
®le:


class


Robot(
object
):










# Set initial values




def


__init__(
self
,


shape,


tempX,


tempY):








self
.
botShape


=


shape








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








self
.
yoffset


=


0.0




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
yoffset)
bots


=


[]




# Create list for Robot objects
botCount


=


20
def


setup
():




size
(720,


480)




robotShape


=


loadShape
(
"robot1.svg"
)




# Create each object




for


i


in


range
(botCount):








# Create a random x coordinate








x


=


random
(
-
40,


width
-
40)








# Assign the y coordinate based on the order








y


=


map
(i,


0,


botCount,


-
100,


height
-
200)
153












bots
.
append
(Robot(robotShape,


x,


y))
def


draw
():




background
(0,


153,


204)




for


b


in


bots:








b
.
update()








b
.
display()







## Exercícios

1. **Criando Listas**:
   - Crie uma lista de números e imprima seus elementos.
   - Experimente com diferentes tipos de dados, como strings ou objetos.

2. **Acessando Elementos**:
   - Escreva um programa que itera através de uma lista e realiza uma operação em cada elemento.
   - Use uma lista para armazenar as posições de várias formas e desenhá-las na tela.

3. **Modificando Listas**:
   - Desenvolva um esboço que adiciona ou remove elementos de uma lista com base na entrada do usuário.
   - Implemente uma lista dinâmica que cresce ou encolhe durante a execução do esboço.

4. **Operações Avançadas com Listas**:
   - Crie um programa que classifica ou filtra uma lista com base em critérios específicos.
   - Use listas aninhadas para gerenciar estruturas de dados mais complexas.
