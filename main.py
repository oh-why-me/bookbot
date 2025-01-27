#For reading things
def generate_report(file_path, word_count, char_counts):

  # Sort characters by count in descending order
  sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True) 

  report = f"--- Begin report of {file_path} ---\n"
  report += f"{word_count} words found in the document\n\n"

  for char, count in sorted_char_counts:
    report += f"The '{char}' character was found {count} times\n"

  report += "--- End report ---"
  print(report)
def count_characters(text):
  char_counts = {}
  for char in text.lower():
    if char.isalpha():  # Consider only alphabetical characters
      char_counts[char] = char_counts.get(char, 0) + 1 
    
  return char_counts

def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    charc_counts2 = count_characters(file_contents)
    generate_report("books/frankenstein.txt", word_count, charc_counts2)
if __name__ == "__main__":
    main()