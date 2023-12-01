#!/usr/bin/python3
# Check if the script is being run as the main program
if __name__ == "__main__":
    import sys

    # Extract the command line arguments (excluding the script name)
    args = sys.argv[1:]

    # Convert arguments to integers and sum them
    result = sum(int(arg) for arg in args)

    # Print the result followed by a new line
    print(result)
