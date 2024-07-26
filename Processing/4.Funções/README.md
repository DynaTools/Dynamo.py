
## Resumo

Este documento foca nas funções no Processing, explicando como definir e usar funções para organizar e reutilizar código. Ele cobre a sintaxe para criar funções, passar parâmetros e retornar valores.

9/Functions
Functions are the basic building blocks
for Processing programs. They have
appeared in every example we•ve presen-
ted. For instance, we•ve frequently used
the
size()
function, the
line()
function,
and the
fill()
function. This chapter
shows how to write new functions to
extend the capabilities of Processing
beyond its built-in features.
The power of functions is modularity. Functions are independ-
ent software units that are used to build more complex pro-
gramsŁlike LEGO bricks, where each type of brick ser ves a spe-
ci®c
purpose, and making a complex model requires using the
di‚erent
parts together. As with functions, the true power of
these bricks is the ability to build many
di‚erent
forms from the
same set of elements. The same group of LEGOs that makes a
spaceship can be reused to construct a truck, a skyscraper, and
many other objects.
Functions are helpful if you want to draw a more complex shape
like a tree over and over. The function to draw the tree shape
would be made up of Processing †s built-in commands, like
line()
, which create the form. After the code to draw the tree is
written, you don†t need to think about the details of tree drawing
againŁyou can simply write
tree()
(or whatever you named the
function) to draw the shape. Functions allow a complex
sequence of statements to be abstracted, so you can focus on
the higher-level goal (such as drawing a tree), and not the
details of the implementation (the
line()
commands that
117




de®ne
the tree shape). Once a function is
de®ned,
the code
inside the function need not be repeated again.
Function Basics
A computer runs a program one line at a time. When a function
is run, the computer jumps to where the function is
de®ned
and
runs the code there, then jumps back to where it left
o‚.
Example 9-1: Roll the Dice
This behavior is illustrated with the
rollDice()
function written
for this example. When a program starts, it runs the code in
setup()
and then stops. The program takes a detour and runs
the code inside
rollDice()
each time it appears:
def


setup
():




print


"Ready to roll!"




rollDice(20)




rollDice(20)




rollDice(6)




print


"Finished."
def


rollDice(numSides):




d


=


1


+


int
(
random
(numSides))




print


"Rolling..."
,


d
The two lines of code in
rollDice()
select a random number
between 1 and the number of sides on the dice, and prints that
number to the Console. Because the numbers are random,
you†ll see
di‚erent
numbers each time the program is run:
Ready to roll!
Rolling... 8
Rolling... 13
Rolling... 2
Finished.
Each time the
rollDice()
function is run inside
setup()
, the
code within the function runs from top to bottom, then the pro-
gram continues on the next line within
setup()
.
The
random()
function (described in
Example 8-7 on page 105
)
returns a number from 0 up to (but not including) the number
speci®ed.
So
random(6)
returns a number between 0 and




5.99999.... Because
random()
returns a
float
value, we also use
int()
to convert it to an integer. So
int(random(6))
will return 0,
1, 2, 3, 4, or 5. Then we add 1 so that the number returned is
between 1 and 6 (like a die). Like many other cases in this book,
counting from 0 makes it easier to use the results of
random()
with other calculations.
Example 9-2: Another Way to Roll
If an equivalent program were written without the
rollDice()
function, it might look like this:
def


setup
():


print


"Ready to roll!"


d1


=


1


+


int
(
random
(20))


print


"Rolling..."
,


d1


d2


=


1


+


int
(
random
(20))


print


"Rolling..."
,


d2


d3


=


1


+


int
(
random
(6))


print


"Rolling..."
,


d3


print


"Finished."
The
rollDice()
function in
Example 9-1 on page 118
makes the
code easier to read and maintain. The program is clearer
because the name of the function clearly states its purpose. In
this example, we see the
random()
function in
setup()
, but its
use is not as obvious. The number of sides on the die is also
clearer with a function: when the code says
rollDice(6)
, it†s
obvious that it†s simulating the roll of a six-sided die. Also,
Example 9-1  on page 118
is easier to maintain, because informa-
tion is not repeated. The phrase
Rolling...
is repeated three
times here. If you want to change that text to something else,
you would need to update the program in three places, rather
than making a single edit inside the
rollDice()
function. In addi-
tion, as you†ll see in
Example 9-5 on page 122
, a function can
also make a program much shorter (and therefore easier to
maintain and read), which helps reduce the potential number of
bugs.
119




