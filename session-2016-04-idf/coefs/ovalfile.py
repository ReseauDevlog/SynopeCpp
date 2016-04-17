# -*- coding: utf-8 -*-

'''
Configuration file for the tool oval.
'''

# compilation targets

#targets = [
#
#    {"name": "analyze_ex0", "command": "pylint ex0_hello_loops.py"},
#    {"name": "analyze_ex1", "command": "pylint ex1_read_image.py"},
#    {"name": "analyze_ex2", "command": "pylint ex2_background.py"},
#    {"name": "analyze_ex3", "command": "pylint ex3_clusters.py"},
#    {"name": "analyze_ex4", "command": "pylint ex4_coordinates.py"},
#    {"name": "analyze_ex5", "command": "pylint ex5_find_stars.py"},
#
#]

targets = []

tps = [
    {"name": "tp1_procedural", "etapes": []},
    {"name": "tp2_objets", "etapes": ["etape1", "etape2"]},
    {"name": "tp3_exceptions", "etapes": ["etape1"]},
    {"name": "tp4_generique", "etapes": []},
    {"name": "tp5_biblio", "etapes": ["etape1", "etape2", "etape3", "etape4"]},
    {"name": "tp6_parallele", "etapes": ["lambda", "thread"]},
]

name = "make_{}_{}"
command = "g++-5 -std=c++14 {0}_{1}.cpp -o {0}_{1}.exe"

for session in tps:

    base = session["name"]
    targets.append({"name": name.format(base,"depart"), "command": command.format(base,"depart")})
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape), "command": command.format(base,etape)})
    targets.append({"name": name.format(base,"arrivee"), "command": command.format(base,"arrivee")})

"""
# generated targets

import os
for exercice in exercices:
    for index, img in enumerate(os.listdir('data')):
        token = "data{}".format(index)
        target = "{}.{}".format(exercice,token)
        command = "./{}.py -b data/{}".\
            format(exercice,img,exercice,exercice,token)
        targets.append({"name": target, "command": command})
"""

# Filters

run_filters_out = []
diff_filters_in = [
    {"name": "make", "re": "%", "apply": "make%"},
]

"""
run_filters_out = [ {"name": "wcs", "re": "^(WARNING:|warning:|Defunct).*$", "apply": "ex(4|5)%"}, ]

diff_filters_in = [
    {"name": "pylint1", "re": "%rated at%", "apply": "(analyze%)|(oval%)"},
    {"name": "pylint2", "re": "[CEWIDR]:%", "apply": "(analyze%)|(oval%)"},
    {"name": "info", "re": "^(.+)$", "apply": "ex%"},
]
"""