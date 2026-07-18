import database
from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD

main_manu = "*************** Library Management System ***************" \
            "\nPlease choose option" \
            "\n1. Add new resources" \
            "\n2. Remove resources" \
            "\n3. Available resources" \
            "\n4. Unavailable resources" \
            "\n5. Search by subject" \
            "\n6. Lend resources" \
            "\n7. Receive resources" \
            "\n8. Exit"


add_resources = "*************** Add New Resources ***************" \
                "\n1. Add book" \
                "\n2. Add Magazine" \
                "\n3. Add Educational DVD" \
                "\n4. Add Lecture CD" \
                "\n5. Back"


remove_resources = "*************** Remove Resources ***************" \
                "\n1. Remove book" \
                "\n2. Remove Magazine" \
                "\n3. Remove Educational DVD" \
                "\n4. Remove Lecture CD" \
                "\n5. Back"
available_resources = "*************** Available Resources ***************" \
                "\n1. Book Available" \
                "\n2. Magazine Available" \
                "\n3. Educational DVD Available" \
                "\n4. Lecture Available" \
                "\n5. Back"

unavailable_resources = "*************** Unavailable Resources ***************" \
                "\n1. Book Unavailable" \
                "\n2. Magazine Unavailable" \
                "\n3. Educational DVD Unavailable" \
                "\n4. Lecture Unavailable" \
                "\n5. Back"

search_resources = "*************** Search resources by subject ***************" \
                "\n1. Science" \
                "\n2. History" \
                "\n3. Literature" \
                "\n4. Technology" \
                "\n5. Sports" \
                "\n5. Astronomy"\
                "\n5. Math"\
                "\n5. Music" \
                "\n5. Foreign_Languages"

