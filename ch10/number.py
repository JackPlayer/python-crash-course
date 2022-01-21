import sys
import json

class FavoriteNumber:
    def __init__(self):
        self.FILE = "numbers.txt"
        pass

    def get_favorite_number(self) -> int:
        number_str: str = input("What is your favorite number: ")
        try:
            number = int(number_str)
        except ValueError:
            print(f"{number_str} is not a number. Exiting")
            sys.exit(-1)
        else:
            with open(self.FILE, 'a') as f:
                json.dump(number, f)
                return number
if __name__ == '__main__':
    fn = FavoriteNumber()
    fn.get_favorite_number()
