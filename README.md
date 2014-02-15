fizzbuzz_playgroud
==================

Where the fizzbuzz play.
------------------

Re. the extensible solution:

Fizzbuzz_ext.py takes two argumets: a number (the dividend) and a dictionary (presumably, pairings of divisors and onomatopoeia). 

The function begins with an empty string called "verbosity". If the number is divisible by 3, "fizz" is appended to verbosity. Then, if the number is divisible by 5, "buzz" is appended to verbosity. 

Next, on lines 10-11, a lambda filters through the dictionary entries; if the number is divisible by an entry's key, that entry's value is appended to verbosity. The filter ignores any entries that are not of types dict[int] = str. The filter also ignores any entries whose keys are 3 or 5, which are reserved for "fizz" and "buzz". #fizzbuzzislaw

Finally, after all of this math takes place, if verbosity is still an empty string, the function prints the number. Otherwise, the function prints the onomatopoetic verbosity. Done! 


Thank you to Luke P. for adivising me to use a dictionary as the second parameter! Also, I borrowed the term onomatopoeia from his solution :D
