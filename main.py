file_to_read = 'books/frankenstein.txt'

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    count = {}
    for letter in text.lower():
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

with open(file_to_read, 'r') as f:
    file_contents = f.read()
    total_words = count_words(file_contents)
    count_letters_dict = count_letters(file_contents)
    print(f'--- Begin report of {file_to_read} ---')
    print(f'{total_words} words found in the document\n')
    keys = list(count_letters_dict.keys())
    keys.sort()
    for key in keys:
        if key.isalpha():
            print(f"The '{key}' character was found {count_letters_dict[key]} times")
    print('--- End report ---')


