#!/usr/bin/env python

def FizzBuzz_Ext(num, d): # d for dictionary
    ''' An extensible solution to FizzBuzz. '''
    verbosity = ""
    if num % 3 == 0: 
        verbosity += "Fizz"
    if num % 5 == 0: 
        verbosity += "Buzz"
    for entry in filter(lambda e: isinstance(e, int) and isinstance(d[e], str) and num % e == 0 and e != 3 and e != 5, d): # FizzBuzz is law
        verbosity += d[entry]
    if len(verbosity) == 0:
        return str(num)
    else:				
        return verbosity

#TEST
#smiles = {3: 'Fizz', 5: 'Buzz', 4: 'Crackle', 7: 'Sivv', 9: 'Pop', 'uhoh': 6}

#print "\033[1m1-9:\033[0m"
#for i in range(1, 10):
#    print FizzBuzz_Ext(i, smiles)

#print "\033[1m3600-3800:\033[0m" 
#for i in range(3600, 3801): # look out for 3780
#    print FizzBuzz_Ext(i, smiles)
