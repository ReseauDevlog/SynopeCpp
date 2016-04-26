# -*- coding: utf-8 -*-

'''
Configuration file for the tool oval.
'''

# tableau récapitulatif de toutes les étapes

tps = [
    {"name": "tp1_procedural",
     "etapes": [
         {"name": "etape00", "mcx": "mcx_utilitaires.simple mcx_main.test_utilitaires", "args": ""},
         {"name": "etape01", "mcx": "mcx_utilitaires.simple mcx_main.boucle_exposant", "args": ""},
         {"name": "etape02", "mcx": "mcx_utilitaires.simple mcx_calculs.approxime_for mcx_main.approxime", "args": ""},
         {"name": "etape03", "mcx": "mcx_utilitaires.simple mcx_calculs.approxime_for_approximation mcx_main.approxime", "args": ""},
         {"name": "etape04", "mcx": "mcx_utilitaires.simple mcx_calculs.approxime_max mcx_main.approxime_max", "args": ""},
         {"name": "etape05", "mcx": "mcx_utilitaires.simple mcx_calculs.approxime_bits mcx_main.approxime_bits", "args": ""},
         {"name": "etape06", "mcx": "mcx_utilitaires.simple mcx_calculs.approxime_ref mcx_tests.approxime mcx_main.teste_approxime", "args": ""},
         {"name": "etape07", "mcx": "mcx_utilitaires.simple mcx_calculs.simple mcx_tests.approxime mcx_main.multiplie", "args": ""},
         {"name": "etape08", "mcx": "mcx_utilitaires.compacte mcx_calculs.simple mcx_tests.simple mcx_main.simple", "args": ""},
         {"name": "etape09", "mcx": "mcx_utilitaires.compacte mcx_framework.pfonctions mcx_calculs.simple mcx_tests.fonctions mcx_main.pfonctions", "args": ""},
         {"name": "etape10", "mcx": "mcx_utilitaires.compacte_rand mcx_framework.pfonctions mcx_calculs.simple mcx_tests.fonctions_rand mcx_main.pfonctions_rand", "args": "10"},
         {"name": "etape11", "mcx": "mcx_utilitaires.compacte_rand mcx_framework.pfonctions_ostream mcx_calculs.simple mcx_tests.fonctions_ostream mcx_main.pfonctions_ostream", "args": "10 resultat.txt"}
         ]},
    {"name": "tp2_objets",
     "etapes": [
         {"name": "etape00", "mcx": "mcx_utilitaires.compacte mcx_calculs.simple mcx_tests.simple mcx_main.simple", "args": ""},
         {"name": "etape08", "mcx": "mcx_utilitaires.compacte mcx_framework.erreur mcx_calculs.classe mcx_tests.classes mcx_main.classes", "args": ""}, 
         {"name": "etape17", "mcx": "mcx_utilitaires.compacte mcx_framework.virtual mcx_calculs.classe mcx_tests.virtual mcx_main.virtual", "args": ""},
         {"name": "etape25", "mcx": "mcx_utilitaires.const mcx_framework.constructeurs_et_statiques mcx_calculs.const mcx_tests.constructeurs mcx_main.constructeurs_et_statiques", "args": ""}
         ]},
    {"name": "tp3_exceptions",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple", "args": ""},
         {"name": "etape1", "mcx": "mcx_utilitaires.simple", "args": ""},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple", "args": ""}
         ]},
    {"name": "tp4_generique",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple", "args": ""},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple", "args": ""}
         ]},
    {"name": "tp5_biblio",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple", "args": ""},
         {"name": "etape1", "mcx": "mcx_utilitaires.simple", "args": ""}, 
         {"name": "etape2", "mcx": "mcx_utilitaires.simple", "args": ""}, 
         {"name": "etape3", "mcx": "mcx_utilitaires.simple", "args": ""}, 
         {"name": "etape4", "mcx": "mcx_utilitaires.simple", "args": ""},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple", "args": ""}
         ]},
    {"name": "tp6_parallele",
     "etapes": [
         {"name": "etape0", "mcx": "mcx_utilitaires.simple", "args": ""},
         {"name": "etape1", "mcx": "mcx_utilitaires.simple", "args": ""}, 
         {"name": "etape2", "mcx": "mcx_utilitaires.simple", "args": ""},
         {"name": "etapeN", "mcx": "mcx_utilitaires.simple", "args": ""}
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
command = "./{}_{}.exe {}"

for session in tps:

    base = session["name"]
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape["name"]), "command": command.format(base,etape["name"],etape["args"])})


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
