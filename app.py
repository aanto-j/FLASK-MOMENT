from operator import itemgetter
from flask import Flask,render_template,request,jsonify
import sqlite3

app=Flask('__name__')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('select * from student')
    t = cursor.fetchall()
    conn.commit()
    conn.close()
    nos = len(t)
    names = list(map(itemgetter(0),t))
    ages = list(map(itemgetter(1),t))
    rollnos = list(map(itemgetter(2),t))
    print(nos)
    # return render_template('result.html',x=names,y=ages,z=rollnos,n=nos)
    return jsonify(names)

@app.route('/getinfo',methods=['GET','POST'])
def getinfo():
    if request.method == 'POST':
        a = request.form.get('name')
        b = request.form.get('age')
        c = request.form.get('rollno')
        try:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute('insert into student values(?,?,?)',(a,b,c)) 
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            return "Value already exists"
        return render_template('home.html')
    return render_template('getinfo.html')
    
if __name__ == '__main__':
    app.run(debug=True)