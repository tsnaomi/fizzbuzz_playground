#!/usr/bin/env python

def FizzBuzz(num):
    ''' A method that takes one number as an argument. For multiples of three, it returns Fizz, and for multiples of five, it returns Buzz. For numbers which are multiples of both three and five, it returns FizzBuzz. In all other cases, it returns the number. '''
    if num % (3 * 5) == 0: 
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0: 
        return "Buzz"
    else:
        return str(num)

#TEST
#for i in range(1,101):
#    print FizzBuzz(i)
