import os

def get_required_files_one_sub(year = '2021', type_of_q = 'SCQ', subject = 'MATH'):
    
    path = os.getcwd()
    path = os.path.join(path, 'exam_data', 'JEE Main Data')
    
    all_files = os.listdir(path)
    all_files = [i for i in all_files if '.xlsx' in i]
    filtered_files = [i[:-9] for i in all_files if (year in i) and (type_of_q in i) and (subject in i) ]

    return (filtered_files)

# print(get_required_files())

def get_required_files():
    math = get_required_files_one_sub(year = '2021', type_of_q = 'SCQ', subject = 'MATH')
    chem = get_required_files_one_sub(year = '2021', type_of_q = 'SCQ', subject = 'CHEM')
    phy = get_required_files_one_sub(year = '2021', type_of_q = 'SCQ', subject = 'PHY')
    return [math, chem, phy]