from os import pardir
from flask import Flask, render_template,request, redirect, url_for
from flask.helpers import flash
from model.main import predict

app = Flask(__name__)

app.secret_key = "btlthdh"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form['text_area']
        if text != "":
            print(text)       
            return render_template('home.html', text = text)
        else:
            flash("Điền nội dung vào mới dự đoán được chứ ơ hay -.-")
            print("please enter into text area")
            return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)