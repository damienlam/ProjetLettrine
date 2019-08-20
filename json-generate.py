# python nomfichier.py
import json
import datetime
import random

num_unite = 2



data = {
    "Numéro d'unité": num_unite,
    "Numéro d'automate": 5,
    "Type d'automate": "0X0000BA20",
    "Température cuve": random.randrange(2.5, 4, 0.10),
    "Température extérieur": random.randrange(8, 14, 0.10),
    "Poids du lait en cuve": random.randrange(3512, 4607, 1),
    "Poids du produit fini réalié": 20,
    "Mesure pH": 7,
    "Mesure K+": 1,
    "concentration de NaCI": 20,
    "Niveau bactérien salmonelle": 20,
    "Niveau bactérien E-coli": 20,
    "Niveau bactérien Listéria": 20,
}

date_unix_epoch = datetime.datetime.now().timestamp()
filename = f'paramunite_{num_unite}_{date_unix_epoch}.json'

with open(filename, 'w') as outfile:
    json.dump(data, outfile)