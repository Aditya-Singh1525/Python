def secretcode():
    actualstring = input("The words to convert to secret code:")
    print(" ")
    reversedstring = actualstring[::-1]
    print(f"Your secret code is: {reversedstring}")


while True:
    secretcode()
    ask = input("Do you want to continue? (y/N): ").lower()
    if ask != "y":
        print("Exiting...")
        break
