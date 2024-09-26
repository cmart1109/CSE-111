import random

# WELCOME TO SENTENCE MAKER----------------------------------------------------------------------
# This Program makes random sentences based on lists---------------------------------------------
# Please Enjoy and feel free to use it as you want :)--------------------------------------------

def main():
    make_sentence(1, "past")
    make_sentence(1, "present")
    make_sentence(1, "future")
    make_sentence(2, "past")
    make_sentence(2, "present")
    make_sentence(2, "future")

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

def get_adjective(): 
      words = [ "dark", "red", "funny", "smelly", "rich",
      "salty", "gorgeous", "long", "happy", "special"]
      adjective = random.choice(words)
      return adjective

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
    adjective = get_adjective()
    noun = get_noun(quantity)
    preposition1 = get_prepositional_phrase(quantity)
    verb = get_verb(quantity, tense)
    preposition2 = get_prepositional_phrase(quantity)
    cap_determiner = determiner.capitalize()
    print(f'{cap_determiner} {adjective} {noun} {preposition1} {verb} {preposition2}.')

# The new functions to complete the prove -------------------------------------------------------

def get_preposition():
    words = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    preposition =get_preposition()
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {adjective} {noun}"    
    return prepositional_phrase

# End -------------------------------------------------------------------------------------------    
main()