def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    num_words = counting_words(text)
    character_counts = count_characters(text)
    sorted_characters = frank(character_counts)

    print("---Begin report---")
    print(f"{num_words} words found in the document")
    for item in sorted_characters:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("---End report---")
    
    
def get_text(path_to_file):
    with open(path_to_file) as f:
                

           
        return f.read()
    

def counting_words(words):
    text = words.split()
    return len(text)

def count_characters(text):
    letter_counts = {}
    letters = text.lower()
    for letter in letters:
        if letter in letters:
            if letter.isalpha():
                if letter not in letter_counts:
                    letter_counts[letter] = 1
                else:
                    letter_counts[letter] += 1
        
    return letter_counts

def sort_on(character_counts):
    return character_counts["num"]

def frank(character_counts):
    list = []
    for char, num in character_counts.items():
        dict_list = {"char":char,"num":num}
        list.append(dict_list)
    list.sort(reverse = True, key = sort_on)
    return list

        
main()
