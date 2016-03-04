#!/usr/bin/env python
def fizzbuzz(n):
    
    if n % 2==0 and n % 3==0:
        return "FizzBuzz!"
    if n % 2 == 0:
        return "Fizz"
    if n % 2 != 0 and n % 3==0:
        return "Buzz"
    if n % 2 != 0 and n % 3 != 0:
        return n
        

o=raw_input("PLease enter a number")
o=int(o)
o=o+1
o=range(o)

for i in o[1:]:
    print fizzbuzz(i)
exit()
