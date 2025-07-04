from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "Espresso", "price": 2.5},
    {"id": 2, "name": "Latte", "price": 3.5},
    {"id": 3, "name": "Cappuccino", "price": 3.0},
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def show_cart():
    cart = session.get('cart', {})
    items = []
    total = 0.0
    for pid, qty in cart.items():
        product = next((p for p in PRODUCTS if p['id'] == pid), None)
        if product:
            subtotal = product['price'] * qty
            total += subtotal
            items.append({
                'product': product,
                'quantity': qty,
                'subtotal': subtotal
            })
    return render_template('cart.html', items=items, total=total)

if __name__ == '__main__':
    app.run(debug=True)
