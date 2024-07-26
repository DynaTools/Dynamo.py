
## Resumo

Este documento discute a gestão de dados no Processing, focando em arrays e dicionários. Ele explica como usar essas estruturas de dados para organizar e acessar dados de forma eficiente.

12/Data and
Dictionaries
Data visualization is one of the most
active areas at the intersection of code
and graphics and is also one of the most
popular uses of Processing. This chapter
builds on what has been discussed about
storing and loading data earlier in the
book and introduces more features rele-
vant to data sets that might be used for
visualization.
There is a wide range of software that can output standard visu-
alizations like bar charts and scatter plots. However, writing
code to create visualization from scratch provides more control
over the output and encourages users to imagine, explore, and
create more unique representations of data. For us, this is the
point of learning to code and using software like Processing, and
we
®nd
it far more interesting than being limited by prepack-
aged methods or tools that are available.
Data Summary
It†s a good time to rewind and discuss how data was introduced
throughout this book. Recall that ever y value in a Py thon pro-
gram has a
data type
. Each kind of data is unique and is stored
in a
di‚erent
way. We started the book talking about simple data
types like
int
(for integers) or
¯oat
(for numbers with decimals).
L ater, we discussed
compound data types
like objects and lists.
A compound data type keeps track of multiple values. The val-
155




ues in a list are accessed by their numerical index, whereas the
values in an object are accessed by name as data attributes.
The examples in this chapter introduce a new compound data
type: the
dictionar y
. Dictionaries are data structures that are
conceptually similar to lists, except instead of accessing values
by numerical index, you access them by name. This makes dic-
tionaries a data type especially suited for storing, transmitting,
and processing structured data. There are several built-in
Py thon tools that read data in various formats (e. g., from
the
data
folder for a sketch) and return dictionaries. We†ll load
data into dictionaries from two
di‚erent
sources: tables of data
in comma-separated values (CSV) format , and data in JSON for-
mat .
Dictionaries
You can think of a dictionar y as being sort of like a list , except
you index its values not with a number but with a
key
. Dictionar y
keys are usually strings that identif y the values they point to in
an easy-to-remember way. Let†s say, for example, that we
wanted to include in our sketch some information about the
planets of our solar system. Here†s what a dictionar y with infor-
mation about Earth might look like in Py thon:
planetInfo


=


{




"name"
:


"Earth"
,




"knownMoons"
:


1,




"eqRadiusKm"
:


6387.1,




"hasRings"
:


False
}


In this example, we† ve created a dictionar y and assigned it to a
variable called
planetInfo
. The
keys
in this dictionar y are
name
,
knownMoons
,
eqRadiusKm
, and
hasRings
. The values for those keys
are
Earth
,
1
,
6387.1
, and
False
, respectively. As this example
shows, dictionar y values can be any data type: strings, integers,
¯oating-point
numbers, booleansŁeven objects, lists, and other
dictionaries can be stored as dictionar y values.
Once you† ve
de®ned
a dictionar y, you can get the value for a
particular key using square bracket notation. This looks similar
to how you get the value for a particular index in a list , except




this time we†re putting a string between the square brackets
instead of a number:
planetInfo


=


{




"name"
:


"Earth"
,




"knownMoons"
:


1,




"eqRadiusKm"
:


6387.1,




"hasRings"
:


False
}


print


planetInfo[
†name†
]


# prints "Earth"
print


planetInfo[
†knownMoons†
]


# prints 1
If you attempt to get the value for a key that is not present in the
dictionar y, Py thon will raise a
KeyError
, and your program will
halt:
print


planetInfo[
†extraterrestrialCount†
]


# raises KeyError
You can check to see whether or not a key is present in a dictio-
nar y by using the special operator
in
. Put the key you want to
check for on the lefthand side of
in
, and the dictionar y you want
to check on the righthand side. The entire expression will
return
True
or
False
, so you can use it in an
if
statement:
print


†extraterrestrialCount†


in


planetInfo


# prints False
if


†eqRadiusKm†


in


planetInfo:




print


"Planetary radius (km): "
,


planetInfo[
†eqRadiusKm†
]
else
:




print


"No radius information available."
The name
dictionar y
is meant to evoke a physical dictionar y, in
which you look up words (
keys
) to
®nd
their
de®nitions
(
values
).
In other computer languages (such as Java and C++), the analo-
gous data structure is called a
map
. Sometimes when talking
about dictionaries, we†ll say that keys ﬁmapﬂ to values. (For
instance, in the preceding example, the key
name
maps to the
value
Earth
.)
Example 12-1: (Keyboard) Keys as
(Dictionary) Keys
The following sketch shows how dictionaries can be used to
store information and retrieve it in response to user input:
157




sizes


=


{




†a†
:


40,




†b†
:


80,




†c†
:


120,




†d†
:


160
}
def


setup
():




size
(200,


200)




rectMode
(
CENTER
)
def


draw
():




background
(0)




fill
(255)




if


keyPressed
:








if


key


in


sizes:












rect
(100,


100,


sizes[
key
],


sizes[
key
])
This sketch displays rectangles of various sizes to the screen in
response to user input . A dictionar y called
sizes
maps particu-
lar keystrokes to integer values. Inside of
draw()
, we check to
see if a keyboard key has been pressed and whether the string
value of that keyboard key is present in the
sizes
dictionar y. If
so, we display a rectangle with its size determined by the value
stored for that key.
Lists of Dictionaries
Let†s return to our dictionar y with information about a particular
planet . It looks like this:
planetInfo


=


{




"name"
:


"Earth"
,




"knownMoons"
:


1,




"eqRadiusKm"
:


6387.1,




"hasRings"
:


False
}


Now, let†s imagine that we want our program to contain infor-
mation not just about Earth, but all of the terrestrial planets




(Mercur y, Venus, Earth, and Mars). We could do this by creating
several dictionaries, one for each planet:
mercuryInfo


=


{




"name"
:


"Mercury"
,




"knownMoons"
:


0,




"eqRadiusKm"
:


2439.64,
}
venusInfo


=


{




"name"
:


"Venus"
,




"knownMoons"
:


0,




"eqRadiusKm"
:


6051.59,
}
earthInfo


=


{




"name"
:


"Earth"
,




"knownMoons"
:


1,




"eqRadiusKm"
:


6387.1,
}
marsInfo


=


{




"name"
:


"Mars"
,




"knownMoons"
:


2,




"eqRadiusKm"
:


3397.0
}
So far, so good. Let†s set ourselves to another task: how would
you calculate the
average equatorial radius
for all planets in this
data? Here†s the most obvious way to do it:
planetCount


=


4
radiusSum


=


mercuryInfo[
†eqRadiusKm†
]
radiusSum


+=


venusInfo[
†eqRadiusKm†
]
radiusSum


+=


earthInfo[
†eqRadiusKm†
]
radiusSum


+=


marsInfo[
†eqRadiusKm†
]
print


radiusSum


/


planetCount


