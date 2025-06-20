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

