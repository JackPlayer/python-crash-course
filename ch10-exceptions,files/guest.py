class Guest:
    def __init__(self):
        self.FILE = "guests.txt"

    @staticmethod
    def get_guest() -> str:
        guest_name: str = input("Welcome, please enter your name: ")
        return guest_name

    def write_to_guests(self, guest_name):
        with open(self.FILE, "a") as guest_book:
            guest_book.write(guest_name + "\n")


if __name__ == "__main__":
    guest: Guest = Guest()
    while True:
        new_guest: str = guest.get_guest()
        print(new_guest)
        guest.write_to_guests(guest_name=new_guest)
        print(f"Welcome {new_guest}")
