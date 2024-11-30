from flask import Flask
from routes import get_users, add_user, get_books, add_book, update_user, get_user, delete_user, get_book, update_book, delete_book
from models import db
from flask import Flask, jsonify  # Add jsonify import here

# Initialize Flask app
app = Flask(__name__)

# Configure the app with MySQL or PostgreSQL settings if needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://avnadmin:AVNS_dzE66_iAZKYZvtKdyd1@mysql-2c58423f-monettenicolas069-7d60.h.aivencloud.com:12112/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Initialize the database

# Initialize database tables
with app.app_context():
    db.create_all()

# Register routes
app.add_url_rule('/users', 'get_users', get_users, methods=['GET']) # Get all users
app.add_url_rule('/user', 'add_user', add_user, methods=['POST'])   # Add a new user
app.add_url_rule('/books', 'get_books', get_books, methods=['GET'])  # Get all books
app.add_url_rule('/book', 'add_book', add_book, methods=['POST'])  # Add a new book
app.add_url_rule('/user', 'update_user', update_user, methods=['PUT'])
app.add_url_rule('/user/<int:user_id>', 'get_user', get_user, methods=['GET'])  # Get user by ID
app.add_url_rule('/user/<int:user_id>', 'update_user', update_user, methods=['PUT', 'PATCH'])  # Update a user
app.add_url_rule('/user/<int:user_id>', 'delete_user', delete_user, methods=['DELETE'])  # Delete a user
app.add_url_rule('/book/<int:book_id>', 'get_book', get_book, methods=['GET'])  # Get book by ID
app.add_url_rule('/book/<int:book_id>', 'update_book', update_book, methods=['PUT', 'PATCH'])  # Update a book
app.add_url_rule('/book/<int:book_id>', 'delete_book', delete_book, methods=['DELETE'])  # Delete a book


# Test route to check database connection
@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        # Test if the connection works and return the message
        with app.app_context():
            result = db.session.execute('SELECT VERSION()')
            version = result.fetchone()
            return jsonify({'message': f"MySQL Database Version: {version[0]}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
