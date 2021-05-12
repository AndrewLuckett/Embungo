Jump 10

27 //N (Size of image)
0 //X
0 //Y

1 //One
3 //Three

Load 5 //Y
Sub 3 //N
JumpIfNeg 35 //Algo
Done


Load 4 //X
Add 7 //One
Store 4 //X

Sub 3 //N
JumpIfNeg 10 //Loop
Load 5 //Y
Add 7 //One
Store 5 //Y
Set 0
Store 4
Set 10
APrint
Jump 10

//Is in set
0 //a
0 //b

Load 4 //X
Store 32 //a
Load 5 //Y
Store 33 //b

Load 32 //a
Mod 8 //Three
Sub 7 //One
JumpIfZero 46//Onto
Jump 51 //Over

Load 33 //b
Mod 8 //Three
Sub 7 //One
JumpIfZero 69 //Print gap

Load 32 //a
Div 8 //Three
Store 32 //a
Load 33 //b
Div 8 //Three
Store 33 //b

JumpIfZero 61
Jump 40 //Loop

Load 32 //a
JumpIfZero 65 //Print dot
Jump 40 //Loop

Set 88
APrint
Jump 16

Set 32
APrint
Jump 16