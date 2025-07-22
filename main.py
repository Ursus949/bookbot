#!/usr/bin/env python3
from stats import get_book_text, get_num_words, count_characters, sort_characters
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    try:
        book_text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)

    word_count = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
