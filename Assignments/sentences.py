import random;
#This Program makes random sentences based on lists
def main():
    make_sentence(1, "past")
    make_sentence(1, "present")
    make_sentence(1, "future")
    make_sentence(2, "past")
    make_sentence(2, "present")
    make_sentence(2, "future")
pass
# Functions-------------------------------------------------------------------------------------
# Here you can get the words -------------------------------------------------------------------
def get_determiner(quantity):
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  word = random.choice(words)
  return word

def get_noun(quantity):
    if quantity == 1: 
      words = [ "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"]
    else: 
      words = ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(words)
    return noun
def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = [  "will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
    else: 
        print("No valid Method")
        words = "0"
    verb = random.choice(words)
    return verb
# This Function creates the sentence using the previous functions to get the words ------------- 
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    cap_determiner = determiner.capitalize()
    print(f'{cap_determiner} {noun} {verb}.')
# End -------------------------------------------------------------------------------------------    
    main();