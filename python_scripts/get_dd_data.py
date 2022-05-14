
import os, re 


def get_paper_names(Exam, Year):
    
    all_files = os.listdir( os.path.join(  os.getcwd(), 'exam_data', 'JEE Main Data'  ) )
    all_files = [i for i in all_files if ((Exam in i) and (Year in i))]
    papers = []
    for file in all_files:
        paper = re.sub(r'(\.xlsx)|(SCQ)|(NUM)|(MATH)|(PHY)|(CHEM)', '', file)
        papers.append(paper)

    papers = list(set(papers))
    papers = [i.strip() for i in papers]
    return papers

# Exam = 'JEE Main'
# Year = '2020'
# print(get_paper_names(Exam, Year)[:5])