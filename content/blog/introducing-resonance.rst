---
title: Resonance
subtitle: Using computational thinking to teach mechanical vibrations
description:
created: !!timestamp '2013-07-08 18:00:00'
tags:
    - education
    - engineering
    - python
    - jupyter
    - computational thinking
---

{% mark image %}

{% endmark %}

{% mark excerpt %}

**Co-authored by co-instructor Kenneth Lyons.**

Course Description
==================

*`Introduction to Mechanical Vibrations`_* is a 30+ year old upper level
elective in the mechanical engineering curriculum at UC Davis. It is a classic
mechanical engineering course that stems from the courses and books of
Timoshenko and Den Hartog from the early 20th century. The course advances
students' understanding of `vibrating mechanical systems`_, that has a
foundation is the theory of small periodic motions resulting from the
mathematical analysis of linear differential equations which are derived from
Newton's Second Law of Motion. These foundational concepts provide insight into
the design of machines to both minimize undesired vibrations and exploit
desired vibrations.

Early mechanical vibration courses have been presented primarily from a
theoretical viewpoint and tied to the analytic tools of the day. There have
also been some courses with accompanying laboratories to experiment with real
vibrating systems, but those are fewer and far between. Also since the late
80s, mechanical vibrations courses have often been enhanced with computational
tools, such as Matlab, to solve problems that are difficult or unwieldy to
solve by hand.

These courses typically have the standard engineering course format, i.e. the
professor lectures in class by deriving mathematical theory on the board and
does example problems to accompany the theory, the students are assigned
homework problems each week for practice at applying and understanding the
theory, and exams are given that are similar to homework problems to assess
student learning.

This format has served the engineering profession well for a century or more,
but there are a number of reasons to believe that this course could be changed
to both improve learning and provide students with skills that are more
relevant to their future work.

.. _Introduction to Mechanical Vibrations: https://github.io/moorepants/eng122
.. _vibrating mechanical systems: https://en.wikipedia.org/wiki/Vibration

{% endmark %}

Why Change?
===========

The main reasons that we wanted to change the course are that:

- This type of course has likely only changed in one significant way in 100
  years with addition of accessible computational tools in the 80s. Although
  it is true that foundational theory does not change much in that time, it
  is equally true that much of traditional materials may not be directly
  relevant to solving modern vibration related problems and thus could be
  removed.
- Traditional engineering textbooks are becoming antiquated due to their high
  cost to the students, their scope not fitting courses they are designed for,
  the fact that they are closed access, and that they do not utilize the
  power of the world wide web to optimally enhance the materials. Additionally,
  there is a long list of mechanical vibrations textbooks and editions from the
  past 100 years that more-or-less provide the same materials.
- There is evidence that methods other than the traditional lecture style of
  typical engineering classes are more effective for student learning.
- We would like to increase the likelihood that students utilize "computational
  thinking" and the related tools to solve engineering problems when they leave
  our bachelor's program.

Computational Thinking
======================

The last point above requires some elaboration, as it is central tenant to the
course redesign. Engineering courses often have computational components, but
students may or may not learn to "think computationally".

An engineer's primary goal is to solve problems, using the knowledge and tools
at hand. Solving each problem effectivley requires some understanding of how
the world works. Engineers perform, potentially costly, experiments and develop
mathematical models of the phenomena they observe so that these models can
predict similar phenomena. Thus, if one could reason about the world using
mathematical language, you could gain great power to change it. With the advent
of computers, computation was typically used to enhance the mathematics so that
mathematical problems could be solve more efficiently. The steps are something
along the lines of:

1. Observe phenomena
2. Optionally, perform a controlled physical experiment to learn specifically
   about the phenomena
3. Develop a mathematical causal relationship that predicts the phenomena
4. Implement the mathematical relationship with computation
5. Make predictions to solve problems

This is a powerful and invaluable process, but it is also true that, taken to
an extreme, one may be able to remove step 3 and reason about the world
directly in the language of computation.

Calculating probabilities offers simple examples that can highlight what we
mean. For example, if you want to answer:

   What is the probability of rolling at least two 3's if you roll a 6 sided
   dice 10 times?

You can mathematically formulate the following equation using probability
theory:

.. math::

   P(A) = \sum_{i=2}^{10} \binom{10}{i} \left(\frac{1}{6}\right)^i \left(\frac{5}{6}\right)^{10-i}

and when you complete the numerical calculation you will find the probability
is about 52 in a 100. To be able to do this you need to be well versed in a
number of mathematical concepts.

