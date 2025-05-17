def get_num_words(book_text):
  words = book_text.split()
  num_words = len(words)
  print(f"----------- Word Count ---------- \nFound {num_words} total words")

def get_num_characters(book_text):
  num_characters = len(book_text)

def count_characters(book_text):
  print(f"--------- Character Count -------")
  book_text = book_text.lower()
  character_dictionary = {}
  for each_character in book_text:
    if each_character.isalpha():  # Only count alphabetic characters
      if each_character in character_dictionary:
        character_dictionary[each_character] += 1
      else:
        character_dictionary[each_character] = 1
  return character_dictionary

def sort_on(character_dictionary):
  return character_dictionary["num"]

