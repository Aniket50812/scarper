# from flask import Flask, render_template

# app = Flask(__name__)

# books = [
#     {"title": "The Great Adventure", "author": "John Doe", "price": "₹1499", "availability": "In Stock"},
#     {"title": "Learning Python", "author": "Jane Smith", "price": "₹2199", "availability": "Out of Stock"},
#     {"title": "Flask for Beginners", "author": "Jake White", "price": "₹1299", "availability": "In Stock"},
#     {"title": "Data Science Handbook", "author": "Alice Cooper", "price": "₹1999", "availability": "In Stock"},
#     {"title": "Machine Learning Mastery", "author": "John Green", "price": "₹2499", "availability": "In Stock"},
#     {"title": "Python for Data Analysis", "author": "David Brown", "price": "₹1799", "availability": "Out of Stock"},
#     {"title": "The Python Programming Guide", "author": "Emma White", "price": "₹1599", "availability": "In Stock"},
#     {"title": "Advanced Flask Development", "author": "Robert Black", "price": "₹2599", "availability": "In Stock"},
#     {"title": "Intro to Web Development", "author": "Lily Green", "price": "₹1399", "availability": "Out of Stock"},
#     {"title": "Flask and Django for Beginners", "author": "Chris Blue", "price": "₹1799", "availability": "In Stock"},
#     {"title": "AI in Practice", "author": "George Harris", "price": "₹2799", "availability": "In Stock"},
#     {"title": "Deep Learning for Everyone", "author": "Sara White", "price": "₹2399", "availability": "In Stock"},
#     {"title": "Full Stack Web Development", "author": "Rachel Adams", "price": "₹2199", "availability": "Out of Stock"},
#     {"title": "The Web Developer's Bible", "author": "James Stone", "price": "₹1599", "availability": "In Stock"},
#     {"title": "The Art of Code", "author": "Olivia Green", "price": "₹1999", "availability": "Out of Stock"},
#     {"title": "Building Scalable Apps", "author": "Lucas White", "price": "₹1899", "availability": "In Stock"},
#     {"title": "React for Beginners", "author": "Sophia Turner", "price": "₹1699", "availability": "In Stock"},
#     {"title": "Introduction to JavaScript", "author": "Ella Miller", "price": "₹1299", "availability": "In Stock"},
#     {"title": "The Future of Programming", "author": "William Scott", "price": "₹2499", "availability": "Out of Stock"},
#     {"title": "Learning Java for Beginners", "author": "Benjamin Clark", "price": "₹1899", "availability": "In Stock"},
#     {"title": "HTML & CSS Essentials", "author": "Amelia Wilson", "price": "₹1499", "availability": "In Stock"},
#     {"title": "The Web Designer's Guide", "author": "Mason Evans", "price": "₹1699", "availability": "In Stock"},
#     {"title": "Blockchain for Beginners", "author": "Sophia Lee", "price": "₹2699", "availability": "In Stock"},
#     {"title": "React Native for Mobile Apps", "author": "David King", "price": "₹2299", "availability": "Out of Stock"},
#     {"title": "Digital Marketing Strategy", "author": "Olivia Scott", "price": "₹1799", "availability": "In Stock"},
#     {"title": "Web Development Bootcamp", "author": "Jack Wilson", "price": "₹2499", "availability": "In Stock"},
#     {"title": "Mastering Algorithms", "author": "Emily Adams", "price": "₹2199", "availability": "In Stock"},
#     {"title": "Python Data Science Handbook", "author": "John Gray", "price": "₹1699", "availability": "In Stock"},
#     {"title": "SQL for Beginners", "author": "Ethan Clark", "price": "₹1599", "availability": "Out of Stock"},
#     {"title": "Artificial Intelligence Basics", "author": "Sophie Green", "price": "₹2899", "availability": "In Stock"},
#     {"title": "Cloud Computing Essentials", "author": "Lucas Turner", "price": "₹2399", "availability": "In Stock"},
#     {"title": "UX/UI Design Principles", "author": "Benjamin White", "price": "₹1799", "availability": "Out of Stock"},
# ]

# @app.route('/')
# def index():
#     return render_template('index.html', books=books)

# if __name__ == '__main__':
#     app.run(debug=True)





import random
from flask import Flask, render_template

app = Flask(__name__)

# Updated books list with random quantities for in-stock items and 0 for out-of-stock items
books = [
    {"title": "The Great Adventure", "author": "John Doe", "price": "₹1499", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Learning Python", "author": "Jane Smith", "price": "₹2199", "availability": "Out of Stock", "quantity": 0},
    {"title": "Flask for Beginners", "author": "Jake White", "price": "₹1299", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Data Science Handbook", "author": "Alice Cooper", "price": "₹1999", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Machine Learning Mastery", "author": "John Green", "price": "₹2499", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Python for Data Analysis", "author": "David Brown", "price": "₹1799", "availability": "Out of Stock", "quantity": 0},
    {"title": "The Python Programming Guide", "author": "Emma White", "price": "₹1599", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Advanced Flask Development", "author": "Robert Black", "price": "₹2599", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Intro to Web Development", "author": "Lily Green", "price": "₹1399", "availability": "Out of Stock", "quantity": 0},
    {"title": "Flask and Django for Beginners", "author": "Chris Blue", "price": "₹1799", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "AI in Practice", "author": "George Harris", "price": "₹2799", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Deep Learning for Everyone", "author": "Sara White", "price": "₹2399", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Full Stack Web Development", "author": "Rachel Adams", "price": "₹2199", "availability": "Out of Stock", "quantity": 0},
    {"title": "The Web Developer's Bible", "author": "James Stone", "price": "₹1599", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "The Art of Code", "author": "Olivia Green", "price": "₹1999", "availability": "Out of Stock", "quantity": 0},
    {"title": "Building Scalable Apps", "author": "Lucas White", "price": "₹1899", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "React for Beginners", "author": "Sophia Turner", "price": "₹1699", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Introduction to JavaScript", "author": "Ella Miller", "price": "₹1299", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "The Future of Programming", "author": "William Scott", "price": "₹2499", "availability": "Out of Stock", "quantity": 0},
    {"title": "Learning Java for Beginners", "author": "Benjamin Clark", "price": "₹1899", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "HTML & CSS Essentials", "author": "Amelia Wilson", "price": "₹1499", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "The Web Designer's Guide", "author": "Mason Evans", "price": "₹1699", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Blockchain for Beginners", "author": "Sophia Lee", "price": "₹2699", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "React Native for Mobile Apps", "author": "David King", "price": "₹2299", "availability": "Out of Stock", "quantity": 0},
    {"title": "Digital Marketing Strategy", "author": "Olivia Scott", "price": "₹1799", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Web Development Bootcamp", "author": "Jack Wilson", "price": "₹2499", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Mastering Algorithms", "author": "Emily Adams", "price": "₹2199", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Python Data Science Handbook", "author": "John Gray", "price": "₹1699", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "SQL for Beginners", "author": "Ethan Clark", "price": "₹1599", "availability": "Out of Stock", "quantity": 0},
    {"title": "Artificial Intelligence Basics", "author": "Sophie Green", "price": "₹2899", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "Cloud Computing Essentials", "author": "Lucas Turner", "price": "₹2399", "availability": "In Stock", "quantity": random.randint(1, 30)},
    {"title": "UX/UI Design Principles", "author": "Benjamin White", "price": "₹1799", "availability": "Out of Stock", "quantity": 0},
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
