import database
class CD:
     def __init__(self,cd_no,title,subject,rental_price,no_of_copies):
        self.cd_no = cd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies

     def insert_cd(cd):
         con = database.db_connect()
         with con:
             try:
                 con.execute("INSERT INTO Lecture_cd(cd_no,title,subject_id,rental_price,no_of_copies) VALUES"
                          "(?,?,?,?,?);",(cd.cd_no,cd.title,cd.subject,cd.rental_price,cd.no_of_copies)
                 )
                 return True
             except:
                 return False
         con.close()


     def get_all_cd(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM Lecture_cd").fetchall()
        con.close()

     def delete_cd_by_cd_no(cd_no):
         con = database.db_connect()
         with con:
             try:
                 con.execute("DELETE FROM Lecture_cd WHERE cd_no=?;", (cd_no,))
                 return True
             except:
                 return False
         con.close()




