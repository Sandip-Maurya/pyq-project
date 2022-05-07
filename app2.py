from flask import Flask, render_template
app = Flask(__name__)
import routes

@app.route('/')
def index2():
   return render_template('index2.html')


if __name__ == '__main__':
   app.run(debug = True)