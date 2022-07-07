Dates 
@author Ava Reese

Libraries used:
For my dates program I used the library re. Re is a built in package which can be used to work with regular expressions. Specfically I used re.split and re.sub. re.spit allows you to split a string, in terms of my program tp split the input when you see an occurance of the specficed regular expression, so I used it to split whenever their was a <space>, / or -. re.sub seraches for a pattern in the string and replaces it with the matched string. For my program I used re.sub to assign it to a varible called seperators which allowed me to check against the conditions.

test cases:
I used a wide range of date inputs to test my program. I came up with different date combinations which test against the specifications. 
1 1 1 
1 jan 01
1 jAn 01
123 jan 01
ava jan 01
0 jan 01
12 ava 12
12 12 ava
12 12 123
12 12 12345
12 jan 202
32 jan 2020
29 feb 2020
29 feb 2021
29 feb 2020
1 12 4000
1 12 1700
12 janu 2000
50 jan 22
12 12 dec

These are twenty of the test cases I used to test my program once it had finished however throughout creating my program I used various other test cases to check against the rules.

resources:
The resources I used for creating my program were W3schools, stack overflow, programiz.com and python documentation. I used all these resources to remind me how the flow of execution works in python espeically with multiple if else statments. They also helped me to learn how to use the re library.


running program:
To run my program please unzip my file, and run by typing into the command promt 'python3 datetesting.py' this should bring up a prompt to enter a date. To end my program please hit control d, this should end the program and leave a message in the prompt saying 'Ending program'.

