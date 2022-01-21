class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type

    def describe(self):
        print(f"{self.name} serves {self.cuisine} food.")

    def open(self):
        print(f"The restaurant {self.name} is now open!")


if __name__ == "__main__":
    italian = Restaurant("Pagliacci's", "Italian")
    japaneese = Restaurant("Konichiwa", "Sushi")
    american = Restaurant("Burger Bob", "American")

    american.describe()
