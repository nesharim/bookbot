def count_words(document):
    words = document.split()
    return len(words)

def count_character_occurences(document):
    chars = {}
    words = document.split()
    
    for word in words:
        for char in word:
            l_char = char.lower()
            if l_char in chars:
                chars[l_char] += 1
            else:
                chars[l_char] = 1

    return chars

def sorted_chars_list(chars_count):
    chars_list = []
    for key, val in chars_count.items():
        chars_list.append({"char": key, "num": val})

    chars_list.sort(reverse=True, key=__sort_on)
    return chars_list

def __sort_on(items):
    return items["num"]
