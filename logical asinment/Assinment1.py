Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.



Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.



Answer:-

 round() :- function float point number from the decimal value to the closest multiple of 10.
            The int value to the closest multiple of 10 to the power minus ndigits, where ndigits is the
            precision after the decimal point. If two multiples are equally close, rounding is done toward the even choice.


 abs()   :- Function returns the absolute (non-negative value) value of a number. For example, absolute value of -5 is 5 
            and absolute of 5 is also 5. In this guide, we will see how to use abs() function in Python with the help of examples.


Code:-

round() :-


print(round(15))
 
# for floating point
print(round(51.6))
print(round(51.5))
print(round(51.4))



abs():-

float = -54.26
print('Absolute value of float is:', abs(float))
 
# An integer
int = -94
print('Absolute value of integer is:', abs(int))
 
# A complex number
complex = (3 - 4j)
print('Absolute value or Magnitude of complex is:', abs(complex)