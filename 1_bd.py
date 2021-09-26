#coding:utf-8

"""
    + avec le logiciel SQLiteDatabaseBrowserPortable on va créer une BD. 
    + créer une connexion à BD 
    + création à un curseur
    + faire du CRUD avec des requettes sql sécurisé
        - C : ajouter (create)
        - R : lire (select)
        - U : modifié (update)
        - D : supprimer (delete)
    + Géstion des erreurs au moment d'envoyer des requettes à la BD
"""

from os import error
import sqlite3
from sqlite3.dbapi2 import Connection

"""
# connexion à la bd => creation de l'objet connexion
connection = sqlite3.connect("base.db")

# création d'un curseur => création de l'objet cursseur
cursor = connection.cursor()
print(type(connection))
print(type(cursor))

# Lancer une requette sql sécurisé exemple select pour lire une ligne 
# /1/ LIRE ==> SELECT * FROM t_users WHERE user_name = 'Omar'
my_username = ("Omar", )
cursor.execute('SELECT * FROM t_users WHERE user_name = ?', my_username)
# récupération de résultat (1 resultat qui est une ligne donc on utiliser "fetchone")
# print(f"le nom de l'utilisateur {cursor.fetchone()[1]}")
nomUser = cursor.fetchone()[1]
print(f"le nom de l'utilisateur {nomUser}")
print(cursor.lastrowid)

# fermé de connexion 
connection.close()
"""
# /2/ AJOUTER ==> INSERT INTO t_users(user_name, user_level) VALUES('Christophe', 15)
try:
    sqliteConnection = sqlite3.connect('base.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite", cursor.lastrowid)

    
    #sqlite_insert_query = 'INSERT INTO t_users (id_user, user_name, user_level) VALUES (?, ?, ?);'
    #newUser = (3, "Christophe", 12)
    #newUser = (cursor.lastrowid, "titi", 12)
    sqlite_insert_query = 'INSERT INTO t_users (user_name, user_level) VALUES (?, ?);'
    newUser = ("muma", 12)
    cursor.execute(sqlite_insert_query, newUser)
    sqliteConnection.commit()
    print("Nouveau utilisateur ajouté", cursor.lastrowid)
    
    touteLaTable = cursor.execute('SELECT * FROM t_users')
    #print(touteLaTable.fetchall())
    for row in touteLaTable.fetchall():
        print(row)
    
except sqlite3.Error as error:
    print(f"erreur {error}")
#except Exception as error:
#    print(f"erreur {error}")
    sqliteConnection.rollback()
finally:
    sqliteConnection.close()

"""
connection = sqlite3.connect("base.db")
cursor = connection.cursor()
newUser = (3, "Christophe", 12)
#cursor.execute('INSERT INTO t_users(id_user, user_name, user_level) VALUES(?,?,?)', newUser)
cursor.execute('INSERT INTO t_users(user_name, user_level) VALUES("titi", 15)')
connection.commit()




"""