Make a Function
In this section, we†ll draw an owl to explain the steps involved in
making a function.
Example 9-3: Draw the Owl
First , we†ll draw the owl without using a function:
def


setup
():


size
(480,


120)
def


draw
():


background
(176,


204,


226)


translate
(110,


110)


stroke
(138,


138,


125)


strokeWeight
(70)


line
(0,


-
35,


0,


-
65)


# Body


noStroke
()


fill
(255)


ellipse
(
-
17.5,


-
65,


35,


35)


# Left eye dome


ellipse
(17.5,


-
65,


35,


35)


# Right eye dome


arc
(0,


-
65,


70,


70,


0,


PI
)


# Chin


fill
(51,


51,


30)


ellipse
(
-
14,


-
65,


8,


8)


# Left eye


ellipse
(14,


-
65,


8,


8)


# Right eye


quad
(0,


-
58,


4,


-
51,


0,


-
44,


-
4,


-
51)


# Beak
Notice that
translate()
is used to move the origin (0,0) to 110
pixels over and 110 pixels down. Then the owl is drawn relative to
(0,0), with its coordinates sometimes positive and negative as
it†s centered around the new 0,0 point . See
Figure 9-1
.




Figure 9-1.
The owl†s coordinates
Example 9-4: Two†s Company
The code presented in
Example 9-3 on page 120
is reasonable if
there is only one owl, but when we draw a second, the length of
the code is nearly doubled:
def


setup
():


size
(480,


120)
def


draw
():


background
(176,


204,


226)


# Left owl


translate
(110,


110)


stroke
(138,


138,


125)




strokeWeight
(70)




line
(0,


-
35,


0,


-
65)




# Body




noStroke
()




fill
(255)
121








ellipse
(
-
17.5,


-
65,


35,


35)


# Left eye dome




ellipse
(17.5,


-
65,


35,


35)




# Right eye dome




arc
(0,


-
65,


70,


70,


0,


PI
)




# Chin




fill
(51,


51,


30)




ellipse
(
-
14,


-
65,


8,


8)










# Left eye




ellipse
(14,


-
65,


8,


8)












# Right eye




quad
(0,


-
58,


4,


-
51,


0,


-
44,


-
4,


-
51)




# Beak


# Right owl


translate
(70,


0);


stroke
(138,


138,


125)




strokeWeight
(70)




line
(0,


-
35,


0,


-
65)




# Body




noStroke
()




fill
(255)




ellipse
(
-
17.5,


-
65,


35,


35)


# Left eye dome




ellipse
(17.5,


-
65,


35,


35)




# Right eye dome




arc
(0,


-
65,


70,


70,


0,


PI
)




# Chin




fill
(51,


51,


30)




ellipse
(
-
14,


-
65,


8,


8)










# Left eye




ellipse
(14,


-
65,


8,


8)












# Right eye




quad
(0,


-
58,


4,


-
51,


0,


-
44,


-
4,


-
51)




# Beak
The program grew from 21 lines to 34: the code to draw the
®rst
owl was cut and pasted into the program and a
translate()
was
inserted to move it to the right 70 pixels. This is a tedious and
ineŸcient
way to draw a second owl, not to mention the head-
ache of adding a third owl with this method. But duplicating the
code is unnecessar y, because this is the type of situation where
a function can come to the rescue.
Example 9-5: An Owl Function
In this example, a function is introduced to draw two owls with
the same code. If we make the code that draws the owl to the
screen into a new function, the code need only appear once in
the program:




def


setup
():


size
(480,


120)
def


draw
():


background
(176,


204,


226)


owl(110,


110)


owl(180,


110)
def


owl(x,


y):


pushMatrix
()


translate
(x,


y)


stroke
(138,


138,


125)


strokeWeight
(70)


line
(0,


-
35,


0,


-
65)


