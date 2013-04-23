'''
Pyroject-euler v. 0.0 by Doc
http://filippo.giomi.it
'''

import math

'''
isPrime(int n)
Return true if n is a prime number
e.g.
>>> isPrime(5)
True
>>> isPrime(4)
False
'''
def isPrime(n):
    i=3
    limit=math.sqrt(n)
    if (n==2) | (n==3):
        return True
    if (n<2) | (n%2==0) | (n%3==0):
        return False
    while (i<=limit):
        if n%i==0:
            return False
        i+=2
    return True

'''
primeList(int n)
Return a list of prime numbers <=n
e.g.
>>> primeList(20)
[2, 3, 5, 7, 11, 13, 17, 19]
'''
def primeList(limit):
    import math
    n=3
    l = [2,]
    while len(l)<=limit:
        for x in l[:int(math.sqrt(len(l)))]:
            if not(n%x): break
        else: l.append(n)
        n+=2
    return l

'''
factorize(int n)
Return a list with factorization of n
e.g.
>>> factorize(20)
[2, 2, 5]
'''
def factorize(n):
    i=1
    l=[]
    while not n==1:
        if isPrime(i) &(n%i==0):
            n/=i
            l.append(i)
            i=0
        i+=1
    return l

'''
isPalindrome(int n)
Return True if n is palindome
e.g.
>>> isPalindrome(1234321)
True
'''
def isPalindrome(n):
	r=False
	if (len(str(n))%2==0):
            if str(n)[:len(str(n))/2]==str(n)[len(str(n))/2:][::-1]:
                r=True
        else:
            if str(n)[(len(str(n))+1)/2:]==str(n)[:len(str(n))/2][::-1]:
                r=True
	return r
