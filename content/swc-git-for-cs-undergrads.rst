=================================
Teaching Git to 100 CS Undergrads
=================================

:authors: Jason K. Moore
:subtitle: or bad jokes in the etherpad
:description: Some info about teaching the SWC style git to UCD CS Undergrads.
:date: 2016-02-01 18:03:00
:tags: education, software carpentry, git, computer science, uc davis



Last week I taught an introduction to version control with Git to the UCD
computer science capstone design course. There were about 100 students and I
took them through the `Software Carpentry`_ Git lesson in just over 1.5 hours.
From the feedback, I think it went really well. But there were some interesting
tidbits that I learned teaching this to undergraduates instead of the typical
group of graduate students.

.. _Software Carpentry: http://software-carpentry.org


We used the `SWC Git novice lesson`_. I only went through sections 1 through 9
as sections 10-12 weren't really relevant to the students in the class and
there wasn't enough time. The class was setup just as normal; I gave the
installation instructions out one week in advance. Surprisingly, there wasn't a
single installation issue at the beginning of class! I had two TA helpers
(maybe three) and at least on undergraduate helper who reviewed the materials
and were given some prompts on how to use the Etherpad, the sticky notes, and
their roles. I live coded through the lesson with the students following along.
I closed with collecting feedback and answering final questions. The following
lists some of the things that I noted during and after the class:

.. _SWC Git novice lesson: http://swcarpentry.github.io/git-novice/

- It was hard to get any kind of verbal reaction from the students or get them
  to volunteer to speak. I generally sensed an emotionless crowd, but the
  feedback I collected at the end told otherwise. Many claimed the lesson was
  good or great. I think most were shy and this style of teaching isn't
  something they are used to.
- The Etherpad wasn't used well, in fact, the chat room became a place for bad
  jokes and goofing off. So much so that the professor asked some students to
  see her after class (they didn't have enough foresight to create a false
  name). We should have monitored this and encouraged proper use. After reading
  the feedback, they would have definitely appreciated having the commands I
  was typing in that document. I'll need to make sure the helpers work at this
  and even start the note taking to initiate good behavior there.
- It was hard to get them to use the sticky notes. This may have been partly
  because I didn't explain them well. So it wasn't until the last sections when
  more people needed help that I was able to get visual feedback with them. And
  still only 60% or so seemed to use the notes at all as a signal.
- Many of the students had used Git before, but after reading the feedback I
  collected at the end, I think the novice lesson was the right choice. There
  were more "too fast" statements than "too slow".
- Many would like to have seen some information on branching and more examples
  on merging and conflicts. The one merge we did didn't seem to provide enough
  to really get it. And we didn't talk about branching at all.
- I covered the material in 1.5 hours, which is faster than a normal SWC
  workshop (~2.5 hrs). As I said above, there were a fair number of "too fast'
  complaints, but I think if they had taken notes in the Etherpad or noticed
  the cheatsheet I had linked in the Etherpad I would have had fewer. I'll need
  to point to the cheatsheet explicitly next time.
- Not many students were familiar with the UNIX command line, so I gave a few
  sentence explanation of commands, sub-commands, flags, and arguments. I think
  since they've done a fair amount of programming that this was easy to pick
  up. This isn't always the case with non-cs students.
- Github happened to go down an hour before I taught this and didn't come back
  online to just at the end of class. This at least gave me a chance to talk
  about why it is really bad to have a SaaS that so many people use go down
  like this. I wish I had an estimate of the money that the downtime cost all
  the users of Gitub. I improvised and used Bitbucket instead. That went pretty
  well except for one hiccup, I didn't know how to properly use the Bitbucket
  https URL in the partner portion of the lesson. You have to specify it as
  ``git clone
  https://yourusername@bitbucket.com/partnerusername/reponame.git``. Some
  students helped me figure that the username before the ``@`` needs to be your
  own username for proper authentication.
- It wasn't until we got to using Bitbucket that I started getting more
  questions from the students and the helpers had to scramble around the room
  to help people out. This let the helpers be a little complacent for the first
  hour or so and they suddenly had to do a bunch.

Overall, I think the lesson was the right scope and level for the class even
though most had some experience with Git in some fashion. Although, we could
think about breaking the section into two: novice and intermediate and teach
two simultaneous lessons in two rooms.

The student feedback is below:

.. raw:: html

  <table border="1" class="dataframe">
    <thead>
      <tr>
        <th>Positive</th>
        <th>Negative</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>good pace, waiting for everyone to be caught up</td>
        <td>I would only recommend slowing down while entering commands.</td>
      </tr>
      <tr>
        <td>structured clear and concise tutorial</td>
        <td>not all students participated so grouping was harder</td>
      </tr>
      <tr>
        <td>easy to follow step-by-step introduction to git</td>
        <td>some parts of lecture can be more smooth (bitbucket)</td>
      </tr>
      <tr>
        <td>great refresher, well put together especially with the interactivity</td>
        <td>go slower, more info</td>
      </tr>
      <tr>
        <td>very clear tutorial, clear instructions and easy to follow</td>
        <td>would have liked some overview of branching</td>
      </tr>
      <tr>
        <td>good basics</td>
        <td>a little fast sometimes but nothing else</td>
      </tr>
      <tr>
        <td>good beginner's material</td>
        <td>don't let github be down, maybe a little fast sometimes</td>
      </tr>
      <tr>
        <td>clear and easy to follow, all commands explained well</td>
        <td>don't let github die! we had technical difficulties. T_T</td>
      </tr>
      <tr>
        <td>liked how you went step-by-step and typed along with us</td>
        <td>need to go a bit slower, need more advanced topic, eg branching, merging, etc</td>
      </tr>
      <tr>
        <td>you were great!, learned a lot, interactive</td>
        <td>it was a little slow</td>
      </tr>
      <tr>
        <td>wish there were more tricks, was very interactive and good</td>
        <td>sometimes you went too fast and itw as hard to keep up</td>
      </tr>
      <tr>
        <td>very informative and a good refresher</td>
        <td>a little fast on some inputs &gt; slow typer</td>
      </tr>
      <tr>
        <td>Thank you! it was very informative and helpful!</td>
        <td>too fast! :) sometimes I got lost as you moved fast</td>
      </tr>
      <tr>
        <td>Tutorial was very comprehensive. I thought it was a good review of what I already knew. :)</td>
        <td>too fast. would be great if you had a list of all your commands somewhere instead of us following you</td>
      </tr>
      <tr>
        <td>great quick overview of big points</td>
        <td>too fast for me</td>
      </tr>
      <tr>
        <td>very informative and comprehensive</td>
        <td>cloning into bitbucket not very well explained and rushed</td>
      </tr>
      <tr>
        <td>good overview for a first time git user</td>
        <td>hard to control class</td>
      </tr>
      <tr>
        <td>enthusiastic!</td>
        <td>some command lines were not visible and/or were cleared too quickly</td>
      </tr>
      <tr>
        <td>very fun and helpful</td>
        <td>consider teaching branching/merging, git mergetool is super cool! try it!</td>
      </tr>
      <tr>
        <td>good review of the basics</td>
        <td>github was down</td>
      </tr>
      <tr>
        <td>very concise and clear</td>
        <td>only covered bare basics, which are already familiar. perhaps more advanced features?</td>
      </tr>
      <tr>
        <td>good review</td>
        <td>would have liked more "merging" tutorials</td>
      </tr>
      <tr>
        <td>helpful for a beginner</td>
        <td>didn't go over revert</td>
      </tr>
      <tr>
        <td>the checkout thing was really cool</td>
        <td>the steps could have been sped up so more could be covered</td>
      </tr>
      <tr>
        <td>good patience and articulation</td>
        <td>need better organization (time intervals of doing nothing took too long to prep repos)</td>
      </tr>
      <tr>
        <td>I understood everything</td>
        <td>too fast!, should handle more of merge conflict</td>
      </tr>
      <tr>
        <td>Great review of Git. went over .gitignore and --config options I forgot about</td>
        <td>didn't go over tag</td>
      </tr>
      <tr>
        <td>very easy to follow, very hands on</td>
        <td>most of the stuff was very basic</td>
      </tr>
      <tr>
        <td>very informative an dmade the material clear and easy to understand</td>
        <td>because each step depended so much on previous steps it was tough to catch up if you fell behind</td>
      </tr>
      <tr>
        <td>clear!</td>
        <td>github is better than bitbucket</td>
      </tr>
      <tr>
        <td>great excitement and passion</td>
        <td>sometimes too fast w/ the commands</td>
      </tr>
      <tr>
        <td>want all of this written down</td>
        <td>didn't cover branches</td>
      </tr>
      <tr>
        <td>very patient and instructions were clear</td>
        <td>too easy, more advanced lecture</td>
      </tr>
      <tr>
        <td>i like your questions!</td>
        <td>github didn't work</td>
      </tr>
      <tr>
        <td>I liked the sticky notes as a clear signal of "ok"/"need help"</td>
        <td>need detail on branch</td>
      </tr>
      <tr>
        <td>Good intro to Git! The quiz like MC questions helped us understanding. Include more of them next time. :) Thanks!</td>
        <td>nothing ...</td>
      </tr>
      <tr>
        <td>Informative, good review for someone q/ knowledge of Github, spoke clearly</td>
        <td>sometimes went too fast :(</td>
      </tr>
      <tr>
        <td>sticky notes were good idea! very clear instructions, awesome!</td>
        <td>uncertainty at points and no gui info</td>
      </tr>
      <tr>
        <td>more options with command line coming from someone using gui</td>
        <td>a crazy looking smiley face</td>
      </tr>
      <tr>
        <td>I thought you worked through a lot of very complicated subjects in a very easy to follow way, very, very, very good. The time activities are great!</td>
        <td>github?</td>
      </tr>
      <tr>
        <td>rather than just a presentation on Git, you made us learn by actually doing it on our computers</td>
        <td>no negative for me, about tutorial, just wish git was more user friendly</td>
      </tr>
      <tr>
        <td>great tutorial on git!</td>
        <td>maybe show off some gui tools</td>
      </tr>
      <tr>
        <td>great job going over many different git scenarios! learned a lot</td>
        <td>diagrams might be helpful</td>
      </tr>
      <tr>
        <td>well organized, very informative and a good refresher</td>
        <td>should make more info on merge</td>
      </tr>
      <tr>
        <td>clear instructions</td>
        <td>lots of people know about git already, should've just advanced to the more cool stuff</td>
      </tr>
      <tr>
        <td>instructions were easy to follow</td>
        <td>could'be gotten into more depth about git features since most people in the class have used git</td>
      </tr>
      <tr>
        <td>great content</td>
        <td>did not address windows commands such as dir instead of ls and cl instead of clear, also went fairly fast</td>
      </tr>
      <tr>
        <td>easy to understand</td>
        <td>some examples took too long</td>
      </tr>
      <tr>
        <td>the activities w/ partners were really helpful and interactive</td>
        <td>a bit slow paced</td>
      </tr>
      <tr>
        <td>the presentation was clear and easy to follow</td>
        <td>too bad github was down :(</td>
      </tr>
      <tr>
        <td>good tutorial, especially for new people</td>
        <td>went very fast over the commands. passing out a list of git commands would have helped.</td>
      </tr>
      <tr>
        <td>examples were helpful</td>
        <td>too slow and only covered the very basics. I wanted to see tags and ssh keys. :(</td>
      </tr>
      <tr>
        <td>very thorough</td>
        <td>I already knew everything.</td>
      </tr>
      <tr>
        <td>Easy to understand, thorough and good for people new to Git</td>
        <td>course is too large (# students) to effectively track students progress</td>
      </tr>
      <tr>
        <td>learning about staging was new</td>
        <td>moved rather fast, making it hard to catch some commands, having a list of the commands on the board would be helpful</td>
      </tr>
      <tr>
        <td>very informative, goes over the most used git commands</td>
        <td>It would be great if you provided a cheatsheet of what is going to be covered. If i get behind then I get really behind.</td>
      </tr>
      <tr>
        <td>you explained things well and went step by step</td>
        <td>want all of this written down</td>
      </tr>
      <tr>
        <td>really liked the setup of the tutorial which was also really helpful, thank you!</td>
        <td>I think we just need one sticky note.</td>
      </tr>
      <tr>
        <td>very positive/patient</td>
        <td>you went a bit fast, someone posting the commands on etherpad would be helpful as you go</td>
      </tr>
      <tr>
        <td>good for a beginner</td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>very well organized</td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>you were enthusiastic and helpful</td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>helpful :)</td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>clear lecture</td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>informative</td>
        <td>NaN</td>
      </tr>
    </tbody>
  </table>
