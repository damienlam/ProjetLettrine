import socket
import os
import pymysql.cursors
import json
dbConection = pymysql.connect(host='localhost',
                             user='root',
                             db='projet_lettrine',
                             cursorclass=pymysql.cursors.DictCursor)

hote = ''
port = 12800

# Create server connection
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Server launch on port : {}".format(port))

# Accept client connection
connexion_avec_client, infos_connexion = connexion_principale.accept()


while True:

    # Msg client
    json_path = connexion_avec_client.recv(1024)

    # JSON DATA
    with open(json_path, 'r') as f:
        datastore = json.load(f)

    # Save to DB
    with dbConection.cursor() as cursor:

        sql = "INSERT INTO automate (num_unite, num_automate, type_automate, temp_cuve, temp_exterieur, poids_lait_cuve, poids_produit_fini, ph, kplus, concentration_naci, niv_bacterien_salmonelle, niv_bacterien_ecoli, niv_bacterien_listeria) VALUES ( '" + str(datastore["Numéro d'unité"]) + "', '" + str(datastore["Numéro d'automate"]) + "', '" + str(datastore["Type d'automate"]) + "', '" + str(datastore["Température cuve"]) + "', '" + str(datastore["Température extérieur"]) + "', '" + str(datastore["Poids du lait en cuve"]) + "', '" + str(datastore["Poids du produit fini réalisé"]) + "', '" + str(datastore["Mesure pH"]) + "', '" + str(datastore["Mesure K+"]) + "', '" + str(datastore["concentration de NaCI"]) + "', '" + str(datastore["Niveau bactérien salmonelle"]) + "', '" + str(datastore["Niveau bactérien E-coli"]) + "', '" + str(datastore["Niveau bactérien Listéria"]) + "')"

        cursor.execute(sql)
        dbConection.commit()

    # Remove file
    if os.path.exists(json_path):
        os.remove(json_path)
    else:
        print("The file does not exist")

    # Show msg from client
    print(json_path.decode())

    # Send msg to client
    connexion_avec_client.send(b"JSON Data was save in Database")

# If msg send by client is "exit"
""" print("Connection close")
connexion_avec_client.close()
connexion_principale.close() """