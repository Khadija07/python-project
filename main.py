import random

MAX_LINES = 3    
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 4,
    "C" : 5,
    "D" : 6
   

}

#generate items in slot machine

def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  #coping the values to current_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) - 1:
                print(column[row], end = " | ")   
            else:
                print(column[row], end = "")

        print()  #takes to the next line


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

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
main()
