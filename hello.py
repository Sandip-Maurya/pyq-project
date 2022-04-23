from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/result')
def result():
    dic = {'p':50,'c':60, 'm':80}
    return render_template('index.html', result=dic)

if __name__ == '__main__':
   app.run(debug = True)