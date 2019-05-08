=======================
Fixin' photo timestamps
=======================

:authors: Jason K. Moore
:subtitle: don't forget the travel setting
:description: Photo timestamp manipulation with Python
:date: 2013-05-26 02:10:00
:tags: photo, python, timestamp, gexiv2, pytz

{% mark image -%}

{%- endmark %}

{% mark excerpt %}

Yumi and I just got back from a month long bicycle tour of Japan. We took two
cameras with us. My Panasonic Lumix stopped autofocusing the first day of the
trip, so we used her Canon Powershot for all the photographing. We dropped the
Canon twice on the trip and now it makes a nasty noise when opening and
closing, but it at least still takes photos.

We forgot to set the travel time on the camera so all 700+ of our photos had
timestamps from Pacific Standard Time while under daylight saving time (Japan
does not use DST). I wanted to correct the timestamps before uploading them to
the web so I wrote a little Python script and used Yorba_\ 's Gexiv2_ and the
PyTZ_ package to sort things out.

.. _Yorba: http://www.yorba.org
.. _Gexiv2: http://redmine.yorba.org/projects/gexiv2/wiki
.. _PyTZ: http://pytz.sourceforge.net

{% endmark %}

To install Gexiv2 in Ubuntu 12.10 I ran these commands::

  $ sudo aptitude install libexiv2-dev libtool libgirepository1.0-dev
  $ git clone git://git.yorba.org/gexiv2
  $ cd gexiv2
  $ ./configure --enable-introspection
  $ make
  $ sudo make install

And installed PyTZ with pip::

  $ sudo pip install pytz

Then I wrote this script which searched my photo directory for the specific
folders and photographs and adjusted the three timestamps in the photos (this
didn't work with the few .mov files we took during the trip because Gexiv2
doesn't support ``.mov`` files, so that will need to be done manually or I need
to find another tool)::

  #!/usr/bin/env python
  # -*- coding: utf-8 -*-

  """This script converts the time/date stamp of photographs we took in Japan
  to Japanese time/date from US Pacific time because we forgot to adjust the
  camera's internal clock at the beginning of the trip."""

  import os
  import re
  from datetime import datetime

  import pytz
  from gi.repository import GExiv2

  # The Canon PowerShot SX200 IS date format.
  DATE_FORMAT = '%Y:%m:%d %H:%M:%S'

  # We snapped photos in Japan while using the current PST time (which is under
  # Daylight Savings Time, but Japan is not).
  pacific_tz = pytz.timezone("America/Los_Angeles")
  japan_tz = pytz.timezone("Asia/Tokyo")

  # Get a list of file names that match the time we were there and the camera
  # filename format.
  directory = "/media/Data/My Pictures"
  pattern = r"/media/Data/My Pictures/2013-0[4-5]-\d\d/img_\d\d\d\d.jpg"

  files_to_adjust = []

  for root, dirnames, filenames in os.walk(directory):
      for filename in filenames:
          path = os.path.join(root, filename)
          result = re.match(pattern, path)
          # if a matching file is found, save it to the list
          if result:
              files_to_adjust.append(path)

  # Now adjust the three timestamps (DateTime, DateTimeDigitized and
  # DateTimeOriginal) for each file and save the results.

  for filename in files_to_adjust:

      print('-' * 20)
      print(filename)
      print('-' * 20)

      metadata = GExiv2.Metadata(filename)

      for tag in metadata.get_exif_tags():
          if 'DateTime' in tag:
              timestamp = metadata[tag]
              pacific_time = pacific_tz.localize(datetime.strptime(timestamp,
                  DATE_FORMAT))
              japan_time = pacific_time.astimezone(japan_tz)
              japan_timestamp = japan_time.strftime(DATE_FORMAT)
              print(tag)
              print('Current time stamp: {}.'.format(timestamp))
              print('Adjusted time stamp: {}.'.format(japan_timestamp))
              print('-' * 20)

              # Set the timestamp.
              metadata[tag] = japan_timestamp

      # Save the file with the adjusted timestamps.
      metadata.save_file()

The resulting output for an example file looked like this::

  --------------------
  /media/Data/My Pictures/2013-05-21/img_5484.jpg
  --------------------
  Exif.Image.DateTime
  Current time stamp: 2013:05:21 00:51:31.
  Adjusted time stamp: 2013:05:21 16:51:31.
  --------------------
  Exif.Photo.DateTimeDigitized
  Current time stamp: 2013:05:21 00:51:31.
  Adjusted time stamp: 2013:05:21 16:51:31.
  --------------------
  Exif.Photo.DateTimeOriginal
  Current time stamp: 2013:05:21 00:51:31.
  Adjusted time stamp: 2013:05:21 16:51:31.
  --------------------

The correct 16 hour difference was applied correctly by PyTZ which takes care
of DST differences. I then had to remove all of the photos from my Shotwell
library and re-add them because the Shotwell database didn't automatically
update with the new times. Once I did that, everything was now correct (except
the ``.mov`` files, of course).

The `photos of the trip`_ can be found in my G+ photo album.

.. _photos of the trip: https://plus.google.com/photos/110966557175293116547/albums/5882019377214495409
