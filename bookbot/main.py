# Set filename
filepath = "books/frankenstein.txt"

# Open the file
with open(filepath) as f:

    # Read content into a string
    file_contents = f.read()
    
    # Calculate number of words
    word_count = len(file_contents.split())

    # Start report
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words foung in the document")
    print()
    
    # Calculate number of words, filter and sort
    letter_count = {}
    for c in file_contents:
        c = c.lower()
        letter_count[c] = letter_count.get(c, 0) + 1
    letter_count_sorted = dict(sorted(filter(lambda item: item[0].isalpha(), letter_count.items()), key=lambda x: x[1], reverse=True))
    for k, v in letter_count_sorted.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
