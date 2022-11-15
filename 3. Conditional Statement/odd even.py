Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
... A number is entered by User. Write a program to check whether
... number is even or odd number.
... 
... even: The number which is completely divisible by 2.
...       Since it is completely division its remainder of
...       the division is Zero.
...       opertor:%
... step1:start
... step2:message to user.=> print()
... step3:store that input in variable.=>input()
... step4:calculate remainder
... step5:if remainder is equal to 0 then it is even
... step6:if remainder is not equal to 0 then it is odd..
... step7:stop
... '''
'\nA number is entered by User. Write a program to check whether\nnumber is even or odd number.\n\neven: The number which is completely divisible by 2.\n      Since it is completely division its remainder of\n      the division is Zero.\n      opertor:%\nstep1:start\nstep2:message to user.=> print()\nstep3:store that input in variable.=>input()\nstep4:calculate remainder\nstep5:if remainder is equal to 0 then it is even\nstep6:if remainder is not equal to 0 then it is odd..\nstep7:stop\n'
>>> print ("Enter number:")
Enter number:
>>> n=int(input())
r=n%2
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    n=int(input())
ValueError: invalid literal for int() with base 10: 'r=n%2'
>>> if r==0:
...     print("Even Number")
... else:
