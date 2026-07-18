import database
class Book:
     def __init__(self,isbn,title,sub_format,subject,rental_price,no_of_copies):
        self.isbn = isbn
        self.title = title
        self.sub_format = sub_format
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies

     def insert_book(book):
         con = database.db_connect()
         with con:
             try:
                 con.execute("INSERT INTO book(isbn,title,sub_format,subject_id,rental_price,no_of_copies) VALUES"
                          "(?,?,?,?,?,?);",(book.isbn,book.title,book.sub_format,book.subject,book.rental_price,book.no_of_copies)
                 )
                 return True
             except:
                 return False
         con.close()


     def get_all_books(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM book").fetchall()
        con.close()

     def delete_book_by_isbn(isbn):
         con = database.db_connect()
         with con:
             try:
                 con.execute("DELETE FROM book WHERE isbn=?;", (isbn,))
                 return True
             except:
                 return False
         con.close()

     def get_all_resorces_search_by_subject(subject_id):
        con =database.db_connect()
        with con:
            try:
               select = con.execute("SELECT b.isbn, b.title,b.sub_format,b.subject_id,b.rental_price,b.no_of_copies AS book, m.mag_no, m.title,m.color,m.subject_id,m.rental_price,m.no_of_copies AS magazine FROM  book b LEFT JOIN magazine m ON b.subject_id = m.subject_id WHERE b.subject_id = ?;", (subject_id,))
               data= select.fetchall()

               return data
            except:
               return False
        con.close()





