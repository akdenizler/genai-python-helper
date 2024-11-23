import os

def save_to_file(data: str, filename: str):
    """
    Saves data to the specified file.

    :param data: Data to be written to the file.
    :param filename: The name of the file to write to.
    """
    with open(filename, "a") as file:
        file.write(data + "\n")

def read_from_file(filename: str) -> str:
    """
    Reads and returns the contents of the specified file.

    :param filename: The name of the file to read from.
    :return: The content of the file as a string.
    """
    if not os.path.exists(filename):
        return "No data found."
    with open(filename, "r") as file:
        return file.read()
