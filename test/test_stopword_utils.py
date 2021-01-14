from utils.stopword.stopword_utils import StopwordUtils
import unittest

class TestStopword(unittest.TestCase):

    def test_error_stopword_list(self):
        self.assertRaises(ValueError, StopwordUtils, "not_a_stopword_list")

    # test for full list

    def test_empty_text_for_full_list(self):
        input_text = ""
        util = StopwordUtils('full')
        output_text = ""
        self.assertEqual(util.remove_stopwords_from_sentence(input_text), output_text, "Should be empty")

    def test_including_stop_words_for_full_list(self):
        input_text = "Công ty có trả tiền tăng ca không"
        util = StopwordUtils('full')
        output_text = "Công ty tiền ca"
        self.assertEqual(util.remove_stopwords_from_sentence(input_text), output_text, "Should remove stop words")

    def test_not_including_stop_words_for_full_list(self):
        input_text = "Thiên ngoại hữu thiên"
        util = StopwordUtils('full')
        output_text = "Thiên ngoại hữu thiên"
        self.assertEqual(util.remove_stopwords_from_sentence(input_text), output_text, "Should not remove any stop words")

    def test_checking_a_stop_word_for_full_list(self):
        input_text = "là"
        util = StopwordUtils('full')
        output = True
        self.assertEqual(util.check_stopword(input_text), output, "Should be a stopword")

    def test_checking_not_a_stop_word_for_full_list(self):
        input_text = "sống"
        util = StopwordUtils('full')
        output = False
        self.assertEqual(util.check_stopword(input_text), output, "Should not be a stopword")

    # test for basic list

    def test_empty_text_for_basic_list(self):
        input_text = ""
        util = StopwordUtils('basic')
        output_text = ""
        self.assertEqual(util.remove_stopwords_from_sentence(input_text), output_text, "Should be empty")

    def test_including_stop_words_for_basic_list(self):
        input_text = "Công ty có trả tiền tăng ca không"
        util = StopwordUtils('basic')
        output_text = "Công ty trả tiền tăng ca"
        self.assertEqual(util.remove_stopwords_from_sentence(input_text), output_text, "Should remove stopwords")

    def test_not_including_stop_words_for_basic_list(self):
        input_text = "Thiên ngoại hữu thiên"
        util = StopwordUtils('basic')
        output_text = "Thiên ngoại hữu thiên"
        self.assertEqual(util.remove_stopwords_from_sentence(input_text), output_text, "Should not remove stopwords")

    def test_checking_a_stop_word_for_basic_list(self):
        input_text = "là"
        util = StopwordUtils('basic')
        output = True
        self.assertEqual(util.check_stopword(input_text), output, "Should be a stopword")

    def test_checking_not_a_stop_word_for_basic_list(self):
        input_text = "sống"
        util = StopwordUtils('basic')
        output = False
        self.assertEqual(util.check_stopword(input_text), output, "Should not be a stopword")

if __name__ == "__main__":
    unittest.main()

