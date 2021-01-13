from pdfminer.high_level import extract_text
from tqdm import tqdm
import os, re
from collections import OrderedDict

raw_data_dir = './raw_data'
save_dir = './data'

def extract_pdf(file_path, save_dir):
    print(f'Processing {file_path}')
    raw_text = extract_text(file_path)
    process_pdf_content(raw_text, file_path.split('/')[-1].split('.pdf')[0], save_dir)

def process_pdf_content(raw_text, topic, save_dir):
    raw_text = re.sub('\s+', ' ', raw_text)
    splitted = re.split('(Table of Contents)\s+(LỜI NHÀ XUẤT BẢN)', raw_text)

    content = splitted[0]
    content = content.split('Đường nguyên còn gọi là đường glucogen – sinh thành từ đường glucoza mất nước – là một loại hidratcacbon quan trọng cung cấp năng lượng cho cơ thể.')[0]
    if len(splitted) > 1:
        # including table of content
        toc = splitted[-1]
        # get questions from table of contents
        questions = re.split('\?\s', toc)

    else:
        # extract questions manually
        iter = re.finditer('[0-9]+\.\s', content)
        questions = list()
        for m in iter:
            idx = m.start()
            question = content[idx:]
            question = question.split('?', 1)[0]
            questions.append(question)


    questions = [clipped_q.strip() for q in questions for clipped_q in re.split('[0-9\s]+\.', q) if clipped_q.strip() != '']

    # split content by question and save result
    QA_map = OrderedDict()
    incremental_idx = 1
    for question in questions:
        try:
            # handle exception when question parsed incorrectly
            answer = content.split(f'{incremental_idx}. ' + question)[1]
            QA_map[question] = answer
            incremental_idx = incremental_idx + 1
        except:
            pass

    print(f'{len(QA_map)} questions in total')
    questions = list(QA_map)
    for i in tqdm(range(len(questions))):
        question = questions[i]
        answer = QA_map[question]
        if i < len(questions) - 1:
            answer = answer.split(f'{i+2}. ' + questions[i+1])[0]
        answer.replace('T ừ', 'Từ')
        with open(f'{save_dir}/{topic}/Q{i+1}.txt', 'w') as f:
            f.write(question + "?")
        with open(f'{save_dir}/{topic}/A{i+1}.txt', 'w') as f:
            f.write(re.sub('^[\s\?]+', '', answer).strip())

if __name__ == '__main__':
    list_pdfs = os.listdir(raw_data_dir)
    # for pdf in list_pdfs:
        # extract_pdf(f'./raw_data/{pdf}', save_dir)
    extract_pdf('./raw_data/Trai_dat.pdf', save_dir)
