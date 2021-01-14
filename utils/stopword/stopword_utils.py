import os.path

class StopwordUtils():
    def __init__(self, stopwords = 'full'):
        my_path = os.path.abspath(os.path.dirname(__file__))
        if stopwords == 'full':
            stopwords_file = 'vietnamese-stopwords.txt'
        elif stopwords == 'basic':
            stopwords_file = 'vietnamese-stopwords-basic.txt'
        else:
            raise ValueError('Illegal stopword list type, expected "full" or "basic", found {0}'.format(stopwords))
        with open(os.path.join(my_path, stopwords_file), 'r') as f:
            self.stopword_list = f.read().split('\n')

    def check_stopword(self, word):
        return word.lower() in self.stopword_list

    def remove_stopwords_from_sentence(self, text):
        return " ".join(list(filter(lambda w: not self.check_stopword(w), text.split())))

