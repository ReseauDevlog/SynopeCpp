#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
#import os
#import os.path
#import re
#import subprocess
#import sys
#import hashlib

# command-line options
parser = argparse.ArgumentParser(description='Assemble des morceaux de code')
parser.add_argument('sortie', help='nom du fichier généré')
parser.add_argument('morceaux', nargs='*', help='liste de morceaux')
args = parser.parse_args()

# get and write snippets
fichier = open(args.sortie,'w')
fichier.write('// -*- coding: utf-8 -*-\n')
for morceau in args.morceaux:
    print(morceau)
    elems = morceau.split('.')
    module = __import__(elems[0])
    fichier.write(module.__dict__[elems[1]])
fichier.close()
