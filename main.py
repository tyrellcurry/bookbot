def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = count_words(text)
    print(f"{word_count} words found in the document\n")
    letters_dict_list = count_letters(text)
    letters_list = convert_dict_to_list(letters_dict_list)
    letters_list.sort(reverse=True, key=sort_on)
    for letter_dict in letters_list:
        print(f"The '{letter_dict["letter"]}' character was found {letter_dict["num"]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)  

def count_letters(words):
    letters_dict = {}
    for char in words:
        lowercase_char = char.lower()
        if(lowercase_char.isalpha()):
            if (lowercase_char in letters_dict):
                letters_dict[lowercase_char] += 1
            else:
                letters_dict[lowercase_char] = 1
    return letters_dict

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    list_of_letters = []
    for letter in dict:
        list_of_letters.append({"letter":letter, "num":dict[letter]})
    return list_of_letters

main()