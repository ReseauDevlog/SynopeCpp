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
         {"name": "etape01", "mcx": "mcx_utilitaires.compacte mcx_calculs.struct mcx_tests.struct mcx_main.simple", "args": ""},
         {"name": "etape02", "mcx": "mcx_utilitaires.compacte mcx_calculs.retour mcx_tests.retour mcx_main.simple", "args": ""},
         {"name": "etape03", "mcx": "mcx_utilitaires.compacte mcx_calculs.classe mcx_tests.coef mcx_main.simple", "args": ""},
         {"name": "etape04", "mcx": "mcx_utilitaires.compacte mcx_calculs.classe mcx_tests.tcoef mcx_main.tcoef", "args": ""},
         {"name": "etape05", "mcx": "mcx_utilitaires.compacte mcx_calculs.coef_bits mcx_tests.tcoefbits mcx_main.tcoef", "args": ""},
         {"name": "etape06", "mcx": "mcx_utilitaires.compacte mcx_calculs.coef_bits mcx_tests.tcoefatt mcx_main.tcoef", "args": ""},
         {"name": "etape07", "mcx": "mcx_utilitaires.compacte mcx_calculs.coef_bits mcx_tests.testeurs mcx_main.testeurs", "args": ""},
         {"name": "etape08", "mcx": "mcx_utilitaires.compacte mcx_framework.erreur mcx_calculs.coef_bits mcx_tests.erreur mcx_main.testeurs", "args": ""}, 
         {"name": "etape09", "mcx": "mcx_utilitaires.compacte mcx_framework.testeur mcx_calculs.coef_bits mcx_tests.heritage mcx_main.heritage", "args": ""}, 
         {"name": "etape10", "mcx": "mcx_utilitaires.compacte mcx_framework.virtual mcx_calculs.coef_bits mcx_tests.heritage mcx_main.virtual", "args": ""}, 
         {"name": "etape11", "mcx": "mcx_utilitaires.compacte mcx_framework.boucle_foncteur mcx_calculs.coef_bits mcx_tests.heritage mcx_main.boucle_foncteur", "args": ""}, 
         {"name": "etape12", "mcx": "mcx_utilitaires.compacte mcx_framework.boucle_conteneur mcx_calculs.coef_bits mcx_tests.heritage mcx_main.boucle_conteneur", "args": ""}, 
         {"name": "etape13", "mcx": "mcx_utilitaires.compacte mcx_framework.conteneur_ptr mcx_calculs.coef_bits mcx_tests.heritage mcx_main.conteneur_ptr", "args": ""}, 
         {"name": "etape14", "mcx": "mcx_utilitaires.compacte mcx_framework.conteneur_indice mcx_calculs.coef_bits mcx_tests.heritage mcx_main.conteneur_indice", "args": ""}, 
         {"name": "etape15", "mcx": "mcx_utilitaires.compacte mcx_framework.conteneur_dyn mcx_calculs.coef_bits mcx_tests.heritage mcx_main.conteneur_dyn", "args": ""}, 
         {"name": "etape16", "mcx": "mcx_utilitaires.compacte mcx_framework.conteneur_owner mcx_calculs.coef_bits mcx_tests.virtual mcx_main.conteneur_owner", "args": ""},
         {"name": "etape17", "mcx": "mcx_utilitaires.compacte mcx_framework.constructeurs_testeurs_derives mcx_calculs.coef_bits mcx_tests.constructeurs_derives mcx_main.constructeurs_testeurs", "args": ""},
         {"name": "etape18", "mcx": "mcx_utilitaires.compacte mcx_framework.constructeurs_testeurs mcx_calculs.coef_bits mcx_tests.constructeurs_testeurs mcx_main.constructeurs_testeurs", "args": ""},
         {"name": "etape19", "mcx": "mcx_utilitaires.compacte mcx_framework.constructeurs_testeurs mcx_calculs.constructeur mcx_tests.constructeurs mcx_main.constructeurs_testeurs", "args": ""},
         {"name": "etape20", "mcx": "mcx_utilitaires.compacte mcx_framework.constructeurs mcx_calculs.constructeur mcx_tests.constructeurs mcx_main.constructeurs", "args": ""},
         {"name": "etape21", "mcx": "mcx_utilitaires.const mcx_framework.const mcx_calculs.const_bits mcx_tests.constructeurs mcx_main.constructeurs", "args": ""},
         {"name": "etape22", "mcx": "mcx_utilitaires.const mcx_framework.const mcx_calculs.affiche mcx_tests.affiche mcx_main.constructeurs", "args": ""},
         {"name": "etape23", "mcx": "mcx_utilitaires.const mcx_framework.conteneur_dedie mcx_calculs.affiche mcx_tests.affiche mcx_main.conteneur_dedie", "args": ""},
         {"name": "etape24", "mcx": "mcx_utilitaires.const mcx_framework.statiques mcx_calculs.affiche mcx_tests.constructeurs mcx_main.statiques", "args": ""}
         ]},
    {"name": "tp3_exceptions",
     "etapes": [
         {"name": "etape00", "mcx": "mcx_utilitaires.const mcx_framework.conteneur_dedie mcx_calculs.affiche mcx_tests.affiche mcx_main.conteneur_dedie", "args": ""},
         {"name": "etape01", "mcx": "mcx_utilitaires.exception mcx_framework.throw mcx_calculs.throw mcx_tests.affiche mcx_main.catch_check", "args": ""},
         {"name": "etape02", "mcx": "mcx_utilitaires.exception mcx_framework.catch mcx_calculs.throw mcx_tests.bug mcx_main.catch", "args": ""},
         {"name": "etape03", "mcx": "mcx_utilitaires.exception mcx_framework.catch mcx_calculs.opmult mcx_tests.opmult mcx_main.catch", "args": ""},
         {"name": "etape04", "mcx": "mcx_utilitaires.exception mcx_framework.opbrackets mcx_calculs.opmult mcx_tests.opmult mcx_main.catch", "args": ""},
         {"name": "etape05", "mcx": "mcx_utilitaires.exception mcx_framework.opbrackets mcx_calculs.opaffect mcx_tests.opaffect mcx_main.catch", "args": ""},
         {"name": "etape06", "mcx": "mcx_utilitaires.exception mcx_framework.opbrackets mcx_calculs.ostream mcx_tests.ostream mcx_main.catch", "args": ""},
         {"name": "etape07", "mcx": "mcx_utilitaires.exception mcx_framework.opbrackets mcx_calculs.opdouble mcx_tests.opdouble mcx_main.catch", "args": ""},
         {"name": "etape08", "mcx": "mcx_utilitaires.exception mcx_framework.opexec mcx_calculs.opdouble mcx_tests.opexec mcx_main.catch", "args": ""},
         ]},
    {"name": "tp4_generique",
     "etapes": [
         {"name": "etape00", "mcx": "mcx_utilitaires.gen0 mcx_framework.gen0 mcx_calculs.gen0 mcx_tests.gen0 mcx_main.gen0", "args": ""},
         {"name": "etape01", "mcx": "mcx_utilitaires.gen0 mcx_framework.gen0 mcx_calculs.gennum mcx_tests.coefint mcx_main.gen0", "args": ""},
         {"name": "etape02", "mcx": "mcx_utilitaires.gen0 mcx_framework.gen0 mcx_calculs.genmult mcx_tests.coefint mcx_main.gen0", "args": ""},
         {"name": "etape03", "mcx": "mcx_utilitaires.gen0 mcx_framework.gen0 mcx_calculs.template mcx_tests.gensomme mcx_main.shortsomme", "args": ""},
         {"name": "etape04", "mcx": "mcx_utilitaires.gen0 mcx_framework.gen0 mcx_calculs.template mcx_tests.gencoef mcx_main.shortcoef", "args": ""},
         {"name": "etape05", "mcx": "mcx_utilitaires.gen0 mcx_framework.gen0 mcx_calculs.uchar mcx_tests.gencoef mcx_main.uchar", "args": ""},
         {"name": "etape06", "mcx": "mcx_utilitaires.gen0 mcx_framework.template mcx_calculs.uchar mcx_tests.gencoef mcx_main.gentesteurs", "args": ""},
         {"name": "etape07", "mcx": "mcx_utilitaires.constexpr mcx_framework.template mcx_calculs.constexpr mcx_tests.gencoef mcx_main.gentesteurs", "args": ""},
         {"name": "etape08", "mcx": "mcx_utilitaires.traits mcx_framework.template mcx_calculs.traits mcx_tests.gencoef mcx_main.traits", "args": ""}
         ]},
    {"name": "tp5_biblio",
     "etapes": [
         {"name": "etape00", "mcx": "mcx_utilitaires.biblio mcx_framework.biblio mcx_calculs.biblio mcx_tests.biblio mcx_main.biblio", "args": ""},
         {"name": "etape01", "mcx": "mcx_utilitaires.biblio mcx_framework.vector mcx_calculs.biblio mcx_tests.biblio mcx_main.vector", "args": ""},
         {"name": "etape02", "mcx": "mcx_utilitaires.pointeur_bavard mcx_framework.pointeur_bavard mcx_calculs.biblio mcx_tests.biblio mcx_main.vector_bavard", "args": ""},
         {"name": "etape03", "mcx": "mcx_utilitaires.auto_pointeur mcx_framework.auto_pointeur mcx_calculs.biblio mcx_tests.biblio mcx_main.vector", "args": ""},
         {"name": "etape04", "mcx": "mcx_utilitaires.biblio mcx_framework.shared mcx_calculs.biblio mcx_tests.biblio mcx_main.shared", "args": ""},
         {"name": "etape05", "mcx": "mcx_utilitaires.biblio mcx_framework.unique mcx_calculs.biblio mcx_tests.biblio mcx_main.unique", "args": ""},
         {"name": "etape06", "mcx": "mcx_utilitaires.biblio mcx_framework.direct mcx_calculs.biblio mcx_tests.biblio mcx_main.direct", "args": ""}
         ]},
    {"name": "tp6_parallele",
     "etapes": [
         {"name": "etape00", "mcx": "mcx_utilitaires.parallele mcx_framework.parallele mcx_calculs.biblio mcx_tests.parallele mcx_main.parallele", "args": ""},
         {"name": "etape01", "mcx": "mcx_utilitaires.parallele mcx_framework.auto mcx_calculs.biblio mcx_tests.parallele mcx_main.auto", "args": ""},
         {"name": "etape02", "mcx": "mcx_utilitaires.parallele mcx_framework.lambdas mcx_calculs.biblio mcx_tests.parallele mcx_main.auto", "args": ""},
         {"name": "etape03", "mcx": "mcx_utilitaires.parallele mcx_framework.forgen mcx_calculs.biblio mcx_tests.parallele mcx_main.auto", "args": ""},
         {"name": "etape04", "mcx": "mcx_utilitaires.parallele mcx_framework.threads mcx_calculs.biblio mcx_tests.parallele mcx_main.auto", "args": ""},
         {"name": "etape05", "mcx": "mcx_utilitaires.parallele mcx_framework.stress mcx_calculs.biblio mcx_tests.parallele mcx_main.stress", "args": ""},
         {"name": "etape06", "mcx": "mcx_utilitaires.parallele mcx_framework.sharedmem mcx_calculs.biblio mcx_tests.parallele mcx_main.mutex", "args": ""},
         {"name": "etape07", "mcx": "mcx_utilitaires.parallele mcx_framework.async mcx_calculs.biblio mcx_tests.parallele mcx_main.auto", "args": ""}
         ]},
]

targets = []


# code generation targets

name = "gen_{}_{}"
command = "./ovalgen.py {}_{}.cpp {}"

for session in tps:

    base = session["name"]
    for etape in session["etapes"]:
        targets.append({"name": name.format(base,etape["name"]), "command": command.format(base,etape["name"],etape["mcx"])})


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
