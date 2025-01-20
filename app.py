from flask import Flask, render_template, session, redirect, url_for, request
import os

app = Flask(__name__)

# Generate a secret key using os.urandom(24)
app.secret_key = os.urandom(24)

# List of books and offers (you can use your existing data here)
books = [
    {"title": "The Great Adventure", "author": "John Doe", "price": "₹1499", "availability": "In Stock", "category": "Adventure"},
    {"title": "Learning Python", "author": "Jane Smith", "price": "₹2199", "availability": "Out of Stock", "category": "Programming"},
    {"title": "Flask for Beginners", "author": "Jake White", "price": "₹1299", "availability": "In Stock", "category": "Web Development"},
    {"title": "Data Science Handbook", "author": "Alice Cooper", "price": "₹1999", "availability": "In Stock", "category": "Data Science"},
    {"title": "Machine Learning Mastery", "author": "John Green", "price": "₹2499", "availability": "In Stock", "category": "Data Science"},
    {"title": "Python for Data Analysis", "author": "David Brown", "price": "₹1799", "availability": "Out of Stock", "category": "Data Science"},
    {"title": "The Python Programming Guide", "author": "Emma White", "price": "₹1599", "availability": "In Stock", "category": "Programming"},
    {"title": "Advanced Flask Development", "author": "Robert Black", "price": "₹2599", "availability": "In Stock", "category": "Web Development"},
    {"title": "Intro to Web Development", "author": "Lily Green", "price": "₹1399", "availability": "Out of Stock", "category": "Web Development"},
    {"title": "AI in Practice", "author": "George Harris", "price": "₹2799", "availability": "In Stock", "category": "Artificial Intelligence"},
    
    # Mobile Development
    {"title": "Mobile App Development for Beginners", "author": "Sophia Lee", "price": "₹2399", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "Android Development Essentials", "author": "David King", "price": "₹2599", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "iOS Development with Swift", "author": "Olivia Green", "price": "₹2699", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "Cross-Platform Mobile Development", "author": "Emma White", "price": "₹2199", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "Flutter for Beginners", "author": "Lucas Turner", "price": "₹2399", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "React Native Cookbook", "author": "James Stone", "price": "₹2599", "availability": "In Stock", "category": "Mobile Development"},

    # Database
    {"title": "Mastering SQL", "author": "Ethan Clark", "price": "₹1599", "availability": "In Stock", "category": "Database"},
    {"title": "MongoDB for Beginners", "author": "Benjamin Clark", "price": "₹1799", "availability": "In Stock", "category": "Database"},
    {"title": "Database Management Systems", "author": "Sophie Green", "price": "₹1999", "availability": "In Stock", "category": "Database"},
    {"title": "SQL for Data Science", "author": "Emily Adams", "price": "₹1799", "availability": "In Stock", "category": "Database"},
    {"title": "PostgreSQL Essentials", "author": "Rachel Adams", "price": "₹1899", "availability": "In Stock", "category": "Database"},
    {"title": "NoSQL Databases Explained", "author": "Olivia Scott", "price": "₹2199", "availability": "In Stock", "category": "Database"},

    # Design
    {"title": "UX/UI Design Essentials", "author": "Lucas White", "price": "₹1799", "availability": "In Stock", "category": "Design"},
    {"title": "Design Patterns for Developers", "author": "David Brown", "price": "₹1999", "availability": "In Stock", "category": "Design"},
    {"title": "Web Design for Beginners", "author": "Sophia Turner", "price": "₹1699", "availability": "In Stock", "category": "Design"},
    {"title": "UX Design Principles", "author": "Olivia Green", "price": "₹1799", "availability": "In Stock", "category": "Design"},
    {"title": "The Art of UI Design", "author": "John Doe", "price": "₹2499", "availability": "In Stock", "category": "Design"},
    {"title": "Web Design Best Practices", "author": "Lucas Turner", "price": "₹2399", "availability": "In Stock", "category": "Design"},

    # Cloud Computing
    {"title": "Cloud Computing Basics", "author": "James Stone", "price": "₹1999", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "AWS Certified Solutions Architect", "author": "Sara White", "price": "₹2699", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Google Cloud Essentials", "author": "Rachel Adams", "price": "₹2199", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Microsoft Azure for Beginners", "author": "David King", "price": "₹2399", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Cloud Native Development", "author": "Olivia Scott", "price": "₹2599", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Docker and Kubernetes for Cloud", "author": "Benjamin White", "price": "₹2499", "availability": "In Stock", "category": "Cloud Computing"},

    # Marketing
    {"title": "Digital Marketing Essentials", "author": "William Scott", "price": "₹1799", "availability": "In Stock", "category": "Marketing"},
    {"title": "SEO for Beginners", "author": "Benjamin White", "price": "₹1599", "availability": "In Stock", "category": "Marketing"},
    {"title": "Social Media Marketing Guide", "author": "Sophia Turner", "price": "₹1899", "availability": "In Stock", "category": "Marketing"},
    {"title": "Content Marketing Strategy", "author": "David Brown", "price": "₹2199", "availability": "In Stock", "category": "Marketing"},
    {"title": "Growth Hacking Techniques", "author": "James Stone", "price": "₹2299", "availability": "In Stock", "category": "Marketing"},
    {"title": "Influencer Marketing Guide", "author": "Rachel Adams", "price": "₹2499", "availability": "In Stock", "category": "Marketing"},
]

offers = [
    {"title": "Buy 1 Get 1 Free", "description": "Buy one book and get another one for free!"},
    {"title": "Buy 6 Books, Get 25% Off", "description": "Purchase six books and get a 25% discount on your total order."},
    {"title": "50% Off on Selected Books", "description": "Check out the selected books with 50% off!"}
]

@app.route('/')
def index():
    categories = set(book['category'] for book in books)  
    return render_template('index.html', books=books, categories=categories)

@app.route('/category/<category_name>')
def category(category_name):
    filtered_books = [book for book in books if book['category'] == category_name]
    categories = set(book['category'] for book in books)
    return render_template('index.html', books=filtered_books, categories=categories)

@app.route('/offers')
def offers_page():
    return render_template('offers.html', offers=offers)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())  
    return render_template('cart.html', cart=cart_items, total_price=total_price)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/add_to_cart/<int:book_id>', methods=['POST'])
def add_to_cart(book_id):
    book = books[book_id]
    cart = session.get('cart', {})
    
    price = float(book['price'][1:])  # Convert price to float (removing ₹ symbol)
    
    if str(book_id) in cart:
        cart[str(book_id)]['quantity'] += 1
    else:
        cart[str(book_id)] = {
            'title': book['title'],
            'price': price,  # Store the price as float
            'quantity': 1,
        }
    
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/update_quantity', methods=['POST'])
def update_quantity():
    book_id = request.form['book_id']
    action = request.form['action']
    cart = session.get('cart', {})
    
    if book_id in cart:
        if action == 'increase':
            cart[book_id]['quantity'] += 1
        elif action == 'decrease' and cart[book_id]['quantity'] > 1:
            cart[book_id]['quantity'] -= 1
        
        session['cart'] = cart
    
    return redirect(url_for('cart'))

@app.route('/proceed_to_pay')
def proceed_to_pay():
    cart_items = session.get('cart', {})
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())  # price already a float
    return render_template('proceed_to_pay.html', cart=cart_items, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)