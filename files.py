import os

def process_and_write_file():
    """
    Reads content from a user-specified file, modifies it by converting to
    uppercase and adding a prefix, and then writes the modified content
    to a new output file. Includes robust error handling.
    """
    input_filename = input("Enter the name of the input file to read from: ")
    output_filename = input("Enter the name for the new output file: ")

    modified_lines = []

    #  Reading from the input file
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            print(f"\nSuccessfully opened '{input_filename}' for reading.")
            lines = infile.readlines()
            if not lines:
                print(f"'{input_filename}' is empty. No content to process.")
            else:
                print("Processing file content...")
                for i, line in enumerate(lines):
                    # File modification
                    # Convert line to uppercase and add a line number/prefix
                    modified_line = f"[{i + 1}] {line.strip().upper()}\n"
                    modified_lines.append(modified_line)
                print("Content processed.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please check the filename and try again.")
        return # Exit the function if the input file is not found
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'. Check file permissions.")
        return
    except IOError as e:
        print(f"An unexpected I/O error occurred while reading '{input_filename}': {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # If no content was read we don't proceed to write.
    if not modified_lines:
        print("No modified content to write to the output file.")
        return

    #  Writing to the output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(modified_lines)
        print(f"Successfully wrote modified content to '{output_filename}'.")
        print(f"You can find the new file at: {os.path.abspath(output_filename)}")
    except PermissionError:
        print(f"Error: Permission denied to write to '{output_filename}'. Check folder permissions.")
    except IOError as e:
        print(f"An I/O error occurred while writing to '{output_filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred during writing: {e}")

# Call the function to run the program
if __name__ == "__main__":
    process_and_write_file()

