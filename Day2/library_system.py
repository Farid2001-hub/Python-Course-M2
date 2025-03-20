# 1️ Classe Book (Livre)
class Book:
    # Initialisation des attributs du livre
    def __init__(self, title, author, isbn):
        self.title = title  # Titre du livre
        self.author = author  # Auteur du livre
        self.isbn = isbn  # ISBN du livre
        self.available = True  # Livre disponible par défaut

    # Méthode pour afficher les détails du livre sous forme lisible
    def __str__(self):
        return f'"{self.title}" de {self.author} (ISBN: {self.isbn})'

    # Méthode pour emprunter le livre (le rendre indisponible)
    def borrow(self):
        self.available = False

    # Méthode pour retourner le livre (le rendre disponible)
    def return_book(self):
        self.available = True


# 2️ Classe User (Utilisateur)
class User:
    # Initialisation des attributs de l'utilisateur
    def __init__(self, name, user_id):
        self.name = name  # Nom de l'utilisateur
        self.user_id = user_id  # ID unique de l'utilisateur
        self.borrowed_books = []  # Liste des livres empruntés (vide au départ)

    # Méthode pour emprunter un livre
    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)  # Ajoute le livre à la liste des livres empruntés
            book.borrow()  # Marque le livre comme emprunté
            print(f'{self.name} a emprunté "{book.title}".')
        else:
            print(f'"{book.title}" n\'est pas disponible.')

    # Méthode pour retourner un livre
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)  # Retire le livre de la liste des emprunts
            book.return_book()  # Marque le livre comme retourné
            print(f'{self.name} a retourné "{book.title}".')
        else:
            print(f'{self.name} n\'a pas emprunté "{book.title}".')

    # Méthode pour afficher les informations de l'utilisateur
    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        borrowed_books_str = ', '.join(borrowed_titles) if borrowed_titles else 'Aucun livre emprunté'
        return f'{self.name} - Livres empruntés : {borrowed_books_str}'


# 3️ Classe Library (Bibliothèque)
class Library:
    # Initialisation des attributs de la bibliothèque
    def __init__(self):
        self.books = []  # Liste des livres de la bibliothèque
        self.users = []  # Liste des utilisateurs inscrits

    # Méthode pour ajouter un livre à la bibliothèque
    def add_book(self, book):
        self.books.append(book)

    # Méthode pour ajouter un utilisateur à la bibliothèque
    def add_user(self, user):
        self.users.append(user)

    # Méthode pour lister les livres disponibles dans la bibliothèque
    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Livres disponibles :")
            for book in available_books:
                print(book)
        else:
            print("Aucun livre disponible.")

    # Méthode pour emprunter un livre par un utilisateur
    def borrow_book(self, user, book_title):
        book = next((b for b in self.books if b.title == book_title and b.available), None)
        if book:
            user.borrow_book(book)
        else:
            print(f'Aucun livre disponible avec le titre "{book_title}".')

    # Méthode pour retourner un livre par un utilisateur
    def return_book(self, user, book_title):
        book = next((b for b in self.books if b.title == book_title), None)
        if book:
            user.return_book(book)
        else:
            print(f'Le livre "{book_title}" n\'est pas trouvé dans la bibliothèque.')

    # Méthode pour afficher les informations de la bibliothèque
    def __str__(self):
        book_titles = [book.title for book in self.books]
        user_names = [user.name for user in self.users]
        return f'Bibliothèque contient {len(self.books)} livres: {", ".join(book_titles)} et {len(self.users)} utilisateurs: {", ".join(user_names)}'


# 4️ Implémentation de l'héritage - PremiumUser (Utilisateur Premium)
class PremiumUser(User):
    # Initialisation des attributs spécifiques aux utilisateurs premium
    def __init__(self, name, user_id):
        super().__init__(name, user_id)  # Appel du constructeur de la classe parente User
        self.max_books = 5  # Les utilisateurs premium peuvent emprunter jusqu'à 5 livres

    # Redéfinition de la méthode borrow_book pour permettre à l'utilisateur premium d'emprunter plus de livres
    def borrow_book(self, book):
        if len(self.borrowed_books) < self.max_books:
            super().borrow_book(book)  # Appel de la méthode borrow_book de la classe parente User
        else:
            print(f'{self.name} ne peut pas emprunter plus de {self.max_books} livres.')


# Exemple d'utilisation du système

# Création de livres
book1 = Book("Python Programming", "John Doe", "978-1234567890")
book2 = Book("Machine Learning Basics", "Jane Smith", "978-0987654321")

# Création d'utilisateurs
user1 = User("Alice", 101)
user2 = PremiumUser("Bob", 102)

# Création de la bibliothèque
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)

# Afficher les livres disponibles
library.list_available_books()

# Alice emprunte "Python Programming"
library.borrow_book(user1, "Python Programming")

# Afficher les livres disponibles après l'emprunt
library.list_available_books()

# Alice retourne "Python Programming"
library.return_book(user1, "Python Programming")

# Afficher les livres disponibles après le retour
library.list_available_books()

# Bob emprunte "Machine Learning Basics"
library.borrow_book(user2, "Machine Learning Basics")

# Afficher les livres disponibles après l'emprunt par Bob
library.list_available_books()

# 5️ Polymorphisme avec la méthode __str__
print(book1)  # Affiche les détails du livre
print(user1)  # Affiche les informations de l'utilisateur avec les livres empruntés
print(library)  # Affiche les livres et utilisateurs de la bibliothèque


# Bonus : Recherche de livres par titre
def search_books_by_title(library, title):
    result = [book for book in library.books if title.lower() in book.title.lower()]
    return result


# Recherche de livres contenant "Python" dans le titre
search_results = search_books_by_title(library, "Python")
for book in search_results:
    print(book)
