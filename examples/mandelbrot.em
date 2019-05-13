Jump 15
50 //Divisions
1 //One
100 //One Hundred
0 //Current Division
0 //Current Lines

32 //Space
77 //M
10 //NewLine

Done

//Main Loop
Load 5
Sub 2
JumpIfZero 31 //NewLine
Load 6
Sub 2
JumpIfPos 12 //Done
Load 5
Add 3 //One
Store 5
Load 46 //Real
Add 48 //Increment
Store 46 //Real
Jump 58 //Algo


//NewLine Code
Load 10
APrint
Set 0
Store 5
Load 6
Add 3 //One
Store 6
Load 47 //Imaginary
Sub 48 //Increment
Store 47 //Imaginary
Set -200
Store 46 //Real
Jump 15 //Back to Loop


-200 //Real
200 //Imaginary
8 //Increment
200 //Max steps
400 //Out of bounds

//Main algo
0 //Steps
0 //r
0 //i
0 //Temp

Load 53 //Steps
Sub 49 //Max steps
JumpIfZero 95 //NotInSet
Load 53 //Steps
Add 3 //One
Store 53 //Steps
Load 55 //i
Mult 55 //i
Div 4 //OneHundred
Store 56 //Temp
Load 54 //r
Mult 54 //r
Div 4 //OneHundred
Add 46 //Real
Store 56 //Temp
Set 2
Mult 54 //r
Mult 55 //i
Div 4 //OneHundred
Add 47 //Imaginary
Store 55 //i
Load 56 //Temp
Store 54 //r
Load 54 //r
Mult 54 //r
Div 4 //OneHundred
Store 56 //Temp
Load 55 //i
Mult 55 //i
Div 4 //OneHundred
Add 56 //Temp
Sub 50 //Out of bounds
JumpIfNeg 58 //Loop
Load 9 //InSet
APrint
Jump 100 //To Reset Code

Load 8 //NotInSet
APrint
Jump 100 //To Reset Code

//Reset Code
Set 0
Store 53
Store 54
Store 55
Store 56
Jump 15 //Back