# prints 4568.8325
But this solution has some problems, the foremost being the
repetition. If we add more planet data, we would have to man-
ually add each new planet to our statements that calculate the
sum of their radii. This could get tedious ver y quickly.
Thankfully, in just the same way that Py thon allows us to make
lists of integers or
¯oating-point
numbers, we can create
lists of
dictionaries
:
planetList


=


[mercuryInfo,


venusInfo,


earthInfo,


marsInfo]
159




This statement creates a list called
planetList
. Each element
of
planetList
is a dictionar y. We can access any value for a par-
ticular key for one of the dictionaries in this list like so:
print


planetList[2][
†name†
]


# prints †Earth†
print


planetList[3][
†knownMoons†
]


# prints 2
That†s a lot of square brackets! Here†s how to understand what
an expression like
planetList[2][†name†]
means. First , we
know that we can put square brackets with a number
inside (e. g.,
[2]
) right after any expression that evaluates to a
list . That expression will evaluate to the value stored at that
index of the list , which in this case is a dictionar y. We also know
that we can put square brackets with a string inside (e. g.,
[†name†]
) right after any expression that evaluates to a dictio-
nar y. That expression will, in turn, evaluate to the value stored in
the dictionar y for that key. Keeping both of these ways to form
expressions in mind, you can read the expression
planetList[2]
[†name†]
from left to right like so:
™
planetList
is a list
™
planetList[2]
is the element at index 2 of
planetList
,
which is a dictionar y
™
planetList[2][†name†]
is the value for key
name
in that dic-
tionar y (
Earth
)
We can loop over a list of dictionaries the same way we loop over
a regular list , with a
for
loop:
radiusSum


=


0
for


i


in


range
(
len
(planetList)):




radiusSum


+=


planetList[i][
†eqRadiusKm†
]
print


radiusSum


/


len
(planetList)


# prints 4568.8325
Alternatively, we can use the
for...in
looping syntax intro-
duced in
Example 11-11 on page 150
. The ﬁtemporar y loop vari-
ableﬂ in this case will be a dictionar y. With that in mind, here†s
some revised code to calculate the average radius of all four ter-
restrial planets:
radiusSum


=


0
for


p


in


planetList:




radiusSum


+=


p[
†eqRadiusKm†
]
print


radiusSum


/


len
(planetList)


# prints 4568.8325




Example 12-2: The Planets
This example takes a
simpli®ed
version of our list of planet infor-
mation dictionaries and uses it as a data source for drawing to
the screen:
planetList


=


[




{
"name"
:


"Mercury"
,


"eqRadiusKm"
:


2439.64},




{
"name"
:


"Venus"
,


"eqRadiusKm"
:


6051.59},




{
"name"
:


"Earth"
,


"eqRadiusKm"
:


6387.1},




{
"name"
:


"Mars"
,


"eqRadiusKm"
:


3397.0}
]
def


setup
():




size
(600,


150)




textAlign
(
LEFT
,


CENTER
)
def


draw
():




background
(0)




fill
(255)




planetCount


=


len
(planetList)




for


i


in


range
(planetCount):








# scale radius to be screen-friendly








planetRadius


=


planetList[i][
†eqRadiusKm†
]


*


0.01








offset


=


50


+


((
width
/
planetCount)


*


i)








ellipse
(offset,


height
/
2,


planetRadius,


planetRadius)








text
(planetList[i][
†name†
],


10
+
offset
+
(planetRadius
/
2),












height
/
2)
The sketch begins with a
simpli®ed
version of our
planet
List
variable. Here, instead of creating a variable for each dictio-
nar y
®rst
and then putting the variable names into the list decla-
ration, we simply write the dictionaries straight into the list . In
the
draw()
function, we loop over the list of planets and use each
planet†s radius and name to draw it to the screen (using the
planet†s position in the list to determine where on the screen to
draw it).
161




CSV Files
Many data sets are stored in spreadsheets. You may have
worked with a program like Microsoft Excel or Google Sheets
that allows you to manipulate data in this format . Spreadsheets
are made out of rows and columns, with each row usually repre-
senting one item and each cell in the row representing some
aspect of that item.
Spreadsheet data is often stored in plain-text
®les
with columns
using commas or the tab character. A
comma-separated values
®le
is abbreviated as
CSV
, and uses the
®le
extension
.csv
. When
tabs are used, the extension
.tsv
is sometimes used. Py thon
includes a librar y to make it easy to work with data stored in this
format . In this chapter, we will focus on loading data from a CSV
®le.
To load a CSV or TSV
®le,
you†ll need to place it in your sketch†s
data
folder (as described in
Chapter 7
).
The data for the next example is a
simpli®ed
version of Boston
Red Sox player David Ortiz†s batting statistics from 1997 to
2014. From left to right , it is the year, number of home runs, runs
batted in (RBIs), and batting average. When opened in a text
editor, the
®rst


®ve
lines of the
®le
look like this:
1997,1,6,0.327
1998,9,46,0.277
1999,0,0,0
2000,10,63,0.282
2001,18,48,0.234
Example 12-3: Read the Data
To load this data into Processing, we need to use one of
Py thon†s built-in libraries called
csv
. The
csv
librar y provides
functions and classes that make it easy to work with data in CSV
format . We also need to use the built-in Py thon func-
tion
open()
to gain access to the
®le
in the sketch†s data folder.
Once we† ve created a CSV reader object , we use a
for
loop to
operate on each row of data in sequence:




import


csv
statsFileHandle


=


open
(
"ortiz.csv"
)
statsData


=


csv
.
reader(statsFileHandle)
for


row


in


statsData:




year


=


row[0]




homeRuns


=


row[1]




rbi


=


row[2]




average


=


row[3]




print


year,


homeRuns,


rbi,


average
The
import
statement at the beginning of the program is what
signals to Py thon that we want to use the built-in
csv
librar y in
our program. The
open()
function takes the name of the CSV
®le
we want to work with as a parameter, and returns a special kind
of object called a
®le
handle
. We then pass that
®le
handle as a
parameter to the
csv.reader()
function, which returns a CSV
reader object (which we† ve assigned to a variable called
stats-
Data
here). A CSV reader object works a lot like a list , in that we
can iterate over it with a
for
loop. (We† ve called the temporar y
loop variable here
row
, but there†s nothing special about that
word. You can call it whatever you want!)
Inside the
for
loop, we can access data for the current row using
the numerical index of the relevant column. The expres-
sion
row[0]
evaluates to the item in the
®rst
column of the row
(i.e., the year), the expression
row[1]
evaluates to the item in the
second column, and so forth.
Getting the Right Type
There†s one tricky thing about using CSV
®les,
which is that they
don†t contain any information about what
kind
of data they †re
storing. To illustrate, think about how you might go about
®nding
the sum of David Ortiz†s home runs in his career. You might
write some code that looks like this:
import


csv
statsFileHandle


=


open
(
"ortiz.csv"
)
statsData


=


csv
.
reader(statsFileHandle)
homeRunTotal


=


0
for


row


in


statsData:
163








homeRunTotal


+=


row[1]
print


