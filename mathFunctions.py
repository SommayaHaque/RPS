#Math Programs By Sommaya Haque

def main():
    randInt()
    print()
    quadCalc()
    print()
    factorialCalc()

#randInt: A function that picks a random int and allows you to guess the int
import random
def randInt():
    number= random.randint(1,10)
    count=0
    guess=int(input('Guess the integer: '))
    while guess!=number:
        print('That number is wrong!')
        if guess>number:
            print('That guess is too high!')
        elif guess<number:
            print('That guess is too low!')
        count=count+1
        guess=int(input('Guess the integer: '))
    if guess==number:
        print(number,"is the correct number!")
        print('You took', count, 'tries!')

#quadCalc: A function that calculates using the quadratic formula when coefficients are input
import math
def quadCalc():
    print('Quadratic Formula Calculator!') 
    a= float(input('What is coefficient a? '))
    b= float(input('What is coefficient b? '))
    c= float(input('What is coefficient c? '))
    d= (b**2)-(4*a*c)

    if d<0:
        print ('There are no real roots. \n Have a nice day!')

    if d>0:
        root1= (-b + (math.sqrt((b**2)-(4*a*c))))/(2*a)
        root2= (-b - (math.sqrt(((b**2)-(4*a*c)))))/(2*a)
        print ('The roots are', root1, 'and', root2)

#factorialCalc: Calculates the factorial of the input number
def factorialCalc():
    print('Factorial Calculator!')
    n=int(input('Enter a positive integer: '))
    factorial=1
    print('i\tfactorial')
    for i in range(n,1,-1): #start at 1, end at n, add 1
        factorial= factorial*i #i is every number within INPUT N's range
        print(i,'\t',factorial) 
    print(n, 'factorial is', factorial)



main()
