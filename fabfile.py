#!/usr/bin/env python

import os
import re

from fabric.api import local, settings

VARIABLES = {
             'username': 'jasonkmoore',
             'server': 'moorepants.info',
             'source': 'deploy/',
             'destination': '/home/jasonkmoore/moorepants.info/',
             'docdir': 'content/media/docs',
             'statementpreamble': r'\usepackage[top=1in,bottom=1in,right=1in,left=1in]{geometry}',
             'presentationsource': '/home/moorepants/Presentations/',
             'presentationdestination': '/home/jasonkmoore/moorepants.info/presentations/',
             'del': '',
            }

def create_doc_dir():
    if not os.path.exists(VARIABLES['docdir']):
        os.makedirs(VARIABLES['docdir'])

def gen_serve():
    get_resume()
    build_statements()
    local('hyde gen -r')
    local('hyde serve')


def get_resume():
    create_doc_dir()
    with settings(warn_only=True):
        local('rsync ~/Documents/resume/resume.pdf content/media/docs/JasonMoore_cv.pdf')
        local('rsync ~/Projects/appropriate-tech/HumanPowerPresentation/hppres.pdf content/media/docs/hppres.pdf')
        local('rsync ~/Projects/appropriate-tech/HumanPowerPresentation/hppres-notes.pdf content/media/docs/hppres-notes.pdf')
        local('rsync ~/Research/structuralid/Hess_Moore_MST_Paper.pdf content/media/docs/hess-moore-mst-final.pdf')


def build_statements():
    create_doc_dir()
    rst_files = ['content/research/research-statement.rst',
                 'content/teaching/teaching-statement-2013.rst',
                 'content/teaching/teaching-statement-2015.rst']
    statements = [
        'rst2latex.py --date --documentoptions="letter,10pt" --use-latex-docinfo --latex-preamble="{statementpreamble}" {inputfile} {docdir}/{prefix}.tex',
        'pdflatex --output-directory={docdir} {docdir}/{prefix}.tex',
        'rm {docdir}/{prefix}.aux {docdir}/{prefix}.out {docdir}/{prefix}.log {docdir}/{prefix}.tex',
        ]
    for rst_file in rst_files:
        VARIABLES['inputfile'] = rst_file
        VARIABLES['prefix'] = os.path.splitext(os.path.basename(rst_file))[0]
        for statement in statements:
            with settings(warn_only=True):
                local(statement.format(**VARIABLES), capture=True)
        VARIABLES.pop('inputfile')
        VARIABLES.pop('prefix')


def push(delete=False):
    if bool(delete):
        VARIABLES['del'] = ' --delete'

    get_resume()
    build_statements()
    statements = [
        'rm -rf deploy',
        'hyde gen -c prod.yaml',
        "rsync -r -t{del} --progress --exclude 'presentations' {source} {username}@{server}:{destination}",
        'rsync -r -t{del} --progress {presentationsource} {username}@{server}:{presentationdestination}',
        "ssh {username}@{server} 'find {destination} -type f -exec chmod 644 {{}} \;'",
        "ssh {username}@{server} 'find {destination} -type d -exec chmod 755 {{}} \;'",
    ]
    for statement in statements:
        local(statement.format(**VARIABLES))

    VARIABLES['del'] = ''


def finish_notebook():
    """If you have a notebook that hasn't been added to the repo and it is
    done, then run this command."""

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
    local('git branch -d {}'.format(current_branch_name))
    push()


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

    local('vim -O {}'.format(path_to_todays_notebook))
