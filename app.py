import os
import qrcode  
import datetime  
from datetime import timedelta  
from flask import Flask, render_template, session, redirect, url_for, request


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
    {"title": "Mobile App Development for Beginners", "author": "Sophia Lee", "price": "₹2399", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "Android Development Essentials", "author": "David King", "price": "₹2599", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "iOS Development with Swift", "author": "Olivia Green", "price": "₹2699", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "Cross-Platform Mobile Development", "author": "Emma White", "price": "₹2199", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "Flutter for Beginners", "author": "Lucas Turner", "price": "₹2399", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "React Native Cookbook", "author": "James Stone", "price": "₹2599", "availability": "In Stock", "category": "Mobile Development"},
    {"title": "Mastering SQL", "author": "Ethan Clark", "price": "₹1599", "availability": "In Stock", "category": "Database"},
    {"title": "MongoDB for Beginners", "author": "Benjamin Clark", "price": "₹1799", "availability": "In Stock", "category": "Database"},
    {"title": "Database Management Systems", "author": "Sophie Green", "price": "₹1999", "availability": "In Stock", "category": "Database"},
    {"title": "SQL for Data Science", "author": "Emily Adams", "price": "₹1799", "availability": "In Stock", "category": "Database"},
    {"title": "PostgreSQL Essentials", "author": "Rachel Adams", "price": "₹1899", "availability": "In Stock", "category": "Database"},
    {"title": "NoSQL Databases Explained", "author": "Olivia Scott", "price": "₹2199", "availability": "In Stock", "category": "Database"},
    {"title": "UX/UI Design Essentials", "author": "Lucas White", "price": "₹1799", "availability": "In Stock", "category": "Design"},
    {"title": "Design Patterns for Developers", "author": "David Brown", "price": "₹1999", "availability": "In Stock", "category": "Design"},
    {"title": "Web Design for Beginners", "author": "Sophia Turner", "price": "₹1699", "availability": "In Stock", "category": "Design"},
    {"title": "UX Design Principles", "author": "Olivia Green", "price": "₹1799", "availability": "In Stock", "category": "Design"},
    {"title": "The Art of UI Design", "author": "John Doe", "price": "₹2499", "availability": "In Stock", "category": "Design"},
    {"title": "Web Design Best Practices", "author": "Lucas Turner", "price": "₹2399", "availability": "In Stock", "category": "Design"},
    {"title": "Cloud Computing Basics", "author": "James Stone", "price": "₹1999", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "AWS Certified Solutions Architect", "author": "Sara White", "price": "₹2699", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Google Cloud Essentials", "author": "Rachel Adams", "price": "₹2199", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Microsoft Azure for Beginners", "author": "David King", "price": "₹2399", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Cloud Native Development", "author": "Olivia Scott", "price": "₹2599", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Docker and Kubernetes for Cloud", "author": "Benjamin White", "price": "₹2499", "availability": "In Stock", "category": "Cloud Computing"},
    {"title": "Digital Marketing Essentials", "author": "William Scott", "price": "₹1799", "availability": "In Stock", "category": "Marketing"},
    {"title": "SEO for Beginners", "author": "Benjamin White", "price": "₹1599", "availability": "In Stock", "category": "Marketing"},
    {"title": "Social Media Marketing Guide", "author": "Sophia Turner", "price": "₹1899", "availability": "In Stock", "category": "Marketing"},
    {"title": "Content Marketing Strategy", "author": "David Brown", "price": "₹2199", "availability": "In Stock", "category": "Marketing"},
    {"title": "Growth Hacking Techniques", "author": "James Stone", "price": "₹2299", "availability": "In Stock", "category": "Marketing"},
    {"title": "Influencer Marketing Guide", "author": "Rachel Adams", "price": "₹2499", "availability": "In Stock", "category": "Marketing"}
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
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
    return render_template('proceed_to_pay.html', cart=cart_items, total_price=total_price)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    # Collect user details from the form
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    payment_mode = request.form['payment_mode']
    upi_id = request.form.get('upi_id')

    # Calculate the total price
    cart_items = session.get('cart', {})
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())

    # Add delivery charges if payment mode is COD
    delivery_charges = 0
    if payment_mode == 'COD':
        delivery_charges = 100  # Add ₹100 for delivery charges

    total_price += delivery_charges  # Add delivery charges to the total price

    # Generate UPI QR code if the payment mode is UPI
    qr_code_url = None
    if payment_mode == 'UPI' and upi_id:
        upi_url = f"upi://pay?pa={upi_id}&pn={name}&mc=0000&tid=1234567890&url=https://upi.payment/verify"
        qr_code = qrcode.make(upi_url)
        qr_code_path = os.path.join('static', 'qrcode.png')
        qr_code.save(qr_code_path)
        qr_code_url = qr_code_path  # Path to the generated QR code image

    # Calculate expected delivery date (5 days from now)
    expected_delivery_date = datetime.datetime.now() + timedelta(days=5)
    expected_delivery_date = expected_delivery_date.strftime('%Y-%m-%d')

    # Store the order information in session
    session['order_summary'] = {
        'name': name,
        'email': email,
        'phone': phone,
        'address': address,
        'payment_mode': payment_mode,
        'upi_id': upi_id if payment_mode == 'UPI' else None,
        'total_price': total_price,  # Updated with delivery charges if COD
        'delivery_charges': delivery_charges,  # Store delivery charges separately
        'expected_delivery_date': expected_delivery_date
    }

    return redirect(url_for('order_summary'))


@app.route('/order_summary', methods=['POST', 'GET'])
def order_summary():
    # Assuming you have order data in the form of a dictionary or model instance
    order_data = session.get('order_summary', None)  # Get order summary from session

    # Calculate the delivery date (5 days from today)
    delivery_date = (datetime.datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')

    if not order_data:
        return redirect(url_for('index'))  # If no order found, redirect to homepage

    return render_template('order_summary.html', order_summary=order_data, delivery_date=delivery_date)

if __name__ == '__main__':
    app.run(debug=True)
