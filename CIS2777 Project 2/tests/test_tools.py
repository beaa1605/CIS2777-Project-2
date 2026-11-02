import unittest
from src.tools.tool_chat import calculator, word_counter


class TestTools(unittest.TestCase):

 def test_calculator_addition(self):
  self.assertEqual(calculator("2 + 3"), "5")

 def test_calculator_multiplication(self):
  self.assertEqual(calculator("25 * 4"), "100")

 def test_word_counter(self):
  self.assertEqual(word_counter("Selina is cool."), "The text contains 3 words.")

 def test_empty_word_counter(self):
  self.assertEqual(word_counter(""), "The text contains 0 words.")


if __name__ == "__main__":
 unittest.main()