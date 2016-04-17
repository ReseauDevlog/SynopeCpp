#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Typing 'oval' or 'oval l' will display the list of targets, as described in in oval.json.
Each target is the association between a name and a shell command.

Typing 'oval r <name>' will execute the shell command associated with the given name
One can execute several ones sequentially: 'oval r <name1> <name2>...'

Typing 'oval fo <name>' show the filtered part of '<name>.out'.
Typing 'oval v <name>' copy the log file '<name>.out' into the ref file '<name>.ref'.
Typing 'oval d <name>' compare the log file '<name>.out' with the ref file '<name>.ref'.
Typing 'oval fr <name>' show the filtered part of '<name>.ref'.

One can use wildcards: 'oval r <pattern1> <pattern2>...'
The only wildcard character is '%'.
One can check how a given pattern expands : 'oval l <pattern>'.

On top of the targets, the configuration oval.json can include a list of filters.
When one run several targets, only the ouput lines which match one of the filters
are displayed.
'''

import argparse
import os
import os.path
import re
import subprocess
import sys
import hashlib

from ovallogging import logging

# process command-line options
parser = argparse.ArgumentParser(description='Automatic running and diffing of executables')
#parser.add_argument('-c', action="store_true", default=False, \
#                    help='crypt the reference output')
parser.add_argument('subcommand',
                    help='the oval subcommand to apply')
parser.add_argument('target', nargs='*', default=['%'],
                    help='the list of targets to be processed')
args = parser.parse_args()

# search for ovalfile in the current working directory
sys.path.insert(0,os.getcwd())
import ovalfile as config

# prepare subcommand
abbrevs = {
    'list': 'list', 'lis': 'list', 'li': 'list', 'l': 'list',
    'run': 'run', 'ru': 'run', 'r': 'run',
    'val': 'val', 'va': 'val', 'v': 'val',
    'diff': 'diff', 'dif': 'diff', 'di': 'diff', 'd': 'diff',
    'crypt': 'crypt', 'cryp': 'crypt', 'cry': 'crypt', 'cr': 'crypt', 'c': 'crypt',
    'filter-out': 'filter-out', 'fo': 'filter-out',
    'filter-ref': 'filter-ref', 'fr': 'filter-ref',
}
abbrev = args.subcommand
if abbrev in abbrevs.keys():
    subcommand = abbrevs[abbrev]
else:
    subcommand = abbrev

# prepare the list of all targets
all_target_names = [t['name'] for t in config.targets]
all_targets = {t['name'] : t for t in config.targets}
if (subcommand == 'diff' or subcommand == 'val' or subcommand == 'crypt'):
    for target_name in all_target_names:
        target = all_targets[target_name]
        if os.path.isfile(target_name+'.out'):
            target['out'] = target_name+'.out'
        else:
            target['out'] = None
        if os.path.isfile(target_name+'.ref'):
            target['ref'] = target_name+'.ref'
        else:
            target['ref'] = None
        if os.path.isfile(target_name+'.md5'):
            target['md5'] = target_name+'.md5'
        else:
            target['md5'] = None

# select the active targets.
# when there is a wildcard '%' and the command is 'd',
# filter-out the targets which do not have a log and a ref.
# multi says if there are several expanded targets
# expanded says if there are targets expanded from wildcard
target_names = []
expanded = False
for p in args.target:
    if '%' in p:
        exp = re.compile('^'+p.replace('%', '.*')+'$')
        for target_name in all_target_names:
            target = all_targets[target_name]
            if exp.match(target_name):
                if ((subcommand == 'diff' and target['out'] and (target['ref'] or target['md5'])) or
                    (subcommand == 'crypt' and target['ref']) or
                    (subcommand == 'val' and target['out']) or
                    (subcommand != 'diff' and args.subcommand != 'val' and args.subcommand != 'crypt')):
                    logging.debug('expand {} to {}'.format(p, target_name))
                    target_names.append(target_name)
                    expanded = True
    else:
        if p in all_target_names:
            target_names.append(p)
        else:
            logging.warning('unknown target '+p)
multi = len(target_names) > 1
logging.debug('targets: {}'.format(target_names))

# add the filters
for target_name in target_names:
    target = all_targets[target_name]
    target['run_filters_out'] = []
    for f in config.run_filters_out:
        exp = re.compile('^'+f['apply'].replace('%', '.*')+'$')
        if exp.match(target_name):
            target['run_filters_out'].append(f['re'])
    target['diff_filters_in'] = []
    for f in config.diff_filters_in:
        exp = re.compile('^'+f['apply'].replace('%', '.*')+'$')
        if exp.match(target_name):
            target['diff_filters_in'].append(f['re'])

# execute the subcommand
if subcommand == 'list':
    for target_name in target_names:
        target = all_targets[target_name]
        logging.info("{}: {}".format(target_name, target["command"]))
elif subcommand == 'run':
    for target_name in target_names:
        target = all_targets[target_name]
        sh_command = "({}) 2>&1 | tee {}.out".format(target["command"],target_name)
        out_file_name = "{}.out".format(target_name)
        proc = subprocess.Popen(sh_command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out_value, err_value = proc.communicate()
        with open(out_file_name,'w') as out_content:
            runexps = [re.compile('^'+f.replace('%', '.*')+'$') for f in target['run_filters_out']]
            diffexps = [re.compile('^'+f.replace('%', '.*')+'$') for f in target['diff_filters_in']]
            for line in out_value.rstrip().split('\n'):
                fmatches = [fexp.match(line) for fexp in runexps]
                if [fmatch for fmatch in fmatches if fmatch]:
                    continue
                out_content.write(line+'\n')
                if multi:
                    fmatches = [fexp.match(line) for fexp in diffexps]
                    if [fmatch for fmatch in fmatches if fmatch]:
                        logging.info(target_name+": "+line)
                else:
                    logging.info(line)
elif subcommand == 'val':
    for target_name in target_names:
        command = 'cp -f {}.out {}.ref'.format(target_name, target_name)
        logging.info(command)
        subprocess.check_call(command, shell=True, universal_newlines=True)
elif subcommand == 'crypt':
    for target_name in target_names:
        target = all_targets[target_name]
        fexps = [re.compile('^'+f.replace('%', '.*')+'$') for f in target['diff_filters_in']]
        ref_file_name = '{}.ref'.format(target_name)
        md5_file_name = '{}.md5'.format(target_name)
        with open(ref_file_name) as ref_content:
            logging.info('crypting {}.ref into {}.md5'.format(target_name, target_name))
            with open(md5_file_name,'w') as md5_content:
                for ref_line in ref_content:
                    line = ref_line.rstrip()
                    for fmatch in [fexp.match(line) for fexp in fexps]:
                        if fmatch:
                            for grp in fmatch.groups():
                                md5_content.write(hashlib.md5(grp).hexdigest()+'\n')
elif subcommand == 'diff':
    for target_name in target_names:
        target = all_targets[target_name]
        logging.debug('process target {}'.format(target_name))
        if not target['out']:
            logging.warning('lacking file {}.out'.format(target_name))
            continue
        if not target['ref'] and not target['md5']:
            logging.warning('lacking file {}.ref or {}.md5'.format(target_name,target_name))
            continue
        out_file_name = target['out']
        if target['ref']:
            ref_file_name = target['ref']
            md5 = False
        else:
            ref_file_name = target['md5']
            md5 = True
        fexps = [re.compile('^'+f.replace('%', '.*')+'$') for f in target['diff_filters_in']]
        proc1 = subprocess.Popen("cat {} 2>&1".format(out_file_name),
                                 shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out_log, _ = proc1.communicate()
        out_log_matches = []
        out_md5_matches = []
        for line in out_log.split('\n'):
            for fmatch in [fexp.match(line) for fexp in fexps]:
                if fmatch:
                    for grp in fmatch.groups():
                        out_log_matches.append(grp)
                        out_md5_matches.append(hashlib.md5(grp).hexdigest())
        proc2 = subprocess.Popen("cat {} 2>&1".format(ref_file_name),
                                 shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out_ref, _ = proc2.communicate()
        out_ref_matches = []
        for line in out_ref.split('\n'):
            for fmatch in [fexp.match(line) for fexp in fexps]:
                if fmatch:
                    for grp in fmatch.groups():
                        out_ref_matches.append(grp)
        # complete lacking matches
        while len(out_log_matches) < len(out_ref_matches):
            out_log_matches.append('EMPTY STRING')
            out_md5_matches.append('EMPTY STRING')
        while len(out_log_matches) > len(out_ref_matches):
            out_ref_matches.append('EMPTY STRING')
        # compare
        zipped = zip(out_log_matches, out_md5_matches, out_ref_matches)
        nbdiff = 0
        if multi or expanded:
            prefix = target_name+': '
        else:
            prefix = ''
        for tpl in zipped:
            if md5:
                if tpl[1] != tpl[2]:
                    logging.info(prefix+'md5("{}") != {}'.format(tpl[0], tpl[2]))
                    nbdiff += 1
            else:
                if tpl[0] != tpl[2]:
                    logging.info(prefix+"{} != {}".format(tpl[0], tpl[2]))
                    nbdiff += 1
        if nbdiff == 0:
            logging.info(prefix+'no difference')
elif subcommand == 'filter-out':
    for target_name in target_names:
        logging.debug('process target {}'.format(target_name))
        if not os.path.isfile(target_name+'.out'):
            logging.warning('lacking file '+target_name+'.out')
            continue
        target = all_targets[target_name]
        fexps = [re.compile('^'+f.replace('%', '.*')+'$') for f in target['diff_filters_in']]
        proc1 = subprocess.Popen("cat {}.out 2>&1".format(target_name),
                                 shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out_log, _ = proc1.communicate()
        out_log_matches = []
        for line in out_log.split('\n'):
            for fmatch in [fexp.match(line) for fexp in fexps]:
                if fmatch:
                    out_log_matches.extend(fmatch.groups())
        nbdiff = 0
        if multi or expanded:
            prefix = target_name+': '
        else:
            prefix = ''
        for group in out_log_matches:
            logging.info(prefix+"{}".format(group))
            nbdiff += 1
        if nbdiff == 0:
            logging.info(prefix+'no match')
elif subcommand == 'filter-ref':
    for target_name in target_names:
        logging.debug('process target {}'.format(target_name))
        if not os.path.isfile(target_name+'.ref'):
            logging.warning('lacking file '+target_name+'.ref')
            continue
        target = all_targets[target_name]
        fexps = [re.compile('^'+f.replace('%', '.*')+'$') for f in target['diff_filters_in']]
        proc1 = subprocess.Popen("cat {}.ref 2>&1".format(target_name),
                                 shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out_ref, _ = proc1.communicate()
        out_ref_matches = []
        for line in out_ref.split('\n'):
            for fmatch in [fexp.match(line) for fexp in fexps]:
                if fmatch:
                    out_ref_matches.extend(fmatch.groups())
        nbdiff = 0
        if multi or expanded:
            prefix = target_name+': '
        else:
            prefix = ''
        for group in out_ref_matches:
            logging.info(prefix+"{}".format(group))
            nbdiff += 1
        if nbdiff == 0:
            logging.info(prefix+'no match')
else:
    logging.error('UNKNOWN SUBCOMMAND: '+subcommand)


