from __main__ import app, request 
import json


@app.route('/get_subjects_from_exam', methods=['GET'])
def get_subjects_from_exam():
   args = request.args
   Exam = args['Exam']
   index = [0, 1, 2]
   if Exam == 'JEE Main' or Exam == 'JEE Advanced':
      subjects = 'Mathematics Chemistry Physics'.split(' ')
   elif Exam == 'NEET':
      subjects = 'Biology Chemistry Physics'.split(' ')
   subjects_dict = dict(zip(index, subjects))
   subjects_json = json.dumps(subjects_dict)

   return subjects_json
