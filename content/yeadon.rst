What's your inertia?
====================

:authors: Jason K. Moore
:date: 2013-07-08 18:00:00
:description: Release materials for the Yeadon software package.
:category: software
:slug: yeadon
:subtitle: Body segment parameters with Python
:summary: Blog post on creating a new interface to test different controller
          designs for the Double Pendulum Robot.
:tags: python, body segment parameters, mayavi, yeadon, inertia

{% mark image %}

.. image:: {{ media_url('images/haya.png') }}
   :class: img-rounded
   :width: 400px

{% endmark %}

{% mark excerpt %}

I recently attended `SciPy 2013`_ where I gave a couple of talks. The second
talk was our first public showing of Yeadon, our Python package which
implements Fred Yeadon's popular method of estimating the body segment
parameters (mass, center of mass, and inertia) of a human. Chris visited our
lab as an intern in the summer of 2011 and spent part of his time writing this
package which I then used to estimate the inertia of a bicycle rider in my
dissertation_ work. Over the past couple of years we've worked on the software
here and there and now have a really nice little package. We released the 1.0
version just in time for the conference.

.. _SciPy 2013: http://conference.scipy.org/scipy2013
.. _dissertation: http://moorepants.github.io/dissertation

The video of the conference talk is below:

{% endmark %}

.. raw:: html

   <iframe width="640" height="360" src="//www.youtube.com/embed/H9AK65ZY-Vw"
    frameborder="0" allowfullscreen></iframe>

You can get the software and learn how to use it from the standard places:

- `download <https://pypi.python.org/pypi/yeadon/>`_
- `documentation <http://pythonhosted.org/yeadon/>`_
- `source code <https://github.com/fitze/yeadon>`_

And there is also a screencast on using the GUI that Chris put together for the
1.0 release:

.. raw:: html

   <iframe width="480" height="360" src="//www.youtube.com/embed/o-5Ss6YLY0I"
    frameborder="0" allowfullscreen></iframe>
