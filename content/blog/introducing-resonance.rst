Outline
=======

- Description of ENG 122
- What are we trying to solve?
- What is computational thinking?
- What we did

  - live computing in class
  - notebooks
  - no exams
  - workshop
  - scipy
  - server

- conclusion

Course Description
==================

*Introduction to Mechanical Vibrations* is a 30+ year old upper level elective
in the mechanical engineering curriculum at UC Davis. It is a classic
mechanical engineering course that likely stems from the courses and books of
Den Hartog in the 1920s at MIT in the USA.

The course advances students' understanding of vibrating mechanical systems,
building on fundmendtal dynamics and providing the theory of small periodic
motions based on analytical analysis of linear differential equations that
derive from Newton's Second Law of Motion. These foundational concepts provide
insight into the design of machines to both minimize undesired vibrations and
exploit desired vibrations.

Early mechanical vibration courses were mostly theorecitcal and not
particularly applied in nature. There may be some accompanying laboratories to
experimeent with real vibrating systems at some universities and since the 80s,
these courses have often been enhanced by utilizing computational tools such as
Matlab to solve problems that are difficult or unwiedly to solve by hand.

These courses typically have the standard engineering course format: professor
lectures in class by deriving mathematical theory on the board and doing
example problems, the students are assigned homework problems each week for
practice at appling and understanding the theory, and exams are given that are
similar to homework problems to assess student learning.

Why Change?
===========

Here are some reasons that we wanted to change the course

- This type of course has likely only changed in one significnat way in 100
  years with addition of computational tools in the 80s. It is true that
  foundational theory doesn't change much in that time, but it is true that
  much of it may not be relevant to solving modern problems.
- Traditional engineering textbooks are becoming antiquated due to their high
  cost to the students, their scope not fitting courses they are designed for,
  the fact that they are closed access materials, and they do not utlize the
  power of the world wide web to optimally enhance the materials. Additionally,
  there is a long list of mechanical vibrations textbooks and editions from the
  past 100 years that more-or-less provide the same materials.
- We would like to increase the likelhood that students utlize computatoinal
  tools to solve engineering problems when they leave our bachelor's program.
- There is evidence that methods other than the traditional lecture style of
  typical engineering classes are more effective for student learning.

Computation
===========

An aside to talk a bit about computational thinking and experimentation.

What We Did
===========

Interactive Digital Textbook
----------------------------

We wrote a series of 14 Jupyter notebooks that serve as the core learning
resources for the course. These notebooks together are effecitvely a textbook
and replace the need for a traditional static, paper text. The design of these
notebooks has these features:

- Approximately 1 notebook per 20 two hour lecture periods, i.e. just the right
  length for the 10 week course.
- The notebooks mix written text, mathematical equations, static figures, and
  live Python code that can be executed to create interactive figures.
- Each notebook introduces a new real vibrating mechanical system as a
  motivation for learning the following concepts.
- The notebooks are licensed under the Creative Commons Attribution license to
  maximize reuse potential.

Software Library
----------------

The text book is accompanied by a custom Python software library called
"resonance". This library was designed with these features in mind:

- Provide a framework for learning mechanical vibration concepts.
- Allow students to construct, simulate, analyze, and visualize vibrating
  systems with a simple application programming interface.
- Hide Python programming details up front, but allow them to be exposed in a
  scoffolded way as the course progresses. Hide object oriented class
  construction completely.
- Structed around "system" objects that have similarities to real vibrating
  mechanical systems.

Active Computing In Class
-------------------------

The notebooks were presented live in class. Each student downloaded the
notebook at the beginning of the class period for use on their laptop. The
instructor led the students through the notebooks by offereing verbal summaries
and addendums via "boardwork" to the written text. The instructor executed the
code cells to produce various figures and then discussed them. Each notebook
included short exercises (about 8-10 per 2 hr period) interspersed throughout
the text that were geared to assessing students on the prior 10 minutes of
instruction. These exercises had easily accessible solutions to ensure students
could move forward even if the solution was not obtained. The notebooks were
submitted at the end of the class for participation credit.

Computational Homeworks
-----------------------


Project Instead of Exams
------------------------

We orginally intended to have a midterm, a final, and a course project. We
dropped the final exam due to two reasons:

1. It was simply too much work for the students.
2. We gave a midterm that required live coding to solve the problems.

Next year, I will likely remove the midterm and break the projec tinto two
phases.

JupyterHub Service
------------------

SciPy BoF
---------

We led a "Birds of a Feather" session on teaching modeling and simulation at
SciPy 2017 in Austin, Texas. There were 13 participants from a variety of
disciplines and schools. Notes from this session can be found on this blogpost.

Computational Thinking Workshop and Seminar
-------------------------------------------

We held a "Computational Thinking in the Engineering and Sciences Curriculum"
workshop on January 5th for about 20 faculty, staff, and graduate students.


What To Improve
===============

- Need classroom that fits the class (tables!)

Conclusion
==========


Acknowledgements
================

This blog post was made possible by the Undergraduate Instructional Innovation
Program at the `Center for Educational Effectiveness`_ at the University of
California, Davis. The funding proposal can be viewed on Figshare_.

.. _Figshare: https://doi.org/10.6084/m9.figshare.5229886.v1
.. _Center for Educational Effectiveness: https://cee.ucdavis.edu/
