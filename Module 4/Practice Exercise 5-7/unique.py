# unique.py

# Function to read a file and return a list of unique words in alphabetical order
def unique_words_from_file(file_name):
    # Initialize an empty list to store unique words
    unique_words = []

    # Open the file for reading
    with open(file_name, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Split the line into words (this will also remove any punctuation)
            words = line.split()

            # Loop through each word in the line
            for word in words:
                # Normalize the word to lowercase and remove any punctuation (basic approach)
                normalized_word = ''.join(e for e in word if e.isalnum()).lower()

                # Add the word to the list if it is not already present
                if normalized_word and normalized_word not in unique_words:
                    unique_words.append(normalized_word)

    # Sort the unique words in alphabetical order
    unique_words.sort()

    return unique_words

# Main function to interact with the user
def main():
    # Ask the user for the file name
    file_name = input("Enter the input file name: ")

    # Get the unique words from the file
    unique_words = unique_words_from_file(file_name)

    # Print each unique word
    for word in unique_words:
        print(word)

# Run the program
if __name__ == "__main__":
    main()
