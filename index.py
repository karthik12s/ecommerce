from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/products')
def products():
    return render_template('products.html')
@app.route('/settings')
def settings():
    return render_template('settings.html')
@app.route('/logout')
def logout():
    return render_template('logout.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/success')
def success():
    return render_template('success.html')
if __name__=='__main__':
    app.run(debug = True)
