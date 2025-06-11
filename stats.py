def get_num_words(book: str):
    words = book.split()
    return len(words)

def get_all_characters(book: str):
    characters = {}

    for char in book:
        if char == " ":
            continue
        if char.lower() in characters:
            characters[char.lower()] = characters[char.lower()]+1
        else:
            characters[char.lower()] = 1

    return characters

def sort_on(dict):
    return dict["num"]

def get_sorted_characters(characters_in):

    characters_out = []
    for char in characters_in:
        characters_out.append({"char": char, "num": characters_in[char]})

    characters_out.sort(reverse=True, key=sort_on)

    return characters_out