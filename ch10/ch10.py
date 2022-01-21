""" Chapter 10 - Exceptions and Files"""

FILE_NAME = "python.txt"


def read_file():
    with open(FILE_NAME) as file:
        for idx, line in enumerate(file):
            print(f"Topic {idx}: {line}")


def replace_language(new_language: str):
    with open(FILE_NAME) as file:
        for idx, line in enumerate(file):
            print(f"Topic {idx}: {line.replace('Python', new_language)}")


if __name__ == "__main__":
    read_file()
    replace_language("C")
