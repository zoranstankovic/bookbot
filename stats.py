def count_words(text):
    return len(text.split())


def get_char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(item):
    return item["num"]


def sort_characters(head_count):
    sorted_list = []
    for ch in head_count:
        sorted_list.append({"char": ch, "num": head_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
