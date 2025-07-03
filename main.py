import sys
from stats import get_word_count, get_character_count, sort_character_count

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
#   # This function reads the content of the book from the specified path
#   # and returns it as a string.

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    # Check if the book file exists
    c_count = get_character_count(get_book_text(book_path))
    # This function counts the occurrences of each character in the book text.
    # It returns a dictionary where keys are characters and values are their counts.
    num_words = get_word_count(get_book_text(book_path))
    # This function counts the number of words in the book text.
    # It returns the total word count as an integer.
    print (
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {book_path}...\n"
        f"----------- Word Count -----------\n"
        f"Found {num_words} total words\n"
        f"------- Character Count -------"
    )
    sorted_count = sort_character_count(c_count)
    for char in sorted_count:
        print(f"{char['char']}: {char['num']}")
        # This prints the character and its count in descending order of occurrences.


main ()