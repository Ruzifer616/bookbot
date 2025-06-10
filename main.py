from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    characters = get_all_symbols(book)
    print(f"{num_words} words found in the document")
    print(characters)

main()