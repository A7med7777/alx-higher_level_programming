#!/usr/bin/python3
# Check if the script is being run as the main program
if __name__ == "__main__":
    import hidden_4

    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
