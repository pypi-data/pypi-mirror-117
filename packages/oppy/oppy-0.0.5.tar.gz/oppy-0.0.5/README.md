# oppy
## Optimization Package in Python

Documentation is available in the docstrings and
online [here](https://www.mathematik.uni-konstanz.de/en/volkwein/python/oppy/).

The idea behind oppy was to provide some optimization methods which are used
in the group of Prof. Dr. Volkwein quite often. After a while oppy
grew up to a whole optimization package.

Besides algorithms for solving constrained, unconstrained and non-linear
optimization problems, the package contains built-in iterative methods for
solving linear systems.

Advanced methods for optimization are included such as SQP (Square Quadratic
Programming), Augmented Lagrangian and different newton-type methods.
Furthermore certain Krylov methods are implemented for solving linear
systems in a stable way.

The goal is to provide a straightforward integration of the library to other
applications such that other methods benefit from it.

The package is still in develop mode.

For access, further questions, remarks and ideas please contact
us <agvolkwein.oppy@uni-konstanz.de>. See also the website 
[here](https://www.mathematik.uni-konstanz.de/en/volkwein/python/oppy/).

## Available subpackages

### conOpt
Subpackage which provide some methods for constraint optimization. For
problems which are subject to equality and inequality constraints like

    min f(x)
    s.t. e(x) = 0
    g(x) <= 0

we can use

* Penalty Method
* Augmented Lagrangian Method
* SQP with a BFGS update strategy (at the moment only equality constraint)

and for box constraint problems like

    min f(x) 
    s. t. x_a <= x <= x_b

we can use

* Projected gradient Method
* The L-BFGS-B Method
* Projected Newton-Krylov Method (if you can provide the
   action of the second derivative)

### itMet
Iterative methods for solving linear systems like

    Ax = b.

Here we can use either stationary methods like

* Jacobi
* Gauß-Seidel
* SOR

or we use krylov methods like

* steepest descent
* CG
* GMRES

For future release we are planing to add preconditioning in the
krylov methods. There of course you will be able to use the
stationary methods as precondition method.

### linOpt
Linear optimization methods. With the methods in this subpackage we can either
solve linear least-squares problem like

    min ||Ax - b||_2

or we solve linear programming

    max  c^T x
    s. t. Ax <= b
    x <= 0

with or without integer constraints. For that kind of problems we have
the following methods:

* linear least square
* simplex
* branch and bound

### multOpt
Scalarization methods for solving (possibly box-constrained) multiobjective
optimization problems of the form

    min (f_1(x), ..., f_k(x)),
    s.t. x_a <= x <= x_b.

The general idea of scalarization methods is to transform the
multiobjective optimization problem into a series of scalar optimization
problems. which can then be solved by using methods from unconstrained or
constrained optimization (see the subpackages unconOpt or conOpt). Here we
can use the following three scalarization methods

* Weighted-Sum Method (WSM)
* Euclidean Reference Point Method (ERPM)
* Pascoletti-Serafini Method (PSM)

### options
This subpackage contains the options class for all methods use in oppy.

### results
This subpackage contains the class for the returns which oppy use.

### tests
Unittests of oppy.

### unconOpt
Subpackage which provide some methods for unconstrained optimization, e.g:

    min f(x)

Right now we can solve this kind of problems with line search based first-
and second-order methods.

* Line Search Methods
    * Armijo
    * Wolfe-Powell
* Optimization Methods
    * Gradient Method
    * Newton Method
    * Nonlinear CG (with different strategies like Fletcher-Reves)
    * Quasi-Newton Methods (with different strategies like
       BFGS, Broyden, DFP, ...)

### visualization
Some methods for visualization.
