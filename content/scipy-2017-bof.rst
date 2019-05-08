============================================
Teaching Modeling and Simulation with Python
============================================

:authors: Jason K. Moore
:subtitle: A SciPy 2017 Birds of a Feather
:description: Notes from a SciPy BoF
:date: 2017-07-20 15:15:00
:tags: teaching, modeling, simulation, jupyter, python, scipy

{% mark image %}

{% endmark %}

{% mark excerpt %}

Many instructors that teach modeling and simulation topics in a variety of
domains are turning to `computational thinking
<http://lorenabarba.com/blog/computational-thinking-i-do-not-think-it-means-what-you-think-it-means/>`__
and active learning in their classrooms. In particular, the `Jupyter Notebook
<http://jupyter.org/>`__ platform is being rapidly adopted by instructors
worldwide to deliver interactive instructional content to students. The Jupyter
Notebook arose from the scientific python community and at this year's `SciPy
conference <https://scipy2017.scipy.org>`__ we lead a "Birds of Feather"
session to connect instructors at the conference to discuss their successes and
struggles using these new teaching strategies and tools. Below are the notes
that were written by Kenneth Lyons and collaboratively edited by the session's
attendees. We hope these will be helpful to the broader community.

{% endmark %}

Overview
========

This document was initialized as a set of notes taken during the
birds-of-a-feather (BoF) session on July 14, 2017 at the SciPy conference in
Austin, Texas. We started with an overview of some potential discussion topics,
then went around the table for introductions, and spent the remaining time
discussing various issues and ideas related to teaching modeling and simulation
with Python.

Attendees
=========

+-----------------------------+--------------------------------------------------+
| Jason Moore (Organizer)     | Mechanical and Aerospace Engineering, UC Davis   |
+-----------------------------+--------------------------------------------------+
| Kenneth Lyons (Organizer)   | Mechanical and Aerospace Engineering, UC Davis   |
+-----------------------------+--------------------------------------------------+
| Charles Weiss               | Chemistry, Wabash College                        |
+-----------------------------+--------------------------------------------------+
| Philip Robinson             | Oregon Health and Science University             |
+-----------------------------+--------------------------------------------------+
| Peter Storm                 | Oklahoma State University                        |
+-----------------------------+--------------------------------------------------+
| John Conery                 | University of Oregon                             |
+-----------------------------+--------------------------------------------------+
| Michael Lange               | Imperial College                                 |
+-----------------------------+--------------------------------------------------+
| Carl Savage                 | High School in BC Canada                         |
+-----------------------------+--------------------------------------------------+
| Blaise Thompson             | University of Wisconsin                          |
+-----------------------------+--------------------------------------------------+
| Natalia (Naty) Clementi     | George Washington University                     |
+-----------------------------+--------------------------------------------------+
| Nicholas (Nick) Murphy      | Harvard-Smithsonian Center for Astrophysics      |
+-----------------------------+--------------------------------------------------+
| Geoffrey (Geoff) Poore      | Physics, University in Tennessee                 |
+-----------------------------+--------------------------------------------------+
| Kyle Sunden                 | University of Wisconsin                          |
+-----------------------------+--------------------------------------------------+

Potential Topics to Discuss
===========================

The following list of topics are a combination of those brought by the
organizers and the ones proposed during the introductions from each
participant.

-  Success stories
-  Struggles
-  Teaching methods
-  Grading/submission
-  Active learning
-  Collaboration among Universities and instructors
-  Project based versus individual
-  Students producing notebooks from scratch or from templates
-  How polished should students' notebooks be?
-  How to ensure domain principles are learned effectively with
   computation
-  Spread of student abilities
-  What is important to teach?
-  What can be taught if students do not have calculus yet?
-  Engineering students being scared of programming.
-  Matlab vs Python battle in departments
-  What prerequisites are necessary?

Teaching Challenges
===================

Students come in with a wide range of programming skills and knowledge
(different languages, different general computer literacy). How do we make sure
students have prerequisites, whether they are explicit or not?

Students feel they spend too much time on programming concepts rather than the
science, theory, etc.

Existing classes teach, for example, C -- students dislike programming by the
time they take a domain-specific class.

Student retention.  Can set up tutoring lab hours, several hours/day all week.
Restrictions like the tutor can't touch their keyboard. Don't let the tutor see
the code, student has to describe it.  Have the student move to the whiteboard
to explain the issue. Could also come to tutoring session with printed code
rather than their computer.

Doing everything openly presents the opportunity for students to copy off each
other or previous instantiations of the class.

Don't teach object oriented things (no classes etc). It is too much overhead.
John suggested not even teaching functions for a similar reason. The students
can likely use objects though without knowing what OO is.

Tab completion in the Jupyter notebook brings in the magics. This is confusing,
you should disable them.

Successes
=========

Jupyter notebooks are great for active learning. Students can fill in notebooks
together with the instructor, plus in-class group work. A computer lab is
helpful for avoiding installation issues and such.  (Ana)conda is very good for
simple installation, however. JupyterHub could be a nice solution for ensuring
the environment is consistent and up-to-date for all students, but it involves
a lot of setup.

Pair programming is helpful. Pair together strong and weak students. With
Jupyterhub, you can tell who's submitting notebooks, but you can't control
copying off one another. Mix up pairs regularly (e.g. weekly).


Have students go find a package or module and teach it to the class. They get
very excited by that. Overview of it, what it does, etc.

