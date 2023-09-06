def count_words(file):
    words = file.split()

    return len(words)

def count_letters(file):
    words = file.split()
    letters = {}

    for word in words:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
    
    return letters

def print_report(word_count, letters):
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")

    for letter, count in sorted_letters:
        print(f"The {letter} character was found {count} times")

    print("--- End report ---")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letters = count_letters(file_contents)
    print_report(word_count, letters)