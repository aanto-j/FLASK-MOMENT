from flask import Flask,render_template,request
import sqlite3

app=Flask('__name__')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('select * from student order by name desc')
    t = cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template('result.html',x=t)

@app.route('/getinfo',methods=['GET','POST'])
def getinfo():
    if request.method == 'POST':
        a = request.form.get('name')
        b = request.form.get('age')
        c = request.form.get('rollno')
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('insert into student values(?,?,?)',(a,b,c)) 
        conn.commit()
        conn.close()
        return render_template('home.html')
    return render_template('getinfo.html')
    
if __name__ == '__main__':
    app.run(debug=True)