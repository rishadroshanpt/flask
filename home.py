from flask import Flask,render_template,request,redirect
import sqlite3

app=Flask(__name__)

@app.route('/')
def sample():
    return "welcome"

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        # print(name,age)
        con = sqlite3.connect("home.db")
        try:
            con.execute("create table data(name text,age int)")
        except:
            con.execute("insert into data(name,age)values(?,?)",(name,age))
        con.commit()
        return redirect('index')
    return render_template('index.html')

@app.route('/second')
def second():
    return render_template('second.html')


@app.route('/index1')
def index1():
    return render_template('index1.html')

app.run()