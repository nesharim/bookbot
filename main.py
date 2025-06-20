from stats import count_words
from stats import count_character_occurences
from stats import sorted_chars_list
import sys

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = args[1]
    file_contents = get_book_text(file_path)
    num_words = count_words(file_contents)
    char_occurrences = count_character_occurences(file_contents)
    sorted_char_count = sorted_chars_list(char_occurrences)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item["num"]}")
    
    print("============= END ===============")

main()
