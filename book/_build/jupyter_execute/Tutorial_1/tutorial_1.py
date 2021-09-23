#!/usr/bin/env python
# coding: utf-8

# # Tutorial 1

# ## Practice Questions
# 
# ### Question 1
# 
# Write a program which use the quadratic formula to print the solution to the quadratic equation $ax^2 + bx + c = 0$, given variables `a`, `b`, and `c`. Your program should print:
# 
# ```
# The solutions are x = 4 and x = 1
# ```
# or
# ```
# The solution is x = 1
# ```
# or
# ```
# There are no real solutions
# ```
# (Hint: first calculate the discriminant $b^2-4ac$).
# 

# In[ ]:





# ### Question 2
# 
# Write a program which prints how many digits the integer `num` has. Assume that `num` is positive and less than 1 million. Store the number of digits in the variable `d` and print the result as:
# 
# ```
# 62463 has 5 digits
# ```
# 
# Hint: Use `if...elif` to check whether the number is < 10, < 100 and so on.
# 
# Extend your answer to negative integers by multiplying by -1 if `num` is negative.

# ### Question 3
# 
# > TODO

# ## Tutorial Questions
# 
# ### Question 1
# A time `t` in seconds can be converted to days, hours, minutes and seconds using integer division:
# 
# 1. Divide `t` by 60; set `t` to the quotient and call the remainder `s`.
# 1. Divide `t` by 60; set `t` to the quotient and call the remainder `m`.
# 1. Divide `t` by 24; set `d` to the quotient and call the remainder `h`.
# 
# Calculate the number of days, hours, minutes and seconds in one million seconds. Display the result as follows:
# 
#     1000000 seconds is xx days H:M:S
# 

# In[ ]:





# ### Question 2 (The Collatz Problem)
# 
# Given a positive integer `n`, consider the following operation:
#     
#  - If the number is even, divide it by two
#  - If the number is odd, triple it and add one
#     
# Write a program which starting with a number `n`, repeatedly applies the above operation until the value of `n` reaches 1.
# 
# For example, if `n = 5` then your program should produce the following:
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
# Now try your program with negative values of `n`. What happens? Explain why.

# In[ ]:





# ### Question 3
# 
# The following algorithm can be used to count the number of digits in a number:
# 
# - *Set counter to 0*  
# - *Repeat the following steps while the number is greater than 1*:
#   - *increase counter value by 1*
#   - *divide the number by 10*
# - *print the final counter value*
# 
# Use a `while` loop to count the number of digits in `x = 9999`, then test your code with `x = 10`, `x = 9.9` and `x = 4356633`

# In[ ]:




