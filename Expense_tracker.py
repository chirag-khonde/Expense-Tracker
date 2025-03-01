from flask import Flask, render_template, request

app = Flask(__name__)
expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form['date']
    category = request.form['category']
    amount = request.form['amount']
    expenses.append({'date': date, 'category': category, 'amount': amount})
    return index()

if __name__ == '__main__':
    app.run(debug=True)
