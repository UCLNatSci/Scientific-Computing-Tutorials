#!/usr/bin/env python
# coding: utf-8

# # Tutorial 3

# ## Question 1
# 
# Given a string representing a DNA sequence, we want to print a sequence of nucleotide names:
# ```
# dna_seq = "gttccccaagctcttacataaatgtcgtagggttccagctacgtgttgttgggccaccca"
# ```
# Output:
# ```
# Guanine
# Thymine
# Thymine
# Cytosine
# ...
# ```
# - Create two lists `letters = ["A", "G", "C", "T"]` and `names = ["Adenine", "Guanine", "Cytosine", "Thymine"]`
# - Loop over every character in `dna_seq`. For each character:
#   - Find the index of the character in `letters`
#   - Print the item in the equivalent position in `names`
# 
# **HINT**: First try just for a single letter. E.g. given `nuc = "A"`, print `Adenine`.
# 

# In[ ]:





# ### Question 2
# 
# > TODO: rewrite this
# 
# A cannon located at position `x = 0` fires a cannonball at an angle `theta` from the horizontal (measured in radians) and speed `speed` m/s. Write a program which plots a graph of the cannonball's trajectory.
# 
# ```{image} cannon.jpg
# :width: 200px
# ```
# 
# Set the initial positions `x` and `y` to zero and velocities `vx` and `vy` to `np.cos(theta)` and `np.sin(theta)`. Each time step, update the positions using `x = x + vx * DELTA_T` and `y = y + vy * DELTA_T`. Update the velocity `vy = vy - g * DELTA_T`. The x velocity remains constant.
# Create lists `x_list` and `y_list` to store the x and y positions, appending the new positions at each timestep.
# 
# Repeat until the `y` position becomes negative (what kind of loop should you use for this?). Finally, use `matplotlib` to plot the two lists.
# 
# 
# Extend your program so that it prints `hit` or `miss` depending if the cannonball lands less than 20m from a target placed at a distance `dis` from the cannon.
# 
# ```{image} cannon_output.png
# :width: 200px
# ```
# `hit`

# In[ ]:





# ### Question 3
# 
# Recall the Collatz Operation from the first week:
# 
#  - If `n` is even, divide it by two
#  - If `n` is odd, triple it and add one
#  
# If we repeatedly apply the operation, we get a sequence of integers which terminates at the number 1. We define the 'Collatz number' of an integer $n$ to be the number of iterations in the sequence.
#  
# Write a program which generates a line graph with integers 0 ... 100 on the x-axis, and Collatz number on the y axis.
#  

# In[ ]:




