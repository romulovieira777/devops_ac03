import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE romulo (id integer, nome text not null, email text null)''')
c.execute("INSERT INTO romulo VALUES (1, 'romulo','romulo@gmail.com')")
c.execute("INSERT INTO romulo VALUES (2, 'vieira', null)")

c.execute('''SELECT * FROM romulo''')

for row in c.fetchall():
    print(row)

conn.commit()
conn.close()
