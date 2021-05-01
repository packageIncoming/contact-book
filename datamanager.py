import sqlite3

database = "contacts.db"

# start up
def initialize():
  db = sqlite3.connect(database)
  c = db.cursor()

  # Create a table
  c.execute("""
  CREATE TABLE contacts (
    first_name text,
    last_name text,
    phone_number text
  )
  """)
  db.commit()
  db.close()

# Delete contact based on rowid
def delete_one(r_id):
  db = sqlite3.connect(database)
  c = db.cursor()
  r = str(r_id)
  c.execute("SELECT * FROM contacts")
  c.execute("DELETE from contacts WHERE rowid = (?)",(r))


  db.commit()
  db.close()

# Insert one contact
def add_one(firstname,lastname,number):
    db = sqlite3.connect(database)
    c = db.cursor()
    c.execute("SELECT rowid, * from contacts WHERE first_name = (?) AND last_name = (?)",(firstname,lastname))
    tot = c.fetchall()
    if len(tot) > 0:
       print("This contact already exists. Updating..")
       first = tot[0]
       update_record(first[0],[firstname,lastname,number])
       for item in tot[1:]:
         #print(item[0])
         print(str(item[0]))
         delete_one(item[0])
       return
    c.execute("""
      INSERT INTO contacts VALUES (?,?,?)
    """, (firstname,lastname,number))
    db.commit()
    db.close()
    print("Added contact successfully.")
    

# Query the database and print out all records
def show_all():
  db = sqlite3.connect(database)
  c = db.cursor()
  c.execute("SELECT rowid, * FROM contacts")
  items = c.fetchall()
  for item in items:
    print("{}:  NAME: {} {}, PHONE: {}".format(*item))
  db.close()

def update_record(r_id,info):
  db = sqlite3.connect(database)
  c = db.cursor()

  firstname = info[0]
  lastname = info[1]
  number = info[2]

  c.execute("""
    UPDATE contacts
    SET first_name = (?),
    last_name = (?),
    phone_number = (?)
    WHERE rowid = (?)
  """,(firstname,lastname,number,r_id))
  db.commit()
  db.close()