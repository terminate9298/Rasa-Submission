import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

## Table Creation
conn.execute('''CREATE TABLE rasa (ID INT PRIMARY KEY  NOT NULL,
         NAME TEXT,
         PHONE TEXT,
         MAIL CHAR(50));''')
print("Table created successfully");

## Print All the rows In table
cursor = conn.execute("SELECT ID, NAME, PHONE, MAIL from rasa")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("PHONE = ", row[2])
   print ("MAIL = ", row[3], "\n")

## Insert In The Table
#conn.execute("INSERT INTO rasa (ID,NAME,PHONE,MAIL) \
      # VALUES (1, 'Kaustubh Pathak', '+919149042316', 'kaus.pathak@gmail.com')");
# conn.commit()
conn.close()