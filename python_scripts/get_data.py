import pandas as pd
import numpy as np
import os, json

# exam_file = 'JEE Main 2021 (Online) 27th July Evening Shift MATH SCQ.xlsx'

def q_data_scq(exam_file):

    path = os.getcwd()
    path = os.path.join(path, r'exam_data\JEE Main Data', exam_file)
    df = pd.read_excel(path)
    q_data = df[['que_desc', 'ans1', 'ans2', 'ans3', 'ans4', 'true_ans', 'Ref_Text']]
    old_options_cond = [ q_data['true_ans']==1,q_data['true_ans']==2,q_data['true_ans']==3,q_data['true_ans']==4]
    new_options = ['(A)', '(B)', '(C)', '(D)']
    q_data['true_ans'] = np.select(old_options_cond, new_options)
    return q_data.to_dict()

def q_data_num(exam_file):

    path = os.getcwd()
    path = os.path.join(path, r'exam_data\JEE Main Data', exam_file)
    df = pd.read_excel(path)
    q_data = df[['que_desc', 'true_ans', 'Ref_Text']]
    return q_data.to_dict()


def get_paper_data_json_main(Paper_view, Subject_view):
    dir_path = os.path.join(  os.getcwd(), 'exam_data', 'JEE Main Data'  )
    subject_mapping = {'Mathematics':['MATH'], 'Physics':['PHY'], 'Chemistry':['CHEM'], 'All Subjects':'MATH PHY CHEM'.split(' ')}
    subjects = subject_mapping[Subject_view]
    q_types = ['SCQ', 'NUM']
    file_names = []

    q_data = {}
    for subject in subjects :
        q_sub_data = {}
        for q_type in q_types:
            file_names.append(f'{Paper_view} {subject} {q_type}.xlsx')
            file = os.path.join(dir_path, f'{Paper_view} {subject} {q_type}.xlsx') 
            df = pd.read_excel(file)
            q_df = df[['que_desc', 'ans1', 'ans2', 'ans3', 'ans4', 'true_ans', 'Ref_Text']]
            q_sub_data[q_type] = q_df.to_dict('records')
        q_data[subject] = q_sub_data

    return json.dumps(q_data) 