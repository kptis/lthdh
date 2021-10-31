from flask import Flask, render_template,request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        text = request.form['text_area']
        if text != "":
            print(text)
            return redirect(url_for('home'))
        else:
            print("please enter into text area")
            return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)