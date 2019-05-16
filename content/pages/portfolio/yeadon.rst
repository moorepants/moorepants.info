======
Yeadon
======

:subtitle: body segment parameter estimation
:description: Details of the Yeadon software project.
:startdate: 2011-06-01 00:00:00
:enddate: 2014-11-30 10:00:00
:status: hidden

.. image:: {{ media_url('images/yeadon-gui-screenshot.png') }}
   :class: img-rounded
   :align: center

``yeadon`` is a software package that implements Fred Yeadon's popular method
for estimating the body segment parameters of a human. The package can be used
as library, as in BicycleParameters_, or as a standalone GUI application.

.. _BicycleParameters: https://github.com/moorepants/BicycleParameters

Software
========

The software is written in pure Python, depends on several components of the
Scientific Python Stack, and is BSD licensed.

- `Download <https://pypi.python.org/pypi/yeadon/>`_
- `Documentation <http://yeadon.readthedocs.org>`_
- `Source code <https://github.com/chrisdembia/yeadon>`_

Publications
============

- Dembia C, Moore JK and Hubbard M. An object oriented implementation of the
  Yeadon human inertia model [v1; ref status: approved 1, http://f1000r.es/4cr]
  F1000Research 2014, 3:223 (doi: 10.12688/f1000research.5292.1)
- Moore, Jason. “Human Control of a Bicycle.” Doctor of Philosophy, University
  of California, Davis, 2012. http://moorepants.github.com/dissertation.

Talks
=====

SciPy 2013
----------

An introductory talk about the ``yeadon`` package.

.. raw:: html

   <iframe
     width="640"
     height="360"
     src="//www.youtube.com/embed/H9AK65ZY-Vw"
     frameborder="0"
     allowfullscreen>
   </iframe>

Media
=====

Screencast
----------

This screencast shows how to use the GUI.

.. raw:: html

   <iframe
     width="480"
     height="360"
     src="//www.youtube.com/embed/o-5Ss6YLY0I"
     frameborder="0"
     allowfullscreen>
   </iframe>

Screenshots
-----------

.. image:: {{ media_url('images/haya.png') }}
   :class: img-rounded
   :align: center

.. image:: {{ media_url('images/ice-skater-double.png') }}
   :class: img-rounded
   :align: center
