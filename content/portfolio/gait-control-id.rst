---
title: Gait Control Identification
subtitle: what keeps us from falling?
description: Details about my post doc work at Cleveland State University
startdate: !!timestamp '2013-07-08 00:00:00'
---

{% mark image -%}

.. image:: http://www.moorepants.info/presentations/2014/DW2014/img/control-system-detailed.png
   :class: img-rounded
   :align: center

{%- endmark %}

{% mark excerpt %}

During my post doc at Cleveland State University, I worked with Ton van den
Bogert and developed methods to identify the human's controller during gait. We
developed both direct and indirect identification methods and methods for
identifying a gain gait scheduled controller for planar walking. The motivation
was to develop a controller that could possibly be used in powered lower
extremity prostheses, such as an exoskeleton.

{% endmark %}

Publications
============

- Moore JK, Hnat SK, van den Bogert AJ. (2014) An elaborate data set on
  human gait and the effect of mechanical perturbations. PeerJ PrePrints 2:e700v2
  http://dx.doi.org/10.7287/peerj.preprints.700v2 [`source repository
  <https://github.com/csu-hmc/perturbed-data-paper>`__]
- `Quiet standing control identification paper draft <https://github.com/csu-hmc/inverted-pendulum-sys-id-paper>`_

Data
====

All of the data collected for this study is published under the Creative
Commons Zero license on Zenodo:

Moore, Jason et al.. (2014). An elaborate data set on human gait and the effect
of mechanical perturbations. ZENODO. `10.5281/zenodo.13030
<http://dx.doi.org/10.5281/zenodo.13030>`_

Software
========

GaitAnalysisToolKit
-------------------

.. image:: https://pypip.in/version/gaitanalysistoolkit/badge.svg
    :target: https://pypi.python.org/pypi/gaitanalysistoolkit/
    :alt: Latest Version

.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.13159.svg
   :target: http://dx.doi.org/10.5281/zenodo.13159

This Python package provides various classes and functions for dealing with
typical gait data, e.g. marker and force plate time series. It contains a
module that parses and organizes the data outputs from Motek Medical's
products.

- `Documentation <http://gait-analysis-toolkit.readthedocs.org>`__
- `Source Code <https://github.com/csu-hmc/GaitAnalysisToolKit>`__

opty
----

``opty`` is a Python library for optimal control and parameter identification
of dynamic systems. It is capable of large scale problems, such as
identification from tens of minutes of gait data.

- `Source Code <https://github.com/csu-hmc/opty>`__

Gait Identification
-------------------

This repository contains Python scripts and IPython notebooks for exploratory
analysis in gait control identification.

- `Source Code <https://github.com/moorepants/walking-sys-id>`__
- `Rendered Notebooks <http://nbviewer.ipython.org/github/moorepants/walking-sys-id/tree/master/notebooks/>`__

Talks
=====

- Indirect Identification of Human Control During Walking, NCSSR Visiting
  Scholar Kickoff, July 15, 2014 [`slides <http://www.moorepants.info/presentations/2014/ncssr-kickoff/>`__]
- Identification of human control during walking, Dynamic Walking, Zurich,
  Switzerland, June 10, 2014 [`slides <http://www.moorepants.info/presentations/2014/DW2014/>`__]
- Identification of human control during walking, TU Delft, Netherlands, June 6, 2014
  [`slides <http://www.moorepants.info/presentations/2014/tu-delft-robotics-talk-2014>`__]
- Identification of human control during walking, Midwest American Society of
  Biomechanics Conference, March 4 2014, [`slides <http://www.moorepants.info/presentations/2014/masb-gait-control-id>`__]
