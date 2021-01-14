from utils.tokenizer.tokenizer_factory import TokenizerFactory
import unittest

class TestTokenizer(unittest.TestCase):

    def test_error_engine(self):
        self.assertRaises(ValueError, TokenizerFactory, "not_an_engine_type")

    def test_empty_text_for_coccoc_engine(self):
        inputText = ""
        engine = TokenizerFactory("coccoc")
        output = []
        self.assertEqual(engine.tokenize(inputText), output)

    def test_tokenizing_a_sentence_for_coccoc_engine(self):
        inputText = "Công việc của tôi hiện tại đang tiến triển tốt"
        engine = TokenizerFactory("coccoc")
        output = ['Công_việc', 'của', 'tôi', 'hiện_tại', 'đang', 'tiến_triển', 'tốt']
        self.assertEqual(engine.tokenize(inputText), output)

    def test_empty_text_for_vncorenlp_engine(self):
        inputText = ""
        engine = TokenizerFactory("vncorenlp")
        output = []
        self.assertEqual(engine.tokenize(inputText), output)

    def test_tokenizing_a_sentence_for_vncorenlp_engine(self):
        inputText = "Công việc của tôi hiện tại đang tiến triển tốt"
        engine = TokenizerFactory("vncorenlp")
        output = ['Công_việc', 'của', 'tôi', 'hiện_tại', 'đang', 'tiến_triển', 'tốt']
        self.assertEqual(engine.tokenize(inputText), output)

if __name__ == "__main__":
    unittest.main()
