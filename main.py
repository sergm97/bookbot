with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words_count = len(file_contents.split())
    print(f"Words count: {words_count}")
