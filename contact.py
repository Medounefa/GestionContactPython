import sqlite3

# conn = sqlite3.connect("contact.db")
# cur = conn.cursor()

with sqlite3.connect("contact.db") as conn:
    cur = conn.cursor()

def create_table () :
    req = "create table contacts(id integer primary key autoincrement, nom text, prenom text, email text, telephone integer, adresse text)"
    cur.execute(req)
    conn.commit()

# createTable()

def insertion():
    # utiliser avec les variable
    nom = input("Entrez votre nom")
    prenom = input("Entrez votre prenom")
    email = input("Entrez votre email")
    telephone = int(input("Entrez votre numero de telephone"))
    adresse = input("Entrez votre adresse")

    req = "insert into contacts (nom, prenom, email, telephone, adresse) values (?, ?, ?, ?,?)"
    # req = "create table contacts(id integer primary key autoincrement, nom text, prenom text, email text, telephone integer, adresse text)"
    cur.execute(req, (nom, prenom, email, telephone, adresse))
    conn.commit()
  
insertion()

def modification() :
    req = "update contacts set telephone=772333333 where id = 3"
    cur.execute(req)
    conn.commit()
    
modification()

def suppression ():
    req = "DELETE FROM contacts WHERE id = 3"
    cur.execute(req)
    conn.commit()
   
    
suppression ()

def liste_contact() :
    req = "SELECT * FROM contacts WHERE telephone = 777"
    result = cur.execute(req)

    for cont in result :
        print("Le contact selectionne est:", cont)

    
    
liste_contact()
    
