#coding:utf-8

"""
    cursor.rowcount => compter la ligne
    cursor.lastrowid => dernier identifient
"""
import mysql.connector as MC

try:
    mysqlConnector = MC.connect(host = 'localhost', database = 'datatest', user = 'root', password = '')
    cursor = mysqlConnector.cursor()

    # /1/ ajouter
    #requetteAjout = 'INSERT INTO ninjatable(id_ninja, ninja_firstnam, ninja_lastname) VALUES(%s, %s, %s)'
    #nouveauNinja = (cursor.lastrowid, 'mch', 'mariem')
    requetteAjout = 'INSERT INTO ninjatable(ninja_firstnam, ninja_lastname) VALUES(%s, %s)'
    nouveauNinja = ('mama', 'mina')
    cursor.execute(requetteAjout, nouveauNinja)
    mysqlConnector.commit()

    # /0/ lire 
    requette = 'SELECT * FROM ninjatable'
    cursor.execute(requette)
    
    print("last id", cursor.lastrowid)
    #fetchone => récuperer une seul information
    #fetchall => récuperer plusieur information
    #fetchmany
    ninjaListe = cursor.fetchall()
    for ninja in ninjaListe:
        print(ninja)
        print(f"Prénom -> {ninja[1]} / nom -> {ninja[2]}")


except MC.Error as err:
    print(err)

finally:
    if(mysqlConnector.is_connected()):
        cursor.close()
        mysqlConnector.close()
