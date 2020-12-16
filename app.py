import sqlite3
import os
from flask import Flask,render_template,request,redirect,session,send_from_directory,url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

#メモ書き
#【todo】dbに登録したLINE IDをLINEボットへ送信




@app.route('/')
def index():
    return render_template('top.html')


@app.route('/register',methods=["GET", "POST"])
def register():
    #  登録ページを表示させる
    if request.method == "GET":
        # if 'user_id' in session :
        #     return redirect ('/top')
        # else:
            return render_template("signup.html")
    # ここからPOSTの処理
    else:
        name = request.form.get("name")
        adress = request.form.get("adress")
        password = request.form.get("password")


        conn = sqlite3.connect('notbose.db')
        c = conn.cursor()
        c.execute("insert into user values(null,?,?,?,?)", (name,adress,password,lineid))
        conn.commit()
        conn.close()
        return redirect('/login.html')









if __name__ =="__main__":
    app.run(debug=True)