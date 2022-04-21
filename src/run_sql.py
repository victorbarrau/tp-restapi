from sqlalchemy import create_engine

db_string="postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

connection.execute("CREATE TABLE IF NOT EXISTS films (title text,director text, year text)")
connection.execute("INSERT INTO Films (title,director,year) VALUES('Doctor Strange','scott Derickson','2016')")
