def get_num_of_words(book_text):
    return len(book_text.split())


def get_num_characters(book_text):
    num_of_char = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in num_of_char:
            num_of_char[lower_char] += 1
        else:
            num_of_char[lower_char] = 1

    return num_of_char

def sort_on(char_dict):
    return char_dict["count"]


def sort_chars_desc(chars_dict):
    chars_list = []
    for chars_count in chars_dict:
        chars_list.append({"char": chars_count, "count": chars_dict[chars_count]})

    chars_list.sort(key=sort_on, reverse=True)
    return chars_list