From another perspective, you can also literally roll 10 dice many many times
and tally how many of the sets of rolls met the criteria. Thinking about this
experiment is much easier than reasoning about probabilities. But you'd have to
roll the ten dice upwards of 10000 times to get an accurate estimate of the
probability. Fortunately, this is something a computer is good at. Being able
to reason about this problem and, for example, write in the following Python
code you will get the same answer as the reasoning through probability theory.
In this case, computational reasoning is likely vastly simpler than what is
needed for the mathematical reasoning if you have basic programming concepts in
your toolbox.

.. code:: python

   from random import choice
   num_trials = 10000
   dice_sides = [1, 2, 3, 4, 5, 6]
   count = 0
   for trial in range(num_trials):
       if [choice(dice_sides) for roll in range(10)].count(3) > 1:
            count += 1
   print(count / num_trials)

This ability to reason about the world through computational language, is a
prime of example "computational thinking". Computational thinking adds a
complementary mode of reasoning to experimentation and mathematical modeling.
In some cases, it may even be used as a replacement for one, the other, or
both.

So this begs the question: "If we drastically increase the focus on
computational thinking to learn about mechanical vibrations, will students be
better equipped to solve real vibration problems when they leave the class?"

We believe they will, but there are a number of aspects that needed to be
changed in the course to do test this.

TODO : Worth showing a vibrations example, e.g. find frequency response via
simulation instead of frequency domain transfer function.

What We Did
===========

The course redesign required quite a number of changes to structure the
learning around computational thinking and meet the other goals. The following
presents summaries of the various changes:

Interactive Open Access Digital Textbook
----------------------------------------

We wrote a `series of 14 modules`_ in the form of Jupyter_ notebooks that serve
as the core learning resources for the course. We consider these notebooks
taken together a textbook and replace the need for a traditional static, paper
text. The design of this text has these features:

- Approximately 1 notebook per each of the 20 two hour lecture periods, i.e.
  just the right length for the 10 week course.
- The notebooks mix written text, mathematical equations, static figures,
  videos, and live Python code that can be executed to create interactive
  figures.
- Each notebook introduces a new real (and hopefully interesting) vibrating
  mechanical system as a motivation for learning the subsequent concepts.
- Computational thinking approaches are utilized if possible.
- The notebooks are licensed under the Creative Commons Attribution license to
  maximize reuse potential.
- The notebooks are intended to be used live in class with embedded interactive
  exercises.

.. _series of 14 modules: https://moorepants.github.io/resonance/
.. _Jupyter: http://jupyter.org

Software Library
----------------

The text book is accompanied by a custom Python software library called
"resonance_". We decided to create this library so that we could carefully
design the application programming interface (API) to scaffold the exposure to
the concepts we introduced in the text. The library was designed with these
features in mind:

- Provide a framework for learning mechanical vibration concepts.
- Allow students to construct, simulate, analyze, and visualize vibrating
  systems with a simple API.
- Hide Python programming details up front, but allow them to be exposed in a
  scoffolded way as the course progresses.
- Hide object oriented class construction completely.
- Include many and appropriately informative error messages.
- Performance is secondary to usability and learning.
- Structured around "system" objects that have similarities to real vibrating
  mechanical systems and can be experimented with in much the same way one
  might do in lab.

.. _resonance: https://github.com/moorepants/resonance/

Active Computing In Class
-------------------------

The notebooks were presented live in class. Each student downloaded the
notebook at the beginning of the class period for use on their laptop. The
instructor led the students through the notebooks by offering verbal summaries
and addenda via "board work" to the written text. The instructor executed the
code cells to produce various figures and then discussed them, often live
coding answers to questions. Each notebook included short exercises (about 8-10
per 2 hr period) interspersed throughout the text that were geared to assessing
students on the prior 10 minutes of instruction and reading. These exercises
had easily accessible solutions to ensure students could move forward even if
the solution was not obtained in the allocated time. We attempted to pace the
exercises such that the vast majority of the class completed them. The students
were encouraged to work together and the instructors were present to answer
questions during the exercises. The notebooks were submitted at the end of the
class for participation credit.

JupyterHub Service
------------------

We purchased a server and installed the cloud computing service JupyterHub_ for
the students to use both in and out of class for their course work. This turned
out to be a great idea for several reasons:

- Students did not have to install any software, we fully controlled the
  computation environment to ensure everything worked as desired.
- We were able to update the custom software library at any time. This allowed
  us to write the library incrementally as we created the course content. At
  one point, Kenny fixed a library bug live in class as soon as we uncovered
  it.
