# python nomfichier.py
import json
import datetime
import random
import decimal

num_unite = 2
temp_cuve = float (decimal.Decimal(random.randrange(250, 400))/100)
temp_exterieur = float (decimal.Decimal(random.randrange(800, 1400))/100)


data = {
    "Numéro d'unité": num_unite,
    "Numéro d'automate": 5,
    "Type d'automate": "0X0000BA20",
    "Température cuve": temp_cuve,
    "Température extérieur": temp_exterieur,
    "Poids du lait en cuve": random.randrange(3512, 4607, 1),
    "Poids du produit fini réalisé": 20,
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