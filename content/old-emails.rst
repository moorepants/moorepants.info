---
title: PST2Gmail
subtitle: missin my old email
description: A brief explanation of the process of pushing old emails from an Outlook .pst file to Gmail.
created: !!timestamp '2013-01-15 15:39:00'
tags:
    - email
    - Outlook
    - Gmail
    - pst
---

{% mark image -%}

{%- endmark %}

{% mark excerpt -%}

I must have started my emailing career sometime in high school. I remember
having the address jive@gamewood.net from our local internet provider around
Danville, VA. I must have erased all of that email during one of the many
Windows 95 reformats I did to clean out all the computer crustiness. But once I
got to college in the Fall of 2000, I started curating all of my email from my
university address jmoor024@odu.edu with Microsoft Outlook. I switched to Gmail
in May of 2005 and backed up all of my previous email in Outlook to a .pst file
on July 16, 2005. This file has been sitting on a backup CD since that day.
I've occasionally wished I could search for emails from those years to dig up
old contacts and such, but never did anything about it.

{%- endmark %}

I got inspired this morning and dug up the CD with the .pst file and found this
nice `post
<http://superuser.com/questions/227488/how-can-i-import-a-pst-file-to-gmail>`_
on superuser.com\ [1]_ with a good solution to getting old Outlook email onto
the Gmail server.

First you need `libpst <http://www.five-ten-sg.com/libpst/>`_ and some
associated tools. On Ubuntu you can get them with::

   $ aptitude install pst-utils

This gives your readpst which can convert your .pst file to other formats. ::

   $ mkdir old-emails
   $ readpst -o old-emails/ backup.pst

This creates an mbox plain text file type for each of folders in your .pst
file. ::

   $ cd old-emails/
   $ ls -l
   total 100316
   -rw-rw-r-- 1 moorepants moorepants   268588 Jan 15 15:09 Bills
   -rw-rw-r-- 1 moorepants moorepants    37924 Jan 15 15:09 Calendar
   -rw-rw-r-- 1 moorepants moorepants  4487790 Jan 15 15:09 Caterpillar
   -rw-rw-r-- 1 moorepants moorepants   271587 Jan 15 15:09 College
   -rw-rw-r-- 1 moorepants moorepants     2108 Jan 15 15:09 Contacts
   -rw-rw-r-- 1 moorepants moorepants  4526958 Jan 15 15:09 Graduate School
   -rw-rw-r-- 1 moorepants moorepants   184027 Jan 15 15:09 Inbox
   -rw-rw-r-- 1 moorepants moorepants  8454804 Jan 15 15:09 India
   -rw-rw-r-- 1 moorepants moorepants   151095 Jan 15 15:09 Jobs
   -rw-rw-r-- 1 moorepants moorepants  2851498 Jan 15 15:09 Junk E-mail
   -rw-rw-r-- 1 moorepants moorepants  2871435 Jan 15 15:09 LFST
   -rw-rw-r-- 1 moorepants moorepants 11234855 Jan 15 15:09 MAGLEV
   -rw-rw-r-- 1 moorepants moorepants 19754204 Jan 15 15:09 ODU HPLV
   -rw-rw-r-- 1 moorepants moorepants    82927 Jan 15 15:09 Purchases
   -rw-rw-r-- 1 moorepants moorepants   215616 Jan 15 15:09 red Love
   -rw-rw-r-- 1 moorepants moorepants 47280735 Jan 15 15:09 Sent Items

Then I made use of this `IMAP script <http://imap-upload.sourceforge.net/>`_
that was written specifically with Gmail in mind. ::

   $ wget http://superb-dca2.dl.sourceforge.net/project/imap-upload/imap-upload/1.2/imap-upload-1.2.zip
   $ unzip imap-upload-1.2.zip

Now use the script and its gmail flag to send an mbox file to a label in
Gmail. ::

   $ python imap-upload-1.2/imap_upload.py --gmail --user=moorepants --box=Caterpillar Caterpillar

I had to create new labels manually in Gmail before running the previous
command for it to work correctly.

.. [1] Side note: why do I have to log in separately to all of Stack
       Exchange's websites, what I a pain. And why the hell do you need 15
       reputation points to vote up an answer? Why not let anonymous accounts
       do this? Stack Exhange would get much more participation if they didn't
       have so many hurdles to participate.
