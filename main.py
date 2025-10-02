from stats import get_string_num
from stats import get_character_num
from stats import count_dic

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    #print(get_book_text("books/frankenstein.txt"))
    num_words = get_string_num(get_book_text("books/frankenstein.txt"))
    num_chars = get_character_num(get_book_text("books/frankenstein.txt"))
    #print(f"Found {num_words} total words", num_chars)
    counted_dic_lst = count_dic(num_chars)
    cleaned = []
    for item in counted_dic_lst:
        ch = item["char"]
        if ch.isalpha():
            cleaned.append(item)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in cleaned:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
