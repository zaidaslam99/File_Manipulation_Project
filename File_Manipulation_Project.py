# This program reads the contents from two text files and compares them in the following ways
    # It should display words that appear in both files
    # It should display a list of words that appear in the first file but not the second file
    # It should display a list of words that appear in the second file but not the first
    # It should display a list of the words that appear in either the first or second file but not both
def main():

    first_file_list_with_words, first_file_text_set = read_from_the_first_file()

    second_file_list_with_words, second_file_text_set = read_from_second_file()

    display_everything(first_file_list_with_words, first_file_text_set, second_file_list_with_words,
                       second_file_text_set)

def read_from_the_first_file():

    read_first_file = open("first_random_file.txt", "r")

    read_first_file_obj = read_first_file.readlines()

    first_file_text_list = []
    first_file_list_with_words = []

    # Parse the List
    index = 0

    while index < len(read_first_file_obj):
        element_rstrip = read_first_file_obj[index].rstrip()
        first_file_text_list.append(element_rstrip)
        index += 1

    for each_element in first_file_text_list:
        for each_word in each_element.split():
            first_file_list_with_words.append(each_word)

    first_file_text_set = set(first_file_list_with_words)

    return first_file_list_with_words, first_file_text_set

def read_from_second_file():

    read_second_file = open("second_random_file.txt", "r")

    read_second_file_obj = read_second_file.readlines()

    second_file_text_list = []
    second_file_list_with_words = []

    index = 0

    while index < len(read_second_file_obj):
        element_rstrip = read_second_file_obj[index].rstrip("\n")
        second_file_text_list.append(element_rstrip)
        index += 1

    for each_element in second_file_text_list:
        for each_word in each_element.split():
            second_file_list_with_words.append(each_word)

    second_file_text_set = set(second_file_list_with_words)

    return second_file_list_with_words, second_file_text_set


def display_everything(first_file_list_with_words, first_file_text_set, second_file_list_with_words,
                       second_file_text_set):
    print()
    # Display unique words in first random file
    print("Unique words in first_random_file.txt is:")
    for each_word in first_file_text_set:
        print(each_word)
    print()

    # Display unique words in first random file
    print("Unique words in second_random_file.txt is:")
    for each_word in second_file_text_set:
        print(each_word)
    print()

    # Get the word difference of first file - second file
    print("The words that appear in the first file and not the second is:")
    first_file_difference = first_file_text_set - second_file_text_set
    for each_word in first_file_difference:
        print(each_word)
    print()

    # Get the word difference of second_file - first_file
    print("The words that appear in the second file and not the first is:")
    second_file_difference = second_file_text_set - first_file_text_set
    for each_word in second_file_difference:
        print(each_word)
    print()

    # Get the symmeteric difference between the first_file and the second_file
    print("The uncommon words between the first file and second file is:")
    symmeteric_difference = first_file_text_set.symmetric_difference(second_file_text_set)
    for each_word in symmeteric_difference:
        print(each_word)
    print()

main()