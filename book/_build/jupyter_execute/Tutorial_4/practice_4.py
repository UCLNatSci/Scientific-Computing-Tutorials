#!/usr/bin/env python
# coding: utf-8

# # Practice 4

# ## Question 1
# 
# Write a Python script which loops over the characters in a string and prints the three character substring starting at each character:
# 
# ```
# s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ...
# ```
# Output:
# ```
# ABC
# BCD
# CDE
# ...
# XYZ
# ```
# 
# ## Question 2
# 
# Write a program which loops over the characters of a string **three at a time** and prints each three character substring. If the number of characters is not divisible by three, ignore the trailing characters.
# 
# ```
# s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ...
# ```
# Output:
# ```
# ABC
# DEF
# GHI
# ...
# VWX
# ```
# 
# ## Question 3
# 
# Write a program which loops over the characters of `s` three at a time, in the same manner as question 2. Use `string_list.index` to find the position of each 3-character string in `string_list`, then print the character in the equivalent position in `character_list`. 
# 
# ```
# s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# string_list = ["MNO", "DEF", "VWX", "JKL", "PQR", "ABC", "STU", "GHI"]
# character_list = ["N", "C", "!", "E", "C", "S", "E", "I"]
# ...
# ```
# output:
# ```
# S
# C
# I
# E
# N
# C
# E
# !
# ```

# ## Question 4
# 
# What image does the data in the string `shape_data` represent?
# The  string contains a sequence of x and y co-ordinates where each x, y pair is separated by a semi-colon. Extract the co-ordinates into two separate lists `x_coords` and `y-coords` then plot them on a scatter plot.
# 
# - use `string.split` to generate a list of co-ordinate pairs
# - loop over the list and split each pair into x and y co-ordinates
# - convert each to a number and add to lists `x_coords` and `y_coords`
# - plot using `plt.scatter(x_coords, y_coords)`
# 
# Adapt your code so that it plots the image the correct way up in a figure of  suitable size.

# In[1]:


shape_data = "13,1; 14,1; 15,1; 16,1; 17,1; 18,1; 12,2; 14,2; 15,2; 16,2; 17,2; 18,2; 19,2; 11,3; 12,3; 14,3; 15,3; 16,3; 17,3; 18,3; 19,3; 20,3; 10,4; 16,4; 17,4; 18,4; 19,4; 20,4; 10,5; 17,5; 18,5; 19,5; 20,5; 21,5; 17,6; 18,6; 19,6; 20,6; 21,6; 9,7; 18,7; 19,7; 20,7; 21,7; 9,8; 18,8; 19,8; 20,8; 21,8; 9,9; 10,9; 12,9; 14,9; 16,9; 17,9; 18,9; 19,9; 20,9; 21,9; 9,10; 16,10; 18,10; 19,10; 20,10; 21,10; 9,11; 18,11; 19,11; 20,11; 21,11; 22,11; 9,12; 18,12; 19,12; 20,12; 21,12; 22,12; 8,13; 9,13; 10,13; 14,13; 17,13; 18,13; 19,13; 20,13; 21,13; 22,13; 8,14; 9,14; 10,14; 13,14; 17,14; 18,14; 19,14; 20,14; 21,14; 22,14; 8,15; 9,15; 10,15; 13,15; 14,15; 17,15; 18,15; 19,15; 20,15; 21,15; 22,15; 8,16; 9,16; 10,16; 11,16; 16,16; 17,16; 18,16; 19,16; 20,16; 21,16; 22,16; 8,17; 9,17; 10,17; 11,17; 15,17; 16,17; 17,17; 18,17; 19,17; 20,17; 21,17; 22,17; 8,18; 9,18; 10,18; 11,18; 12,18; 14,18; 15,18; 16,18; 17,18; 18,18; 19,18; 20,18; 21,18; 22,18; 9,19; 10,19; 11,19; 12,19; 13,19; 14,19; 15,19; 16,19; 17,19; 18,19; 19,19; 20,19; 21,19; 22,19; 9,20; 10,20; 11,20; 12,20; 13,20; 15,20; 16,20; 17,20; 19,20; 20,20; 21,20; 22,20; 23,20; 10,21; 11,21; 12,21; 13,21; 19,21; 20,21; 21,21; 22,21; 23,21; 20,22; 21,22; 22,22; 23,22; 9,23; 10,23; 20,23; 21,23; 22,23; 23,23; 24,23; 8,24; 9,24; 10,24; 20,24; 21,24; 22,24; 23,24; 24,24; 25,24; 8,25; 9,25; 10,25; 20,25; 21,25; 22,25; 23,25; 25,25; 26,25; 7,26; 8,26; 9,26; 20,26; 21,26; 25,26; 26,26; 27,26; 6,27; 7,27; 8,27; 19,27; 24,27; 25,27; 26,27; 27,27; 28,27; 5,28; 6,28; 7,28; 8,28; 22,28; 23,28; 24,28; 25,28; 26,28; 27,28; 28,28; 29,28; 5,29; 6,29; 7,29; 8,29; 9,29; 20,29; 21,29; 22,29; 23,29; 24,29; 25,29; 26,29; 27,29; 28,29; 29,29; 4,30; 5,30; 6,30; 7,30; 8,30; 9,30; 10,30; 11,30; 12,30; 19,30; 20,30; 21,30; 22,30; 23,30; 24,30; 25,30; 26,30; 27,30; 28,30; 29,30; 3,31; 4,31; 5,31; 6,31; 7,31; 8,31; 9,31; 10,31; 11,31; 12,31; 13,31; 14,31; 15,31; 16,31; 17,31; 18,31; 19,31; 20,31; 21,31; 22,31; 23,31; 24,31; 25,31; 26,31; 27,31; 28,31; 29,31; 30,31;"

