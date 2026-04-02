def char_to_ascii(char):
    """
    Converts a single ASCII character to its decimal ASCII value.

    Args:
      char: A single character string.

    Returns:
      An integer representing the ASCII value of the character, or None if
      the input is not a single character.
    """
    if not isinstance(char, str) or len(char) != 1:
        print("Error: Input must be a single character string.")
        return None
    return ord(char)


def ascii_to_char(ascii_value):
    """
    Converts a decimal ASCII value to its corresponding character.

    Args:
      ascii_value: An integer representing an ASCII value.

    Returns:
      A single character string, or None if the input is not a valid ASCII value.
    """
    if not isinstance(ascii_value, int) or not (0 <= ascii_value <= 127):
        print(
            "Error: Input must be an integer between 0 and 127 (inclusive) for standard ASCII."
        )
        return None
    return chr(ascii_value)


def main():
    while True:
        print("\n--- ASCII Converter ---")
        print("1. Convert Character to ASCII Number")
        print("2. Convert ASCII Number to Character")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            char_input = input("Enter a character: ")
            ascii_num = char_to_ascii(char_input)
            if ascii_num is not None:
                print(f"The ASCII value of '{char_input}' is: {ascii_num}")
        elif choice == "2":
            try:
                num_input = int(input("Enter an ASCII number (0-127): "))
                char_output = ascii_to_char(num_input)
                if char_output is not None:
                    print(
                        f"The character for ASCII value {num_input} is: '{char_output}'"
                    )
            except ValueError:
                print("Error: Invalid input. Please enter an integer.")
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
