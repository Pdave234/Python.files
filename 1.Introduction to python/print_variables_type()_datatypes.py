#print value
'''
x=10
print(x)
print("x")
print('x')
print("value of x is:",x)
'''
#Print variables type()
Code editor 
==========
IDLE

I :Integrated
DL:Development
E :Environment


Output function
===============
1)Message to User use print() function.

  ()=>Round brackets are called as Parenthesis.
  
  syntax:
  ======
  print("type message here")
  
  e.g
  
  python file                          output screen|console
  
  
  print("Hello all") --------------->  Hello all
  print('This is first program')---->  This is first program.


2)print value of a variable on output.

variables
========
  1) Variables are used to store values.
  2) variable are temporary memory location on RAM.
  3) value in the variables remains till program is running.
  4) Once program is completed or finished memory allocated 
     to the variable along with its value is relased for 
	 future use.
	 
	 
	 x=10
	 
	 10 is data
	 x is variable used to store data.
	 
	 x1=90
	 rno_12=78
	 _x=34
	 
	 rno 12=78 => Invalid 
	 rno@12=67 => invalid only _ is allowed.
	 

Data type of variable 
====================
The value stored in the variable is called as Data.

Basic Data types 
================
1) Number
2) String
3) Boolean

1) Number 
   a) Integer: Complete number or whole number [No Fraction]
   
      e.g:1,2,100,-45,67,89,1000 etc.[Both positive and negative]
	  
   b) float: Whole number as well as frational value 
      e.g: 1.5,-89.78,67.00
	  
2) String: collection of character.

   single line string 
   
   'Hello world'
   "itvedant"
   "itvedant123"
   'itvedant123@'
   "12345"
   '12.56'
   
   "12345" => String       12345=> Number (int)
   '12.56' => String       12.56=> Number (float)
   
3) Boolean 
   1) True 
   2) False 
   
type(): This function is used to show data type of the 
        variable.
		Data type of the variable depends on type of 
		value assigned to that variable.
		
		

		
		
		syntax:
		type(variable_name)
		
		
x=10
x=10.5
x="10.5"


2) Print value of variable.
   ========================

syntax:
print(variablename)

e.g

code editor              console
x=10
print(x)---------------> 10


3)Message + value

syntax:

print("Message",variable) 

e.g
x=10
print("value of x is:",x)



comments in Python 
==================
Comments are unexecutable part of the program.
They are ignored during execution.
They help developer to know the explaination about the
functionality of a code in the application. 

Two types of comments in python 
===============================
1) single line comment 
   # code written after has is commented or unexecutable or ignore.
2) Multi line comment 
   
   This is first  instrction   
   This is second instrction   
   This is Third  instrction   
   This is fourth instrction 

   '''
      setion of code between triple quote open  and 
	  triple quote close is commented or unexecutable or
	  ignored.
   '''
