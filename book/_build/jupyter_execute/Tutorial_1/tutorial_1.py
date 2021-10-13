#!/usr/bin/env python
# coding: utf-8

# # Tutorial 1
# 
# ## Question 1
# A time `t` in seconds can be converted to days, hours, minutes and seconds using integer division:
# 
# 1. Divide `t` by 60; set `t` to the quotient and call the remainder `s`.
# 1. Divide `t` by 60; set `t` to the quotient and call the remainder `m`.
# 1. Divide `t` by 24; set `d` to the quotient and call the remainder `h`.
# 
# Calculate the number of days, hours, minutes and seconds in one million seconds. Display the result as follows:
# ```
# 1000000 seconds is xx days H:M:S
# ```

# In[ ]:





# ## Question 2
# 
# Iodine-131 is a radioisotope with a half-life $t_\mathrm{half} = 8.02$ days.
# 
# 1. Use the equation $r = \left(\frac{1}{2}\right) ^ {1/t_\mathrm{half}}$ to calculate the daily decay rate (i.e. the proportion of a sample of Iodine 131 that decays in one day).
# 1. A sample of radioactive material containing Iodine-131 has an activity of $1.67 \times 10^{12}$ Becquerels. Write a program which calculates the number of days it takes for the sample to reach an activity of $10000$ Becquerels.
# 1. Print the activity of the sample once every 7 days.

# In[ ]:





# ## Question 3
# 
# We can calculate how many digits there are in a number by repeatedly dividing by 10 until the number is less than one.
# 
# 1. Write peudo-code for this calculation.
# 1. Write a Python program to implement it, displaying the result in the format `1234 has 4 digits.`
# 1. Test your program with a variety of numbers.
# 1. Extend your program so that it works for negative numbers.
# 

# In[ ]:





# ## Question 4 (The Collatz Problem)
# 
# Given a positive integer `n`, the Collatz Operation is defined as follows:
#     
#  - If the number is even, divide it by two
#  - If the number is odd, triple it and add one
#  
# Repeatedly applying the Collatz Operation results in a sequence of integers which eventually reaches the number 1.
# 
# > Write a program which generates the Collatz Sequence for a given positive integer $n$. 
# 
# For example, if $n = 5$ then your program should produce the following:
# 
# ```
# 5
# 16
# 8
# 4
# 2
# 1
# ```
# 
# Given a positive integer $n$, define the Collatz Number to be the length of the Collatz Sequence for $n$. For example, the Collatz number of 5 is 6.
# 
# > Write a program which calculates and prints the Collatz number of a given number $n$. For example, if $n=5$ your program should print `The Collatz number of 5 is 6`.
# 
# > Write a program which finds the smallest number $n$ whose Collatz Number is greater than 200.
# 

# In[ ]:





# In[ ]:




