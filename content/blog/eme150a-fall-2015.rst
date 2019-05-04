---
title: Teaching Mechanical Design
subtitle: a first attempt
description: Description of what did and didn't work in teaching Mechanical Design.
created: !!timestamp '2015-12-14 08:01:00'
tags:
    - teaching
    - education
    - ucd
    - engineering
---

{% mark image -%}
{%- endmark %}

{% mark excerpt %}

My first quarter as a lecturer at UCD ended this past Friday with my final exam
for my mechanical design course. I think the quarter went really well and that
my students developed some solid design skills. Mike Hill, a veteran Prof. in
our department, hit the nail on the head when he described the quarters as like
being on a treadmill. It definitely felt like that, even though I was only
teaching one new course. But I thrive in environments where others are
expecting a lot from me and had a lot of fun developing and leading the course,
among the other things that I've been working on. This post will cover the
educational aspects of this course, what I tried, and what I learned.

{% endmark %}

Course Objectives
=================

The course's main objective is to develop the student's ability to design
mechanical elements and structures with the prevention failure due to static
and dynamic loads as a primary design concern. We begin the quarter learning
about `predicting stress and strain in mechanical elements
<https://en.wikipedia.org/wiki/Strength_of_materials>`_ and during the second
half work through predicting static and fatigue failure based on the stresses
and material properties. Additionally, the students worked through two
projects: reverse engineering everyday human-made things and the design of a
bicycle rack for the front of a bus.

I started about a week before the class began with Mike Hill's and Jim Schaaf's
notes and materials as a foundation. They both generously provided all of their
materials, which helped significantly. I used a combination of their lecture
schedules and project ideas too.

My course objectives were mostly copied from from Mike and Jim's:

   1. To develop your analytical skills and intuitive judgment in mechanical
      design and the evaluation of structural integrity.
   2. To improve your skills in identifying and using appropriate resources in
      engineering design and failure analysis.
   3. To expose you to open-ended design problems that require conceptual and
      analytical problem solving and documentation of a design solution.
   4. To enhance your skills in engineering writing.

These still seem good, but for future classes I'll change the last one to:

   To enhance your skills in engineering communication.

because I push the students to develop their graphical/visual, written, and
oral engineering communication skills.

It is nice to step back, reflect, and think about whether the course met these
objectives. I can only answer this from my observation of the course assignment
results. The final project report and the exam results clearly indicate that 1
and 2 were met, except maybe for the "intuitive judgment" part, which I didn't
explicitly check for or even try to teach. By comparing their project 1
analyses with the project 2 analyses, a strong growth seems to have occurred.
Number 3 was met by the second project for the course and 4 was shown by the
drastic improvements in the project reports over the course (4 memos, two
reports, and a one report draft).

Course Content
==============

I used a combination of a public `course website`_ and Smartsite (Sakai_ 9) to
deliver content and materials to the class. I did my best to share any
non-private materials on the public website for reuse. All of the content there
is licensed in the public domain CC0_. This includes the syllabus, the project
descriptions, the course notes, lesson plans, lesson preparation notes,
homework problems, and some other resources. The course was managed with the
static site generator Pelican_, which I enjoyed using and even developed a
`homework generation script`_. On Smartsite, I shared copyrighted exam,
homework, and quiz solutions in addition to email announcements, and Q&A.

.. _course website: http://moorepants.github.io/eme150a-website/
.. _Sakai: https://sakaiproject.org/
.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _Pelican: http://blog.getpelican.com/
.. _homework generation script: https://github.com/moorepants/eme150a-website/blob/master/fabfile.py#L99

I made use of the document camera during lectures, writing with four colored
fine tip markers on white paper and immediately scanning the notes after class
and posting them online. I encouraged the students to listen in class and take
notes only on things I didn't write down. Some did this, but many wrote
everything anyways. The document camera has the disadvantage that only one
sheet can be shown at a time and I had to learn to wait for people to finish
writing. I also have poor handwriting and some students complained about that,
although my initial admission of this probably prompted the complaints. I am
one of the last engineering generations that actually learned lettering, but
CAD and computers were already too dominant in the late 90's for that to stick
with me. Nice handwriting from engineers is probably a lost art.

We made use of the first 6 chapters of the 10th edition of `Shigley's
Mechanical Engineering Design`_ book. This is what past instructors have used
and is also the standard text for this type of course. I'm going to work this
summer on developing a textbook myself for the class on the UCD Chemwiki_
system so that we can wean away from the closed expensive ($275) content.

.. _Shigley's Mechanical Engineering Design: http://www.amazon.com/Shigleys-Mechanical-Engineering-Design-McGraw-Hill/dp/0073398209
.. _Chemwiki: http://chemwiki.ucdavis.edu/

Active Learning
===============

At the beginning of the course I imagined segmenting the 50 minute class
periods into a series of 10 minutes of instruction followed by 10 minutes of
student doing. The "student doing" would mostly be based around peer learning
on short conceptual problems. I launched the class with an activity
that took the entire first period and the first couple of weeks I reasonably
pulled off the more active classroom. Unfortunately, this didn't last long. I
quickly realized I wasn't going to get through the quantity of material and my
lecture preparation shifted to 5 and 6 AM the morning of class (i.e, barely
staying on the treadmill). Thus after a few weeks the course mostly reverted to
me lecturing for 50 minutes straight.

To pull this off in the future, I need to figure out how to provide the
students with ways to watch me doing example problems outside of class and
provide an incentive to read the relevant material before coming to class. This
could then free up time during class to execute more learning activities. To do
this I'm going to use a touchscreen tablet/stylus with voice over to generate
videos of me doing examples that I can distribute online.

I did manage to co-opt many of the discussion sections for activities. Instead
of simply having the TA go over example problems, we spent time on design
ideation, technical communication, and building team capacity. The ideation
session for Project 2 went especially well. One student was so excited to do
this that they were shaking in their seat. I had the students go through a
question generation with sticky notes, followed by team discussion and sorting
of the information, and closed with a sketching session where students modified
each other's designs strictly with additions. They'll get more of this from me
in the capstone design course next quarter.

Time
====

I track my time with Hamster_ and it seems I spent around 375 hours prepping
and running this course. That comes out to about 30 hours per week over 12
weeks (1 week prep, 10 week course, 1 week finals). This is about the same
amount of time it took me to develop my `last full course`_. A few colleagues
confirmed that is typical, i.e. teaching for the first time takes most of your
time. I averaged about 53 hours of actual work time per week. This is the
breakdown of time for the course:

- 70 hrs: Lecture preparation
- 50 hrs: General course preparation (projects, materials, website, etc)
- 41 hrs: Lecture
- 36 hrs: Homework prep (created most of my own problems)
- 35 hrs: Grading
- 30 hrs: Post lecture processing (scanning/fixing notes)
- 18 hrs: Office hours
- 16 hrs: Final exam preparation
- 13 hrs: Midterm exam preparation
- 11 hrs: Instructor meetings
- 8 hrs: Piazza (answering questions)
- 47 hrs: Other stuff

.. _Hamster: https://github.com/projecthamster/hamster
.. _last full course: http://www.moorepants.info/jkm/courses/eng4/

In addition, my excellent TA spent around 10 hrs per week on grading, office
hours, discussion/activity participation, etc.

When I'm teaching two or three courses per quarter, this is going to have to be
reduced significantly. I can't imagine having to develop two courses at once,
but I hear that was normal in the early days of the department and also for
teachers at community colleges.

Reverse Engineering Project
===========================

During the first five weeks the students work on a mostly individual `reverse
engineering project`_. The goals are to:

- improve the student's ability to identify the needs a product solves
- identify what decisions the designers made to have it meet these needs
- improve technical communication

.. _reverse engineering project: http://moorepants.github.io/eme150a-website/pages/project-one-reverse-engineering.html

To do this I had the students:

- Identify one engineering aspect of 50 human-made things in their sketchbook
  with an emphasis on visual communication. (Similar to 100 ideas in an hour
  ideation sessions)
- Choose five of the items and develop more details about the need and design
  in their sketchbook.
- Present their top two items to their team in 2 minute lightning talks for
  team feedback.
- Choose one item to write a three page draft report in Google Docs detailing a
  single design.
- Peer review each team members' report with at least two positive and two
  negative comments.
- Finally, turn in a final three page professional report (with appendices)
  about the single design.

Some students complained that 50 items was way too much work, but I also seemed
to have failed to communicate that a single equation or a single sketch was
sufficient per item. They didn't realize that quantity over quality was what I
was after. I had my TA give an example item that was a little too extensive and
they proceeded to copy that format for every one of their items, causing
themselves more work than necessary. If I do this again, I'll need to give a
variety of different examples that are simpler or maybe reduce the # of items.

Overall, the final reports were very good. The main issues were clarity and not
using graphics effectively. If "A picture is worth a thousand words" is true,
few realize that it takes the same amount of time to prepare that picture as it
does to write and hone the 1000 words. I think we focus too much on teaching
CAD in engineering and forget to actually teach other means of graphical
communication, which are often needed more than CAD drawings are.

We made use of Google Docs commenting and suggestions features for the peer
reviewing. The peer review and my comments on their drafts helped them improve
the quality of the final report significantly.

We graded the drafts by copying them via Google Docs and using the commenting
features. This seemed to work pretty well and was all electronic. I had them
submit a PDF for the final report submission but a handful of reports'
formatting didn't stay intact in the GDocs PDF export, which seems like a bug.

Unitrans Bus Bicycle Rack Design Project
========================================

The `second project`_ was an open ended mechanical design task that a teams of
3 or 4 students worked on collaboratively. One previous course project that is
commonly used by other instructors is to design a bicycle rack for an
automotive hitch socket. This is a nicely scoped project because most of the
design simply involves the stress analysis of cantilever beams. But for better
or worse, I decided to have a similar but bit more complex project: the design
of a bicycle rack for the front of a Unitrans_ bus.

.. _second project: http://moorepants.github.io/eme150a-website/pages/project-two-unitrans-bicycle-rack-design.html
.. _Unitrans: http://unitrans.ucdavis.edu/

To give the students some hands on time inspecting a bus, I contacted the
general manager of Unitrans, Anthony Palmere, and asked him if he'd let my
students come inspect a bus. He agreed, but we got way more than just some time
with a bus. Anthony connected us with Andy Wyly, the Maintenance Manager, and
he spent two hours with us at the Unitrans shop where he hoisted a bus on the
lift and removed the bumper for the students to inspect. Andy answered their
questions about buses and bicycle racks, showing us some bicycle rack designs
and closed with a great tour of their facilities. The students seemed to really
dig this. Andy also came an judged the final presentations.

The project commenced and the students were tasked with turning in a single
page memo each week from the teams based on different topics: a plan, design
concepts, static failure, and fatigue failure. The students struggled with the
first couple of memos when trying to keep them concise and focused. This
improved significantly in the later two memos after they'd gotten feedback.

For the fatigue analysis, my TA rode one Unitrans route and used his smart
phone to collected acceleration data of the front of the bus. We withheld the
data for a while hoping that the students would start asking for information to
compute fatigue failure, but they didn't (at least not early enough). We
provided them with the acceleration data and they made use of it estimate the
fluctuating stresses in their designs.

.. image:: {{ media_url('images/eme150a-fall-2015/bus-accel-data.png') }}
   :class: img-rounded
   :width: 600px

The students worked super hard on the project and every team did an excellent
job on the final presentations and reports. I was quite proud of their
demonstration of strong applied engineering in their designs and their
application of the course content for design iteration. Here is a little eye
candy from their presentations/reports of the different designs:

.. raw:: html

   <table>
     <tr>
       <td>
         <img width="400 px" src={{ media_url('images/eme150a-fall-2015/capscrew.png') }} />
       </td>
       <td>
         <img width="400 px" src={{ media_url('images/eme150a-fall-2015/crankshaft.png') }} />
       </td>
     </tr>
     <tr>
       <td>
         <img width="400 px" src={{ media_url('images/eme150a-fall-2015/flywheel.png') }} />
       </td>
       <td>
         <img width="400 px" src={{ media_url('images/eme150a-fall-2015/helical-spring.png') }} />
       </td>
     <tr>
       <td>
         <img width="400 px" src={{ media_url('images/eme150a-fall-2015/planetary-gear.png') }} />
       </td>
       <td>
         <img width="400 px" src={{ media_url('images/eme150a-fall-2015/roller-bearing.png') }} />
       </td>
     </tr>
     <tr>
       <td>
         <img width="400 px" src={{ media_url('images/eme150a-fall-2015/weldment.png') }} />
       </td>
       <td>
       </td>
     </tr>
   </table>

I believe the project really allowed the students to exercise their mechanical
design muscles but there are some things that need thought and improvement. The
project is a pretty significant design task and since most of the designs end
up with complex statically indeterminate loadings, the stress analysis is
significantly harder than the simple cantilever modeling required for a
automotive bicycle rack design. This is good and bad. The students are tasked
with tougher modeling choices but the stress to figure it out is higher. Few of
the students came to office hours early enough to get individualized help on
the modeling decisions. Next time I will devote an activity or lecture or more
to modeling. They really need some examples of taking real machine elements and
making simplifications for stress/strain modeling purposes. All of the
homeworks and examples I give are already in the simplified form, which leaves
them just guessing how to do the actual modeling step.

Feedback
========

I collected a large amount of feedback during the course. Each Friday I passed
out sticky notes to the class and had them write one positive comment, one
negative comment, and how many hours they spent outside of class on the course
work and preparation. This was anonymous feedback. Before each exam I collected
votes on review topics. I also had the students fill out a midterm reflection
when I returned the midterm. And finally, I collected the standard course
evaluations for my department.

The weekly feedback was very constructive and I used it to improve a number of
things during the course like:

- Providing more examples.
- Better presentation of the materials with the document camera.
- Sticking with the same pace (I got equal "too fast" and "too slow" comments).
- Clarifying a variety of misconceptions.
- Focusing on confusing topics.

The exam review topics made it easy to focus on the things the students felt
most confused about. That worked out well.

The `midterm reflection`_ was collected and passed back to the students a week
or so before the final exam so that they would think about better ways to study
and prepare. It also included some feedback for us to improve the preparation
for the exam from the instructor's side. It isn't really possible to tell if
this worked at all, but education research `seems to say that it does`_. I also
found no correlation from hours spent prepping for the midterm and the
student's grades, which was surprising.

.. _midterm reflection: https://docs.google.com/forms/d/1ohm-HJWNVI8CqLaMotXXZoJs6dhwMOJD36QS79ooAWU/viewform
.. _seems to say that it does: https://teachingcommons.stanford.edu/teaching-talk/exam-wrappers

The standard department course evaluations had differences than the feedback I
collected myself (22/27 response rate), probably because I asked for both
positive and negative comments, unlike the evaluations. For the questions that
only had ratings from 1 (strongly disagree) to 5 (strongly agree), these were
the scores:

- 4.55/5.00: I feel comfortable asking questions and speaking with my professor.
- 4.23/5.00: The course builds understanding of concepts and principles.
- 4.05/5.00: Please indicate the overall educational value of the course.
- 4.00/5.00: This course is well organized.
- 3.95/5.00: The exams are reasonable in length and difficulty.
- 3.95/5.00: I am satisfied with how much I learned in this course.
- 3.86/5.00: I am generally pleased with the text(s) required for this course.
- 3.73/5.00: Please indicate the overall teaching effectiveness of the instructor.
- 3.67/5.00: The instructor explains concepts clearly.
- 3.45/5.00: The course assignments are reasonable in length and difficulty.

My highest rating was 4.55/5.00 for "I feel comfortable asking questions and
speaking with my professor.", which felt nice. I asked the students to call me
by my first name and generally try to treat them as a collaborator on their
education as opposed to a subordinate. So that seems to have worked. The worst
rating was for the length of the assignments, although it averaged between
"neutral" and "agree". The average amount of work per week they reported was 15
hours. This was a 4 unit course, so the minimum from the `Carnegie Rule`_ says
the total work should be about 12 hours (including class time). Note that this
evaluation was collected during the last week of class when the final was
coming up and the final project was due. The data I collected weekly for
outside class time spent averaged to about 8 hours, so they reported 3 more
hours on the course eval than what they reported during the course. If our
engineering students take four 4-unit courses per quarter, the Carnegie rule
suggests they should be putting in 48 hrs of work, which is extremely heavy.
I'm guessing they normally take three courses per quarter: 36 hrs.

