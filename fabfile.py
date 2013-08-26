#!/usr/bin/env python

import os

from fabric.api import local
from datetime import datetime, timedelta


def new_notebook():

    notebook_dir = 'content/notebook'

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    local('git checkout -b notebook-{}'.format(today))

    path_to_todays_notebook = os.path.join(notebook_dir,
                                  'notebook-{}.html'.format(today))

    n = 1
    not_found = True
    while not_found:
        date_n_days_ago = datetime.now() - timedelta(days=n)
        most_recent = date_n_days_ago.strftime("%Y-%m-%d")
        path_to_most_recent = os.path.join(notebook_dir,
                                           'notebook-{}.html'.format(most_recent))
        try:
            with open(path_to_most_recent, 'r') as f:
                pass
        except IOError:
            n += 1
        else:
            local('cp {0}/notebook-{1}.html {0}/notebook-{2}.html'.format(notebook_dir, most_recent, today))
            not_found = False

    # TODO : Replace the text in the new file

    local('vim {}'.format(path_to_todays_notebook))