# Body


noStroke
()


fill
(255)


ellipse
(
-
17.5,


-
65,


35,


35)


# Left eye dome


ellipse
(17.5,


-
65,


35,


35)


# Right eye dome


arc
(0,


-
65,


70,


70,


0,


PI
)


# Chin


fill
(51,


51,


30)


ellipse
(
-
14,


-
65,


8,


8)


# Left eye


ellipse
(14,


-
65,


8,


8)


# Right eye


quad
(0,


-
58,


4,


-
51,


0,


-
44,


-
4,


-
51)


# Beak


popMatrix
()
You can see from the illustrations that this example and
Exam-
ple 9-4 on page 121
have the same result , but this example is
shorter, because the code to draw the owl appears only once,
inside the aptly named
owl()
function. This code runs twice,
because it†s called twice inside
draw()
. The owl is drawn in two
di‚erent
locations because of the parameters passed into the
function that set the
x
and
y
coordinates.
Parameters are an important part of functions, because they
provide
¯exibility.
We saw another example in the
rollDice()
function; the single parameter named
numSides
made it possible
to simulate a 6-sided die, a 20-sided die, or a die with any num-
ber of sides. This is just like many other Processing functions.
For instance, the parameters to the
line()
function make it pos-
sible to draw a line from any pixel on screen to any other pixel.
Without the parameters, the function would be able to draw a
line only from one
®xed
point to another.
Each parameter is a variable that gets created each time the
function runs. When this example is run, the
®rst
time the owl
123




function is called, the value of the
x
parameter is 110, and
y
is
also 110. In the second use of the function, the value of
x
is 180
and
y
is again 110. Each value is passed into the function and
then wherever the variable name appears within the function,
it†s replaced with the incoming value.
Example 9-6: Increasing the Surplus
Population
Now that we have a basic function to draw the owl at any loca-
tion, we can draw many owls
eŸciently
by placing the function
within a
for
loop and changing the
®rst
parameter each time
through the loop:
def


setup
():


size
(480,


120)
def


draw
():


background
(176,


204,


226)


for


x


in


range
(35,


width


+


70,


70):


owl(x,


110)
# Insert owl() function from Example 9-5
It†s possible to keep adding more and more parameters to the
function to change
di‚erent
aspects of how the owl is drawn.
Values could be passed in to change the owl†s color, rotation,
scale, or the diameter of its eyes.
Example 9-7: Owls of Different Sizes
In this example, we† ve added two parameters to change the gray
value and size of each owl:




def


setup
():


size
(480,


120)
def


draw
():


background
(176,


204,


226)


randomSeed
(0)


for


i


in


range
(35,


width


+


40,


40):


gray


=


int
(
random
(0,


102))


scalar


=


random
(0.25,


1.0)


owl(i,


110,


gray,


scalar)
def


owl(x,


y,


g,


s):


pushMatrix
()


translate
(x,


y)


scale
(s)


# Set the scale


stroke
(138
-
g,


138
-
g,


125
-
g)


# Set the gray value


strokeWeight
(70)


line
(0,


-
35,


0,


-
65)


# Body


noStroke
()


fill
(255)


ellipse
(
-
17.5,


-
65,


35,


35)


# Left eye dome


ellipse
(17.5,


-
65,


35,


35)


# Right eye dome


arc
(0,


-
65,


70,


70,


0,


PI
)


# Chin


fill
(51,


51,


30)


ellipse
(
-
14,


-
65,


8,


8)


# Left eye


ellipse
(14,


-
65,


8,


8)


# Right eye


quad
(0,


-
58,


4,


-
51,


0,


-
44,


-
4,


-
51)


# Beak


popMatrix
()
Return Values
Functions can make a calculation and then return a value to the
main program. We† ve already used functions of this type, includ-
ing
random()
and
sin()
. Notice that when this type of function
appears, the return value is usually assigned to a variable:
r


=


random
(1,


10)
125




