from flask import Flask, render_template, request, url_for
from python_scripts.gen_files_names import get_required_files
from python_scripts.get_data import q_data_scq, q_data_num


app = Flask(__name__)

# value = ['Just sending data from python to html', 'Drop Down Value from Python']
file_names = get_required_files()

exam_name = 'test exam'
result_from_python = {'exam_name':exam_name, 'q1':[1,2,3,4,5,6], 'q2':[2,3,4,5,6], 'q3':[3,4,5,6]}
result_math_scq = ''
result_math_num = ''
result_chem_scq = ''
result_chem_num = ''
result_phy_scq = ''
result_phy_num = ''


@app.route('/')
def student():
   return render_template('index.html', values = file_names)


@app.route('/math',methods = ['POST', 'GET'])
def math():
   if request.method == 'POST':
      user_input = request.form.get('examFileNameMath')
      # exam_year = request.form.get('year')
      exam_file_scq = f'{user_input} SCQ.xlsx' 
      result_math_scq = q_data_scq(exam_file_scq)

      exam_file_num = f'{user_input} NUM.xlsx' 
      result_math_num = q_data_num(exam_file_num)

      exam_name_math = [exam_file_scq[:-5], exam_file_num[:-5]]

      return render_template("result.html", exam_name_math = exam_name_math, result_scq = result_math_scq, result_num = result_math_num)

@app.route('/chemistry',methods = ['POST', 'GET'])
def chemistry():
   if request.method == 'POST':
      user_input = request.form.get('examFileNameChem')
      # exam_year = request.form.get('year')
      exam_file_scq = f'{user_input} SCQ.xlsx' 
      result_math_scq = q_data_scq(exam_file_scq)

      exam_file_num = f'{user_input} NUM.xlsx' 
      result_math_num = q_data_num(exam_file_num)

      exam_name_math = [exam_file_scq[:-5], exam_file_num[:-5]]

      return render_template("result.html", exam_name_math = exam_name_math, result_scq = result_math_scq, result_num = result_math_num)

@app.route('/physics',methods = ['POST', 'GET'])
def physics():
   if request.method == 'POST':
      user_input = request.form.get('examFileNamePhy')
      # exam_year = request.form.get('year')
      exam_file_scq = f'{user_input} SCQ.xlsx' 
      result_math_scq = q_data_scq(exam_file_scq)

      exam_file_num = f'{user_input} NUM.xlsx' 
      result_math_num = q_data_num(exam_file_num)

      exam_name_math = [exam_file_scq[:-5], exam_file_num[:-5]]

      return render_template("result.html", exam_name_math = exam_name_math, result_scq = result_math_scq, result_num = result_math_num)


if __name__ == '__main__':
   app.run(debug = True)