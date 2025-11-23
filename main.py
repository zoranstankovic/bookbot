def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    total_words = count_words(book_text)
    print(f"Found {total_words} total words")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    return len(text.split())


main()
