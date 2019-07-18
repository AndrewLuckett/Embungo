Jump 10

32 //N (Size of image)
0 //Y
0 //i
0 //X

1 //One

Load 3 //N
Store 4 //Y

Load 4 //Y
JumpIfPos 18 //Main
Done


//Main
Load 4 //Y
Sub 8 //One
Store 4 //Y
// Y = Y - 1

Set 0
Store 5 //i
//i = 0

Load 5 //i
Sub 4 //Y
JumpIfNeg 47 //Sub 1

Set 0
Store 6 //X
//X = 0

Load 6 //X
Add 4 //Y
Sub 3 //N
JumpIfNeg 65 //Sub 2

Set 10
APrint //Print newline

Jump 13


//Sub 1
Set 32
APrint //Print(" ")

Load 5
Add 8
Store 5 //i += 1

Jump 28


//Sub 2
//BitWise And (kinda)
0 //a
0 //b
0 //temp
2 //Two

Load 6 //X
Store 60 //a
Load 4 //Y
Store 61 //b

Load 60 //a
JumpIfZero 95 //Print dot
Mod 63 //Two
Store 62 //temp
Load 61 //b
Mod 63 //Two
Add 62 //temp
Sub 63 //two
JumpIfZero 90 //Print spaces

Load 60 //a
Div 63 //Two
Store 60 //a
Load 61 //b
Div 63 //Two
Store 61 //b

Jump 70 //Loop


Set 32
APrint //Print(" ")
APrint //Print(" ")
Jump 100//Forward

Set 42
APrint //Print("*")
Set 32
APrint //Print(" ")

Load 6 //X
Add 8 //One
Store 6 //X += 1

Jump 36