## Bisection Method

1. The [bisection method](https://x-engineer.org/wp-content/uploads/2016/11/The-Bisection-Method-Explained-Poster.jpg) can be used to find roots of functions. Write a Python script which uses the bisection method to calculate the root of the equation $f(x) = x^2 - 2$ to a tolerance of $|f(x)|<0.01$.

2. Write a function `find_root(func, a, b, tol)` which calculates the root of *any* given `func` in the interval $(a, b)$ to the tolerance `tol`. `func` should be a Python function that takes at one argument, and returns a single value. For example:
```
def xsqminus2(x):
    return x^2 - 2
    
find_root(xsqminus2, 0, 5, 0.001)
# should return a value close to sqrt(2) (within 0.001)
```