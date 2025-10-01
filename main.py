from stats import get_string_num
from stats import get_character_num

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    #print(get_book_text("books/frankenstein.txt"))
    num_words = get_string_num(get_book_text("books/frankenstein.txt"))
    num_chars = get_character_num(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words", num_chars)


main()
