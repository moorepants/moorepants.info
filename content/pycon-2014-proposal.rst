===========================
PyCon 2014 Walking Proposal
===========================

:authors: Jason K. Moore
:subtitle: just a little too late
:description: I waited too late to try to submit this talk to PyCon 2014.
:date: 2013-09-16 10:16:00
:tags: python, pycon




I wrote up a last minute PyCon 2014 proposal last night at 11:30 and pressed
save at 24:00...which was too late. Here are the details so I can save it for
another time. I did manage to submit a tutorial on PyDy, but I think that has
a much lower probability to be accepted.


Using Python to Understand Human Motion and Control During Walking

Python is a dominate tool in our human motion and control laboratory. This talk
will demonstrate methods of dealing with and analyzing typical datasets
collected in human walking experiments. It will cover data management of
discrete times series, typical gait analysis computations, model simulation,
and system identification using open source software written in Python.

Attendees will come away with a better understanding of managing high frequency
time series data of dynamical systems and the most appropriate Python tools for
analysis. They will also get a sense of how to generate and wrap dynamic models
for rapid simulation and visualization and use these models for prediction and
system identification.

Human dynamics during walking are typically measured with motion capture
systems or inertial measurement units for the kinematics (positions, angles,
rates, accelerations) and force plates for the ground reaction forces. This
data comes in the form of high frequency (100-1000hz) time series streams.
Furthermore, the human can be modeled using Newton's laws to show the
relationship in the motion and the forces. These models paired with the
measured data and system identification routines can be used to predict the
human's control system.

We use a Python to bring the data, models, and identification techniques into a
completely open and reproducible scientific work flow and utilize a variety of
tools from the SciPy stack and custom packages for walking specific analysis
and system identification. We will go over the tool chain from data management
and storage to data analysis and presentation.

- Introduction to human motion and control
- The reproducible workflow
- Tools: IPython, Matplotlib, PyDy, OpenSim, DynamicistToolKit, SciPy, NumPy,
  python-control
- Data types
- Data management: generalized human motion online database
- Gait analysis
- Walking models and C wrapping
- System identification of non-linear systems
- Interactive web based sharing of research results
- Publishing scientific papers with Python
