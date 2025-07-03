def get_word_count(text):
    return len(text.split())
# This function counts the number of words in the book text.

def get_character_count(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
# This function counts the occurrences of each character in the book text.
# It returns a dictionary where keys are characters and values are their counts.


def sort_character_count(character_count):
    sorted_count = []
    for char, num in character_count.items():
        if char.isalpha():
            sorted_count.append({'char': char, 'num': num})
    sorted_count.sort(reverse=True, key=lambda x: x['num'] )
    return sorted_count
# This function sorts the character count dictionary by the number of occurrences
# in descending order and returns a list of dictionaries with character and count.