#!/usr/bin/env python
# coding: utf-8

# # Tutorial 4
# 
# ## Practice Questions

# ### Question 1
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
# ### Question 2
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
# ### Question 3
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

# ### Question 4
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

# ## Tutorial Questions

# ## Question 1
# 
# In biology, an RNA sequence consists of a chain of the nucleotides Adenine, Uracil, Cytosine and Guanine in a specific order. We can represent an RNA sequence by a string consisting of the four letters `A`, `U`, `C` and `G` [1].
# ```
# rna_seq = "GCAUAUGUUCAUAUGAAUA"
# ```
# each three character substring identifies a 'codon' which either identifies a specific amino acid within a protein, or a 'start' or 'stop' instruction.  
# 
# start codon: AUG  
# stop codons: UAA, UAG, UGA  
# 
# |Amino Acid| | codons |
# |---|---|---|
# |Glycine|G|GGA, GGU, GGG, GGC|
# |Alanine|A|GCA, GCU, GCG, GCC|
# |Valine|V|GUA, GUU, GUG, GUC|
# |Leucine|L|UUA, UUG, CUU, CUC, CUA, CUG|
# |Isoleucine|I|AUA, AUU, AUC|
# |Serine|S|UCA, UCU, UCG, UCC, AGU, AGC|
# |Threonine|T|ACA, ACU, ACG, ACC|
# |Cysteine|C|UGU, UGC|
# |Methionine|M|AUG|
# |Lysine|K|AAA, AAG|
# |Arginine|R|CGA, CGU, CGG, CGC|
# |Histidine|H|CAU, CAC|
# |Proline|P|CCA, CCU, CCG, CCC|
# |Aspartic Acid|D|GAU, GAC|
# |Asparagine|N|AAU, AAC|
# |Glutamic Acid|E|GAA, GAG|
# |Glutamine|Q|CAA, CAG|
# |Phenyl Alanine|F|UUU, UUC|
# |Tyrosine|Y|UAU, UAC|
# |Tryptophane|W|UUG|
# 
# 
# Given an RNA sequence, we would like to identify all the amino acid-encoding codons (in **bold**) lying between with the first 'start' codon and the first 'stop' codon (in <span style="color:red">red</span>).
# 
# GCAU<span style="color:red">AUG</span>**UUCAUA**<span style="color:red">UGA</span>AUA
# 
# amino acid-encoding codons:  
# UUC, AUA
# 
# Having identified the codons, we can determine the sequence of amino acids by looking them up in the table above.
# 
# amino acid sequence:  
# 
# FI
# 
# By following the steps below, write a program which translates an RNA sequence into a sequence of amino-acids.
# 
# **Hint: Do Practice question 1 first.**
# 
# 
# ### Step 1
# 
# Write a program that loops over the characters in the string and checks whether each three character substring is equal to the 'start' codon, `AUG`. Once it finds the start codon, it should store the position in the variable `j`, then use the `break` keyword to abort the loop.
#  
# For example,
# ```
# rna_seq = "GCAUAUGUUCAUAUGAAUA"
# 
# # Your code
# ...
# 
# print(j)
# ```
# Output:
# ```
# 4
# ```
# 
# ### Step 2
# 
# Make a second loop which prints out three characters at a time, starting from position `j`.
# 
# Abort the loop when it reaches one of the stop codons `UAA`, `UAG`, or `UGA`.
# 
# Output:
# 
# ```
# UUC
# AUA
# ```
# 
# ### Step 3
# 
# Adapt the second loop so that it uses `list.index` to find the position of each codon in the list `genetic_code`, then prints out the character in the equivalent position in `amino_acids`.
# 
# ```
# genetic_code = ['GCA', 'GCC', 'GCG', 'GCU', 'UGC', 'UGU', 'GAC', 'GAU', 'GAA',
#                 'GAG', 'UUC', 'UUU', 'GGA', 'GGC', 'GGG', 'GGU', 'CAC', 'CAU',
#                 'AUA', 'AUC', 'AUU', 'AAA', 'AAG', 'UUA', 'UUG', 'CUA', 'CUC',
#                 'CUG', 'CUU', 'AUG', 'AAC', 'AAU', 'CCA', 'CCC', 'CCG', 'CCU',
#                 'CAA', 'CAG', 'AGA', 'AGG', 'CGA', 'CGC', 'CGU', 'CGG', 'AGC',
#                 'AGU', 'UCA', 'UCC', 'UCG', 'UCU', 'ACA', 'ACC', 'ACG', 'ACU',
#                 'GUA', 'GUC', 'GUG', 'GUU', 'UGG', 'UAC', 'UAU', 'UAG', 'UAA', 'UGA']
# 
# amino_acids = ['A', 'A', 'A', 'A', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F',
#                'G', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'K', 'K', 'L',
#                'L', 'L', 'L', 'L', 'L', 'M', 'N', 'N', 'P', 'P', 'P', 'P',
#                'Q', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S',
#                'S', 'S', 'T', 'T', 'T', 'T', 'V', 'V', 'V', 'V', 'W', 'Y',
#                'Y', '!', '!', '!']
# ```
# 
# ### Step 4
# 
# Test your finished program against the following RNA sequences:
# 
# `rna_1 = "CAACAAUGCUCCCCGCCUAGUUG"`
# 
# Output:
# 
# ```
# L
# P
# A
# ```
# 
# `rna_2 = "UAAAAUGAAUAAUAGAUAA"`
# 
# Output:
# ```
# N
# N
# R
# ```
# 
# [1] https://bmm.crick.ac.uk/~chalei01/tutorial/Session6/Rasp_Pi_Visit_6_handout.pdf

# In[ ]:





# ### Part 1
# Write a program which counts the frequency of each letter in the file `english.txt`, and displays the results as a [bar graph](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html). Make sure to include upper and lower case characters but do not count them separately. Do not count punctuation or spaces.
# 
# ```{image} alphabet.png
# :width: 400px
# ```
# 
# Use the following code to load the contents of the text file into a string variable:
# ```
# with open("english.txt") as f:
#      text = f.read()
# ```
# 
# Hint: create a variable to store the alphabet and use `string.find` to locate each character in the alphabet.
# 
# ### Part 2
# Let $A_i$ be the relative frequency of letter $i$ in text $A$, where a is letter 0, b is letter 1 etc. (E.g. if A = "alphabet!", $A_0 = 2/8 = 0.25$ since the letter a appears 2 times out of 8 alphabetic characters). We define a similarity index for two pieces of text using the following formula:
# $$\sum_{i=0}^{25} (A_i - B_i)^2$$
# 
# Write a program which predicts the language of a piece of text by comparing the text to the each of the four languages English, French, German and Spanish. Relative frequencies for each these languages can be found here: https://en.wikipedia.org/wiki/Letter_frequency. (Make sure the relative frequences sum to 1!)
# 
# Your program should calculate the value of the similarity index for each of the languages then print the name of the language with the lowest score.

# In[ ]:




