from crypt import methods
from flask import *
app= Flask(__name__)
@app.route('/')
def home():
    return redirect('/login')
    
@app.route('/login_confirm', methods=['POST'])
def login_confirm():
    id = request.form['id']
    pw = request.form['id']
    if id == 'admin' and pw == 'admin':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/index')
def index():
    return render_template('/index.html')
if __name__ == '__main__':
    app.run(debug=True)