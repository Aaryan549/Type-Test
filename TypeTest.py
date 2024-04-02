import time
import random

word_categories = {
    "nouns": [
        "cat", "dog", "book", "computer", "house", "tree", "cloud", "rain", "sun", "moon",
        "ocean", "mountain", "river", "forest", "city", "country", "animal", "bird", "insect", "food"
    ],
    "verbs": [
        "walks", "runs", "reads", "writes", "plays", "sleeps", "eats", "drinks", "talks", "sings",
        "jumps", "flies", "swims", "crawls", "thinks", "feels", "loves", "hates", "dreams", "wishes"
    ],
    "adjectives": [
        "big", "small", "red", "blue", "green", "yellow", "happy", "sad", "angry", "funny",
        "tall", "short", "wide", "narrow", "deep", "shallow", "hot", "cold", "soft", "hard"
    ],
    "adverbs": [
        "quickly", "slowly", "loudly", "softly", "carefully", "happily", "sadly", "angrily", "funnily",
        "very", "really", "quite", "almost", "always", "never", "sometimes", "everywhere", "nowhere"
    ],
    "prepositions": [
        "in", "on", "at", "to", "from", "by", "with", "about", "as", "like"
    ],
    "conjunctions": [
        "and", "but", "or", "because", "so", "if", "then", "although", "while", "until"
    ]
}

def random_sentence(min_words=18, max_words=22):

  num_words = random.randint(min_words, max_words)

  sentence_words = []

  for _ in range(num_words):
    category = random.choice(list(word_categories.keys()))
    random_word = random.choice(word_categories[category])
    sentence_words.append(random_word)

  sentence = " ".join(sentence_words)
  sentence = sentence.capitalize() + '.' 

  return sentence

def main():
 loop = True
 while loop :
     Sentence = random_sentence()
     Words = len(Sentence.split())
     print(Sentence)
     tint =time.time()
     inputtxt = str(input("Enter the Sentence: "))
     tend=time.time()
     acc = len(set(inputtxt.split())&set(Sentence.split()))
     wordsin = len(inputtxt.split())
     accuracy= acc/Words
     AccPercen= int(accuracy * 100)
     timetaken = tend - tint
     raw = int(wordsin/timetaken *100)
     wpm = int(raw * accuracy)     
     print("WPM:",wpm,"Accuracy:",AccPercen,"% ""Raw WPM:",raw)
     again = input("Again? (y/n): ")  
     loop = again.lower() == 'y'
 print("Exiting...") 
     
 
    
    
if __name__ == '__main__':
   main()    
    