Scope and sequence is very import as it aids in retention of concepts. Here is
an example from Carl Savage's Physics 12 course. It should be noted that the
students have had 3 Python tutorials in Jupyter Notebooks - Basic Coding, Numpy
and Matplotlib:

Hooke's Law Lab (Second lab of course, first lab is traditional to provide me
with information on students strengthens and weakness)

#. Start with traditional lesson on the theory
#. Traditional problem set to reinforce physical concepts.
#. Jupyter Notebook on modelling data with a review on arrays, splicing
   data, graphing plus the new concept regression modelling. This is
   done through a guided in class lesson (30 min).
#. Collect data in traditional manner.
#. Model data and lab write up in Jupyter Notebook.
#. Review concepts both concept and coding.

This only adds about one hour to instructional classroom time but is the
foundation of all other labs that they will be doing in the course.  Other labs
the students do this way are: Friction on Inclined Planes, Circular Motion,
Work energy theorem and Electric Circuits.

Projects and Other Ideas
========================

Natalia is working on an engineering programming course. Engineering-focused
intro programming courses are often lacking.

What if students were self-paced? Let them work (in a long session?) and then
ask for a quiz/exam when they feel ready.

Have an interpreter open that can facilitate tinkering. Students may be
confused by adding a "sandbox" cell.

Question: for domain-specific classes, do you have an explicit module on basic
Python / NumPy / matplotlib module? Natalia's approach: give them a notebook on
basic concepts, let them get up to speed if needed. Works for grad-level but
not really undergrad? Teach basic concepts but not too abstractly. Do not try
to teach OOP. Have a set of notebooks on basic concepts, let students get
through them self-paced (works at high school level) -- don't assume they
totally understand everything you give them.

Would be great if we could have intro notebooks collaboratively edited or
centrally available.

Can show them nested for loop approach then show them vectorized operations.
Good idea to reinforce concepts with multiple approaches to a problem. Could be
overwhelming in some cases?

Definitely encourage students to make use of the internet to see documentation,
stack overflow, etc. Force writing of docstrings when they write functions.

How to make sure they learn the physical concepts and not just programming.
Spark device streams data over wifi so students can grab data on their phone.
Have a shared lab apparatus. Sabotage the device to see if they can figure out
what's wrong.

To check whether students understand the physical principles, ask them
questions about the concepts using something like Socratic and you can see how
many people answered which questions correctly. Then after than have them use
the computation in the notebook to verify their answer, for example using a
parameter sweep.

Three P's: problem posing, problem solving, peer persuasion. Starting even
further back, start with a real system, have them generate a model. The
students need to examine a physical thing and try to create the model of the
phenomena themselves.

MIT or BSD 3-clause for code, CC-BY for written materials. Two sections in
LICENSE file.

Resources
=========

- Allen Downey's work-in-progress textbook on modeling and simulation with
  Python: `http://greenteapress.com/wp/modsimpy/
  <https://www.google.com/url?q=http://greenteapress.com/wp/modsimpy/&sa=D&ust=1500342535521000&usg=AFQjCNG1pgUuiWQHOVe5x5rK6aYlbBAnSQ>`__,
  (slides: `http://tinyurl.com/yamfnlpb
  <https://www.google.com/url?q=http://tinyurl.com/yamfnlpb&sa=D&ust=1500342535522000&usg=AFQjCNFh3IU4DBEs2pbIwJBZlYNC07I0tA>`__)
- John Conery's book "Explorations in Computing":
  `http://ix.cs.uoregon.edu/~conery/eic/ <https://www.google.com/url?q=http://ix.cs.uoregon.edu/~conery/eic/&sa=D&ust=1500342535522000&usg=AFQjCNEOtEmG8QPdu-N9JDY_ZHrsQ1B1bg>`__
- Michael uses SymPy for finite difference methods:
  `https://github.com/opesci/devito <https://www.google.com/url?q=https://github.com/opesci/devito&sa=D&ust=1500342535522000&usg=AFQjCNE6CqM9eSnDatNw56g-1SA9fzh0KQ>`__
- Journal of Open Source Education (JOSE):
  `https://github.com/openjournals/jose
  <https://www.google.com/url?q=https://github.com/openjournals/jose&sa=D&ust=1500342535523000&usg=AFQjCNHrMFAc8TFs03CafLXsKbGqmZ93Vg>`__
- Coursera course on modeling and simulation using Python (starts July 25,
  2017): `https://www.coursera.org/learn/modeling-simulation-natural-processes
  <https://www.google.com/url?q=https://www.coursera.org/learn/modeling-simulation-natural-processes&sa=D&ust=1500342535523000&usg=AFQjCNGVuITx4Cdavotb34tHzQGZxx9xcg>`__
- App to broadcast live data from experiment to students:
  `https://www.pasco.com/sparkvue/ <https://www.google.com/url?q=https://www.pasco.com/sparkvue/&sa=D&ust=1500342535524000&usg=AFQjCNGuGnFbjxRrOTeYeFj0zb5S-sMkuQ>`__

Acknowledgements
================

This blog post was made possible by the Undergraduate Instructional Innovation
Program at the `Center for Educational Effectiveness`_ at the University of
California, Davis. The funding proposal can be viewed on Figshare_.

.. _Figshare: https://doi.org/10.6084/m9.figshare.5229886.v1
.. _Center for Educational Effectiveness: https://cee.ucdavis.edu/
