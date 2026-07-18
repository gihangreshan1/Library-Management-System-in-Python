import database
class DVD:
     def __init__(self,dvd_no,title,subject,rental_price,no_of_copies):
        self.dvd_no = dvd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies

     def insert_dvd(dvd):
         con = database.db_connect()
         with con:
             try:
                 con.execute("INSERT INTO Educational_dvd(dvd_no,title,subject_id,rental_price,no_of_copies) VALUES"
                          "(?,?,?,?,?);",(dvd.dvd_no,dvd.title,dvd.subject,dvd.rental_price,dvd.no_of_copies)
                 )
                 return True
             except:
                 return False
         con.close()


     def get_all_dvd(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM Educational_dvd").fetchall()
        con.close()

     def delete_dvd_by_dvd_no(dvd_no):
         con = database.db_connect()
         with con:
             try:
                 con.execute("DELETE FROM Educational_dvd WHERE dvd_no=?;", (dvd_no,))
                 return True
             except:
                 return False
         con.close()




