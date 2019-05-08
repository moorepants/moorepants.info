============================
Vectorized Matrix Evaluation
============================

:authors: Jason K. Moore
:subtitle: using SymPy code generators
:description:
:date: 2014-08-28 14:11:00
:tags: sympy, cython, fortran, c, matrices, code generation, python

{% mark image -%}
{%- endmark %}

{% mark excerpt %}

I'm working on using direct collocation and nonlinear programming for
system/parameter identification. This requires evaluating a vector of
constraint equations and it's sparse Jacobian. When there are thousands of
collocation nodes and a fair number of model states the equations need to be
evaluated on the order of a million times at each optimization step. I've been
generating the constraints equations and non-sparse Jacobian entries with SymPy
and then generating code to evaluate the equations.

{% endmark %}

SymPy has a few facilities for generating fast code:

1. ``lambdify``: generates Python code and can utilize NumPy
2. ``autowrap/codegen``: generates and wraps Fortran 95 and C code
3. ``ufuncify``: same as ``autowrap`` but "vectorizes" in the inputs and outputs

First I create the symbolic form of some sample expressions (these are much
shorter than my real problems).

.. sourcecode:: python

   a, b, c = sp.symbols('a, b, c')

   expr_00 = a**2 * sp.cos(b)**c
   expr_01 = sp.tan(b) / sp.sin(a + b) + c**4
   expr_10 = a**2 + b**2 - sp.sqrt(c)
   expr_11 = ((a + b + c) * (a + b)) / a * sp.sin(b)

   sym_mat = sp.ImmutableDenseMatrix([[expr_00, expr_01],
                                      [expr_10, expr_11]])

Then simply set up some large one dimensional arrays that will be used in the
expression evaluation.

.. sourcecode:: python

   n = 10000

   a_vals = np.random.random(n)
   b_vals = np.random.random(n)
   c_vals = np.random.random(n)

The mathematical expressions are generally generated symbolically with SymPy.
The easiest method available in SymPy is to use the lambdify function to
generate a NumPy backed numerical function.

I'll try two methods:

1. lambdify the matrix and rely on numpy's underlying broadcasting
2. lambdify each expression individually

.. sourcecode:: python

   f = sp.lambdify((a, b, c), sym_mat, modules='numpy', default_array=True)

   f00 = sp.lambdify((a, b, c), expr_00, modules='numpy', default_array=True)
   f01 = sp.lambdify((a, b, c), expr_01, modules='numpy', default_array=True)
   f10 = sp.lambdify((a, b, c), expr_10, modules='numpy', default_array=True)
   f11 = sp.lambdify((a, b, c), expr_11, modules='numpy', default_array=True)


   def eval_matrix_loop_lambdify():
       """This evaluates the lambdified matrix of expressions all in one
       shot."""
       return f(a_vals, b_vals, c_vals)


   def eval_matrix_loop_lambdify_individual():
       """This allocates a 3D array inserts the evaluated lambdified
       expressions in the correct entries."""

       result = np.empty((n, 2, 2))

       result[:, 0, 0] = f00(a_vals, b_vals, c_vals)
       result[:, 0, 1] = f01(a_vals, b_vals, c_vals)
       result[:, 1, 0] = f10(a_vals, b_vals, c_vals)
       result[:, 1, 1] = f11(a_vals, b_vals, c_vals)

       return result

These two methods are explicit Python functions that use NumPy to do
exactly what lambdify does under the hood.

.. sourcecode:: python

   def eval_matrix_loop_numpy_broadcast():
       """This is the same thing as lambdifying the SymPy matrix."""

       result = np.array(
           [[a_vals**2 * np.cos(b_vals)**c_vals,
             np.tan(b_vals) / np.sin(a_vals + b_vals) + c_vals**4],
            [a_vals**2 + b_vals**2 - np.sqrt(c_vals),
             ((a_vals + b_vals + c_vals) * (a_vals + b_vals)) / a_vals *
             np.sin(b_vals)]])

       return result


   def eval_matrix_loop_numpy():
       """Since the number of matrix elements are typically much smaller than
       the number of evaluations, NumPy can be used to compute each of the
       Matrix expressions. This is equivalent to the individual lambdified
       expressions above."""

       result = np.empty((n, 2, 2))

       result[:, 0, 0] = a_vals**2 * np.cos(b_vals)**c_vals
       result[:, 0, 1] = np.tan(b_vals) / np.sin(a_vals + b_vals) + c_vals**4
       result[:, 1, 0] = a_vals**2 + b_vals**2 - np.sqrt(c_vals)
       result[:, 1, 1] = (((a_vals + b_vals + c_vals) * (a_vals + b_vals)) /
                          a_vals * np.sin(b_vals))

       return result

The most basic method of building the result array is a simple loop in
Python. But this will definitely be the slowest due to Python's overhead.
But this is what we ultimately want to improve with all these methods that
rely on fast low level code for the loop (vectorizing). This is the speed
benchmark. All other method will be compared against it.

