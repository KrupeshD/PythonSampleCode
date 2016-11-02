"""wo module - Contains Function : word_occur()"""


def words_occur():

    """
    word_occur()
    :return: count occurrences of words in a file
    """
    # prompt user for the name of the file
    file_name = input("Enter the name of the file: ")

    #Open the file, read it and store its words in a file
    with open(file_name,'r') as f:
        word_list = f.read().split()

    # Count occurrences of each word
    occurs_dict = {}
    for word in word_list:
        # Increment the counter as you pass through each word
        occurs_dict[word] = occurs_dict.get(word,0) + 1

    # Print the result
    print("File %s had %d words where %d are unique" \
          % (file_name,len(word_list),len(occurs_dict)))
    print(occurs_dict)

# Following code run the word_count function when this python program is executed from command line using python wo.py\

if __name__ == '__main__':
    words_occur()

