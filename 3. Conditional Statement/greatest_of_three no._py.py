'''
Greatest of the three number entered by user.


a=int(input("Enter first Number:")) #70,70
b=int(input("Enter first Number:")) #50,50
c=int(input("Enter first Number:")) #20,100

if a>b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")
else:
    if b>c:
        print(b,"is greater")
    else:
        print(c,"is greater")

'''        
'''
Greatest of the three number using logical no.
'''

a=int(input("Enter first Number:")) #70,70
b=int(input("Enter first Number:")) #50,50
c=int(input("Enter first Number:")) #20,100

if a>b and a>c:
    print(a,"is greater")
else:
    if b>a and b>c:
         print(b,"is greater")
    else:
        if c>a and c>b:
           print(c,"is greater")

'''
In user input of a=70,b=50,c=20
First if condition is evaluated to be True and we
got the result of greatest of three numbers.

If we got the result in first if condition, then
ideally there is no need to check further if conditions.
Since in above program its checking other two condition,
there is waster of interpreter time in code execution
which is not  going to give us output.

'''

'''
Greatest of the three number using elif.
'''

a=int(input("Enter first Number:")) #70,70
b=int(input("Enter first Number:")) #50,50
c=int(input("Enter first Number:")) #20,100

if a>b and a>c:
    print(a,"is greater")
    
elif b>a and b>c:
     print(b,"is greater")

elif c>a and c>b:
    print(c,"is greater")

