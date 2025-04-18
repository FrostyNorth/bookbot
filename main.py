from stats import word_counter,char_count,char_sort
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = word_counter(book_text)
    characters = char_sort(char_count(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in characters:
        character = item["char"]
        if character.isalpha():
            character_count = item["char_count"]
            print(f"{character}: {character_count}")
    print("============= END ===============")



main()


