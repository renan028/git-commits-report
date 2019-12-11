#!/usr/bin/env python

import subprocess
import os

BASE = '/home/renan/dev/squid/'
repos = ['bundles/squidbot', 'control/auv_trajectory_follower', 'control/orogen/auv_trajectory_follower', \
         'control/squid_acceleration_controller', 'control/orogen/squid_acceleration_controller', \
         'planning/auv_trajectory_planning','planning/orogen/auv_trajectory_planning', \
         'simulation/gazebo_underwater', 'simulation/gpu_sonar_simulation', 'simulation/orogen/imaging_sonar_simulation', \
         'slam/imaging_sonar_filter', 'slam/imaging_sonar_localization', 'slam/imaging_sonar_mapping', \
         'slam/octomap', 'slam/orogen/imaging_sonar_localization', 'slam/orogen/imaging_sonar_mapping']

USERNAME = 'renan028'
SINCE = '01 Nov 2019'
UNTIL = '01 Dec 2019'

repos = [os.path.join(BASE, repo) for repo in repos]

commits = ""
for dir in repos:
    command = 'cd ' + dir + ' && git log --all --no-merges ' + \
        '--author="' + USERNAME + '" --since="' + SINCE + '" --until="' + UNTIL + '" --oneline'
    commits = subprocess.getstatusoutput(command)[1]
    print(os.path.relpath(dir, BASE))
    commits = [' '.join(['-'] + commit.split(' ')[1:]) for commit in commits.split('\n')]
    print('\n'.join(commits) + '\n')
 
