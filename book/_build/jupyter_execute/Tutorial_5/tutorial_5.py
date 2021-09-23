#!/usr/bin/env python
# coding: utf-8

# # Tutorial 5
# 
# ## Practice Questions

# ### Question 1
# 
# Create a 2 by 3 numpy array containing the following data:
# 
# $$
# \begin{bmatrix}
# 10 & 12 & 13\\
# 5 & 6 & 7
# \end{bmatrix}
# $$
# 
# Use slice notation to create one-dimensional arrays containing:
# 
# 1. The first row
# 1. The last column
# 
# Calculate:
# 
# 1. A 3 element array containing the sum of each of the three columns
# 1. A 2 element array containing the sum of each of the two rows

# ## Question 2
# 
# A particle follows a trajectory given by the following equations between $t=0$s and $t = 10$s:
# 
# $$
# x = 4\sin(7t)\\
# y = 4\cos(6t)
# $$
# 
# 
# 
# Use `np.arange` to create an array `t` containing 100 evenly spaced time points from 0 to 10. Calculate arrays `x` and `y` containing the x and y co-ordinates, then plot the x and y co-ordinates against time on the same graph. On a separate graph, plot x against y.

# ## Tutorial Questions

# The purpose of this question is to simulate the trajectory of an object under gravity. The question adapts and extends the techniques for solving differential equations explained in the 'Linear Oscillator' example. Make sure you can understand that example before attempting this question.
# 
# See the accompanying file `gravity_notes.ipynb` for a derivation of the equations of motion of an object moving under gravity.
# 
# ### Part 1
# 
# First you will consider the one-dimensional case of a projectile fired vertically from the surface of The Earth. Does it fall back to earth or does it escape into space? 
# 
# A projectile at distance $x$ from the centre of the Earth and moving at a velocity $v$ in a vertical direction moves according to the following coupled pair of differential equations:
# 
# $$\begin{align*}
# \frac{dx}{dt} &= v\\
# \frac{dv}{dt} &= -\frac{Gm_\mathrm{e}}{x^2}
# \end{align*}$$
# 
# Determine the update rule which calculates $x_{i+1}$ and $v_{i+1}$ from $x_{i}$ and $v_{i}$, then adapt the linear oscillator example to calculate the trajectory of the projectile. Plot the trajectory as distance `x` against time `t` and determine at what time the projectile returns to The Earth's surface.
# 
# | | |
# |---|---|
# |duration | $10000~\mathrm{s}$|
# |time step | $1~\mathrm{s}$|
# |mass of Earth | $5.972 \times 10^{24}~\mathrm{kg}$|
# |radius of Earth | $6.371~\times 10^6~\mathrm{m}$ |
# |initial velocity | $5000~\mathrm{m}/\mathrm{s}$ |
# |gravitational constant | $6.674 \times 10^{11}~\mathrm{Nm}^2/\mathrm{kg}^2$ |
# 
# **Hint** you should exit the loop (using the `break` keyword) once the projectile's position falls below the surface of the earth.

# ### Part 2
# 
# By experimenting with different values of $v_0$, find an estimate of The Earth's escape velocity (the minimum initial velocity that results in the projectile escaping into space).
# 
# (You will have to increase the duration of the simulation. You might need to increase the time step $\Delta t$ in order for the simulation to run in a reasonable time - but this will decrease the accuracy. Experiment!)

# ### Part 3
# 
# The previous example only considered motion in one dimension. In this part you will extend to two dimensions.
# 
# Consider a projectile fired horizontally from the surface of the earth. Its position $\mathbf{x} = (x_1, x_2)$ relative to the centre of The Earth and its velocity is $\mathbf{v} = (v_1, v_2)$. The distance between the projectile and the centre of The Earth is $r = \sqrt{x_1^2 + x_2^2}$.
# 
# The vector equations governing its motion are:
# $$\begin{align*}
# \frac{d\mathbf{x}}{dt} &= \mathbf{v}\\
# \frac{d\mathbf{v}}{dt} &= -\frac{Gm_\mathrm{e}}{r^3}\mathbf{x}
# \end{align*}$$
# 
# Defining a timestep $\Delta t$:
# 
# $$ \begin{align*}
# \mathbf{x}_{i+1} &= \mathbf{x}_i + \mathbf{v}_i\Delta t\\
# \mathbf{v}_{i+1} &= \mathbf{v}_i -\frac{Gm_\mathrm{e}}{r^3}\mathbf{x_i}\Delta t
# \end{align*}$$
# 
# Since $\mathbf{x}_i$ and $\mathbf{x}_i$ and are 2-dimensional vectors, `x` and `v` are now 2 by `n_steps` numpy arrays, where `x[0,i]` and `x[1,i]` are $x_1$ and $x_2$ co-ordinates of the projectile at timestep `i`.
# 
# ```
# x = np.zeros((2, n_steps))
# v = np.zeros((2, n_steps))
# ```
# 
# The update step for the position `x` becomes:
# 
# ```
# x[:,i+1] = x[:,i] + v[:,i] * delta_t
# ```
# 
# Determine the code for the update step for the velocity `v` (hint: first calculate the value of the scalar quantity `r`).
# 
# Use this code to write a simulation of the trajectory of the projectile. Create three plots of its trajectory, $x_1$ against $t$, $x_2$ against $t$, and $x_1$ against $x_2$.
# 
# 
# | | |
# |---|---|
# |duration | $10000~\mathrm{s}$|
# |time step | $1~\mathrm{s}$|
# |mass of Earth | $5.972 \times 10^{24}~\mathrm{kg}$|
# |radius of Earth | $6.371~\times 10^6~\mathrm{m}$ |
# |initial velocity (horizontal) | $10000~\mathrm{m}/\mathrm{s}$ |
# |initial velocity (vertical) | $0~\mathrm{m}/\mathrm{s}$ |
# |gravitational constant | $6.674 \times 10^{11}~\mathrm{Nm}^2/\mathrm{kg}^2$ |

# ### Part 4
# 
# The kinetic energy (in Joules) of the projectile is given by the equation
# 
# $$ E_\mathrm{K} = \frac{1}{2}{mv}^2$$
# 
# where $m$ is the mass of the projectile and $v$ is the magnitude of its velocity.
# 
# Its potential energy (in Joules) is given by:
# 
# $$ E_\mathrm{P} = -\frac{Gm_\mathrm{e}mv}{r}$$
# 
# where $r$ is the distance between the projectile and the centre of The Earth.
# 
# Use array slicing and vector operations to calculate one-dimensional arrays `E_K` and `E_P` representing the kinetic and potential energies of the projectile (i.e. `E_K[i]` is the kinetic energy at time point `i`). Plot `E_K`, `E_P` and the total energy `E_K` + `E_P` on the same graph. Add suitable x and y labels and a legend.
# 

# In[ ]:




