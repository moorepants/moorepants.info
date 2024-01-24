The source code for moorepants.info_.

Editing Guide
=============

- The website is built using Pelican. Review the `Pelican documentation`_ to
  get familiar with how to create pages and articles.
- The source files are in the git branch called ``master``. This is the default
  branch of the repository.
- All articles, pages, and similar content should be written in
  reStructuredText_. See the `Sphinx reStructuredText primer`_ to learn the
  syntax.
- Binary Assets such as images, videos, etc should be served from an external
  hosting site. The information for pushing binary objects to the Dreamhost
  DreamObject bucket is in the Fietslab Commons Google Drive. Do not commit
  binary assets to this repository. Images should be all lower case unique
  filenames with a ``-`` to separate words, for example:
  ``my-image-for-this-blog-post.png``. All assets are store in the same
  directory on the object store and should have unique file names.

.. _Pelican documentation: http://docs.getpelican.com/en/stable/
.. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
.. _Sphinx reStructuredText primer: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Building Locally
================

It is good practice to build the documentation locally so that you can review
change before submitting a pull request.

First, clone the plugin repository::

   $ git clone git@github.com:getpelican/pelican-plugins.git

Note the path to the plugin repository, e.g.::

   /home/my_username/.../pelican-plugins

Clone the theme repository (you want the mechmotum branch to be active)::

   $ git clone -b mechmotum git@github.com:mechmotum/pelican-alchemy.git

Note the path to the theme, e.g.::

   /home/my_username/.../pelican-alchemy

Clone your fork of this repository and change into the new directory::

   $ git clone git@github.com:<your github username>/moorepants.info.git
   $ cd moorepants.info/

Create a configuration file called ``config.yml`` and add the full path to
where you installed the plugins and theme (note the added /alchemy subfolder in
THEME_PATH)::

   $ echo "THEME_PATH: /home/my_username/.../pelican-alchemy/alchemy" > config.yml
   $ echo "PLUGIN_PATHS: /home/my_username/.../pelican-plugins" >> config.yml

Now you can build and serve the documentation with::

   $ make devserver

If this succeeds you can open the website in your web browser at
http://localhost:8000.

While the server is running you can change the website source files and they
will be build automatically. Refresh your web browser to view the changes. Use
``<Ctrl>+C`` to kill the webserver.

LICENSE
=======

This repository is licensed under the CC-BY 4.0 license.
