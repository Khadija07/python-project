MAX_LINES = 3    
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("what amount do you want to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("enter number greater than 0.")
        else:
            print("please enter a valid number.")
    return amount 

def number_of_lines():
    while True:
        lines = input("Enter number of lines to bet between 1 to "+ str(MAX_LINES)+"? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter number of lines between 1 to "+ str(MAX_LINES)+"? ")
        else:
            print("please enter a valid number.")
    return lines 

def bet_amount():
    while True:
        bet = input(f"Enter the amount to bet between ${MIN_BET} and ${MAX_BET}  ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"enter number of lines between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a valid number.")
    return bet 

def main():
    balance_amount = deposit()
    total_lines = number_of_lines()
    while True:
        bet = bet_amount()
        total_bet = bet * total_lines
        if total_bet > balance_amount:
            print(f"Your amount is greater than your balance of ${balance_amount}")
        else:
            break

    
    print(f"your total bet for ${bet} on {total_lines} lines is ${total_bet}.")
main()
