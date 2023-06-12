from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def home():
    if 'cart' not in session:
        session['cart'] = []  # Ініціалізація кошика покупок у сесії, якщо він ще не існує
    return render_template('index.html', cart=session['cart'])


@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    item = request.form.get('item')
    session['cart'].append(item)  # Додавання товару до кошика покупок у сесії
    return redirect('/')


@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    item = request.form.get('item')
    session['cart'].remove(item)  # Видалення товару з кошика покупок у сесії
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
