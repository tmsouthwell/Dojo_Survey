from flask import Flask, render_template, redirect, request, session

app = Flask(__name__) 
app.secret_key = 'keep it safe'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['userlocation'] = request.form['dloc']
    session['userlanguage'] = request.form['lang']
    session['usercomments'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def user_result():
    return render_template('result.html')


if __name__=="__main__":  
    app.run(debug=True)   

