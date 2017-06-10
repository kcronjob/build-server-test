#!/usr/bin/env python

# https://github.com/UCSB-CS-Using-GitHub-In-Courses/PyGitHubExamples.git

import os
import sys
import time

import yaml
from github import Github

from utils import read_data

# files/directories
dir_path = os.path.dirname(os.path.realpath(__file__))
credentials_filepath = os.path.join(dir_path, 'secrets', 'credentials.yaml')
num_attempts = 2
interval = 2


class Poller(object):

    def __init__(self):
        # exit if missing file
        if not os.path.exists(credentials_filepath):
            print 'Credentials filepath not found at [{}]'.format(credentials_filepath)
            sys.exit()
        self.credentials = read_data(credentials_filepath)
        if self.credentials is None:
            print 'Problem reading credentials'
            sys.exit()
        self.g = Github(self.credentials['user'], self.credentials['password'])

    def print_credentials(self):
        print 'Got valid credentials: {}'.format(self.credentials)

    def check_repo(self):
        for repo in self.g.get_user().get_repos():
            print 'Repo Name: {}'.format(repo.name)

    def run(self):
        for i in range(num_attempts):
            print 'Attempt [{0}]'.format(i)
            self.check_repo()
            time.sleep(interval)
        print 'Done'


if __name__ == '__main__':
    p = Poller()
    p.run()
