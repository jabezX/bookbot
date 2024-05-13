def count_words(text):
    words = text.split()
    return len(words)

def read_file(file_url):
    with open(file_url) as f:
        return f.read()
    
def count_letters(text):
    lower_text = text.lower()
    counter_dict = {}
    for char in lower_text:
        if(char in counter_dict):
            counter_dict[char] += 1
        else:
            counter_dict[char] = 1
    print(counter_dict)

def main():
    book_url = "books/frankenstein.txt"
    content = read_file(book_url)
    word_count = count_words(content)
    print(f"{word_count} words found in the document")
    count_letters(content)

main()