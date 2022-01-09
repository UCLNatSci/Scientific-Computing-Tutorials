#!/usr/bin/env python
# coding: utf-8

# # Tutorial 5
# 
# ## Question 1
# 
# The (approximate) orbit of a planet around the sun is given by the following equations:
# 
# $$x = d\cos(2\pi t/p)\\
#  y = d\sin(2\pi t/p)$$
#  
# where $d$ is the distance from the sun, and $p$  is the orbital period in days.
#  
# Values for $d$ and $p$ for the Solar System can be found in the following link:
# 
# http://www.astronomynotes.com/tables/tablesb.htm
# 
# :::{sidebar} Animation Code
# ```
# import numpy as np
# from matplotlib import animation
# from IPython.display import HTML, display
# import random
# 
# # Parabolic Trajectory
# 
# t = np.arange(10)
# y = 25 - (t-5)**2
# 
# # Animation code:
# 
# filename = "animation.gif"
# frames = len(t)
# interval = 100
# 
# def ganimate(frame):
#     plt.cla()
#     plt.scatter(t[frame], y[frame])
#     plt.xlim(0, 10)
#     plt.ylim(0, 30)
#     
# fig = plt.figure(figsize=(5, 5))
# anim = animation.FuncAnimation(fig, ganimate, frames=frames, interval=interval)
# anim.save(filename, writer='imagemagick')
# plt.close()
# 
# __counter__ = str(random.randint(0,2e9))
# display(HTML('<img src="' + filename + '?' + __counter__ + '">'))
# ```
# :::
#  
# 1. Create an array `t` containing the 365 days of the year then calculate the trajectory of planet Earth's orbit around the sun for one (Earth) year. Plot a graph showing $x$ and $y$ against $t$, and  another graph showing $y$ against $x$.
# 1. Calculate the trajectories of the four innermost planets around the sun, and add their trajectories to the two graphs (of course you'll have to increase the simulation duration). [hint: you could create separate variables `x_earth`, `y_earth`, `x_mercury`, `y_mercury` etc, but it is neater to make two 2-dimensional arrays `x` and `y` where each row corresponds to a planet].
# 1. Adapt the animation code to generate an animation of the orbits of the four planets. [Hint: generating the animation can be quite slow, so start by reducing the number elements in your array `t` by increasing the timestep]

# ## Question 2
# 
# The spread of an infectious disease amongst a population can be modelled by the SIR model. The number of susceptible ($S_i$) and infected ($I_i$) peeople are modelled by the following pair of coupled equations:
# 
# $$ S_{i+1} = S_i - bS_iI_i $$
# $$ I_{i+1} = I_i + bS_iI_i - aI_i $$
# 
# where $i$ represents the number of days since the start of the outbreak. There are two parameters: the recovery rate parameter $a$ and the infection rate parameter $b$.
# 
# 1. With parameter values $a = 0.1$ and $b = 0.00005$ and the initial populations $S_0 = 20000$ and $I_0 = 100$, simulate the infection for a duration 100 days. Plot the resulting arrays `S` and `I` on the same figure. [You should see that the number of infected people peaks at around 15000 at about day 15, while the number of susceptible people drops to about zero at about the same time].
# 
#  The number of recovered people $R_i$ is given by $P = S_i + I_i + R_i$ where the total population $P$ is a constant.
# 
# 2. Given the total population $P = S_0 + I_0$, calculate an array `R` representing the number of recovered people over the 100 days. Plot `R` on the graph together with `S` and `I`.
# 
#  The infection rate parameter $b$ can be influenced by public policy - for example the imposition of social distancing, vaccination or other measures. 
# 
# 3. Experiment with various values of $b$ to see how it affects the outbreak. Roughly what is the minimum value of $b$ which results in an epidemic? (We say there is an epidemic if $I_i$ initially rises to a peak, however small).
# 
#  The Government would like to understand how $b$ affects the the peak value of $I_i$. 
# 
# 4. Write a function `max_I(a, b)` which runs the simulation with the given values for the parameters $a$ and $b$ and returns the maximum value of `I_i`. Then, write a loop which calculates `max_I(a, b)` for values of `b` ranging from 0.0 to 0.00005. Plot a graph showing peak $I_i$ against $b$.
# 
# ```
# def max_I(a, b):
#     
#     # run the simulation for parameter values a, b
#     
#     # return maximum value of I
# ```
