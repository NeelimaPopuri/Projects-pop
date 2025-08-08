

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100


def deposit():
    while True:
        amount = input(" Would you like to desposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            " Enter the number of lines to bet on(1-"+str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid no of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input(" What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter the bet between ${"MIN_BET"} - ${"MAX_BET"}")
        else:
            print("Please enter a number.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    total_bet = lines*bet
    bet = get_bet()
    print(
        f"You are bettting ${bet} on ${lines}lines. Total bet is equal to ${total_bet}")


main()
