#!/usr/bin/env python

# https://github.com/UCSB-CS-Using-GitHub-In-Courses/PyGitHubExamples.git

import os
import sys
import time
import yaml

DEBUG = True

def read_data(filepath):
    exists = os.path.exists(filepath)
    if DEBUG:
        print ('read data [{0}] exists: [{1}]'.format(filepath, exists))
    if exists:
        with open(filepath, 'r') as f:
            try:
                data = yaml.safe_load(f)
                return data
            finally:
                f.close()
    return None
