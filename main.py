import sys
from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    characters = get_all_characters(book)
    characters = get_sorted_characters(characters)


    print("========= BOOKBOT =========")
    print("Analyzing book found at books/frankenstein.txt")
    print("-------- Word Count -------")
    print(f"Found {num_words} total words")
    print("----- Character Count -----")
    for d in characters:
        print(f"{d["char"]}: {d["num"]}")

main()