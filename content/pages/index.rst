---
extends: columns.j2
default_block: main
title: moorepants
subtitle: a website
description: webspace de moorepants
---

<div class="row">
	<div class="span12">
{% filter restructuredtext -%}
.. image:: {{ media_url('images/headshot.jpg') }}
   :class: img-rounded pull-right

moorepants /mʊərpænts/
	 A reverend, a wizard, a bicyclist, a doer. Raised among the tobacco fields
	 of southern Virginia, now exploring the world thinking, learning, teaching,
	 absorbing, creating. Plus, his mom claims he is a super duper guy.
{%- endfilter %}
	</div>
</div>

</section>
