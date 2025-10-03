from stats import get_string_num
from stats import get_character_num
from stats import count_dic
import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    #print(get_book_text("books/frankenstein.txt"))
    book_text = get_book_text(book_path)
    num_words = get_string_num(book_text)
    num_chars = get_character_num(book_text)
    #print(f"Found {num_words} total words", num_chars)
    counted_dic_lst = count_dic(num_chars)
    cleaned = []
    for item in counted_dic_lst:
        ch = item["char"]
        if ch.isalpha():
            cleaned.append(item)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in cleaned:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
