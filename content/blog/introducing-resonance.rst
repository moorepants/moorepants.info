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
Timoshenko and Den Hartog in the early 20th century.

The course advances students' understanding of vibrating mechanical systems,
building on fundmendtal dynamics and providing the theory of small periodic
motions based primarily on the mathematical analysis of linear differential
equations which are derived from Newton's Second Law of Motion. These
foundational concepts provide insight into the design of machines to both
minimize undesired vibrations and exploit desired vibrations.

Early mechanical vibration courses were presented from a theorecitcal veiwpoint
and tied to the analtyic tools of the day. There may have been some courses
with accompanying laboratories to experimeent with real vibrating systems and
since the 80s, mechanical vibrations courses have often been enhanced with
computational tools such as Matlab to solve problems that are difficult or
unwiedly to solve by hand.

These courses typically have the standard engineering course format: professor
lectures in class by deriving mathematical theory on the board and does example
problems to accompany the theory, the students are assigned homework problems
each week for practice at appling and understanding the theory, and exams are
given that are similar to homework problems to assess student learning.

This format has served the engineering profession for a century or more, but
there are a number of reasons to believe that this course could be changed to
both improve learning and provide students with skills that are more relevant
to their future work.

Why Change?
===========

Here are the main reasons that we wanted to change the course:

- This type of course has likely only changed in one significnat way in 100
  years with addition of computational tools in the 80s. It is true that
  foundational theory doesn't change much in that time, but it is equally true
  that much of traditional materials may not be directly relevant to solving
  modern vibration related problems and thus could be removed.
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
- We wanted to experiement with using computational thinking methods.

Computation
===========

An aside to talk a bit about computational thinking and experimentation.

An engineer's primary goal is to solve problems. Solving each problem requires
some minimal understanding of how the world works. Before computers, engineers
performed, potentially costly, experiments and developed mathematical models of
the phoemoma the observed so that these models can predict similar phenomena.
Thus, if one could reason about the world uwsing mathematical language, you
could gain great power. With the advent of computers, computation was typically
used to enhance the mathematics so that mathematical problems could be solve
more efficiently. The steps were:

1. Observe phenomena
2. Develop a mathematical causal relationship that predicts the phenomena
3. Implement the mathematical relationship with computation
4. Make predictions to solve problems

This is a powerful and invaluable process, but it is also true that,
taken to an extream, one can remove step 2 and potentially reason about the
world directly in the language of computation. Calculating probabilites offer
simple examples.

TOOD : Rolling dice example
TODO : Or do the frequency response example

.. code:: python

   from random import choice
   count = 0
   num_trials = 10000
   for trial in range(num_trials):
       rolls = []
       for roll in range(10):
               rolls.append(choice([1, 2, 3, 4, 5, 6]))
       if len([r for r in rolls if r == 3]) > 1:
               count += 1
   print(count / num_trials)

This abilty to reason about the world through computational languages, is the
essence of "computational thinking". Computational thinking adds a
complementary mode of reasoning to experimentation and mathematical modeling.
In some cases, it may even be used as a replacement.

What We Did
===========

Interactive Digital Textbook
----------------------------

We wrote a series of 14 Jupyter_ notebooks that serve as the core learning
resources for the course. We consider these notebooks taken together a textbook
and replace the need for a traditional static, paper text. The design of this
text has these features:

- Approximately 1 notebook per each of the 20 two hour lecture periods, i.e.
  just the right length for the 10 week course.
- The notebooks mix written text, mathematical equations, static figures,
  videos, and live Python code that can be executed to create interactive
  figures.
- Each notebook introduces a new real vibrating mechanical system as a
  motivation for learning the subsequent concepts.
- The notebooks are licensed under the Creative Commons Attribution license to
  maximize reuse potential.
- The notebooks are intended to be used live in class with embedded interactive
  exercises.

.. _Jupyter: http://jupyter.org

Software Library
----------------

The text book is accompanied by a custom Python software library called
"resonance". We decided to develop the custom library so that we could
carefully design it to scaffold the exposure to the concepts we introduced in
the text. The library was designed with these features in mind:

- Provide a framework for learning mechanical vibration concepts.
- Allow students to construct, simulate, analyze, and visualize vibrating
  systems with a simple application programming interface.
- Hide Python programming details up front, but allow them to be exposed in a
  scoffolded way as the course progresses. Hide object oriented class
  construction completely.
- Include many very informative error messages.
- Performance is secondary to usability.
- Structed around "system" objects that have similarities to real vibrating
  mechanical systems and can be experiemented with in much the same way one
  might do in lab.

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

The previous course design had two in-class pen and paper exams. We added an
individual course project to more effectively assess the course learning
objectives and provide a realistic engineering exercise.

We orginally intended to have a midterm, a final, and a course project but we
dropped the final exam due to two reasons:

1. Two exams and a project was simply too much work.
2. We gave a midterm that required live coding to solve the problems that did
   not effectively assess what the students had learned.

Next year, I will likely remove the midterm and break the project into two
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
workshop at the UCD Data Science Institute on January 5th for about 20 faculty,
staff, and graduate students from a variety of discplines around campus. We
proposed seven methods of utilizing computation to learn domain specific
concepts and the attendees developed examples from their domains.

What To Improve
===============

- Need classroom that is appropirate for the class activities (i.e. need tables!)
- Analytical ODEs need to be shown after the computational methods, could
  motivate students to learn more about them.

Conclusion
==========


Acknowledgements
================

This blog post was made possible by the Undergraduate Instructional Innovation
Program at the `Center for Educational Effectiveness`_ at the University of
California, Davis. The funding proposal can be viewed on Figshare_.

.. _Figshare: https://doi.org/10.6084/m9.figshare.5229886.v1
.. _Center for Educational Effectiveness: https://cee.ucdavis.edu/
