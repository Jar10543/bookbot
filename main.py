import sys
from stats import *


def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    get_num_words(book_text)
    get_num_characters(book_text)
    character_counts = count_characters(book_text)
    sorted_character_counts = sorted(
        character_counts.items(), key=lambda item: item[1], reverse=True
    )
    for char, count in sorted_character_counts:
        print(f"{char}: {count}")


main()