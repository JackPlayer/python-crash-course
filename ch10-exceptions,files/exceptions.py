def two_adder():
    num1 = input("First number: ")
    num2 = input("Second number: ")

    try:
        num1_int = int(num1)
        num2_int = int(num2)
    except ValueError:
        print("One of the numbers was not an integer!")
    else:
        print(f"{num1_int} + {num2_int} = {num2_int + num1_int}")


if __name__ == "__main__":
    while True:
        two_adder()
