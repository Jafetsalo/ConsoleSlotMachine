import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#THIS IS A DICTIONARY -- If you go over C# that's what this is ;)

symbol_dictionary = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValue_dictionary = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#Ex: symbol: "A" - symbol_count: 2

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] # For every line you bet | we take the A item = first column at the line 'row' in order to compare
        for column in columns:
            symbol_to_check = column[line] #This is the B item to compare against
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

        # the character " _ " underscore is an anonymous variable in Python        

   # columns = [[], [], []] #Interior list -- looks like a [1][3] multidimensional vector to me
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #SLICE OPERATOR "[:]" when included copies data, otherwise it would hold value by reference with equals "="
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):

        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else: 
                print(column[row], end="")    
        print(end="\n")
##Uppercase variables makes them CONSTANTS

def deposit(): 
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amountValue = int(amount)
            if amountValue > 0:
                break
            else: 
                print("Amount needs to be greater than Zero 0.")
        else:
            print("Please enter an actual number like: 2, 25, 7, etc.")        
    return amountValue
 #Remember this is a indented language - indentation instead of shitty brackets

def get_bet(): 
    while True:
        amount = input("What would you like to BET on each line? $")
        if amount.isdigit():
            amountValue = int(amount)
            if MIN_BET <= amountValue <= MAX_BET:
                break
            else: 
                print(f"Bet Amount needs to be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter an actual number like: 2, 25, 7, etc.")        
    return amountValue


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        key = input("Press enter to play (q to quit).")
        if key == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

    
def spin(balance):
    lines = get_number_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enought yo bet that amount, current balance: ${balance} requested bet: $-{total_bet}")
        else:
            break


    print(f"You're betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
   # print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_dictionary)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbolValue_dictionary)
    print(f"You won ${winnings}. \n You won on lines: " , *winning_lines) #UNPACK OPERATOR "*""
    return winnings - total_bet



def get_number_lines():
    while True:
        lines = input("Enter # of lines to bet on  (1 -" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            linesValue = int(lines)
            if (1 <= linesValue <= MAX_LINES):
                break
            else: 
                print("Lines need to between 0 and " + str(MAX_LINES))
        else:
            print("Please enter an actual number like: 2, 3, 1, etc.")        
    return linesValue


main()