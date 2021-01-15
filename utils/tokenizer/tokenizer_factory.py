import os.path

class TokenizerFactory():
    def __init__(self, engine = 'coccoc'):
        my_path = os.path.abspath(os.path.dirname(__file__))
        self.engine = engine
        if engine == 'coccoc':
            from CocCocTokenizer import PyTokenizer
            self._tokenizer = PyTokenizer()
        elif engine == 'vncorenlp':
            from vncorenlp import VnCoreNLP
            self._tokenizer = VnCoreNLP(os.path.join(my_path, "vncorenlp","VnCoreNLP-1.1.1.jar"), annotators="wseg", max_heap_size='-Xmx500m')
        elif engine == 'pyvi':
            from pyvi import ViTokenizer
            self._tokenizer = ViTokenizer
        else:
            raise ValueError('Invalid engine type, expected "coccoc","vncorenlp" or "pyvi", found {0}'.format(engine))

    def tokenize(self, text):
        if self.engine == 'coccoc':
            return self._tokenizer.word_tokenize(text)
        elif self.engine == 'vncorenlp':
            result = self._tokenizer.tokenize(text)
            return result[0] if len(result) > 0 and type(result[0]) is list else result
        elif self.engine == 'pyvi':
            return self._tokenizer.tokenize(text).split()
