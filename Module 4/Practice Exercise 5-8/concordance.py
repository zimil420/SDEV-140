# Open the file and process the contents
def main():
    # Take the input file name from the user
    inName = input("Enter the input file name: ")

    try:
        # Open the input file in read mode
        inputFile = open(inName, 'r')

        # Initialize an empty dictionary to store words and their frequencies
        uniqueWords = {}

        # Process each line in the input file
        for line in inputFile:
            # Split the line into words (assumes words are separated by spaces)
            words = line.split()

            # Process each word in the line
            for word in words:
                # If the word is already in the dictionary, increment its frequency
                if word in uniqueWords:
                    uniqueWords[word] = uniqueWords[word] + 1
                # If the word is not in the dictionary, add it with a frequency of 1
                else:
                    uniqueWords[word] = 1

        # Close the input file after processing
        inputFile.close()

        # Get the list of unique words and sort them alphabetically
        wordList = list(uniqueWords.keys())
        wordList.sort()

        # Print the unique words and their frequencies
        for word in wordList:
            print(f"{word} {uniqueWords[word]}")

    except FileNotFoundError:
        # If the file is not found, display an error message
        print(f"Error: The file '{inName}' does not exist.")

# Call the main function
if __name__ == "__main__":
    main()
