from string import ascii_lowercase

def count_characters(words):
  char_count = {}
  for letter in ascii_lowercase:
    char_count[letter] = 0
  
  for word in words:
    for letter in word:
      if letter in char_count:
        char_count[letter.lower()] += 1

  return char_count

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    characters = count_characters(words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    for letter in characters:
      print(f"The {letter} character was found {characters[letter]} times")