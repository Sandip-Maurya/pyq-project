from flask import Flask, render_template, request
app = Flask(__name__)
import api

# Web Pages

# 1. Home Page
@app.route('/')
def index2():
   return render_template('index2.html')

# 2. View Page
@app.route('/view_all')
def view_all():
    return render_template('view_all.html')

# 3. Practice Page
@app.route('/practice')
def practice():
    return render_template('practice.html')


if __name__ == '__main__':
   app.run(debug = True)