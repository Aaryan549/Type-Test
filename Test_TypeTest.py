import random
import time
from TypeTest import random_sentence


def test_word_count_range():
  sent = random_sentence()
  word = len(sent.split())
  assert 18 <= word <= 22, f"Word count is out of range: {word}"

def test_sentence_structure():
  sent = random_sentence()
  assert sent[0].isupper(), "Sentence does not start with a capital letter"
  assert sent[-1] == ".", "Sentence does not end with a period"

def test_randomness_basic():
  sentence1 = random_sentence()
  sentence2 = random_sentence()
  assert sentence1 != sentence2, "Generated sentences are identical (may be a fluke in randomness)"

def test_type_test_integration():
  sent = random_sentence()
  user_input = sent  
  word = len(sent.split())
  accuracy = 1.0
  time_taken = 1.0  
  wpm = int(word / time_taken * accuracy)
  original_words = set(sent.split())
  typed_words = set(user_input.split())
  assert original_words == typed_words, "Typed sentence does not match the original"
  assert 18 <= wpm <= 22, f"WPM ({wpm}) seems out of expected range" 
