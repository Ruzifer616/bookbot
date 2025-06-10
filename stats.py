def get_num_words(book: str):
    words = book.split()
    return len(words)

def get_all_symbols(book: str):
    characters = {}

    for char in book:
        if char.lower() in characters:
            characters[char.lower()] = characters[char.lower()]+1
        else:
            characters[char.lower()] = 1

    return characters