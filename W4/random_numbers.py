import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    append_random_words(words, 5)
    print(words)

def append_random_numbers(numbers, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0,100)
        random_number = round(random_number, 1)
        numbers.append(random_number)

def append_random_words(words, quantity=1):
    random_words = ["Money","Castle","Cadet","Bycicle","Dinner","House","Nightmare","software","Wolf"]
    for _ in range(quantity):
        random_word = random.choice(random_words)
        words.append(random_word)


if __name__ == "__main__":
    main()