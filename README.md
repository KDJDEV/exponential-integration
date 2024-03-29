# Simple Euler integration approximation of exponential functions

The fun fact shown in this code is that the natural logarithm of the base of an exponential function times the values of that exponential function equals the rate of change of that function with respect to the input.
I find this fact rather nice, as it shows part of the importance of the natural logarithm and how it can give you the rate of change of any exponential function.

In this code, I simply used Euler integration to approximate values of the exponential function based on the rate of change given by the product of the natural logarithm and the function.

The fun thing is that the base (which is the number 2 currently) isn't actually used in this computation of the powers of 2 after we compute the natural logarithm on line 10.