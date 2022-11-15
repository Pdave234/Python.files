
'''
Write a program to check whether character entered by
user is vowel or consonant.

vowels=> a,e,i,o,u,A,E,I,O,U
consonants: Other than vowels are consonants.

'''

ch=input("Enter a Character:")#a,q,T
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
    print("Its a vowel")
else:
    print("Its a Consonant")
    
'''
Write a program to check whether character entered by
user is vowel or consonant.

vowels=> a,e,i,o,u,A,E,I,O,U
consonants: Other than vowels are consonants.

in and not in are called as membership operators.
'''

ch=input("Enter Character:")
if ch in('a','e','i','o','u','A','E','I','O','U'):
    print("Its a vowel")
else:
    print("Its a Consonant")
