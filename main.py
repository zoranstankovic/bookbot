from stats import get_num_of_words, get_num_characters, sort_chars_desc
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    num_words = get_num_of_words(book_text)
    print(f"Found {num_words} total words")
    num_chars = get_num_characters(book_text)
    num_chars_sorted = sort_chars_desc(num_chars)
    print("--------- Character Count -------")
    for char_dict in num_chars_sorted:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")
    print("============= END ===============")


if __name__ == '__main__':
    main()
