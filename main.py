#!/usr/bin/env python

import subprocess
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--username", help="Your github username. E.g: renan028")
parser.add_argument("--startdate", help="The start date you want to be in your report. \
                    E.g: 01 Nov 2019", required=False)
parser.add_argument("--enddate", help="The end date you want to be in your report \
                    E.g: 01 Dec 2019")
args = parser.parse_args()

USERNAME = 'renan028' if args.username is None else args.username
SINCE = '01 Nov 2019' if args.startdate is None else args.startdate
UNTIL = '01 Dec 2019' if args.enddate is None else args.enddate

BASE = '~/dev/squidbot/'
repos = ['bundles/squidbot', 'control/auv_trajectory_follower', 'control/orogen/auv_trajectory_follower', \
         'control/squid_acceleration_controller', 'control/orogen/squid_acceleration_controller', \
         'planning/auv_trajectory_planning','planning/orogen/auv_trajectory_planning', \
         'simulation/gazebo_underwater', 'simulation/gpu_sonar_simulation', 'simulation/orogen/imaging_sonar_simulation', \
         'slam/imaging_sonar_filter', 'slam/imaging_sonar_localization', 'slam/imaging_sonar_mapping', \
         'slam/octomap', 'slam/orogen/imaging_sonar_localization', 'slam/orogen/imaging_sonar_mapping']

OUTPUT_FILE = './reports/'+ USERNAME + '-commits-report-' + \
		SINCE.replace(' ','') + '-' + UNTIL.replace(' ','') 

repos = [os.path.join(BASE, repo) for repo in repos]

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

#Making sure the file is empty in case it already exists
with open(OUTPUT_FILE, "w") as f:
    pass

#Opening the file with the proper permission
f = open(OUTPUT_FILE, 'a')

commits = ""
for dir in repos:
    command = 'cd ' + dir + ' && git log --all --no-merges ' + \
        '--author="' + USERNAME + '" --since="' + SINCE + '" --until="' + UNTIL + '" --oneline'
    commits = subprocess.getstatusoutput(command)[1]
    commits = [' '.join(['-'] + commit.split(' ')[1:]) for commit in commits.split('\n')]
    
    repo_list = os.path.relpath(dir, BASE)
    f.write(repo_list + '\n')
    f.write('\n'.join(commits) + '\n')
    f.write('\n')
    
f.close()
