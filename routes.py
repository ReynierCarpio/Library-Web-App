from flask import Flask, request, jsonify
from models import db, User, Book

# You don't need to initialize Flask here, just the routes
app = Flask(__name__)

# Configure the app with MySQL or PostgreSQL settings if needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://avnadmin:AVNS_dzE66_iAZKYZvtKdyd1@mysql-2c58423f-monettenicolas069-7d60.h.aivencloud.com:12112/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Initialize the database

# Initialize database tables
with app.app_context():
    db.create_all()

# Routes for User
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])


# Get user 
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.serialize())

# Add
@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201


# update user
@app.route('/user/<int:user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({"message": "User updated successfully", "user": user.serialize()})



# Routes for Book
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize() for book in books])

@app.route('/book', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        publication_date=data['publication_date'],
        ISBN=data['ISBN'],
        summary=data['summary']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.serialize()), 201


# delete user
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})


# get book
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.serialize())


# update book
@app.route('/book/<int:book_id>', methods=['PUT', 'PATCH'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)
    book.publication_date = data.get('publication_date', book.publication_date)
    book.ISBN = data.get('ISBN', book.ISBN)
    book.summary = data.get('summary', book.summary)
    db.session.commit()
    return jsonify({"message": "Book updated successfully", "book": book.serialize()})



# delete book
@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"})




# Helper function for serializing models
def serialize_user(user):
    return {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email
    }

def serialize_book(book):
    return {
        'book_id': book.book_id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'publication_date': book.publication_date,
        'ISBN': book.ISBN,
        'summary': book.summary
    }



# Serialize helpers
def serialize_user(user):
    return {
        'user_id': user.id,
        'username': user.username,
        'email': user.email
    }

def serialize_book(book):
    return {
        'book_id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'publication_date': book.publication_date,
        'ISBN': book.ISBN,
        'summary': book.summary
    }