- We were able to utilize nbgrader_ for distribution, collection, and grading
  of the materials and assignments (see more below).

Computational Homeworks
-----------------------

We created X number of homework sets using nbgrader. TODO : tell more about the
design, etc.

Project Instead of Exams
------------------------

The previous course design had two in-class pen and paper exams. We added an
individual course project to more effectively assess the course learning
objectives and provide a realistic engineering exercise.

We originally intended to have a midterm, a final, and a course project but we
dropped the final exam due to two reasons:

1. Two exams and a project was simply too much work.
2. We gave a midterm that required live coding to solve the problems that did
   not effectively assess what the students had learned, due to student getting
   caught on programming issues more than anticipated.

Next year, I will likely remove the midterm and break the project into two
phases. The projects proved to be a much more effective method for students to
demonstrate what they had learned.

SciPy BoF
---------

We led a "Birds of a Feather" session on teaching modeling and simulation at
SciPy 2017 in Austin, Texas. There were 13 participants from a variety of
disciplines and schools. Notes from this session can be found in a `separate
blog post`_. This BoF introduced a large number best practices for teaching
these types of courses and established a network of potential collaborators.

.. _separate blog post: http://www.moorepants.info/blog/scipy-2017-bof.html

Computational Thinking Workshop and Seminar
-------------------------------------------

We held a workshop titled "Computational Thinking in the Engineering and
Sciences Curriculum" at the UCD Data Science Institute on January 5th for about
20 faculty, staff, and graduate students from a variety of disciplines around
campus. We proposed seven methods of utilizing computation to learn domain
specific concepts and the attendees developed a variety of examples from their
domains. The abstract read:

   This workshop invites faculty to think about computation in the context of
   engineering education and to design classroom experiences that develop
   programming skills and apply them to engineering topics. Starting from
   examples in signal processing and mechanics, participants will identify
   topics that might benefit from a computational approach and design course
   materials to deploy in their classes. Although our examples come from
   engineering, this workshop may also be of interest to faculty in the natural
   and social sciences as well as mathematics.

The workshop was recorded and can be viewed below along with the accompanying
slides:

.. raw:: html

   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/lfRVRqdYdjM"
     frameborder="0"
     allow="autoplay; encrypted-media"
     allowfullscreen>
   </iframe>

.. raw:: html

   <iframe
     src="https://docs.google.com/presentation/d/e/2PACX-1vTCq_A4DKcigYd8JZBTFV5YCtX_OVbKaOz_y3dgq-836_jQ4uHRP1javXpXCkE4pj5Una21Lttvkg3a/embed?start=false&loop=false&delayms=3000"
     frameborder="0"
     width="960"
     height="569"
     allowfullscreen="true"
     mozallowfullscreen="true"
     webkitallowfullscreen="true">
   </iframe>

http://allendowney.blogspot.com/2018/01/computation-in-stem-workshop.html

Additionally, Allen gave a more general seminar on "Programming as a Way of
Thinking":

.. raw:: html

   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/6noFqh7JIR0"
     frameborder="0"
     allow="autoplay; encrypted-media"
     allowfullscreen>
   </iframe>

TODO : Added slides.

What To Improve
===============

- Need classroom that is appropriate for the class activities (i.e. need tables!)
- Analytical ODEs need to be shown after the computational methods, could
  motivate students to learn more about them.

Conclusion
==========

After the first delivery of the course, a good question to ask may be "Can
students solve problems related to mechanical vibrations better than if they
were to have taken a different course?", as that is our primary objective. It
was evident from their final project that they could, but the problem was
designed by me to be solvable with the things I knew (or hoped) they'd learned.
This question is difficult to answer without a properly designed and executed
experiment, which may be something that should be done in the future. I have
received a mix of feedback on the course that encompassed students enjoying it
thorourghly to students that struggled getting past the programming
requirements.

Acknowledgements
================

This effort was supported with funding from the Undergraduate Instructional
Innovation Program, which is backed by the Association of American Universities
(AAU) and Google, and administered by UC Davis's `Center for Educational
Effectiveness`_. The funding proposal can be viewed on Figshare_.

We thank Allen Downey from Olin College for visitng and teaching us, Pamela
Reynolds at the UC Davis Data Science Initiative for hosting the workshop, Luiz
Irber for filming and editing the videos, MAE staff for the seminar setup, and
Kenneth Lyons and Benjamin Margolis for help with organizing the workshops.

.. _Figshare: https://doi.org/10.6084/m9.figshare.5229886.v1
.. _Center for Educational Effectiveness: https://cee.ucdavis.edu/