homeRunTotal
In this code, we made a variable called
homeRunTotal
to store the
total number of home runs. As we iterate over each row, we add
the number from the second column, which contains the num-
ber of home runs for that year. Looks good, right? But there†s a
problem. If you tr y to run this, you†ll get the following error:
TypeError: unsupported operand type(s) for +: †int† and †str†
This error is telling you that you were attempting to add
an
int
to a
str
. Py thon doesn†t know how to do that , so your
program didn†t work. This happened because the
csv
librar y
always gives you data from a CSV
®le
as a
string
, even if the
underlying data
looks
like a number. If you want to use that
string as a number, you have to explicitly convert it your-
self, using one of Py thon†s built-in conversion functions
like
int()
.
Here†s a corrected version of the preceding example. The only
change we† ve made is to the line inside the
for
loop, where we
use the
int()
function to convert the value from the CSV
®le
from


a string to an
int
:
import


csv
statsFileHandle


=


open
(
"ortiz.csv"
)
statsData


=


csv
.
reader(statsFileHandle)
homeRunTotal


=


0
for


row


in


statsData:




homeRunTotal


+=


int
(row[1])
print


homeRunTotal
Example 12-4: Draw the Table
The next example builds on the last . It creates a list
called
homeRuns
to store data after it is loaded inside
setup()
and
the data from that list is used within
draw()
. In
setup()
, we again
use
open()
to get a
®le
handle for our CSV
®le,
and then give the
®le
handle as a parameter to
csv.reader()
. In a
for
loop, we




append each home run count to our
homeRuns
list , taking care to
convert the values to integers
®rst.
Two separate tasks are accomplished in
draw()
. First , a
for
loop
draws vertical lines for our graph based on the number of
entries in the
homeRuns
list . A second
for
loop reads each ele-
ment of the
homeRuns
list and plots a line on the graph using the
data.
This example is the visualization of a
simpli®ed
version of Bos-
ton Red Sox player David Ortiz†s batting statistics from 1997 to
2014 drawn from a table:
import


csv
homeRuns


=


list
()
def


setup
():




size
(480,


120)




statsFileHandle


=


open
(
"ortiz.csv"
)




statsData


=


csv
.
reader(statsFileHandle)




for


row


in


statsData:








homeRuns
.
append
(
int
(row[1]))




print


homeRuns
def


draw
():




background
(204)




# Draw background grid for data




stroke
(153)




line
(20,


100,


20,


20)




line
(20,


100,


460,


100)




for


i


in


range
(
len
(homeRuns)):








x


=


map
(i,


0,


len
(homeRuns)
-
1,


20,


460)








line
(x,


20,


x,


100)




# Draw lines based on home run data




noFill
()




stroke
(0)




beginShape
()
165








for


i


in


range
(
len
(homeRuns)):








x


=


map
(i,


0,


len
(homeRuns)
-
1,


20,


460)








y


=


map
(homeRuns[i],


0,


60,


100,


20)








vertex
(x,


y)




endShape
()
This example is so minimal that it†s not necessar y to store this
data in lists, but the idea can be applied to more complex exam-
ples you might want to make in the future. In addition, you can
see how this example will be enhanced with more informationŁ
for instance, information on the vertical axis to state the number
of home runs and on the horizontal to
de®ne
the year.
Example 12-5: 29,740 Cities
To get a better idea about the potential of working with data
tables, the next example uses a larger data set and introduces a
convenient feature. This table data is
di‚erent
because the
®rst
rowŁthe
®rst
line in the
®leŁis
a
header
. The header
de®nes
a
label for each column to clarif y the context . This is the
®rst


®ve
lines of our new data
®le
called
cities.csv
:
zip,state,city,lat,lng
35004,AL,Acmar,33.584132,-86.51557
35005,AL,Adamsville,33.588437,-86.959727
35006,AL,Adger,33.434277,-87.167455
35007,AL,Keystone,33.236868,-86.812861
The header makes it easier to read the dataŁfor example, the
second line of the
®le
states the zip code of Acmar, Alabama, is
35004 and
de®nes
the latitude of the city as 33.584132 and the
longitude as -86.51557. In total, the
®le
is 29,741 lines long and it
de®nes
the location and zip codes of 29,740 cities in the United
States.
The next example loads this data within the
setup()
and then
draws it to the screen in a
for
loop within the
draw()
.
The
setXY()
function converts the latitude and longitude data
from the
®le
into a point on the screen:




import


csv
citiesData


=


None
def


setXY(lat,


lng):




x


=


map
(lng,


-
180,


180,


0,


width
)




y


=


map
(lat,


90,


-
90,


0,


height
)






point
(x,


y)
def


setup
():




global


citiesData




size
(240,


120)




citiesFileHandle


=


open
(
"cities.csv"
)




citiesData


=


list
(csv
.
DictReader(citiesFileHandle))




strokeWeight
(0.1)




stroke
(255)
def


draw
():




background
(0,


26,


51)




xoffset


=


map
(
mouseX
,


0,


width
,


-
width
*
3,


-
width
)




translate
(xoffset,


-
300)




scale
(10)




for


row


in


citiesData:








latitude


=


float
(row[
"lat"
])








longitude


=


float
(row[
"lng"
])








setXY(latitude,


longitude)
The
csv.DictReader
object is a little
di‚erent
from the
csv.reader
object that we used in the previous example. When
we used the
csv.reader
object , we had to access each cell in a
row of data by its numerical index. The
csv.DictReader
object ,
on the other hand, gives us a
dictionar y
for each row. This dictio-
nar y uses the strings in the header line of the CSV
®le
as its
keys, and each key maps to the corresponding value for the row
in question. Because each row is a dictionar y, we can use (for
example) the expression
row["lat"]
to access the latitude col-
167




umn, which is much easier to remember than if we needed to
reference the column by its numerical index.
You may have noticed the curious use of the built-in
list()
function in
setup()
. This is necessar y because
csv.DictReader
objects, unlike regular lists, can only be iterated
over once. We use the
list()
function to read all of the rows
from one of these objects at once and store them in a separate
variable. The resulting value, stored in the variable
citiesData
, is
a list of dictionaries (much like the
planetsList
variable in
Example 12-2 on page 161
).
JSON
The JavaScript Object Notation (JSON) format is another com-
mon system for storing data. Like HTML and XML formats, the
elements have labels associated with them. For instance, the
data for a
®lm
might include labels for the title, director, release
year, rating, and more. These labels will be paired with the data
like this:
"title": "Alphaville"
"director": "Jean-Luc Godard"
"year": 1964
"rating": 9.1
To work as a JSON
®le,
the
®lm
labels need a little more punctu-
ation to separate the elements. Commas are used between
each data pair, and braces enclose it . The data
de®ned
within
the curly braces is a
JSON object
.
With these changes, our valid JSON data
®le
looks like this:
{
"title": "Alphaville",
"director": "Jean-Luc Godard",
"year": 1964,
"rating": 9.1
}
There†s another interesting detail in this short JSON sample
related to data types: you†ll notice that the title and director
data is contained within quotes to mark them as strings, and the
year and rating are without quotes to
de®ne
them as numbers.
Speci®cally,
the year is an integer and the rating is a
¯oating-




