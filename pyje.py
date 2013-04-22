import math
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
