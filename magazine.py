import database
class Magazine:
     def __init__(self,mag_no,title,color,subject,rental_price,no_of_copies):
        self.mag_no = mag_no
        self.title = title
        self.color = color
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies

     def insert_magazine(magazine):
         con = database.db_connect()
         with con:
             try:
                 con.execute("INSERT INTO magazine(mag_no,title,color,subject_id,rental_price,no_of_copies) VALUES"
                          "(?,?,?,?,?,?);",(magazine.mag_no,magazine.title,magazine.color,magazine.subject,magazine.rental_price,magazine.no_of_copies)
                 )
                 return True
             except:
                 return False
         con.close()





     def get_all_magazines(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM magazine").fetchall()
        con.close()

     def delete_magazine_by_mag_no(mag_no):
         con = database.db_connect()
         with con:
             try:
                 con.execute("DELETE FROM magazine WHERE mag_no=?;", (mag_no,))
                 return True
             except:
                 return False
         con.close()