point
number. This distinction becomes important after the
data is loaded into a sketch.
To add another
®lm
to the list , a set of brackets placed at the top
and bottom are used to signif y that the data is an array of JSON
objects. Each object is separated by a comma.
Putting it together looks like this:
[
{
"title": "Alphaville",
"director": "Jean-Luc Godard",
"year": 1964,
"rating": 9.1
},
{
"title": "Pierrot le fou",
"director": "Jean-Luc Godard",
"year": 1965,
"rating": 7.3
}
]
This pattern can be repeated to include more
®lms.
At this
point , it†s interesting to compare this JSON notation to the cor-
responding CSV representation of the same data.
As a CSV
®le,
the data looks like this:
title,director,year,rating
Alphaville,Jean-Luc Godard,1965,9.1
Weekend,Jean-Luc Godard,1967,7.3
Notice that the CSV notation has fewer characters, which can
be important when working with massive data sets. On the
other hand, the JSON version is often easier to read because
each piece of data is labeled.
Now that the basics of JSON and its relation to CSV data has
been introduced, let†s look at the code needed to read a JSON
®le
into a Processing sketch.
Example 12-6: Read a JSON File
You may have noticed that the JSON format looks ver y similar to
the way Py thon data structures look when we include them
169




directly in our program. This similarity is a little misleading, as
there are a number of subtle
di‚erences
between the two, and
you can†t just paste a JSON data structure verbatim into your
Py thon program and expect it to work. What we need is a way to
read data stored in JSON format and convert it into a Py thon
data structure that we can use in our program. Py thon supplies
us with this functionality through the built-in
json
librar y.
This sketch loads the JSON
®le
from the beginning of this sec-
tion, the
®le
that includes only the data for the
®lm


Alphaville
:
import


json
def


setup
():




filmFileHandle


=


open
(
"film.json"
)




film


=


json
.
load(filmFileHandle)




title


=


film[
"title"
]




director


=


film[
"director"
]




year


=


film[
"year"
]




rating


=


film[
"rating"
]




print


"Title: "
,


title




print


"Director: "
,


director




print


"Year: "
,


year




print


"Rating: "
,


rating
The
json.load()
function loads data in JSON format from a
given
®le
handle. (Just as with the CSV examples, we need to
create the
®le
handle
®rst
with the built-in
open()
function.)
The
json.load()
function returns a value of a compound data
type that corresponds to the data in the JSON
®le.
In this exam-
ple, the JSON object in
®lm.json
is converted into a Py thon dic-
tionar y, which we store in the variable
film
. We can then use
square bracket syntax to access values for particular keys in
that dictionar y. After we† ve converted the JSON into Py thon, the
types of the values retrieved will
re¯ect
their types from the
original JSON data structure (i.e., JSON integers will become
Py thon integers, JSON strings will become Py thon strings, etc.).
Example 12-7: Visualize Data from a
JSON File
In this example, the data
®le
started before has been updated to
include all of the director†s
®lms
from 1960Š1966. The name of




each
®lm
is placed in order on screen according to the release
year and assigned a gray value based on the rating value.
There are several
di‚erences
between this example and
Exam-
ple 12-4 on page 164
. The most important is the fact that the
data structure in
®lms.json
is a list of dictionaries, not just a sin-
gle dictionar y. As a result , the call to
json.load()
in
setup()
returns a list . Each item in this list is a dictionar y that contains
data for a particular
®lm.
Inside
draw()
, we iterate over each
item in this list and display its values to the screen:
import


json
films


=


[]
def


setup
():




global


films




size
(480,


120)




filmFileHandle


=


open
(
"films.json"
)




films


=


json
.
load(filmFileHandle)
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
(films)):








film


=


films[i]








ratingGray


=


map
(film[
"rating"
],


6.5,


8.1,


102,


255)








pushMatrix
()








translate
(i
*
32


+


32,


105)








rotate
(
-
QUARTER_PI
)








fill
(ratingGray)








text
(film[
"title"
],


0,


0)








popMatrix
()
This example is bare bones in its visualization of the
®lm
data. It
shows how to load the data and how to draw based on those
data values, but it†s your challenge to format it to accentuate
what you
®nd
interesting about the data. For example, is it more
interesting to show the number of
®lms
Godard made each
171




year? Is it more interesting to compare and contrast this data
with the
®lms
of another director? Will all of this be easier to
read with a
di‚erent
font , sketch size, or aspect ratio? The skills
introduced in the earlier chapters in this book can be applied to
bring this sketch to the next step of
re®nement.


Network Data and APIs
Public access to massive quantities of data collected by govern-
ments, corporations, organizations, and individuals is changing
our culture, from the way we socialize to how we think about
intangible ideas like privacy. This data is most often accessed
through software structures called
APIs
.
The acronym
API
is mysterious, and its meaningŁapplication
programming interfaceŁisn†t much clearer. However, APIs are
essential for working with data and they aren†t necessarily
diŸ-
cult
to understand. Essentially, they are requests for data made
to a ser vice. When data sets are huge, it†s not practical or
desired to copy the entirety of the data; an API allows a pro-
grammer to request only the trickle of data that is relevant from
a massive sea.
This concept can be more clearly illustrated with a hypothetical
example. Let†s assume there†s an organization that maintains a
database of temperature ranges for ever y city within a countr y.
The API for this dataset allows a programmer to request the
high and low temperatures for any city during the month of
October in 1972. In order to access this data, the request must
be made through a
speci®c
line or lines of code, in the format
mandated by the data ser vice.
Some APIs are entirely public, but many require authentication,
which is typically a unique user ID or key so the data ser vice can
keep track of its users. Most APIs have rules about how many, or
how frequently, requests can be made. For instance, it might be
possible to make only 1,000 requests per month, or no more
than one request per second. Many APIs also require you to reg-
ister as a developer on their site to obtain an ﬁAPI key,ﬂ a special
identif ying string that must be included with the API request .




