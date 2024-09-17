import argparse


def init_parser():
    # Instantiate the parser
    parser = argparse.ArgumentParser(prog='python3 main.py', description="A python program that can analyze an entire book and print out an interesting statistical report.")
    parser.add_argument('-v', '--verbose', action='store_true') # on/off flag
    required_arguments = parser.add_argument_group("required arguments")
    required_arguments.add_argument('-f', '--filename', help="Specify the filename to process", type=str, required=True) # positional argument
    optional_arguments = parser.add_argument_group("optional arguments")
    optional_arguments.add_argument('-cw', '--count-words', help="Returns the count of the words in the document", action='store_true')
    optional_arguments.add_argument('-cc', '--count-chars', help="Returns the number of times each character appears in the document", action='store_true')
    optional_arguments.add_argument('-pr', '--print-report', help="Returns a report of the document", action='store_true')

    # Parse and pass arguments to the main function
    return parser.parse_args()


def count_words(text):
    return len(text.split())


def count_characters(text):
    char_dict = {}
    for char in text:
        if char not in char_dict:
            lowered_char = char.lower()
            char_dict[lowered_char] = 0
        char_dict[lowered_char] += 1
    return char_dict


def sort_on(dict):
        return dict["num"]


def print_report(text):
    print(f"--- Begin report of document ---")
    print(f"{count_words(text)} words found in the document")
    print()
  
    char_dict = count_characters(text)
    list_of_dicts = []
    for key in char_dict:
         if key.isalpha():
            list_of_dicts.append({"char": key, "num": char_dict[key]})

    list_of_dicts.sort(reverse=True, key=sort_on)

    for item in list_of_dicts:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    
    print(f"--- End report of document ---")