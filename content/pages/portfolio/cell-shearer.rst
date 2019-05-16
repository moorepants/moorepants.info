---
title: Cell Shearer
subtitle: shear your blood
description: a device that applies shear stress to fluids
startdate: !!timestamp '2007-08-01 00:00:00'
enddate: !!timestamp '2009-08-31 00:00:00'
---

{% mark image -%}

.. image:: {{ media_url('images/fancy-cell-shearer.png') }}

{%- endmark %}

{% mark excerpt %}

Biomedical blood cell shearing device machine design.

{% endmark %}

While I was employed at the student machine shop at UC Davis my supervisor
arranged for me to work on a design project with `Anthony Passerini`_ and his
students in my "spare" time. This ended up being quite a complex little machine
that was designed to apply known shear forces to a fluid through a rotating
cone.

.. _Anthony Passerini: http://www.bme.ucdavis.edu/people/departmental-faculty/profiles2/tony-g-passerini/

The design was mostly an attempt to recreate the cell shearing machine
constructed by Blackman for his 1998 dissertation work at the University of
Pennsylvania. His machine is somewhat documented in his dissertation and
accompanying papers, but not in enough detail for full reproduction.

The design criteria for the tolerances of the cone/fluid interaction were
extremely tight and most of the work was spent figuring out ways to ensure the
relative dimensions of the cone and plate.

.. image:: {{ media_url('images/cone-diagram.png') }}

The principle of operation is based around rotation of a shallow cone in a
fluid which theoretically generates a linear variation in shear stress with
respect to the height of the cone.

.. image:: {{ media_url('images/cell-shearer-fea.png') }}

Downloads
=========

- 2010 Poster Presentation [pdf__]
- Working drawings [pdf__]
- Assembly drawings [pdf__]

__ {{ media_url('docs/DeVerse2010.pdf')}}
__ {{ media_url('docs/cell-shearer-08-11-12.pdf')}}
__ {{ media_url('docs/cell-shearer-assembly.pdf')}}
