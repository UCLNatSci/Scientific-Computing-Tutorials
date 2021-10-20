#!/usr/bin/env python
# coding: utf-8

# # Tutorial 2
# 
# ## Question 1
# 
# Use `for` loops and `print(end="")` to write functions which print the following patterns:
# 
# 1. `print_square(n)` where `n` is the number of stars along each edge.
# 
# ```
# *****
# *   *
# *   *
# *   *
# *****
# ```
# 2. `print_rhombus(n)` where `n` is the number of stars along each edge.
# 
# ```
#     *****
#    *   *
#   *   *
#  *   *
# *****
# ```
#  
# 3. `print_numbers(n)` where `n` is the number at the centre.
# 
# ```
# 1       1
#  2     2
#   3   3
#    4 4
#     5
#    4 4
#   3   3
#  2     2
# 1       1
# ```

# In[ ]:





# ## Question 2
# 
# An integer $n$ is a *prime number* if it is divisible only by 1 and $n$. 
# 
# 1. Write a function `is_divisible(n, m)` which returns `True` if `n` is divisible by `m`, and otherwise returns `False`.
# 1. Write a function `is_prime(n)` which returns `False` if `n` is divisible by any integer between `2` and `n-1`, and otherwise returns `True`.
# 1. Write a function `number_of_primes(n)` which returns the number of prime numbers less than or equal to `n` [NB 1 is *not* a prime number].
# 
# Check the correctness of your functions by writing two tests for each.

# In[ ]:





# ## Question 3
# 
# A [solid of revolution](https://en.wikipedia.org/wiki/Solid_of_revolution) is a three-dimensional figure contstructed by rotating a curve about a straight line. We can estimate the volume of a solid of revolution by dividing it into a sequence of stacked discs and summing the volume of each.
# 
# A sphere of radius $R$ is formed by rotating the curve $y = \sqrt{R^2 - x^2}$ around the x-axis between $-R$ and $R$.
# 
# ![a](https://miro.medium.com/max/2400/0*d7QEcno6XhPOiJSt.png)
# 
# Use the following steps to estimate the volume of a sphere of radius 1.
# 
# 1. Write a function `vol_disc(R, x, dx)` which returns the volume of the disc centred at position `x` with thickness `dx`. 
# 1. Estimate the volume of a sphere of radius 1 by dividing the figure into 10 discs equally spaced between `-1` and `1` [use a value of 3.14159 for $\pi$].
# 1. Write a function `sphere_vol(R, n)` which returns the estimate of the volume of a sphere of radius `R` calculated by dividing it into `n` discs.
# 1. The estimate should get more accurate as we increase `n`. We can estimate the accuracy by calculating the difference between `sphere_vol(R, n)` and `sphere_vol(R, n-1)`. For `R = 1`, how large does `n` need to be so that difference between consecutive estimates is less than $10^{-4}$?

# In[ ]:





# ## Extension Questions (Optional)
# 
# These questions are open-ended and designed to allow to you challenge yourself beyond the material we have studied.
# 
# 1. Investgate the [Prime Number Theorem](https://en.wikipedia.org/wiki/Prime_number_theorem).
# 1. Write a function `volume_of_revolution(func, x_min, x_max, n)` which calculates the volume of the surface of revolution of the curve given by function `func`. `func(x)` should be a function of a single variable which returns the y-value of the curve given the x value. You'll have to learn how to [pass a function as an argument to another function](https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/). Test your function by calculating the volume of a sphere,  a paraboloid and another curve of your choice.
# 
# 

# In[ ]:




