#import mysql.connector 
#baseDeDonnees = mysql.connector.connect(host="localhost:3307",user="root", database="projet_lettrine")
import pymysql.cursors
import json
connection = pymysql.connect(host='localhost',
                             user='root',
                             db='projet_lettrine',
                             cursorclass=pymysql.cursors.DictCursor)




with open('paramunite_2_1566465299.371275.json', 'r') as f:
    datastore = json.load(f)

#Use the new datastore datastructure

try:
    with connection.cursor() as cursor:
        # Create a new record

        sql = "INSERT INTO automate (num_unite, num_automate, type_automate, temp_cuve, temp_exterieur, poids_lait_cuve, poids_produit_fini, ph, kplus, concentration_naci, niv_bacterien_salmonelle, niv_bacterien_ecoli, niv_bacterien_listeria) VALUES ( '" + str(datastore["Numéro d'unité"]) + "', '" + str(datastore["Numéro d'automate"]) + "', '" + str(datastore["Type d'automate"]) + "', '" + str(datastore["Température cuve"]) + "', '" + str(datastore["Température extérieur"]) + "', '" + str(datastore["Poids du lait en cuve"]) + "', '" + str(datastore["Poids du produit fini réalisé"]) + "', '" + str(datastore["Mesure pH"]) + "', '" + str(datastore["Mesure K+"]) + "', '" + str(datastore["concentration de NaCI"]) + "', '" + str(datastore["Niveau bactérien salmonelle"]) + "', '" + str(datastore["Niveau bactérien E-coli"]) + "', '" + str(datastore["Niveau bactérien Listéria"]) + "')"

        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()