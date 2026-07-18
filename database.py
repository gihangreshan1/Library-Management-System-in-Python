import sqlite3

def db_connect():
    return sqlite3.connect('library.db')

def create_tables():
    con = db_connect()
    with con:
        con.execute("CREATE TABLE IF NOT EXISTS subjects( subject_id INTEGER  PRIMARY KEY AUTOINCREMENT, name TEXT );")
        con.execute("CREATE TABLE IF NOT EXISTS book("
                    "isbn VARCHAR  PRIMARY KEY,"
                    "title TEXT, "
                    "sub_format TEXT,"
                    "subject_id INTEGER,"
                    "rental_price REAL,"
                    "no_of_copies INTEGER,"
                    
                    "FOREIGN KEY(subject_id) REFERENCES subject(sub_id));"

                    )

        con.execute("CREATE TABLE IF NOT EXISTS magazine("
                    "mag_no VARCHAR  PRIMARY KEY,"
                    "title TEXT, "
                    "color TEXT, "
                    "subject_id INTEGER,"
                    "rental_price REAL,"
                    "no_of_copies INTEGER,"
    
                    "FOREIGN KEY(subject_id) REFERENCES subject(sub_id));"
                    )

        con.execute("CREATE TABLE IF NOT EXISTS Educational_dvd("
                    "dvd_no VARCHAR  PRIMARY KEY,"
                    "title TEXT, "
                    "subject_id INTEGER,"
                    "rental_price REAL,"
                    "no_of_copies INTEGER,"

                    "FOREIGN KEY(subject_id) REFERENCES subject(sub_id));"
                    )
        con.execute("CREATE TABLE IF NOT EXISTS Lecture_cd("
                    "cd_no VARCHAR  PRIMARY KEY,"
                    "title TEXT, "
                    "subject_id INTEGER,"
                    "rental_price REAL,"
                    "no_of_copies INTEGER,"

                    "FOREIGN KEY(subject_id) REFERENCES subject(sub_id));"
                    )
    con.close()

def insert_subject():
    con = db_connect()
    with con:
        con.execute("INSERT INTO subjects(name) VALUES ('Science')")
        con.execute("INSERT INTO subjects(name) VALUES ('History')")
        con.execute("INSERT INTO subjects(name) VALUES ('Literature')")

        con.execute("INSERT INTO subjects(name) VALUES ('Technology')")
        con.execute("INSERT INTO subjects(name) VALUES ('Sports')")

        con.execute("INSERT INTO subjects(name) VALUES ('Astronomy')")
        con.execute("INSERT INTO subjects(name) VALUES ('Math')")
        con.execute("INSERT INTO subjects(name) VALUES ('Music')")
        con.execute("INSERT INTO subjects(name) VALUES (' Foreign_Languages')")






    con.close()

def get_all_Subjects():
    con = db_connect()
    with con:
        print(con.execute("SELECT * FROM subjects").fetchall())
    con.close()




