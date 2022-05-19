import json
from flask import Flask, render_template, request, url_for
from python_scripts.get_data import get_paper_data_json_main
app = Flask(__name__)
import api

# Web Pages

# 1. Home Page
@app.route('/')
def index2():
   return render_template('index2.html')

# 2. View Page
@app.route('/view_all', methods = ['POST'])
def view_all():
    global Paper_view
    global Subject_view
    Paper_view = request.form['Paper']
    Subject_view = request.form['Subject']    
    return render_template('view_all.html')

# 3. Practice Page
@app.route('/practice', methods=['POST'])
def practice():
    Exam, Year, Paper, Subject = request.form['Exam'], request.form['Year'], request.form['Paper'], request.form['Subject']
    filter_data = {'Exam': Exam, 'Year': Year, 'Paper': Paper, 'Subject': Subject}
    return render_template('practice.html', filter_data = filter_data)

# API for sending paper data for 
@app.route('/get_paper_data_view', methods=['POST'])
def get_paper_data():
    return get_paper_data_json_main(Paper_view, Subject_view)
    # return json.dumps ({'key':'value'})

if __name__ == '__main__':
   app.run(debug = True, port=7000)