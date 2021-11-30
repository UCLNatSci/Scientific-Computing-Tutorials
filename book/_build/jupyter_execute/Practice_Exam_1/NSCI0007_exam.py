#!/usr/bin/env python
# coding: utf-8

# # NSCI0007 Practice Exam 1
# **Exam Start:** N/A  
# **Exam End:** N/A
# ## Instructions
# - Enter your answers in the file `answers.ipynb` in the practice exam folder.
# 
# ## Genome Sequencing
# 
# A genome is an organism's complete set of deoxyribonucleic acid (DNA), a chemical compound that contains the genetic instructions needed to develop and direct the activities of every organism. A strand of DNA is made of four chemical units, called nucleotide bases. The bases are adenine (A), thymine (T), guanine (G) and cytosine (C).
# 
# In this assessment you will use a method similar to the Human Genome Project to sequence DNA. In a laboratory, a strand of DNA is duplicated several times, then all the strands are broken into smaller, overlapping fragments. The bases of the smaller fragments are determined and entered into a file. The goal of this assessment is to reconstruct a full DNA strand from the set of DNA fragments.
# 
# The basic operation is to process all the fragments by matching two fragments and merging them into a new fragment. This process decreases the number of fragments by one since two fragments are merged into one. The match/merge operation is repeated until there is only one fragment left - this will be the original DNA - or until no further matches are possible.
# 
# Our starting point is a list of strings, each string representing a DNA fragment:
# 
# ```
# ['tgaaaattcctttctattttaggccc', 'tgaaaattcctttctattttaggcccatgcaat', 'ggcattagggcggttaa', 'atgcaatggcattagggcggttaa', 'ggttaa', 'tgaaaattcctttctattt', 'taggcccatgcaatggcattagggc']
# ```
# 
# We identify a pair of strings where the end of one string matches the start of the other.
# 
# ```
# taggcccatgcaatggcattagggc
#               ggcattagggcggttaa
# ```
# A new string is formed by merging the two together:
# ```
# taggcccatgcaatggcattagggcggttaa
# ```
# The pair of strings are then replaced by the merged string in the list.
# 
# This process is repeated until no further matches are possible.

# ## Question 1 [7]
# The overlap between two strings `x` and `y` is the largest number `n` such that the last `n` characters of `x` are the same as the first `n` characters of `y`.
#  - Write a function `overlap(x, y)` which returns the overlap between strings `x` and `y`
#  - Test your function using the code below.
# 
# ```
# n1 = overlap("XXXABC", "ABCYYY")
# n2 = overlap("ABCYYY", "XXXABC")
# n3 = overlap("XXXABC", "ABC")
# print(n1, n2, n3)
# 3 0 3
# ```
# 

# ## Question 2 [5]
# 
#  - Write a function `merge(x, y)` which returns a string formed by overlapping the two strings `x` and `y`.
#  - Test your function using the code below.
# ```
# s1 = merge("XXXABC", "ABCYYY")
# s2 = merge("ABCYYY", "XXXABC")
# s3 = merge("XXXABC", "ABC")
# print(s1, s2, s3)
# XXXABCYYY ABCYYYXXXABC XXXABC
# ```

# ## Question 3 [10]
# - Write a function `longest_overlap(string_list)` which returns a list `[i, j, k]` of three integers.
# 
# The function should loop over every pair of strings in `string_list` to determine the pair with the largest overlap. It should return a list `[i, j, k]` where `i` and `j` are the indices of the two strings in `string_list` and `k` is the overlap. (It may be the case that more than one pair has the largest overlap. In this case your function may return any of those pairs).
# 
#  - Test your function with the code below.
# ```
# i, j, k = longest_overlap(["XXXABC", "ABCYYY", "BC"])
# print(i, j, k)
# 0 1 3
# ```

# ## Question 4 [10]
# 
# Write a Python function `identify_strand(fragment_list, n)` which repeatedly applies the `longest_overlap` function to the list `fragment_list`. At each iteration, if the longest overlap is `n` or greater, then the code should:
# 1. remove the two identified strings from the list.
# 1. merge the two strings and append the merged string to the list.
# 
# The function should terminate when the list contains only a single string OR the longest overlap is strictly less than `n`.
# 
# The function should then return the list.
# 
# **Hint:** Use the `del` keyword to remove an item from a list. For example, `del x[4]` removes the item at index 4 from the list `x`. Be very careful to remove the items in the correct order!
# 
# Test your function with the code below:
# ```
# simple_dna = ['tgaaaattcctttctattttaggccc', 'tgaaaattcctttctattttaggcccatgcaat', 'ggcattagggcggttaa', 'atgcaatggcattagggcggttaa', 'ggttaa', 'tgaaaattcctttctattt', 'taggcccatgcaatggcattagggc']
# s = identify_strand(simple_dna, 4)
# print(s)
# ['tgaaaattcctttctattttaggcccatgcaatggcattagggcggttaa']
# ```

# ## Question 5 [8]
# 
# The following three text files each contains a set of DNA fragments. For each file:
# 
# - Read the DNA fragments into a Python list (ignore any lines starting `'>'`).
# - Use the function `identify_strand` to reconstruct and print the DNA strand (assume the desired strand is the longest one)
# 
# <a href="../practice_exam_1/strand_100.fasta" download>strand_100.fasta</a>  
# <a href="../practice_exam_1/strand_200.fasta" download>strand_200.fasta</a>  
# <a href="../practice_exam_1/strand_500.fasta" download>strand_500.fasta</a>
# 