.. _Carnegie Rule: https://en.wikipedia.org/wiki/Carnegie_rule

For the free form questions here are some summaries:

Was your previous course work adequate preparation for this course (explain)? YES/NO
   Everyone said "Yes" and pointed out that ENG 104 (Strength of Materials) and
   even ENG 35 (Statics) and ENG 45 (Material Science) were useful. Some said
   they struggled from weaker ENG 104 backgrounds.
Which parts of this course should be emphasized the most?
   Some said that we should've only focused on the second half of the class
   (static and dynamic failure) and that the first part was too much of a
   review.
What comments do you have concerning the content and grading of examinations and homework?
   Most said that this was fair. One said the expectations for reports wasn't
   clear. Couple commented on having to memorize equations for the midterm
   was a pointless activity.
Please comment on the instructor’s presentation of course material.
   Good that notes were posted online, my handwriting is sloppy, doc camera
   doesn't show old notes long enough, poor prep with lots of mistakes and
   revisions, well organized and helpful, well done, rusty on some topics,
   slightly unorganized, very organized and clear, breezes over important
   stuff, very organized, presented very well, very excited, tried hard to get
   students to learn, will be good in years to come, very organized in notes
   and lectures, occasionally makes mistakes, liked doc cam and simultaneous
   explanation, seems to only have basic understanding first time he presents
   things, easier to understand in office hours, don't use markers with doc
   cam, copies exactly from book so notes are useless, runs out of time, seems
   lost when asked questions, rushed to cover too much material, email feedback
   helped clarify things, first time teaching and it shows, notes are
   unorganized and rushed.
Please make additional comments on any other aspects of the course including the curriculum, the instruction, amount of weekly work required and on whether you would recommend this course to other students.
   - too many assignments
   - project instructions were open ended and vague, pacing of project 2 was
     poor
   - occasionally too much work
   - too much weekly work, misleading project expectations, will recommend this
     course but not this professor
   - I wished the class was longer than 1 hour.
   - Too much work, homework was hard and long but good educational value,
     needed more assistance on project 2 hand calcs, needed better instruction
     on modeling. Great concepts, now have good understanding. Knowledgeable prof
     and enjoyed learning from him. Cut out time wasting stuff. Needed to have
     less ambiguous assignments. It was hard to know what assumptions to make.
   - Too much work.
   - Too much work. Not everyone checks Piazza regularly, so bad way to share
     info. Prof has good potential. Better to rely on textbook.

So there was a mix. Many didn't like the workload even though they were about
at the Carnegie Rule. They also had a lot to say about my presentation, with a
mix of results ranging from great to poor.

I'll continue my "Feedback Fridays", as one student put it, as that really
helps me actively adjust things during the course. I'm also going to work on
improving the questions we ask on the final evaluations to get more informative
results, especially since there is `lots of indication`_ that the evals are less
than useful.

.. _lots of indication: http://www.stat.berkeley.edu/~stark/Preprints/evaluations14.pdf

Q&A Outside of Class
====================

UC Davis provides access to a tool called Piazza_ through Smartsite. Piazza is a
student Q&A application and we made use of it extensively. I encouraged
students to use it and if they emailed me with a question that wasn't of a
private nature I always asked them to post it to Piazza instead. Piazza allows
for questions with two collaboratively edited answers: one from the students
and one from the instructors. It also allows instructors to endorse the student
answers. Furthermore, students can ask and answer anonymously if they desire.

.. _Piazza: https://piazza.com/

Here are the basic stats for the duration of the course:

============== ====
Questions      71
Answers        122
Notes          10
Contributions  312
Views          1408
============== ====

I was actually hoping that Piazza was more like `Stack Exchange`_ and allowed
us to vote up the best answers. Being able to vote for the best answers can be
an incentive for the students to answer each other's questions. I could reward
the top answerers with grade points. I may install an instance of OSQA_ for
this purpose in the future.

