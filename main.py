# This function gets a number and a list and gives a boolean, whether that number is prime to that list or not 
# This function is needed on getprime(): line 13
def isprime(num,parent) :
     for i in parent:
         if  num % i == 0 :
             return False
     return True

# This function gets a number and gives a list maintaining all prime numbers smaller than that number
def getprimes(n) :
    primes=[2]
    for num in range(3,n,2) :
        if isprime(num,primes):
            primes.append(num)
    return primes    

# Console Part
number = input("Type a number to get prime numbers to: ")
number = int(number)
print( getprimes(number) )
