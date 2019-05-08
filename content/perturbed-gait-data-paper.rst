===================
My first data paper
===================

:authors: Jason K. Moore
:subtitle: Is it worth it?
:description: Some thoughts on publishing an open access data paper.
:date: 2015-04-28 10:56:00
:tags: data, gait, research, publishing

{% mark image -%}
{%- endmark %}

{% mark excerpt %}

I have been working on a `gait control identification project`_ since I started
as a post doc at Cleveland State University in July 2013. Last night the `first
publication`_ from this effort was published in `PeerJ`_. The paper is
unconventional in that it is solely about the data we collected and does not
include any research findings concluded from the data. We published this data
set for a number of reasons, many explained in the paper, but I'd like to share
one reason that isn't in the paper.

.. _gait control identification project: <http://hmc.csuohio.edu/projects/gait-control-id>
.. _first publication: https://peerj.com/articles/918/
.. _PeerJ: http://peerj.com

{% endmark %}

Ton, my PI at CSU, gave me a starting point for a project when I started work
in July 2013. This involved collecting data and applying a "simple" direct
identification method to identify a feedback controller in gait. [#]_ I first
developed the methods on some existing unperturbed data sets and they showed
promise. Then we collected the data. At this point I was about nine months in
to my postdoc. It took a while to get to this point; probably longer than
necessary due to me starting off with zero computational tools for gait analyses
and being in a fresh brand new lab with lots of equipment bugs to work around
and non-research related tasks to attend to. But once I got all the data we
took a look at the results and I came to the conclusion that the results were
crap. The method produced something but I was not able to come up with any
reasons that prove the results actually produced a real feedback controller (it
was not capable of controlling anything). At this point I think I also
convinced Ton that this method should be abandoned. So I was left with no
results but a very meticulously collected and unique data set.

I essentially wanted to present the data, maybe independently, from the get go
so the fact that the results were weak reinforced that. But I also needed to
come up with something new to do with the data, as a data paper wasn't likely
to gain many strides in the academia job race. So I wrote a proposal for the
`NCSRR program`_ for the summer to try indirect identification with the data
and the Opensim team. It was then conference season and I did my rounds showing
off the less that stellar results, making it seem like it was something it
wasn't. I spent most of the summer on the new methods and started a draft of
the data paper in August 2014. The Biomech-L users `helped me`_ get started
finding previous examples of public gait data.

.. _NCSRR program: http://opensim.stanford.edu/support/scholars.html
.. _helped me: http://biomch-l.isbweb.org/threads/27347-Looking-for-existing-public-gait-data

I was going to submit the data paper to F1000Research because they seem to be
one of the few journals that explicitly says they will accept data papers and I
had an OK experience with them on a `software paper`_. But PeerJ launched a
deal for a free article at the end of the year and we decided to give them
shot, as there model and papers are super attractive.

.. _software paper: http://f1000research.com/articles/3-223

The process at PeerJ was excellent in general. They have a fast review turn
over, there are a lot of legitimate well-known academic editors, the web
interface to the articles is awesome (section commenting, article stats, etc.)
and the model of a $100-$300 for lifetime open access publishing is awesome. I
wrote to PeerJ and showed them my data paper draft to see if it was even within
scope, i.e. would they accept a "data paper". They said that it was and that I
should submit by the December 19, 2014 deadline so we changed our direction and
posted a preprint_.

.. _preprint: https://peerj.com/preprints/700/

My only complaint with PeerJ was that they have horrible support for LaTeX
submissions. I found that surprising being that they seem technologically savvy
otherwise. Their excuse is that 90% of submissions in with MS Word, so there is
little incentive to support other submission types. This is unfortunate for me
because I've been creating "papers as software" for a long time now and each of
my papers is essentially a software build that separates content and
presentation and self-generates all of the figures and tables from raw data
(e.g. see the `repo for the data paper`_). MS Word and other WSYSWIG word
processors are not suited for this method. I'm not sure why they don't pay
someone to develop a LaTeX template that generates their PDF style from the get
go. They probably wouldn't have to waste so much time typesetting.

.. _repo for the data paper:  https://github.com/csu-hmc/perturbed-data-paper

The reviews for the paper (which are `publicly available`_! +1 for PeerJ) were
interesting. Two of the three seemed to reject the paper on the stance that you
have to have results to publish and that we were simply slicing out the methods
section of a normal paper so that we can get two publications for the price of
one. The third reviewer gave us praise and said that other researchers should
follow suit. The editor made the decision that only minor revisions were
needed. This was confusing because it seemed that two of three reviewers were
outright rejecting the paper, yet the editor moved it forward. I had a few
email exchanges with Pete Binfield, the PeerJ founder, asking whether they had
a stance on data papers so I could determine if these reviewers were going to
be able to put up a full blockade on the paper. Pete would not take a stance on
whether "data papers" were valid publications, so I just submitted a rebuttal_
to see what happened.

.. _publicly available: https://peerj.com/articles/918/reviews/
.. _rebuttal: https://github.com/csu-hmc/perturbed-data-paper/blob/master/first-review-response.rst

Only the two dissenting reviewers replied to the rebuttal even though the
majority of the changes in the paper were with respect to the third reviewer's
thoughtful and detailed comments. One reviewer seemed to still reject the paper
but the academic editor accepted the paper anyways. It was less than clear
whether the reviewers were rejecting the paper (their words made it seem so)
during the process and it always conflicted with the editor's response. This
may have been due to the fact that you couldn't see whether each reviewer had
selected specific options like "reject", "accept with minor revisions", "accept
with major revisions", etc.

All in all the publication process took 130 days, which is a lot faster than
many journals (most of my submissions take closer to or more than a year). So
kudos to PeerJ for that. I've also tracked all of my time for the past few
years. I don't have data that is fine grained enough to tell exactly how much
time I put into everything that culminated in this paper, but it seems to be on
the order of 500 hours which is only like 13 weeks of work, yet it spanned
something like 94 weeks. I'm not sure what to make of that. It's disheartening
thinking that, at maximum efficiency, I could have done all this in half a year
instead of almost 2 years (of course I did ton of other things during that time
span but I haven't maximized my journal article to time spent ratio at all).

I am optimistic that this paper will have some impact. I believe that the data
can be used for a variety of studies. For example, I think someone could redo
the results in `this paper`_ with our data and make a stronger claim. I hope that
being extremely meticulous and detailed about the data collection and it's
presentation will make it as easy as possible to reuse. There are are some
examples of this with biomechanical data but it is not apparent that much of it
gets reused. We'll just have to wait and see. I also hope I can make some use
of the data. I am going to publish my "null results". I'm not sure it is worth
the time it is taking to making it publishable though, I don't see the pay off
being high.

.. _this paper: http://rsbl.royalsocietypublishing.org/content/10/9/20140405.long

I really like the idea of creating beautiful data sets and explaining them in
enough detail for broad reuse but the amount of effort needed to do so is large
and the payoff, in academic terms, is likely to be much less than a profound
results paper. But the payoff for the biomechanics community and their research
may be worth it, even if the credit structure doesn't recognize these kinds of
contributions. I'm inclined to continue trying to write data papers but if they
show no payoff, it may be a just be a career killer because too much time is
needed to make the data actually reusable.

Ok, enough rambling, time to get back to my profound research findings. :)

.. [#] Ton wrote to me on July 10th (second day of work) about this and the
   final statement in the email was "These things are never as simple as they
   first seem."
