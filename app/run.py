from flask import *
import pymysql

app= Flask(__name__)
app.secret_key=b'230&6^240)'
host = '0.0.0.0'
port = '8080'

db = pymysql.Connect(host='localhost',user='root',password='eodus6450', database='web_db')
cursor = db.cursor()

@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home():
    query = "SELECT * FROM user"
    cursor.execute(query)
    result = cursor.fetchall()
    if 'id' in session:
        return render_template('/home.html',id=session['id'],reg=result)
    else:
        return render_template('/home.html',id='X',reg=result)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        query = "INSERT INTO user (id, pw) VALUES (%s, %s)"
        data = (id,pw)
        try:
            cursor.execute(query,data)
            return redirect('/home')
        except:
            return redirect('/')

    else:
        return render_template('/register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        query = "SELECT id, pw FROM user WHERE id=%s and pw=%s"
        data = (id,pw)
        try:
            cursor.execute(query,data)
        except:
            return redirect('/')
        result = cursor.fetchall()
        if len(result)==0:
            return redirect('/home')
        else:
            session['id']=request.form['id']
            return redirect('/home')
    else:
        return render_template('/login.html')

@app.route('/pwchange',methods=['GET','POST'])
def pwchange():
    if request.method=='POST':
        id = request.form['id']
        bpw = request.form['bpw']
        apw = request.form['apw']
        query = "SELECT id FROM user WHERE id=%s and pw=%s"
        data = (id,bpw)
        try:
            cursor.execute(query,data)
        except:
            return redirect('/')
        result = cursor.fetchall()
        if len(result)==0:
            return render_template('pwchange.html')
        else:
            query = "UPDATE user SET id=%s, pw=%s"
            data = (id,apw)
            try:
                cursor.execute(query,data)
                return redirect('/home')
            except:
                return redirect('/')
    else:
        return render_template('/pwchange.html')

@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        id = request.form['id']
        pw = request.form['pw']
        query = "SELECT id FROM user WHERE id=%s and pw=%s"
        data = (id,pw)
        try:
            cursor.execute(query,data)
        except:
            return redirect('/')
        result = cursor.fetchall()
        if len(result)==0:
            return render_template('/delete.html', alert=1)
        else:
            query = "DELETE FROM user where id=%s and pw=%s"
            data = (id,pw)
            try:
                cursor.execute(query,data)
                return redirect('/logout')
            except:
                return redirect('/')
    else:
        return render_template('/delete.html')

@app.route('/logout')
def logout():
    session.pop('id',None)
    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
    session.clear()