Processing can request data over the Internet when the com-
puter that is running the program is online. CSV, TSV, JSON, and
XML
®les
can be loaded using the corresponding load function
with a URL as the parameter. For instance, the current weather
in Cincinnati is available in JSON format at this URL:
™
http://api.openweathermap.org/data/2.5/®nd?q=Cincin-
nati&units=imperial&appid=YOUR_API_KEY
Read the URL closely to decode it:
1.It requests data from the
api
subdomain of the
openweather-
map.org
site.
2. It
speci®es
a city to search for (
q
is an abbreviation for
quer y
, and is frequently used in URLs that specif y searches).
3. It indicates that the data will be returned in imperial format ,
which means the temperature will be in Fahrenheit . Replac-
ing
imperial
with
metric
will provide temperature data in
degrees Celsius.
4. It includes your API key, supplied as the
appid
parameter.
Visit
http://openweathermap.org/api
for more information on
accessing the Open Weather Map API and obtaining an API key.
Looking at this data from OpenWeatherMap is a more realistic
example of working with data found in the wild rather than the
simpli®ed
data sets introduced earlier. At the time of this writ-
ing, the
®le
returned from that URL looks like this:
{"message":"accurate","cod":"200","count":1,"list":[{"id":
4508722,"name":"Cincinnati","coord":{"lon":-84.456886,"lat":
39.161999},"main":{"temp":34.16,"temp_min":34.16,"temp_max":
34.16,"pressure":999.98,"sea_level":1028.34,"grnd_level":
999.98,"humidity":77},"dt":1423501526,"wind":{"speed":
9.48,"deg":354.002},"sys":{"country":"US"},"clouds":{"all":
80},"weather":[{"id":803,"main":"Clouds","description":"broken
clouds","icon":"04d"}]}]}
This
®le
is much easier to read when it†s formatted with line
breaks and the JSON object and list structures
de®ned
with
braces and brackets:
173




{
"message": "accurate",
"count": 1,
"cod": "200",
"list": [{
"clouds": {"all": 80},
"dt": 1423501526,
"coord": {
"lon": -84.456886,
"lat": 39.161999
},
"id": 4508722,
"wind": {
"speed": 9.48,
"deg": 354.002
},
"sys": {"country": "US"},
"name": "Cincinnati",
"weather": [{
"id": 803,
"icon": "04d",
"description": "broken clouds",
"main": "Clouds"
}],
"main": {
"humidity": 77,
"pressure": 999.98,
"temp_max": 34.16,
"sea_level": 1028.34,
"temp_min": 34.16,
"temp": 34.16,
"grnd_level": 999.98
}
}]
}
Note that brackets are seen in the
"list"
and
"weather"
sec-
tions, indicating a list of JSON objects. Although the list in this
example only contains a single item, in other cases, the API
might return multiple days or variations of the data from multi-
ple weather stations.




Example 12-8: Parsing the Weather
Data
The
®rst
step in working with this data is to study it and then to
write minimal code to extract the desired data. In this case,
we†re curious about the current temperature. We can see that
our temperature data is 34.16. It†s labeled as
temp
and it†s inside
the
main
object , which is inside the list of objects given as a
value for the key
list
. A function called
getTemp()
was written
for this example to work with the format of this
speci®c
JSON
®le
organization:
import


json
def


getTemp(fileName):




weatherFileHandle


=


open
(fileName)




weather


=


json
.
load(weatherFileHandle)




list_value


=


weather[
"list"
]


# get value for "list" key




item


=


list_value[0]


# get first item from list_value




main


=


item[
"main"
]


# item is a dictionary; get "main" value




temperature


=


main[
"temp"
]


# get value for "temp" key




return


temperature
def


setup
():


temp


=


getTemp(
"cincinnati.json"
)


print


temp
The name of the JSON
®le,


cincinnati. json
, is passed into the
getTemp()
function inside
setup()
and loaded there. Next ,
because of the format of the JSON
®le,
a series of lists and dic-
tionaries are needed to get deeper and deeper into the data
structure to
®nally
arrive at our desired number. This number is
stored in the
temperature
variable and then returned by the
function to be assigned to the
temp
variable in
setup()
where it is
printed to the console.
Example 12-9: Chaining Square
Brackets
The sequence of JSON variables created in succession in the
last example can be approached
di‚erently
by chaining the
indexes together. This example works like
Example 12-8  on page
175
except that each square bracket index is connected directly
175




to the previous one, rather than calculated one at a time and
assigned to variables in between:
import


json
def


getTemp(fileName):


weather


=


json
.
load(
open
(fileName))




return


weather[
"list"
][0][
"main"
][
"temp"
]
def


setup
():


temp


=


getTemp(
"cincinnati.json"
)


print


temp
This example can be
modi®ed
to access more of the data from
the feed and to build a sketch that displays the data to the
screen rather than just writing it to the console. You can also
modif y it to read data from another online APIŁyou†ll
®nd
that
the data returned by many APIs shares a similar format .
Robot 10: Data
The
®nal
robot example in this book is
di‚erent
from the rest
because it has two parts. The
®rst
part generates a data
®le
using random values and
for
loops, and the second part reads
that data
®le
to draw an army of robots onto the screen.




The
®rst
sketch uses several new code elements. First , we†ll use
the
open()
function to create a new
®le,
and then we†ll use the
®le
handle object†s
write()
method to write data to that
®le.
In
this example, the
®le
handle object is called
output
and the
®le
is
called
botArmy.tsv
. (You†ll need to adjust the path in the follow-
ing example to
re¯ect
a folder that exists on your own com-
puter.) Random values are used to
de®ne
which of three robot
images will be drawn for each coordinate. For the
®le
to be cor-
rectly created, the
close()
method must be run before the pro-
gram is stopped.
Notice that we called the
open()
function in this example with a
second parameter: the string
"w"
. This parameter signals to
Py thon that we want to open the
®le
not just to read its con-
tents, but to write new contents to it . (The
w
stands for
write
.)
The code that draws an ellipse is a visual preview to reveal the
location of the coordinate on screen, but notice that the ellipse
isn†t recorded into the
®le.
Also note that the we need to use the
str()
function to explicitly convert the
x
,
y
, and
robotType
values
to strings so that we can build the line of text that gets written to
the
®le:
def


setup
():


size
(720,


480)


# Create the new file




output


=


open
(
"/Users/allison/botArmy.tsv"
,


"w"
)


# Write a header line with the column titles


output
.
write(
"type
\t
x
\t
y
\n
"
)


for


y


in


range
(0,


height
+
1,


60):


for


x


in


range
(0,


width
+
1,


20):


robotType


=


str
(
int
(
random
(1,


4)))


output
.
write(robotType
+
"
\t
"
+
str
(x)
+
"
\t
"
+
str
(y)
+
"
\n
"
)


ellipse
(x,


y,


12,


12)


output
.
close
()


# Finish the file
After that program is run, you†ll
®nd
a
®le
named
botArmy.tsv
in
the location you
speci®ed
in the
®rst
parameter to the
open()
function. Open it to see how the data is written. The
®rst


®ve
lines of that
®le
will be similar to this:
type


x


y
3


0


0
1


20


0
2


40


0
177




1


60


0
3


80


0
The
®rst
column is used to
de®ne
which robot image to use, the
second column is the
x
coordinate, and the third column is the
y
coordinate.
The next sketch loads the
botArmy.tsv


®le
and uses the data for
these purposes. Note that because the data was written in tab-
separated values (TSV) format instead of comma-separated val-
ues (CSV) format , we need to include
delimiter="\t"
as an
extra parameter in the call to
csv.DictReader
:
import


csv
def


setup
():




size
(720,


480)


background
(0,


153,


204)




bot1


=


loadShape
(
"robot1.svg"
)




bot2


=


loadShape
(
"robot2.svg"
)




bot3


=


loadShape
(
"robot3.svg"
)




shapeMode
(
CENTER
)




robotsFileHandle


=


open
(
"/Users/allison/botArmy.tsv"
)




robots


=


csv
.
DictReader(robotsFileHandle,


delimiter
=
"
\t
"
)




for


row


in


robots:








bot


=


int
(row[
"type"
])








x


=


int
(row[
"x"
])








y


=


int
(row[
"y"
])








sc


=


0.3








if


bot


==


1:












shape
(bot1,


x,


y,


bot1
.
width
*
sc,


bot1
.
height
*
sc)








elif


bot


==


2:












shape
(bot2,


x,


y,


bot2
.
width
*
sc,


bot2
.
height
*
sc)








else
:












shape
(bot3,


x,


y,


bot3
.
width
*
sc,


bot3
.
height
*
sc)




13/Extend
This book focuses on using Processing
for interactive graphics, because that•s
the core of what Processing does. How-
ever, the software can do much more and
is often part of projects that move
beyond a single computer screen. For
example, Processing has been used to
control machines, create images used in
feature
®lms,
and export models for 3D
printing.
Over the last decade, Processing has been used to make music
videos for Radiohead and R.E.M., to make illustrations for publi-
cations such as
Nature
and the
New York Times
, to output
sculptures for galler y exhibitions, to control huge video walls, to
knit sweaters, and much more. Processing has this
¯exibility
because of its system of libraries.
A Processing
librar y
is a collection of code that extends the soft-
ware beyond its core functions and classes. Libraries have been
important to the grow th of the project , because they let devel-
opers add new features quickly. As smaller, self-contained
projects, libraries are easier to manage than if these features
were integrated into the main software.
To use a librar y, select Import Librar y from the Sketch menu and
select the librar y you want to use from the list . Choosing a
librar y adds a line of code that indicates that the librar y will be
used with the current sketch.
179




For instance, when the PDF Export Librar y (pdf ) is added, this
line of code is added to the top of the sketch:
add_library(
†pdf†
)
In addition to the libraries included with Processing (these are
called the
core
libraries), there are over 100
contributed
libraries
that are linked from the Processing website. All libraries are lis-
ted online at
http://processing.org/reference/libraries/
.
Before a contributed librar y can be imported through the
Sketch menu, it must be added through the
Librar y Manager
.
Select the Import Librar y option from the Sketchbook menu
and then select Add Librar y to open the Librar y Manager inter-
face. Click on a librar y description and then click on the Install
button to download it to your computer.
The downloaded
®les
are saved to the
libraries
folder that is
located in your sketchbook. You can
®nd
the location of your
sketchbook by opening the Preferences. The Librar y Manager
can also be used to update and remove libraries.
As mentioned before, there are more than 100 Processing libra-
ries, so they clearly can†t all be discussed here. We† ve selected a
few that we think are fun and useful to introduce in this chapter.
Sound
The
Sound audio librar y
introduced with Processing 3.0 has the
ability to play, analyze, and generate (synthesize) sound. This
librar y needs to be downloaded with the Librar y Manager as
described earlier. (It†s not included with the main Processing
download because of its size.)
Like the images, shape
®les,
and fonts introduced in
Chapter 7
,
a sound
®le
is another type of media to augment a Processing
sketch. Processing †s Sound librar y can load a range of
®le
for-
mats including WAV, AIFF, and MP3. Once a sound
®le
is loaded,
it can be played, stopped, and looped, or even distorted using
di‚erent


ﬁe‚ectsﬂ
classes.




Example 13-1: Play a Sample
The most common use of the Sound librar y is to play a sound as
background music or when an event happens on screen. The
following example builds on
Example 8-5 on page 103
to play a
sound when the shape hits the edges of the screen. The
blip.wav
®le
is included in the
media
folder that can be downloaded by
following the instructions in
Chapter 7
.
As with other media, the variable that will contain the
SoundFile
object is
de®ned
at the top of the sketch, it†s loaded within
setup()
, and after that , it can be used anywhere in the program:
add_library(
†sound†
)
blip


=


None
radius


=


120
x


=


0
speed


=


1.0
direction


=


1
def


setup
():




global


blip,


x




size
(440,


440)




ellipseMode
(
RADIUS
)




blip


=


SoundFile(this,


"blip.wav"
)




x


=


width
/
2


# Start in the center
def


draw
():




global


x,


direction




background
(0)




x


+=


speed


*


direction




if


x


>


width
-
radius


or


x


<


radius:








direction


=


-
direction


# Flip direction








blip
.
play()




if


direction


==


1:








arc
(x,


220,


radius,


radius,


0.52,


5.76)


# Face right




else
:








arc
(x,


220,


radius,


radius,


3.67,


8.9)


# Face left
The sound is triggered each time its
play()
method is run. This
example works well because the sound is only played when the
value of the
x
variable is at the edges of the screen. If the sound
were played each time through
draw()
, the sound would restart
60 times each second and wouldn†t have time to
®nish
playing.
181




The result is a rapid clipping sound. To play a longer sample
while a program runs, call the
play()
or
loop()
method for that
sound inside
setup()
so the sound is triggered only a single
time.
The
SoundFile
class has many methods to control
how a sound is played. The most essential are
play()
to play the sample a single time,
loop()
to
play it from beginning to end over and over,
stop()
to
halt the playback, and
jump()
to move to a
speci®c
moment within the
®le.


Example 13-2: Listen to a Microphone
In addition to playing a sound, Processing can listen. If your
computer has a microphone, the Sound Librar y can read live
audio through it . Sounds from the mic can be analyzed, modi-
®ed,
and played:
add_library(
†sound†
)
mic


=


None
amp


=


None
def


setup
():




global


mic,


amp




size
(440,


440)




background
(0)




# Create an audio input and start it
mic
=
AudioIn(this, 0)
mic
.
start
()
# Create a new amplitude analyzer and patch into input
amp
=
Amplitude(this)
amp
.
input(mic)
def
draw
():
# Draw a background that fades to black
noStroke
()
fill
(26, 76, 102, 10)
rect
(0, 0,
width
,
height
)
# The analyze() method returns values between 0 and 1,
# so map() is used to convert the values to larger numbers
diameter
=
map
(amp
.
analyze(), 0, 1, 10,
width
)
# Draw the circle based on the volume
fill
(255)
ellipse
(
width
/
2,
height
/
2, diameter, diameter)
There are two parts to getting the
amplitude
(volume) from an
attached microphone. The
AudioIn
class is used to get the sig
-
nal data from the mic and the
Amplitude
class is used to meas
-
ure the signal. Objects from both classes are
de®ned
at the top
of the code and created inside
setup()
.
After the
Amplitude
object (named
amp
here) is made, the
AudioIn
object (named
mic
) is patched in to the
amp
object with
the
input()
method. After that , the
analyze()
method of the
amp
object can be run at any time to read the amplitude of the
microphone data within the program. In this example, that is
done each time through
draw()
and that value is then used to
set the size of the circle.
In addition to playing a sound and analyzing sound as demon
-
strated in the last two examples, Processing can synthesize
sound directly. The fundamentals of sound synthesis are wave
-
forms that include the sine wave, triangle wave, and square
wave.
A sine wave sounds smooth, a square wave is harsh, and a trian
-
gle wave is somewhere between. Each wave has a number of
properties. The
frequency
, measured in hertz, determines the
pitchŁthe highness or lowness of the tone. The
amplitude
of the
wave determines the volumeŁthe degree of loudness.




Example 13-3: Create a Sine Wave
In the following example, the value of
mouseX
determines the fre-
quency of a sine wave. As the mouse moves left and right , the
audible frequency and corresponding wave visualization
increase and decrease:
add_library(
†sound†
)
sine


=


None
freq


=


400.0
def


setup
():




global


sine




size
(440,


440)




# Create and start the sine oscillator




sine


=


SinOsc(this)




sine
.
play()
def


draw
():




background
(176,


204,


176)




# Map the mouseX value from 20Hz to 440Hz for frequency




hertz


=


map
(
mouseX
,


0,


width
,


20.0,


440.0)




sine
.
freq(hertz)




# Draw a wave to visualize the frequency of the sound




stroke
(26,


76,


102)




for


x


in


range
(
width
):








angle


=


map
(x,


0,


width
,


0,


TWO_PI


*


hertz)








sinValue


=


sin
(angle)


*


120








line
(x,


0,


x,


height
/
2


+


sinValue)




The
sine
object , created from the
SinOsc
class, is
de®ned
at the
top of the code and then created inside
setup()
. Like working
with a sample, the wave needs to be played with the
play()
method to start generating the sound. Within
draw()
, the
freq()
method continuously sets the frequency of the waveform based
on the left-right position of the mouse.
Image and PDF Export
The animated images created by a Processing program can be
turned into a
®le
sequence with the
saveFrame()
function. When
saveFrame()
appears at the end of
draw()
, it saves a numbered
sequence of TIFF-format images of the program†s output
named
screen-0001.tif
,
screen-0002.tif
, and so on to the
sketch†s folder.
These
®les
can be imported into a video or animation program
and saved as a movie
®le.
You can also specif y your own
®le-
name
and image
®le
format with a line of code like this:
saveFrame
(
"output-####.png"
)
Use the
#
(hash mark) symbol to show where the numbers will
appear in the
®lename.
They are replaced with the actual frame
numbers when the
®les
are saved. You can also specif y a sub-
folder to save the images into, which is helpful when working
with many image frames:
saveFrame
(
"frames/output-####.png"
)
When using
saveFrame()
inside
draw()
, a new
®le
is
saved each frameŁso watch out , as this can quickly
®ll
your
sketch
folder with thousands of
®les.
Example 13-4: Saving Images
This example shows how to save images by storing enough
frames for a two-second animation. It loads and moves the
robot
®le
from
ﬁRobot 5: Mediaﬂ on page 97
. See
Chapter 7
for
instructions for downloading the
®le
and adding it to the sketch.
185




The example runs the program at 30 frames per second and
then exits after 60 frames:
bot


=


None
x


=


0
def


setup
():




global


bot




size
(720,


480)




bot


=


loadShape
(
"robot1.svg"
)




frameRate
(30)
def


draw
():




global


x




background
(0,


153,


204)




translate
(x,


0)




shape
(bot,


0,


80)




saveFrame
(
"frames/SaveExample-####.tif"
)




x


+=


12




if


frameCount


==


60:










exit
()
Processing will write an image based on the
®le
extension that
you use (
.png
,
. jpg
, and
.tif
are all built in, and some platforms
may support others). A
.tif
image is saved uncompressed, which
is fast but takes up a lot of disk space. Both
.png
and
. jpg
will
create smaller
®les,
but because of the compression, will usually
require more time to save, making the sketch run slowly.
If your desired output is vector graphics, you can write the out-
put to PDF
®les
for higher resolution. The PDF Export librar y
makes it possible to write PDF
®les
directly from a sketch. These
vector graphics
®les
can be scaled to any size without losing
resolution, which makes them ideal for print outputŁfrom post-
ers and banners to entire books.




Example 13-5: Draw to a PDF
This example builds on
Example 13-4 on page 185
to draw more
robots, but it removes the motion. The PDF librar y is imported
at the top of the sketch to extend Processing to be able to write
PDF
®les.
This sketch creates a PDF
®le
called
Ex-13-5.pdf
because of the
third and fourth parameters to
size()
:
add_library(
†pdf†
)
bot


=


None
def


setup
():




global


bot


size
(600,


800,


PDF
,


"Ex-13-5.pdf"
)


bot


=


loadShape
(
"robot1.svg"
)
def


draw
():


background
(255)


for


i


in


range
(100):


rx


=


random
(
-
bot
.
width
,


width
)


ry


=


random
(
-
bot
.
height
,


height
)


shape
(bot,


rx,


ry)


exit
()
The geometr y is not drawn on the screen; it is written directly
into the PDF
®le,
which is saved into the sketch†s folder. The
code in this example runs once and then exits at the end of
draw()
. The resulting output is shown in
Figure 13-1
.
There are more PDF Export examples included with the Pro-
cessing software. Look in the
PDF Export
(pdf ) section of the
Processing examples to see more techniques.
187




Figure 13-1.
PDF export from
Example 13-5
Hello, Arduino
Arduino is an electronics prototyping platform with a series of
microcontroller boards and the software to program them. Pro-
cessing and Arduino share a long histor y together; they are sis-




ter projects with many similar ideas and goals, though they
address separate domains. Because they share the same editor
and programming environment and a similar syntax, it†s easy to
move between them and to transfer knowledge about one into
the other.
In this section, we focus on reading data into Processing from
an Arduino board and then visualizing that data on screen. This
makes it possible to use new inputs into Processing programs
and to allow Arduino programmers to see their sensor input as
graphics. These new inputs can be any thing that attaches to an
Arduino board. These devices range from a distance sensor to a
compass or a mesh network of temperature sensors.
This section assumes that you have an Arduino board and a
basic working knowledge of how to use it . If not , you can learn
more online at
http://www.arduino.cc
and in the excellent book
Getting Started with Arduino
by Massimo Banzi (Maker Media).
Once you† ve covered the basics, you can learn more about send-
ing data between Processing and Arduino in another outstand-
ing book,
Making Things Talk
by Tom Igoe (Maker Media).
Data can be transferred between a Processing sketch and an
Arduino board with some help from the Processing Serial
Librar y.
Serial
is a data format that sends one by te at a time. In
the world of Arduino, a
by te
is a data type that can store values
between 0 and 255; it works like an
int
, but with a much smaller
range. L arger numbers are sent by breaking them into a list of
by tes and then reassembling them later.
In the following examples, we focus on the Processing side of
the relationship and keep the Arduino code simple. We visualize
the data coming in from the Arduino board one by te at a time.
With the techniques covered in this book and the hundreds of
Arduino examples online, we hope this will be enough to get you
started.
Example 13-6: Read a Sensor
The following Arduino code is used with the next three Process-
ing examples:
189




// Note: This is code for an Arduino board, not Processing
int sensorPin = 0;  // Select input pin
int val = 0;
void setup() {
Serial.begin(9600);  // Open serial port
}
void loop() {
val = analogRead(sensorPin) / 4;  // Read value from sensor
Serial.write((byte)val);  // Print variable to serial port
delay(100);  // Wait 100 milliseconds
}
There are two important details to note about this Arduino
example. First , it requires attaching a sensor into the analog
input on pin 0 on the Arduino board. You might use a light sen-
sor (also called a photo resistor, photocell, or light-dependent
resistor) or another analog resistor such as a thermistor
(temperature-sensitive resistor),
¯ex
sensor, or pressure sensor
(force-sensitive resistor). The circuit diagram and drawing of the
breadboard with components are shown in
Figure 13-2
. Next ,
notice that the value returned by the
analogRead()
function is
divided by 4 before it†s assigned to
val
. The values from
analog
Read()
are between 0 and 1023, so we divide by 4 to convert
them to the range of 0 to 255 so that the data can be sent in a
single by te.
Figure 13-2.
Attaching a light sensor (photo resistor) to analog
in pin 0




Example 13-7: Read Data from the
Serial Port
The
®rst
visualization example shows how to read the serial data
in from the Arduino board and how to convert that data into the
values that
®t
to the screen dimensions:
add_library(
†serial†
)
port


=


None




# for object from Serial class
val


=


0.0








# Data received from the serial port
def


setup
():




global


port




size
(440,


220);




# IMPORTANT NOTE:




# The first serial port retrieved by Serial.list()




# should be your Arduino. If not, uncomment the next




# line by deleting the # before it. Run the sketch




# again to see a list of serial ports. Then, change




# the 0 in between [ and ] to the number of the port




# that your Arduino is connected to.




#print Serial.list()




arduinoPort


=


Serial
.
list
()[0]




port


=


Serial(this,


arduinoPort,


9600)
def


draw
():




global


val




if


port
.
available()


>


0:














# If data is available,








val


=


port
.
read()
























# read it and store it in val








val


=


map
(val,


0,


255,


0,


height
)


# Convert the value




rect
(40,


val
-
10,


360,


20)
The Serial librar y is imported on the
®rst
line and the serial port
is opened in
setup()
. It may or may not be easy to get your Pro-
cessing sketch to talk with the Arduino board; it depends on
your hardware setup. There is often more than one device that
the Processing sketch might tr y to communicate with. If the
code doesn†t work the
®rst
time, read the comment in
setup()
carefully and follow the instructions.
Within
draw()
, the value is brought into the program with the
read()
method of the Serial object . The program reads the data
from the serial port only when a new by te is available. The
available()
method checks to see if a new by te is ready and
returns the number of by tes available. This program is written
191




so that a single new by te will be read each time through
draw()
.
The
map()
function converts the incoming value from its initial
range from 0 to 255 to a range from 0 to the height of the
screen; in this program, it†s from 0 to 220.
Example 13-8: Visualizing the Data
Stream
Now that the data is coming through, we†ll visualize it in a more
interesting format . The values coming in directly from a sensor
are often erratic, and it†s useful to smooth them out by averag-
ing them. Here, we present the raw signal from the light sensor
illustrated in the top half of the example and the smoothed sig-
nal in the bottom half:
add_library(
†serial†
)
port


=


None


# for Serial object
val


=


0.0






# Data received from the serial port
x


=


0
easing


=


0.05
easedVal


=


0.0
def


setup
():




global


port




size
(440,


440)




frameRate
(30)




arduinoPort


=


Serial
.
list
()[0]




port


=


Serial(this,


arduinoPort,


9600)




background
(0)
def


draw
():








global


x,


val,


easedVal




if


port
.
available()


>


0:












# If data is available,








val


=


port
.
read()






















# read it and store it in val








val


=


map
(val,


0,


255,


0,


height
)


# Convert the values




targetVal


=


val;




easedVal


+=


(targetVal


-


easedVal)


*


easing




stroke
(0)




line
(x,


0,


x,


height
)
























# Black line




stroke
(255)




line
(x
+
1,


0,


x
+
1,


height
)
















# White line




line
(x,


220,


x,


val)


























# Raw value




line
(x,


440,


x,


easedVal


+


220)




# Averaged value




x


+=


1




if


x


>


width
:








x


=


0
Similar to
Example 5-8  on page 52
and
Example 5-9  on page 53
,
this sketch uses the easing technique. Each new by te from the
Arduino board is set as the target value, the
di‚erence
between
the current value and the target value is calculated, and the cur-
rent value is moved closer to the target . Adjust the
easing
vari-
able to
a‚ect
the amount of smoothing applied to the incoming
values.
Example 13-9: Another Way to Look
at the Data
This example is inspired by radar display screens. The values
are read in the same way from the Arduino board, but they are
visualized in a circular pattern using the
sin()
and
cos()
func-
tions introduced earlier in
Example 8-12 on page 111
to
Example
8-15 on page 113
:
193




add_library(
†serial†
)
port


=


None




# Serial class object
val


=


0.0








# Data received from the serial port
angle


=


0.0
radius


=


0.0
def


setup
():




global


port




size
(440,


440)




frameRate
(30)




strokeWeight
(2)




arduinoPort


=


Serial
.
list
()[0]




port


=


Serial(this,


arduinoPort,


9600)




background
(0)
def


draw
():




global


val,


angle,


radius




if


port
.
available()


>


0:




# If data is available,








val


=


port
.
read()














# read it and store it in val








# Convert the values to set the radius








radius


=


map
(val,


0,


255,


0,


height


*


0.45)




middleX


=


width
/
2




middleY


=


height
/
2




x


=


middleX


+


cos
(angle)


*


height
/
2




y


=


middleY


+


sin
(angle)


*


height
/
2




stroke
(0)




line
(middleX,


middleY,


x,


y)




x


=


middleX


+


cos
(angle)


*


radius




y


=


middleY


+


sin
(angle)


*


radius








stroke
(255)




line
(middleX,


middleY,


x,


y)




angle


+=


0.01
The
angle
variable is updated continuously to move the line
drawing the current value around the circle, and the
val
variable
scales the length of the moving line to set its distance from the
center of the screen. After one time around the circle, the values
begin to write on top of the previous data.
We†re excited about the potential of using Processing and Ardu-
ino together to bridge the world of software and electronics.
Unlike the examples printed here, the communication can be
bidirectional. Elements on screen can also
a‚ect
what†s happen-
ing on the Arduino board. This means you can use a Processing
program as an interface between your computer and motors,
speakers, lights, cameras, sensors, and almost any thing else
that can be controlled with an electrical signal. Again, check out
http://www.arduino.cc
for more information about Arduino.
195











## Exercícios

1. **Trabalhando com Arrays**:
   - Crie um array de números e use um laço para calcular a soma.
   - Desenvolva um esboço que armazena as posições de várias formas em um array.

2. **Usando Dicionários**:
   - Escreva um programa que usa um dicionário para mapear chaves a valores.
   - Implemente uma tabela de consulta simples usando um dicionário.

3. **Gestão de Dados**:
   - Combine arrays e dicionários para gerenciar conjuntos de dados mais complexos.
   - Desenvolva um esboço que carrega dados de um arquivo e os processa em arrays ou dicionários.

4. **Manipulação Avançada de Dados**:
   - Crie um programa que atualiza dinamicamente arrays ou dicionários com base na entrada do usuário.
   - Implemente uma visualização de dados que muda à medida que novos dados são adicionados.
