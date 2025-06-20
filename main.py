from stats import count_words
from stats import count_character_occurences

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    num_words = count_words(file_contents)
    char_occurrences = count_character_occurences(file_contents)
    print(f"{num_words} words found in the document")
    print(char_occurrences)

main()
