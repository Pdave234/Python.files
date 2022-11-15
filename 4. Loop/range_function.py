'''
range():This function generate list of numbers in a sequence.
syntax:

     range(start,stop,step)

     start=> initialization
     stop => conditon
     step => increment/decrement [positive or negative]
     
'''
'''
x=list(range(1,15,1)) #start=1,stop=10 and step=1 [increment in step]
print(x)
'''

'''
#int(input())
x=list(range(2,20,2))#postive number
print(x)
'''

'''
#int(input())
x=list(range(20,2,-2))#negative number
print(x)
'''

'''
#int(input())
x=list(range(2,20))#default step is 1
print(x)
'''
#No step and start
'''
#int(input())
x=list(range(20))#default step is 0
print(x)
'''

'''
#int(input())
x=list(range())#error as range() require at least one argument
print(x)
'''
