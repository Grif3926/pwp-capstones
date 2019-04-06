class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        

    def get_email(self):
        for user in self.name:
            return self.email
            

    def change_email(self, address):
        for user in self.name:
            self.email = address
            print("Your email has been changed to {}".format(address))

    def __repr__(self):
        return "User {}, email: {}, Books Read: {}".format(self.name, self.email, self.books)
    
        
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
        
    def read_book(self, book, rating=None):
        self.books[book] = rating
      
    def get_average_rating(self):
        total = 0
        how_many_books = 0
        for book in self.books.keys():
            if self.books[book] != None:
                total += self.books[book]
                how_many_books += 1
        return total  /how_many_books 
        
class Book(object):

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
      
    def get_isbn(self):
        return self.isbn

    def __repr__(self):
        return self.title

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{} has a new ISBN of {}".format(self.title, isbn))
    
    def add_rating(self, rating):
        if rating >=0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
          
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return None
        book_rating = 0
        for rating in self.ratings:
            book_rating += rating
        return book_rating / len(self.ratings)

class Fiction(Book):
    
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author    
  
    def get_author(self):
        return self.author
      
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
  
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject) 
        

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
  
    def create_book(self, title, isbn):
            return Book(title, isbn)
  
    def create_novel(self, title, author, isbn):
            return Fiction(title, author, isbn)
  
    def create_non_fiction(self, title, subject, level, isbn):
            return Non_Fiction(title, subject, level, isbn)
  
    def add_user(self, name, email, user_books=None):
            if email in self.users:
                print("A user with that email already exists")
            else:
                user = User(name, email)
                self.users[email] = user
                if user_books != None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
  
    def add_book_to_user(self, book, email, rating=None):
            if email not in self.users:
                print("No user with email: {} exists".format(email))
            else:
                self.users[email].read_book(book,rating)
                if rating != None:
                    book.add_rating(rating)
                if book in self.books:
                    self.books[book] += 1
                else:
                    self.books[book] = 1   
  

    def print_catalog(self):
            for book in self.books.keys():
                print(book)
      
    def print_users(self):
            for user in self.users.values():
                print(user)
  
    def most_read_book(self):
            return max(self.books, key=self.books.get)
  
  
    def highest_rated_book(self):
        high_book_rate = None
        high_num_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > high_num_rating:
                high_book_rate = book
                high_num_rating = rating
            return high_book_rate
  
    def most_positive_user(self):
            pos_user = None
            high_user_rating = 0
            for user in self.users.values():
                avg_user_rating = user.get_average_rating()
                if avg_user_rating > high_user_rating:
                    pos_user = user
                    high_user_rating = avg_user_rating
            return pos_user
