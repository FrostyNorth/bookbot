def word_counter(text):
    word_list = text.split()
    return len(word_list)


def char_count(text):
    key = {}
    for char in text:
        c = char.lower()
        if c not in key:
            key[c] = 1
        else:
            key[c] += 1
    return key


def char_sort(characters):
    new_list = []
    def sort_on(dict):
        return dict["char_count"]
    for c in characters:
        new_list.append({"char": c, "char_count": characters[c]})
    new_list.sort(reverse = True, key = sort_on)
    

    return new_list
