BEGIN Library Management System

FUNCTION Main(master_window, login_window, member_name)
  CREATE main application window
  SETUP all user interface elements (buttons, labels, frames)
  SET window title
  CALL DisplayBooks(all_books)
  CREATE button to Open AddBook window
  CREATE button to Open AddMember window
  CREATE button to Open BorrowBook window
  CREATE button to Open ReturnBook window
END FUNCTION


FUNCTION DisplayBooks(filter_type)
  CLEAR existing list of books from display
  IF filter_type is 'ALL BOOKS'
    GET all books from 'books' table
  ELSE IF filter_type is 'AVAILABLE BOOKS'
    GET books with 'AVAILABLE' status
  ELSE IF filter_type is 'BORROWED BOOKS'
    GET books with 'BORROWED' status
  END IF
  
  FOR each book in the list
    ADD book name and ID to the list display
  END FOR
END FUNCTION

FUNCTION AddBook(Name, Author, Pages, Year)
  IF Name AND Author AND Pages AND Year ARE NOT EMPTY
    TRY
      SAVE new book record to 'books' table in database
      DISPLAY "Book Added Successfully" message
    CATCH database error
      DISPLAY "Error adding book" message
    END CATCH
  ELSE
    DISPLAY "Please fill all details" message
  END IF
END FUNCTION

FUNCTION AddMember(Name, Email, Phone, Username, Password)
  IF all fields are NOT EMPTY
    ENCRYPT Name, Email, and Phone
    HASH Username and Password
    TRY
      SAVE new member record to 'members' table in database
      DISPLAY "Member Added Successfully" message
    CATCH database error
      DISPLAY "Error adding member" message
    END CATCH
  ELSE
    DISPLAY "Please fill all details" message
  END IF
END FUNCTION

FUNCTION BorrowBook(BookID, MemberID)
  GET book status from 'books' table USING BookID
  IF book status is 'AVAILABLE' (0)
    SET today's date
    SAVE new borrow record to 'borrows' table in database
    UPDATE book status to 'BORROWED' (1) in 'books' table
    SAVE changes to database (commit)
    DISPLAY "Book Given Successfully" message
  ELSE
    DISPLAY "Book is already borrowed" message
  END IF
END FUNCTION

FUNCTION ReturnBook(BookID)
  SET return date to today's date
  TRY
    UPDATE book status to 'AVAILABLE' (0) in 'books' table
    UPDATE borrow record with the return date
    SAVE changes to database (commit)
    DISPLAY "Book Returned Successfully" message
  CATCH database error
    DISPLAY "Error returning book" message
  END CATCH
END FUNCTION
