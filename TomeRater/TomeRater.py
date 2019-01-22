# TomeRater project

# 1. class
class User(object):
# constructor method
    def __init__(self, name, email):
        self.name = name #name is a string
#        assert ("@" in email and re.search(".com|.edu|.org", email)), "Invalid e-mail address format."
        self.email = email #email is a string
        self.books = {} #books is a dictionary


    def get_email(self):
        return self.email

    def change_email(self, address):
 #       assert ("@" in email and re.search(".com|.edu|.org", email)), "Invalid e-mail address format."
        self.email = address
        print("The email address has been updated.")

    def __repr__(self):
        return "User: {}, email: {}, books read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating
    
    def get_average_rating(self):
# iterates through all of the vlaues in self.books
        sum = 0
        num_rated_books = 0
        for book in self.books.keys():
            if self.books[book] != None:
                sum += self.books[book]
                num_rated_books += 1
        return sum/num_rated_books


# 2. class
class Book(object):
# constructor method
    def __init__(self, title, isbn):
        self.title = title #title is a string
        self.isbn = isbn #isbn is a number
        self.ratings = []
 #       self.price = price

    def __hash__(self):
        return hash((self.title, self.isbn))      
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
 #   def get_price(self):
 #       return self.price

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("ISBN has been updated for {title}.".format(title = self.title))
    
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn and self.price == other_book.price

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        if len(self.ratings) == 0:
            return None
        sum = 0
        for rating in self.ratings:
                sum += rating
        return sum/len(self.ratings)


 
# 3. class
class Fiction(Book):
# constructor method
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
         return "{title} by {author}".format(title=self.title, author=self.author)
 

# 4. class
class Non_Fiction(Book):
# constructor method
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject # subject will be a string
        self.level = level # level will be a string
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


# 5. class
class TomeRater():
# constructor method
    def __init__(self):
        self.users = {} # dictionary
        self.books = {} # dictionary
    
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with e-mail {email}!".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
    
    def add_user(self, name, email, user_books=None):
        if email in self.users:
            print("Error: That user already exists.")
        else:
            user = User(name, email)
            self.users[email] = user
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)


# Some Analysis Methods for TomeRater
    def print_catalog(self):
# which are Book objects
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
# which are the User objects
        for user in self.users.values():
            print(user)
    
    def most_read_book(self):
# book that has been read the most
        return max(self.books, key=lambda key: self.books[key])
    
    def highest_rated_book(self):
# book that has the highest average rating
        highest_rated = None
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_rated = book                
                highest_rating = rating
        return highest_rated
    
    def most_positive_user(self):
# user that has the highest average rating
        positive_user = None
        highest_rating = 0
        for user in self.users.values():
            avg_user_rat = user.get_average_rating()
            if avg_user_rat > highest_rating:
                positive_user = user
                highest_rating = avg_user_rat
        return positive_user
    
# do Some Analysis 

    def get_n_most_read_books(self, n):
        sorted_by_value = sorted(self.books.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_by_value[0:n]

    def get_n_most_prolific_readers(self, n):
        readers = []
        for email in self.users:
            books_read = len(self.users[email].books)
            readers.append((books_read, email))
        readers.sort(reverse=True)

        if n > len(readers):
            n = len(readers)

        result = []
        for i in range(n):
            result.append(self.users[readers[i][1]])
        return result

    def get_n_most_expensive_books(self, n):
        most_expensive_books = []
        for book in self.books.keys():
            most_expensive_books.append((book.price, book))
        most_expensive_books.sort(reverse=True)

        if n > len(most_expensive_books):
            n = len(most_expensive_books)

        return most_expensive_books[0:n]

    def get_worth_of_user(self, user_email):
        total_worth = 0
        user = self.users[user_email]
        
        for book in user.books:
            total_worth += book.price
        return "Total price of books owned by user {0}: ${1:.2f}".format(user_email, total_worth)

# populate.py file

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
