.. _Stack Exchange: http://stackexchange.com/
.. _OSQA: http://www.osqa.net/

The full Piazza data is unfortunately stored on Piazza's servers with no easy
way to download it. Support told me that I could email them for a json file
containing the data for the class, which I'll probably do. The statistics from
each course can be downloaded as a csv file very easily, just not the actual
questions. It is also worth noting that you can push questions from one course
to another course.

I tried to see if there were any correlations in Piazza use and grades but
didn't find anything simple. My `stats notebook`_ shows the attempt and some
other basic stats from the midterm and final.

.. _stats notebook: https://gist.github.com/moorepants/a44ddbab1eaa51b4991f

Assigning Groups
================

I used the tool developed at Purdue called CATME_ for forming the project teams
and collecting peer evaluations of the team work. This tool seems to work
really well. My only complaint is that the UI design is horrendous. But the
functionality is very nice.

.. _CATME: http://info.catme.org/

I surveyed the students before the first day of class with a pretty solid
response rate via CATME and asked a variety of the default questions, e.g. GPA,
free time, gender, dedication level, etc. CATME uses the information and runs
an iterative optimization algorithm to construct optimal groups based on the
survey data. Two things that I recognized was that teams were generally grouped
based on their past performance and dedication levels, which is good, and
secondly at least two women were placed on each team, which is also good in a
discipline such as engineering. Only one team seemed to have mismatches enough
such that a single student felt compelled to bear the majority of the weight of
the team. But the rest of the teams seemed to work very well together and I'd
like to think that CATME played a big role in that.

I plan on continuing to use this service. I just need to figure out how to
incorporate student project preferences for the senior design teams.

I don't recommend setting up the teams before the first day of class because
meant that I had to readjust them when students dropped the class in the first
week.

FEA
===

I hadn't planned on teaching anything about `Finite Element Analysis`_ but my
TA had developed four or five FEA lectures/demos and accompanying assignments
his previous times teaching the course. I worried that I wouldn't actually be
able to fit these in, but we ended up including three of them. One as a
pre-class assignment and two in-class 50 minute tutorials. I encouraged the TA
to modify the first in-class one to be a live tutorial with students working in
pairs with their laptops and to follow the `Software Carpentry`_ style of
speaking no more than 10 minutes before letting the students do for a while.

.. _Finite Element Analysis: https://en.wikipedia.org/wiki/Finite_element_method
.. _Software Carpentry: http://software-carpentry.org/

The students loved the tutorials. They are generally very excited about FEA,
which, in my opinion, is likely a bit misplaced. The first tutorial didn't go
as smoothly as hoped because the TA wasn't that comfortable with the SWC style
of tutorialing that I pushed on him. He decided to lecture the second one in
his style, which was much better for him. My TA let me know that he had to be
strong willed to work with me and I think my pressure to teach this SWC style
was the main reason.

This whirlwind tour of FEA gave the students something to play with but I think
it lacked some of the fundamental concept transfer that is needed to do good
FEA. The result was that the students tried to run FEA on their final huge
geometrically accurate models for their second project and often hit hurdles.
I'd have rather had them learn how to make simpler FEA models of the structures
and evaluate them. I'm not sure that the subtleties of constraints and meshing
were passed on either. But at least they got a taste of things and they made
really great progress learning about it on their own. There is just always
that fear that resorting to canned tools like FEA promotes bad modeling and
assumptions more so than manual modeling.

There is a lot of room for improvement on these tutorials. I think we can
design them to teach a few key topics and make them more interactive too. But
overall it was an awesome and unexpected edition that was all initiated by my
TA.

Conclusion
==========

I believe the course was successful and most of the things I tried worked out
and I will do them again. I'm going to spend some time this summer thinking
about the core objectives of the course and try to imagine what a mythical
class would look like that meets those objectives. It may be what is already
there, but I'd really like to see a course that is flipped such that the
students' interest in solving a design task will lead us to learning the
theoretical design concepts instead of the other way around, i.e. where we
present the concepts and then tell them to use them to do design. I'm also
going to work on pushing some of the conceptual learning to outside class
activities, so that we can "do" more together in class.
