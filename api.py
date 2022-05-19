from __main__ import app, request
import json
from  python_scripts.get_dd_data import get_paper_names
# , get_q_data_from_filter_data

@app.route('/get_exams', methods = ['GET'])
def get_exams():
   Exams_list = 'JEE Main, NEET, JEE Advanced'.split(', ')
   Exams = dict (zip (range(len(Exams_list)), Exams_list))
   return json.dumps(Exams)


@app.route('/get_years_from_exam', methods = ['GET'])
def get_years_from_exam():
   args = request.args
   Exam = args['Exam']
   years = '2021 2020 2019 2018'.split(' ')
   # print(Exam)
   return json.dumps( dict( zip( range(len(years)), years ) ) )


@app.route('/get_papers_from_exam_and_year', methods=['GET'])
def get_papers_from_exam_and_year():
   args = request.args
   Exam = args['Exam']
   Year = args['Year']
   if Exam!='JEE Main':
      return json.dumps({0:'Papers will be added soon'})
   papers = get_paper_names(Exam, Year)

   return json.dumps( dict( zip( range(len(papers)), papers ) ) )


@app.route('/get_subjects_from_exam_and_year', methods=['GET'])
def get_subjects_from_exam():
   args = request.args
   Exam = args['Exam']
   if Exam == 'JEE Main' or Exam == 'JEE Advanced':
      subjects = 'Mathematics Chemistry Physics'.split(' ')
   elif Exam == 'NEET':
      subjects = 'Biology Chemistry Physics'.split(' ')
   subjects_dict = dict(zip(range(len(subjects)), subjects))
   subjects_json = json.dumps(subjects_dict)

   return subjects_json

# q_data = get_q_data_from_filter_data()
@app.route('/test')
def test():
   test_mathml = r'<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mfrac><mrow data-mjx-texclass="ORD"><mi>d</mi><mi>y</mi></mrow><mrow data-mjx-texclass="ORD"><mi>d</mi><mi>x</mi></mrow></mfrac></mrow><mo>=</mo><mrow data-mjx-texclass="ORD"><mfrac><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="ORD"><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mi>x</mi><mo>+</mo><mi>y</mi></mrow></msup></mrow><mo>+</mo><mrow data-mjx-texclass="ORD"><msup><mn>2</mn><mi>x</mi></msup></mrow></mrow><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="ORD"><msup><mn>2</mn><mi>y</mi></msup></mrow></mrow></mfrac></mrow></math>, y(0) = 1, then y(1) is equal to :</p>'
   return json.dumps({0:test_mathml})