.. sourcecode:: python

   def eval_matrix_loop_python():
       """This is the standard Python method, i.e. loop through each array and
       compute the four matrix entries."""

       result = np.empty((n, 2, 2))

       for i in range(n):
           result[i, 0, 0] = a_vals[i]**2 * math.cos(b_vals[i])**c_vals[i]
           result[i, 0, 1] = (math.tan(b_vals[i]) / math.sin(a_vals[i] +
                              b_vals[i]) + c_vals[i]**4)
           result[i, 1, 0] = a_vals[i]**2 + b_vals[i]**2 - math.sqrt(c_vals[i])
           result[i, 1, 1] = (((a_vals[i] + b_vals[i] + c_vals[i]) * (a_vals[i]
                              + b_vals[i])) / a_vals[i] * math.sin(b_vals[i]))

       return result

The next methods utilized hand written C functions and some Cython
wrappers. I have two flavors. In the Cython one the loop is in Cython and
the expression eval is in C. In the second one, _c, both the loop and the
expression evals are in C, with just a light Cython wrapper.

.. sourcecode:: python

   def eval_matrix_loop_cython():
       """This is equivalent to the naive Python loop but is implemented in a
       lower level as a combination of Cython and C. The loop is in Cython and
       the expression eval is in C."""

       result = np.empty((n, 4))

       return cython_loop(a_vals, b_vals, c_vals, result)


   def eval_matrix_loop_c():
       """This is equivalent to the naive Python loop but is implemented in a
       lower level as a combination of Cython and C. The loop and expression
       evals are all in C."""

       result = np.empty((n * 4))

       return c_loop(a_vals, b_vals, c_vals, result)

``sympy.utilities.ufuncify`` automatically generates the broadcasting loop in
the low level. The default settings use Fortran and f2py. Currently, ufuncify
only supports scalar expressions and an array for the first argument. But I've
included a modified version in multiindex.py that requires all of the arguments
to the function to be arrays of equal length.  ufuncify currently doesn't
support a list of expressions (or sympy matrices) so I ufuncify each
expression. If all of the expressions were in the low level loop then things
will likely be faster especially if cse is used and other optimizations.

.. sourcecode:: python

   g00 = ufuncify((a, b, c), expr_00, language='F95', backend='f2py',
                  tempdir='ufunc-fortran-code')
   g01 = ufuncify((a, b, c), expr_01, language='F95', backend='f2py')
   g10 = ufuncify((a, b, c), expr_10, language='F95', backend='f2py')
   g11 = ufuncify((a, b, c), expr_11, language='F95', backend='f2py')


   def eval_matrix_loop_ufuncify_f2py():
       """This creates the result using the Fortran backend."""

       result = np.empty((n, 2, 2))

       result[:, 0, 0] = g00(a_vals, b_vals, c_vals)
       result[:, 0, 1] = g01(a_vals, b_vals, c_vals)
       result[:, 1, 0] = g10(a_vals, b_vals, c_vals)
       result[:, 1, 1] = g11(a_vals, b_vals, c_vals)

       return result

   h00 = ufuncify((a, b, c), expr_00, language='C', backend='Cython',
                  tempdir='ufunc-cython-code')
   h01 = ufuncify((a, b, c), expr_01, language='C', backend='Cython')
   h10 = ufuncify((a, b, c), expr_10, language='C', backend='Cython')
   h11 = ufuncify((a, b, c), expr_11, language='C', backend='Cython')


   def eval_matrix_loop_ufuncify_cython():
       """This creates the result using the C/Cython backend."""

       result = np.empty((n, 2, 2))

       result[:, 0, 0] = h00(a_vals, b_vals, c_vals)
       result[:, 0, 1] = h01(a_vals, b_vals, c_vals)
       result[:, 1, 0] = h10(a_vals, b_vals, c_vals)
       result[:, 1, 1] = h11(a_vals, b_vals, c_vals)

       return result

So these the program is run as so::

   $ python test_eval_matrix.py

And it prints these results (example timings on my machine)::

   Testing results.

   Timing the functions.

   Timing: cython
   cython time: 0.00300521969795 s

   Timing: numpy_broadcast
   numpy_broadcast time: 0.00657413101196 s

   Timing: lambdify_individual
   lambdify_individual time: 0.00323091069857 s

   Timing: ufuncify_f2py
   ufuncify_f2py time: 0.0021202070713 s

   Timing: python
   python time: 0.136805589199 s

   Timing: ufuncify_cython
   ufuncify_cython time: 0.00302646199862 s

   Timing: numpy
   numpy time: 0.00317755591869 s

   Timing: c
   c time: 0.00297607461611 s

   Timing: lambdify
   lambdify time: 0.00649729514122 s

   Benchmark time: 0.136805589199 s

   Ratios of the timings to the benchmark time:
   --------------------------------------------

   ufuncify_f2py ratio: 64.5246358484
   c ratio: 45.9684674767
   cython ratio: 45.5226582244
   ufuncify_cython ratio: 45.2031412459
   numpy ratio: 43.0537157172
   lambdify_individual ratio: 42.3427330441
   lambdify ratio: 21.0557757075
   numpy_broadcast ratio: 20.8096840404