def terminal():
    con = database.db_connect()
    database.create_tables()
    database.insert_subject()


    print(main_manu)
    main_option = input("Choose option: ")



    while True:
        if main_option == '1':
            print(add_resources)
            sub_option = input('Your option: ')

            if sub_option == '1':
                 print("*************** Add new book ***************")
                 isbn=title=sub_format=subject=rental_price=no_of_copies = None

                 while True:
                     isbn = input('ISBN: ')
                     if len(isbn) == 0:
                         print("Invalid ISBN")
                     else:
                        break
                 while True:
                     title = input('Title: ')
                     if len(title) == 0:
                         print("Invalid Title")
                     else:
                        break
                 while True:
                     sub_format = input('Format [1. Hardcover | 2. Paperback]: ')
                     if sub_format in ('1','2'):
                         if sub_format =='1':
                             sub_format='Hardcover'
                         else:
                             sub_format='Paperback'
                         break
                     else:
                         print('Invalid format')
                 while True:
                     subject= input('Subject [1. Science | 2. History | 3. Literature ] ')
                     if subject in ('1','2','3'):
                         if subject=='1':
                             subject='Science'
                         elif subject=='2':
                             subject='History'
                         else:
                             subject='Literature'
                         break
                     else:
                         print("Invalid subject")
                 while True:
                     rental_price = input('Rental price: ')
                     if rental_price.isnumeric() and rental_price !='0':
                         break
                     else:
                         print("Invalid Rental price")

                 while True:
                     no_of_copies = input("No_of_copies: ")
                     if no_of_copies.isnumeric():
                         break
                     else:
                         print("Invalid No of copies")


                 book = Book(isbn,title,sub_format,subject,rental_price,no_of_copies)
                 if Book.insert_book(book):
                     print("Successfully saved a book")
                 else:
                     print("Already saves this book")

                 print(Book.get_all_books(book))

            elif sub_option == '2':
                print("*************** Add new magazine ***************")
                mag_no = title = color = subject = rental_price = no_of_copies = None

                while True:
                    mag_no = input('Magazine Number: ')
                    if len(mag_no) == 0:
                        print("Invalid Magazine Number")
                    else:
                        break
                while True:
                    title = input('Title: ')
                    if len(title) == 0:
                        print("Invalid Title")
                    else:
                        break
                while True:
                    color = input('Color [1. Color | 2. Black & White]: ')
                    if color in ('1', '2'):
                        if color == '1':
                            color = 'Color'
                        else:
                            color = 'Black & White'
                        break
                    else:
                        print('Invalid Color format')
                while True:
                    subject = input('Subject [1. Science | 2. Technology | 3. Sports ]')
                    if subject in ('1', '2', '3'):
                        if subject == '1':
                            subject = 'Science'
                        elif subject == '2':
                            subject = 'Technology'
                        else:
                            subject = 'Sports'
                        break
                    else:
                        print("Invalid subject")
                while True:
                    rental_price = input('Rental price: ')
                    if rental_price.isnumeric() and rental_price != '0':
                        break
                    else:
                        print("Invalid Rental price")

                while True:
                    no_of_copies = input("No_of_copies: ")
                    if no_of_copies.isnumeric():
                        break
                    else:
                        print("Invalid No of copies")

                magazine = Magazine(mag_no,title,color,subject,rental_price,no_of_copies)
                if Magazine.insert_magazine(magazine):
                    print("Successfully saved a magazine")
                else:
                    print("Already saves this magazine")

                print(Magazine.get_all_magazines(magazine))


            elif sub_option == '3':
                print("*************** Add new educational DVD ***************")
                dvd_no = title = subject = rental_price = no_of_copies = None

                while True:
                    dvd_no = input('DVD Number: ')
                    if len(dvd_no) == 0:
                        print("Invalid DVD Number")
                    else:
                        break
                while True:
                    title = input('Title: ')
                    if len(title) == 0:
                        print("Invalid Title")
                    else:
                        break

                while True:
                    subject = input('Subject [1. Technology | 2. Astronomy | 3. Math | ] ')
                    if subject in ('1', '2', '3'):
                        if subject == '1':
                            subject = 'Technology'
                        elif subject == '2':
                            subject = 'Astronomy'
                        else:
                            subject = 'Math'
                        break
                    else:
                        print("Invalid subject")
                while True:
                    rental_price = input('Rental price: ')
                    if rental_price.isnumeric() and rental_price != '0':
                        break
                    else:
                        print("Invalid Rental price")

                while True:
                    no_of_copies = input("No_of_copies: ")
                    if no_of_copies.isnumeric():
                        break
                    else:
                        print("Invalid No of copies")

                dvd = DVD(dvd_no,title,subject,rental_price,no_of_copies)
                if DVD.insert_dvd(dvd):
                    print("Successfully saved a DVD")
                else:
                    print("Already saves this DVD")

                print(DVD.get_all_dvd(dvd))


            elif sub_option == '4':
                print("*************** Add new Lecture CD ***************")
                cd_no = title = subject = rental_price = no_of_copies = None

                while True:
                    cd_no = input('CD Number: ')
                    if len(cd_no) == 0:
                        print("Invalid CD Number")
                    else:
                        break
                while True:
                    title = input('Title: ')
                    if len(title) == 0:
                        print("Invalid Title")
                    else:
                        break

                while True:
                    subject = input('Subject [1. Math | 2.  Music | 3. Foreign Language | ] ')
                    if subject in ('1', '2', '3'):
                        if subject == '1':
                            subject = 'Math'
                        elif subject == '2':
                            subject = 'Music'
                        else:
                            subject = 'Foreign Language'
                        break
                    else:
                        print("Invalid subject")
                while True:
                    rental_price = input('Rental price: ')
                    if rental_price.isnumeric() and rental_price != '0':
                        break
                    else:
                        print("Invalid Rental price")

                while True:
                    no_of_copies = input("No_of_copies: ")
                    if no_of_copies.isnumeric():
                        break
                    else:
                        print("Invalid No of copies")

                cd = CD(cd_no,title,subject,rental_price,no_of_copies)
                if CD.insert_cd(cd):
                    print("Successfully saved a CD")
                else:
                    print("Already saves this CD")

                print(CD.get_all_cd(cd))


            elif sub_option == '5':
                print(main_manu)
                main_option = input("Choose option:")

            else:
                print("Invalid option......")







        elif main_option =='2':
            while True:
                print(remove_resources)
                sub_option= input('Choose your option: ')
                if sub_option == '1':
                    print("************ Remove  book ************")
                    isbn = None
                    while (True):
                        isbn = input('ISBN: ')
                        if len(isbn) != 0:
                            break
                        else:
                            print('Invalid ISBN...')

                    if Book.delete_book_by_isbn(isbn):
                        print('Successfully deleted...')

                    else:
                        print('Error...')





                if sub_option == '2':
                    print("************ Remove  magazine ************")
                    mag_no = None
                    while (True):
                        mag_no = input('Magazine number: ')
                        if len(mag_no) != 0:
                            break
                        else:
                            print('Invalid magazine number...')

                    if Magazine.delete_magazine_by_mag_no(mag_no):
                        print('Successfully deleted...')
                    else:
                        print('Error...')



                elif sub_option == '3':
                    print("************ Remove Educational DVD ************")
                    dvd_no = None
                    while True:
                        dvd_no = input('Magazine number: ')
                        if len(dvd_no) != 0:
                            break
                        else:
                            print('Invalid magazine number...')

                    if DVD.delete_dvd_by_dvd_no(dvd_no):
                        print('Successfully deleted...')
                    else:
                        print('Error...')

                elif sub_option == '4':
                    print("************ Remove Lecture CD ************")
                    cd_no = None
                    while (True):
                        cd_no = input('CD number: ')
                        if len(cd_no) != 0:
                            break
                        else:
                            print('Invalid magazine number...')

                    if CD.delete_cd_by_cd_no(cd_no):
                        print('Successfully deleted...')
                    else:
                        print('Error...')

                elif sub_option == '5':
                    print(main_manu)
                    main_option = input("Choose option:")
                    break







        elif main_option == '3':
            print(available_resources)
            sub_option = input('Choose option: ')
            if sub_option =='1':
                book = None
                print('*************** book available ***************')
                print('Number of all books:',len(Book.get_all_books(book)))
                print(Book.get_all_books(book))

            elif sub_option =='2':
                magazine = None
                print('*************** magazine ***************')
                print('Number of all magazines:', len(Magazine.get_all_magazines(magazine)))
                print(Magazine.get_all_magazines(magazine))

            elif sub_option =='3':
                dvd = None
                print('*************** Educational DVD ***************')
                print('Number of all DVDs:', len(DVD.get_all_dvd(dvd)))

                print(DVD.get_all_dvd(dvd))

            elif sub_option =='4':
                cd = None
                print('*************** Lecture CD ***************')
                print('Number of all CDs:', len(CD.get_all_cd(cd)))


                print(CD.get_all_cd(cd))
            elif sub_option =='5':
                print(main_manu)
                main_option = input("Choose option:")
            else:
                print('Invalid Option... ')



        elif main_option=='4':
            while True:
                print(unavailable_resources)
                sub_option= input('Choose your option: ')
                if sub_option == '5':
                    print(main_manu)
                    main_option = input("Choose option:")
                    break
                else:
                     print('Invalid ISBN...')







        elif main_option=='5':
            print(search_resources)

            subject_id = None
            while (True):
                subject_id = input('subject id: ')
                if subject_id=='1':
                    subject_id='Science'
                elif subject_id=='2':
                    subject_id='History'
                elif subject_id=='3':
                    subject_id='Literature'
                elif subject_id=='4':
                    subject_id='Technology'
                elif subject_id=='5':
                    subject_id='Sports'
                elif subject_id=='6':
                    subject_id='Astronomy'
                elif subject_id=='7':
                    subject_id='Math'
                elif subject_id=='8':
                    subject_id='Music'
                else:
                    subject_id='Foreign_Languages'
                if len(subject_id) != 0:
                    break
                else:
                    print('Invalid number...')

            if Book.get_all_resorces_search_by_subject(subject_id ):
                print(Book.get_all_resorces_search_by_subject(subject_id ))
                print('Successfully search...')
                print(main_manu)
                main_option = input("Choose option: ")


            else:
                print('There are no resources related to this subject...')
                print(main_manu)
                main_option = input("Choose option: ")






        elif main_option=='6':
            while True:
                print('*************** Lend Resources ***************')
                print('1. Back')
                sub_option= input('Choose your option: ')

                if sub_option == '1':
                    print(main_manu)
                    main_option = input("Choose option:")
                    break
                else:
                     print('Invalid option...')


        elif main_option == '7':
            while True:
                print('*************** Receive resources ***************')
                print('1. Back')
                sub_option = input('Choose your option: ')

                if sub_option == '1':
                    print(main_manu)
                    main_option = input("Choose option:")
                    break
                else:
                    print('Invalid option...')

        elif main_option == '8':
            print('*************** Thank you ***************')
            break
terminal()