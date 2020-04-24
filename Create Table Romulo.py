import sqlite3
conn = sqlite3.connect('exercicio1.db')

c = conn.cursor()

c.execute('''CREATE TABLE romulo(
                id integer,
                nome text not null,
                email text,
                primary key (id) )'''
                )

c.execute("INSERT INTO romulo VALUES (1,'Romulo Vieira','romulo.vieira@aluno.faculdadeimpacta.com.br')")


conn.commit()

conn.close()