I'm actually using the ``python`` loop in my Jacobian evaluation currently so I
can get ~60X speedup using `ufuncify` with Fortran 95 code. And I can get a 3X
speedup on my lambify code for the constraints.

Other notes of interest:

- Assuming the number of expressions is much greater than the number of
  evaluations, the loop on the expressions with NumPy expression evaluations,
  ``numpy``, is pretty fast and is 2X faster than the default lambdify method.
  You can even speed up lambdify by simply computing each expression in the
  matrix seperately.
- The three Cython/C based methods all give about the same speed.
- I don't know why the Fortran backend is faster. But I've seen a number of
  other benchmarks that show Fortran is generally faster than C for these kinds
  of things.
- I'd like to get the ufuncify_f2py version working for evaluating all the
  matrix entries in the same loop. Common sub expressions may help there too
  depending on whether the Fortran compiler does this or not.

The working code is avaiable in this gist:

https://gist.github.com/moorepants/6ef8ab450252789a1411

Update (September 11, 2014)
---------------------------

My PI was curious how these speeds compare to Matlab, so I wrote two Matlab
functions that mirror ``eval_matrix_loop_python`` and
``eval_matrix_loop_numpy``. The code is in the gist and these are the results::

   >> version

   ans =

   8.3.0.532 (R2014a)

   >> test_matrix_eval
   ------------------------------------
   Mean time to evaluate the loop 0.1158 s
   Ratio to the Python loop benchmark time is 1.18
   Ratio to the Python vectorized time is 0.03
   ------------------------------------
   Mean time to evaluate the vectorized loop 0.0026 s
   Ratio to the Python loop benchmark time is 53.60
   Ratio to the Python vectorized time is 1.24
   ------------------------------------

Matlab beats Python on both functions in this case but not by leaps and bounds.
Matlab as a JIT since version 6.5 that helps speed up loops and Pure python
doesn't. There are several JITs for Python (pypy, numba, parakeet, etc). I
tried a version that grows lists in Python and PyPy and get these results::

   $ python -mtimeit -s "import test_pypy" "test_pypy.eval_matrix_loop_pypy()"
   10 loops, best of 3: 36.2 msec per loop

   $ pypy -mtimeit -s "import test_pypy" "test_pypy.eval_matrix_loop_pypy()"
   100 loops, best of 3: 7.2 msec per loop

This gives an improvement but Matlab still beats PyPy. This isn't a good
comparison though, as the arrays are preallocated in Matlab and not in the PyPy
version.

Matlab's vectorized version is closer in speed to my generated Fortran code.

Also I created a basic function that ufuncifies a SymPy matrix all in one shot.
It even uses CSE to improve things. It automatically creates what I did
manually for the Cython files. New timings show the obvious, that it gives the
same results and the manual one. But for large matrices, the compile times are
significantly reduced. Now I need to make that function generate Fortran code
and I think that will be the fastest option.

::

   Testing results.

   Timing the functions.

   Timing: cython
   cython time: 0.00288254904747 s

   Timing: numpy_broadcast
   numpy_broadcast time: 0.00597401690483 s

   Timing: lambdify_individual
   lambdify_individual time: 0.00303873364131 s

   Timing: ufuncify_f2py
   ufuncify_f2py time: 0.00201614236832 s

   Timing: python
   python time: 0.119000189304 s

   Timing: ufuncify_cython
   ufuncify_cython time: 0.00293522365888 s

   Timing: numpy
   numpy time: 0.00303197193146 s

   Timing: c
   c time: 0.0029081483682 s

   Timing: lambdify
   lambdify time: 0.00599523711205 s

   Timing: ufuncify_matrix_cython
   ufuncify_matrix_cython time: 0.00292766968409 s

   Benchmark time: 0.119000189304 s

   Ratios of the timings to the benchmark time:
   --------------------------------------------

   ufuncify_f2py ratio: 59.0237034717
   cython ratio: 41.2829711983
   c ratio: 40.9195729508
   ufuncify_matrix_cython ratio: 40.6467266273
   ufuncify_cython ratio: 40.5421198294
   numpy ratio: 39.2484468836
   lambdify_individual ratio: 39.1611122761
   numpy_broadcast ratio: 19.9196271454
   lambdify ratio: 19.8491214076

After all this, I'm not sure this is the best benchmark. I really need a
benchmark that includes varying the size of the matrices and the expression
length and complexity to find the best solution.
