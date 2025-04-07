def read_and_modify_file():
    import os

    # Function to read, modify and write file
    def process_file(input_filename, output_filename, modification_function):
        try:
            with open(input_filename, 'r') as input_file:
                file_content = input_file.read()
        except FileNotFoundError:
            print(f"Error: File '{input_filename}' does not exist.")
            return
        except PermissionError:
            print(f"Error: Insufficient permissions to read file '{input_filename}'.")
            return
        except Exception as e:
            print(f"Error: An unexpected issue occurred while reading the file: {e}.")
            return

        # Apply modification function
        modified_content = modification_function(file_content)

        # Write to new file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
        except OSError:
            print(f"Error: Unable to create or write to file '{output_filename}'.")
        else:
            print(f"File '{output_filename}' has been created with modified content.")

    # Function to remove comments as an example modification
    def remove_comments(content):
        return '\n'.join(line for line in content.split('\n') if not line.startswith('#'))

    # Get the input and output filenames from the user
    while True:
        input_filename = input("Enter the input file name: ")
        try:
            os.path.exists(input_filename)
        except Exception as e:
            print(f"Error: {e}. Please check your file name or path.")
            continue
        break

    while True:
        output_filename = input("Enter the output file name: ")
        try:
            if os.path.exists(output_filename):
                print("File already exists. Overwrite (y/n)? ")
                overwrite = input().lower().strip()
                if overwrite != 'y':
                    print("Operation cancelled.")
                    exit(1)
            else:
                break
        except Exception as e:
            print(f"Error: {e}. Please check your output file name or path.")
            continue

    # Ask for a modification function (example: removing comments)
    while True:
        modification_function_name = input("Enter 'remove_comments' to remove comments, or a function you've defined: ")
        if modification_function_name == 'remove_comments':
            modification_function = remove_comments
        else:
            try:
                modification_function = eval(modification_function_name)
            except Exception as e:
                print(f"Error: Invalid function name. Make sure to enter a valid function: {e}.")
                continue
            else:
                break

    process_file(input_filename, output_filename, modification_function)

    print("\nOperation completed. Check your output file.")

# Run the program
read_and_modify_file()
