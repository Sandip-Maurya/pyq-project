from flask import  render_template

from __main__ import app

@app.route('/test')
def index3():
   return render_template('index3.html')
