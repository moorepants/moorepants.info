#!/usr/bin/env python

import os
import re

from fabric.api import local


def finish_notebook():

    current_branch_name = local('git rev-parse --abbrev-ref HEAD',
                                capture=True)
    if not current_branch_name.startswith('notebook-'):
        raise Exception("You are not in a notebook branch.")
    the_date = current_branch_name.split('notebook-')[1]
    path_to_notebook = 'content/notebook/{}.html'.format(current_branch_name)
    local('git add {}'.format(path_to_notebook))
    local('git commit {} -m "Added the notebook for {}."'.format(
        path_to_notebook, the_date))
    local('git rebase master')
    local('git checkout master')
    local('git merge {}'.format(current_branch_name))
    local('git push origin master')
    local('make push')


def new_notebook():
    from datetime import datetime, timedelta

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
            local('cp {} {}'.format(path_to_most_recent,
                                    path_to_todays_notebook))
            not_found = False

    with open(path_to_todays_notebook, 'r') as f:
        text = f.read()

    new_text = re.sub(date_n_days_ago.strftime('%B %-d, %Y'),
                      now.strftime('%B %-d, %Y'), text)

    new_text = re.sub(date_n_days_ago.strftime('%Y-%m-%d') + ' \d\d:\d\d:\d\d',
                      now.strftime('%Y-%m-%d %X'), new_text)

    with open(path_to_todays_notebook, 'w') as f:
        f.write(new_text)

    local('vim {}'.format(path_to_todays_notebook))
