import re


def find_longest_word():
    sentence = "London is the capital of Gret Britain. I want to see this city, because it will be so interesting"

    print(f"'{sentence}'")

    words = re.findall(r'[a-zA-Zа]+', sentence)

    if not words:
        print("\nThe sentence is empty.")
        return

    longest_word = max(words, key=len)

    print(f"List of words: {words}")
    print(f"\nBiggest word: '{longest_word}'")
    print(f"Len of symb: {len(longest_word)} ")

find_longest_word()
