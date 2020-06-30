#!/usr/bin/env python3

import sys
import os
import urllib.request
import venv
import subprocess


def make_project_dir(directory):
    try:
        os.makedirs(directory)
    except FileExistsError:
        print("The directory you provided already exists, not doing anything")
        exit(1)
    return


def get_gitignore(directory):
    url = "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore"
    urllib.request.urlretrieve(url, os.path.join(directory, '.gitignore'))
    return


def make_venv(directory):
    venvdir = os.path.join(directory, 'venv')
    venv.create(env_dir=venvdir, with_pip=True)
    return venvdir


def prepare_venv(venv):
    whichpip = os.path.join(venv, 'bin', 'pip')
    output = subprocess.check_output(
        [whichpip, 'install', 'autopep8', 'pylint'])
    return


def main():
    directory = sys.argv[1]
    make_project_dir(directory)
    get_gitignore(directory)
    venv = make_venv(directory)
    prepare_venv(venv)
    return


if __name__ == '__main__':
    main()