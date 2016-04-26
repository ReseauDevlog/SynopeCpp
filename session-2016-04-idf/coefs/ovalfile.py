# -*- coding: utf-8 -*-

'''
Configuration file for the tool oval.
'''

# tableau récapitulatif de toutes les étapes

tps = [
    {"name": "tp1_procedural",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple mcx_main.test_utilitaires"},
         {"name": "etapeN", "mcx": "mcx_utilitaires.rand mcx_framework.pfonctions mcx_calculs.simple mcx_tests.fonctions mcx_main.pfonctions"}
         ]},
    {"name": "tp2_objets",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.compacte mcx_calculs.simple mcx_tests.simple mcx_main.simple"},
         {"name": "etape1", "mcx": "mcx_utilitaires.compacte mcx_framework.erreur mcx_calculs.classe mcx_tests.classes mcx_main.classes"}, 
         {"name": "etape2", "mcx": "mcx_utilitaires.compacte mcx_framework.virtual mcx_calculs.classe mcx_tests.virtual mcx_main.virtual"},
         {"name": "etapeN", "mcx": "mcx_utilitaires.const mcx_framework.constructeurs_et_statiques mcx_calculs.const mcx_tests.constructeurs mcx_main.constructeurs_et_statiques"}
         ]},
    {"name": "tp3_exceptions",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple"},
         {"name": "etape1", "mcx": "mcx_utilitaires.simple"},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple"}
         ]},
    {"name": "tp4_generique",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple"},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple"}
         ]},
    {"name": "tp5_biblio",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple"},
         {"name": "etape1", "mcx": "mcx_utilitaires.simple"}, 
         {"name": "etape2", "mcx": "mcx_utilitaires.simple"}, 
         {"name": "etape3", "mcx": "mcx_utilitaires.simple"}, 
         {"name": "etape4", "mcx": "mcx_utilitaires.simple"},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple"}
         ]},
    {"name": "tp6_parallele",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple"},
         {"name": "etape1", "mcx": "mcx_utilitaires.simple"}, 
         {"name": "etape2", "mcx": "mcx_utilitaires.simple"},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple"}
         ]},
]

targets = []


# backup targets

name = "bak_{}_{}"
command = "cp {0}_{1}.cpp bak_{0}_{1}.cpp"

for session in tps:

    base = session["name"]
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape["name"]), "command": command.format(base,etape["name"])})


# code generation targets

name = "gen_{}_{}"
command = "./ovalgen.py {}_{}.cpp {}"

for session in tps:

    base = session["name"]
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape["name"]), "command": command.format(base,etape["name"],etape["mcx"])})


# source diff targets

name = "sdiff_{}_{}"
command = "diff bak_{0}_{1}.cpp {0}_{1}.cpp"

for session in tps:

    base = session["name"]
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape["name"]), "command": command.format(base,etape["name"])})


# compilation targets

name = "make_{}_{}"
command = "g++ -std=c++11 {0}_{1}.cpp -o {0}_{1}.exe"

for session in tps:

    base = session["name"]
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape["name"]), "command": command.format(base,etape["name"])})


# execution targets

name = "run_{}_{}"
command = "./{0}_{1}.exe"

for session in tps:

    base = session["name"]
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape["name"]), "command": command.format(base,etape["name"])})


# filters

run_filters_out = []
diff_filters_in = [
    {"name": "all", "re": "%", "apply": "%"},
]

"""
run_filters_out = [ {"name": "wcs", "re": "^(WARNING:|warning:|Defunct).*$", "apply": "ex(4|5)%"}, ]

diff_filters_in = [
    {"name": "pylint1", "re": "%rated at%", "apply": "(analyze%)|(oval%)"},
    {"name": "pylint2", "re": "[CEWIDR]:%", "apply": "(analyze%)|(oval%)"},
    {"name": "info", "re": "^(.+)$", "apply": "ex%"},
]
"""
