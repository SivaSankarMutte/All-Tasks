import math
class Calci:
    def add(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        return n1-n2
    def mul(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):  #Exact division 5/2=2.5
        return n1/n2
    def exp(self,n1):
        return math.exp(n1)
    def fdiv(self,n1,n2):  #floor division 5/2=2
        return n1//n2
    def mod(self,n1,n2):
        return n1%n2
    def remainder(self,n1,n2):
        return n1%n2
    
class MyMath:
    def isEven(num):
        if(num%2==0):
            return True 
        return False
    def isOdd(num):
        if(num%2!=0):
            return True
        return False
    
    def isPrime(num):
        for i in range(2,num):
            if(num%i==0):
                return False
        return True