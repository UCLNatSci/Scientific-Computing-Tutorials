#!/usr/bin/env python
# coding: utf-8

# # Tutorial 2
# 
# ## Practice Questions

# [Turtle Graphics](https://en.wikipedia.org/wiki/Turtle_graphics) is a graphical computer language often used to introduce programming to beginners. The user controls an on-screen turtle by sending commands such as 'forward 50' and 'rotate 90'. The turtle follows the commands in sequence, drawing a line as it moves.
# 
# The code below implements a Turtle program in Python.
# 
# ```
# import matplotlib.pyplot as plt
# import numpy as np
# 
# # function definitions
# 
# def start():
#     state[0] = 0
#     state[1] = 0
#     state[2] = 0
#     
#     plt.figure(figsize=(5,5))
#     plt.xlim(-2, 2)
#     plt.ylim(-2, 2) 
# 
# def draw_forward(dis):
#     x = state[0]
#     y = state[1]
#     angle = state[2]
#     state[0] = x + dis * np.cos(angle)
#     state[1] = y + dis * np.sin(angle)
#     plt.plot([x, state[0]], [y, state[1]], color="black", linewidth=2)
#     
# def rotate_left(theta):
#     state[2] = state[2] + theta * np.pi / 180
#     
# state = [0, 0, 0]
# 
# # Turtle instructions
#     
# start()
# move_forward(2)
# rotate_left(90)
# move_forward(2)
# ```
# 
# `start` is a function which creates a new drawing surface and moves the turtle back to the origin.
# 
# `draw_forward` is a function which updates the x and y co-ordinates and draws a line between the old and new co-ordinates.
# 
# `rotate_left` is a function which updates the angle by `theta` degrees.
# 
# `state` is a list containing the current x co-ordinate, y co-ordinate and angle of the turtle in radians.
# 
# ### Question 1
# 
# Complete the turtle instructions code so that it draws a square. Then, write a function `draw_square` which draws a square (put your function definitions near the top of the code file, underneath `# function definitions`.)
# 
# ```
# # draw a square
# draw_square()
# ```
# ![](images/square.png")
# 
# ### Question 2
# 
# Write a function `draw_polygon(n, dis)` which draws an n-sided polygon with side length `dis`. Use it to draw a hexagon with side-length 1.
# 
# ```
# # draw a hexagon
# draw_polygon(6, 1)
# ```
# 
# ![](images/hexagon.png)
# 
# ### Question 3
# 
# Write a function `draw_rotated_polygons(n, m)` which draws a pattern like below.
# 
# ```
# # Draw 5 rotated squares
# draw_rotated_polygons(4, 5)
# ```
# 
# ![](images/rotated_polygon.png)
# 

# ### Question 4
# 
# Copy the three function definitions `get_number_of_day`, `get_day_of_week` and `print_day_of_week_from_number_of_year` from the notes. Correct the code so that it prints the day of the week correctly.

# In[ ]:





# ### Question 5
# 
# Write a program which prints a multiplication table, like this:
# ```
#  1  2  3  4  5  6  7  8  9 10
#  2  4  6  8 10 12 14 16 18 20
#  3  6  9 12 15 18 21 24 27 30
# ...
# 10 20 30 40 50 60 70 80 90 100
# ```
# 
# You will need to use two nested loops.

# In[ ]:





# ## Tutorial Questions

# ### Question 1
# In this question you will write a function `nth_digit(n, num)` which returns the `n`th digit of the number `num`.
# 
# ### Step 1
# 
# Write a function `count_digits`. `count_digits(num)` calculates the number of digits in the integer `num`. `countDigits` should return `1` for `0–9`, `2` for `10–99`, `3` for `100–999`, etc.  
# **Hint**: Use a while loop to repeatedly divide `num` by `10` until it is less than 1.
# 
# ### Step 2
# 
# Write a function `nthDigitBack`. `nthDigitBack(n, num)` finds the nth lowest order digit in `num`, i.e., the nth digit from the right. We take the rightmost digit to be the 0th digit. `nthDigitBack` should evaluate to `0` for digits beyond the "start" of the number.  
# **Hint**: use a `for` loop to repeatedly divide by 10, followed by the modulo (`%`) operator and the `round` function to pick out just the rightmost digit. 
# For example:
# ```
# nth_digit_back(0,123)
# 3
# nth_digit_back(1,123)
# 2
# nth_digit_back(2,123)
# 1
# nth_digit_back(3,123)
# 0
# nth_digit_back(0,0)
# 0
# nth_digit_back(3,18023)
# 8
# ```
# 
# ### Step 3
# 
# Write a function `nth_digit`, using `nth_digit_back` and `count_digits`. `nth_digit(n, num)` finds the nth highest order digit of `num`, i.e., the nth digit from the left. We take the leftmost digit to be the 0th. `nth_digit` should evaluate to 0 for digits beyond the "end" of the number. For example:
# ```
# nth_digit(0,123)
# 1
# nth_digit(1,123)
# 2
# nth_digit(2,123)
# 3
# nth_digit(3,123)
# 0
# nth_digit(0,0)
# 0
# nth_digit(3,18023)
# 2
# ```
# 
# 

# 
# 

# In[ ]:




