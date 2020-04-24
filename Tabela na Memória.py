import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE Romulo (id integer, nome text not null, email text null)''')
c.execute("INSERT INTO Romulo VALUES (1, 'romulo','romulo.vieira@123456789.com')")
c.execute("INSERT INTO Romulo VALUES (2, 'romulo', romulo.silva@123456789.com)")

c.execute('''SELECT * FROM Romulo''')

for row in c.fetchall():
    print(row)

conn.commit()
conn.close()