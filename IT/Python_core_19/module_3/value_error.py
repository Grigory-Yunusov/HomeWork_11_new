# чому цей скріпт не опрацьовує ValueError?:

while True:
    pool = 1000
    quantity = input("Enter the number of mailings, Q for exit: ")
    if quantity == "Q":
        break
    try:
        quantity = int(quantity)
    except ValueError:
        print("The sign you've entered is not a number")
        continue
    try:
        chunk = pool // quantity
    except ZeroDivisionError:
        print("The number can not be 0")
    else:
        print(f"The number of available malings per person is: {chunk}")

print("Have a nice day")
