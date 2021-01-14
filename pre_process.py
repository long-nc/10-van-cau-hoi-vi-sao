import argparse

from utils.tokenizer.tokenizer_factory import TokenizerFactory
from utils.stopword.stopword_utils import StopwordUtils
import string, sys, re

class PreProcessor():

    def __init__(self, stopword, tokenizer = 'coccoc'):
        self.tokenizer = TokenizerFactory(tokenizer)
        if stopword is not None:
            self.stopwordUtils = StopwordUtils(stopword)
        else:
            self.stopwordUtils = None

    def preProcess(self, text):

        # 1: split into sentences
        sentences = filter(lambda s: s != '', re.split('\.|\?', text))
        sentences = [s.translate(str.maketrans('', '', string.punctuation)) for s in sentences]

        # 2: tokenizing
        for index, s in enumerate(sentences):
            words = self.tokenizer.tokenize(s)
            if self.stopwordUtils is not None:
                sentences[index] = " ".join(filter(lambda w: not self.stopwordUtils.checkStopword(w), words))
            else:
                sentences[index] = " ".join(words)

        print(sentences)
        return sentences

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Question pre-processing')
    parser.add_argument('text', help="Input text")
    parser.add_argument('-s', '--stopword', help="Stopword list: full, basic")
    parser.add_argument('-t', '--tokenizer', default='coccoc', help="Tokenizer engine: coccoc, vncorenlp (default is coccoc)")

    args = parser.parse_args()

    preProcessor = PreProcessor(stopword = args.stopword, tokenizer = args.tokenizer)
    preProcessor.preProcess(text = args.text)
