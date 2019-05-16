=========================
Langley Full Scale Tunnel
=========================

:subtitle: behemoth of wind machines
:description: Work I did at the NASA full scale tunnel.
:startdate: 2004-06-01 00:00:00
:enddate: 2005-08-31 00:00:00

.. image:: {{ media_url('images/lfst-bwb.jpg') }}
   :class: img-rounded
   :width: 640

Work at the Langley full scale tunnel.

My senior design project advisor, Dr. Drew Landman, at Old Dominion University
offered me a unique internship opportunity at `NASA Langley's Full Scale Tunnel
<http://en.wikipedia.org/wiki/Full-Scale_Tunnel>`_ the summer after I had
finished my major coursework at ODU\ [#minor]_. The tunnel was opened in 1931
and has a `long and notable history
<http://crgis.ndc.nasa.gov/historic/30_X_60_Full_Scale_Tunnel>`_ in the field
of aeronautics but by the end of the century NASA's activities at the Full
Scale Tunnel, or 30 x 60, had ramped down to almost nothing. At this point,
Dean James Cross at ODU negotiated a deal with NASA to operate the tunnel for
research and teaching purposes and their business plan included funding the
operations by selling wind tunnel time to racecar teams, primarily `NASCAR
<http://en.wikipedia.org/wiki/NASCAR>`_\ [#stockcar]_. This allowed many
students to work with testing equipment that was typically well out of reach
and I was one of the fortunate to spend some time there. These fact sheets give
more info about the tunnel: one_, two_.

.. _one: http://www.nasa.gov/centers/langley/news/factsheets/30X60.html
.. _two: http://www.nasa.gov/centers/langley/news/factsheets/fst_fs_prt.htm

.. figure:: {{ media_url('images/lfst-car.jpg') }}
   :class: img-rounded
   :width: 640

I worked at the tunnel from June 2004 to August 2005 in both part-time and
full-time positions. My primary task under Dr. Landman's guidance was to design
a full scale automotive balance that could measure all six degrees of force
(three forces and three moments) acting on the car while under aerodynamic
load. The wind tunnel had a 30' x 60' open cross section with wind speeds
approaching 100 mph. Dr. Landman had designed and oversaw the construction of
the first balance used in the full scale tunnel some years before I arrived but
it couldn't measure all of the forces and moments. So we designed a new balance
that could measure everything to keep up with the competition from other
racecar wind tunnels. But just as we had finished the design, the powers that be
shut down the project. Luckily, Dr. Landman was able to negotiate a cheaper
alternative based in the 14' x 22' subsonic tunnel and we proceeded with the
project and redesigned the balance with slightly fewer force measuring
capabilities to save money.

.. figure:: {{ media_url('images/lfst-final-balance.jpg') }}
   :class: img-rounded
   :width: 640

   A CAD model rendering of the full final balance design mounted to the top of
   the 14' x 22' turn table system.

I modeled the structural details using Autodesk's Inventor software package and
wrote a detailed stress report for NASA qualification on every critical nut and
bolt in the assembly using standard stress analyses practices and FEA analysis
based on ANSYS which was provided with the Inventor software.

.. figure:: {{ media_url('images/lfst-balance-fea.jpg') }}
   :class: img-rounded
   :width: 640

   An image from the stress analyses report showing overall deformation of the
   metric portion of the balance while under maximum loading.

We custom designed the flexures for the load cell mounts with safety mechanisms
for overload protection. There were two load cells measure lateral force and
the vertical moment, one load cell measuring drag force, and four load cells
measure down force at each wheel pad.

.. figure:: {{ media_url('images/R1-00.jpg') }}
   :class: img-rounded
   :width: 640

   One of the three horizontal load cell rods showing the flexures and overload
   protection.

I also drew up detailed part and cut lists working directly with fabricators on
the construction details. Unfortunately, I moved away to grad school before
ever seeing the whole thing assembled and put into practice. But I did finally
drop by in December 2007 and got to see the completed balance. The balance was
used for testing for some time at the 14' x 22' tunnel, but the competitors
rolling road balances quickly made our balance obsolete.

.. figure:: {{ media_url('images/lfst-finished-balance.jpg') }}
   :class: img-rounded
   :width: 640

   Drew and I standing on the finished balance at the 14' x 22' wind tunnel.

Sadly, the Full Scale Tunnel `was demolished`_ in 2011 but not after a long and
prosperous life.

.. _was demolished: http://www.nasa.gov/centers/langley/news/researchernews/rn_LFST16ftdemo.html

The following gives a brief over view of my work at LFST:

- Extensive design, modeling and drafting with Autodesk Inventor.
- Designed a portable floor system for a car balance.
- Designed a six degree of freedom full scale car balance.
- Wrote stress analysis reports for NASA specifications.
- Test-model design, fabrication and repair.
- Support in daily activities (test preparation, taking data, etc.).

.. [#minor] I had finished my mechanical engineering requirements by June 2004 but
   stayed one more semester, Fall 2004, to complete Philosophy and Mathematics
   minors.

.. [#stockcar] The stock car racing that grew out bootlegging and delivering
   moonshine during prohibition in the Southern United States. Some of which
   happened in the county I grew up in.
