class Gutenberg:
    def __init__(self, file_name):

        try:
            with open(file_name, "r") as f:
                self.content = f.read()
        except FileNotFoundError:
            self.content = ""
            print("File could not be found")

    def get_count(self, word: str) -> int:
        if self.content == "":
            return 0
        content_list = self.content.split()
        total = 0
        for curr_word in content_list:
            if curr_word.lower() == word.lower():
                total += 1
        return total


if __name__ == "__main__":
    file: str = input("What file would you like to analyze: ")
    word_search: str = input("What word would you like to search: ")
    gutenberg: Gutenberg = Gutenberg(file)
    print(
        f"{word_search} appears {gutenberg.get_count(word_search)} times in the text."
    )
