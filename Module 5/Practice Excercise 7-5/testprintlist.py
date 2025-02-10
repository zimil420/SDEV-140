def print_list(seq):
    """
    A recursive function that prints each element of a sequence.
    Each recursive call slices the sequence and prints the first element of that slice.
    """
    if seq:  # If the sequence is not empty
        print(f"{seq} -> {seq[0]}")  # Print the entire sequence and its first element
        print_list(seq[1:])  # Call the function recursively on the sliced list

# Test the function
test_sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # The sequence to test
print_list(test_sequence)  # Call the function with the test sequence