In this case,
random()
returns a value between 1 and 10, which is
then assigned to the
r
variable.
A function that returns a value is also frequently used as a
parameter to another function. For instance:
point
(
random
(
width
),


random
(
height
));
In this case, the values from
random()
aren†t assigned to a vari-
ableŁthey are passed as parameters to
point()
and used to
position the point within the window.
Example 9-8: Return a Value
To make a function that returns a value, specif y the data to be
passed back with the keyword
return
. For instance, this exam-
ple includes a function called
calculateMars()
that calculates
the weight of a person or object on our neighboring planet:
def


setup
():


yourWeight


=


132.0


marsWeight


=


calculateMars(yourWeight)


print


marsWeight
def


calculateMars(w):


newWeight


=


w


*


0.38


return


newWeight
Notice the last line of the block, which returns the variable
new
Weight
. In the second line of
setup()
, that value is assigned to
the variable
marsWeight
. (To see your own weight on Mars,
change the value of the
yourWeight
variable to your weight .)




Robot 7: Functions
In contrast to Robot 2 (see
ﬁRobot 2: Variablesﬂ on page 45
),
this example uses a function to draw four robot variations within
the same program. Because the
drawRobot()
function appears
four times within
draw()
, the code within the
drawRobot()
block
is run four times, each time with a
di‚erent
set of parameters to
change the position and height of the robot†s body.
Notice how what were global variables in Robot 2 have now been
isolated within the
drawRobot()
function. Because these vari-
ables apply only to drawing the robot , they belong inside the
drawRobot()
function block. Because the value of the
radius
variable doesn†t change, it need not be a parameter. Instead, it
is
de®ned
at the beginning of
drawRobot()
:
def


setup
():


size
(720,


480)


strokeWeight
(2)


ellipseMode
(
RADIUS
)
def


draw
():


background
(0,


153,


204)


drawRobot(120,


420,


110,


140)


drawRobot(270,


460,


260,


95)
127






drawRobot(420,


310,


80,


10)


drawRobot(570,


390,


180,


40)
def


drawRobot(x,


y,


bodyHeight,


neckHeight):


radius


=


45


ny


=


y


-


bodyHeight


-


neckHeight


-


radius


# Neck


stroke
(102)


line
(x
+
2,


y
-
bodyHeight,


x
+
2,


ny)


line
(x
+
12,


y
-
bodyHeight,


x
+
12,


ny)


line
(x
+
22,


y
-
bodyHeight,


x
+
22,


ny)


# Antennae


line
(x
+
12,


ny,


x
-
18,


ny
-
43)


line
(x
+
12,


ny,


x
+
42,


ny
-
99)


line
(x
+
12,


ny,


x
+
78,


ny
+
15)


# Body


noStroke
()


fill
(255,


204,


0)


ellipse
(x,


y
-
33,


33,


33)


fill
(0)


rect
(x
-
45,


y
-
bodyHeight,


90,


bodyHeight
-
33)


fill
(255,


204,


0)


rect
(x
-
45,


y
-
bodyHeight
+
17,


90,


6)


# Head


fill
(0)


ellipse
(x
+
12,


ny,


radius,


radius)


fill
(255)


ellipse
(x
+
24,


ny
-
6,


14,


14)


fill
(0)


ellipse
(x
+
24,


ny
-
6,


3,


3)


fill
(153)


ellipse
(x,


ny
-
8,


5,


5)


ellipse
(x
+
30,


ny
-
26,


4,


4)


ellipse
(x
+
41,


ny
+
6,


3,


3)







## Exercícios

1. **Definindo Funções**:
   - Escreva uma função que desenha uma forma específica e a chame em seu esboço.
   - Experimente mudar os parâmetros da função para desenhar diferentes variações da forma.

2. **Usando Parâmetros**:
   - Crie uma função que aceita parâmetros para controlar a posição e tamanho de uma forma.
   - Chame a função várias vezes com diferentes argumentos para criar um padrão.

3. **Retornando Valores**:
   - Escreva uma função que realiza um cálculo e retorna o resultado.
   - Use o valor retornado em seu esboço para controlar um aspecto do desenho.

4. **Organizando Código**:
   - Refatore um esboço existente, dividindo-o em várias funções.
   - Certifique-se de que cada função tenha um propósito claro e seja usada para simplificar o laço principal `draw()`.
