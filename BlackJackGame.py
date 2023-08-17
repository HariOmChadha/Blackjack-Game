# Author: Hari Om Chadha
# This is a blackjack game


import random
import os
import time
import sys


# declares and inatializes all the global variables used in the program
amount = 0.0
betAmount = 0.0
compCardNum = []
compCardType = []
playerCardNum = []
playerCardType = []
closedType = ""
closedNum = ""
compTotal = 0
playerTotal = 0
tempTotal = 0


# method to welcome the user. This only runs once
def start():
    os.system('cls||clear')
    print("""
Welcome to the best Casino in town!!
""")
    global amount
    amount = totalAmount()
    print("""
We only have one game right now so get ready to lose all your money. 


Welcome to...

$$$$$$$\\  $$\\        $$$$$$\\   $$$$$$\\  $$\\   $$\\   $$$$$\\  $$$$$$\\   $$$$$$\\  $$\\   $$\\ 
$$  __$$\\ $$ |      $$  __$$\\ $$  __$$\\ $$ | $$  |  \\__$$ |$$  __$$\\ $$  __$$\\ $$ | $$  |
$$ |  $$ |$$ |      $$ /  $$ |$$ /  \__|$$ |$$  /      $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$$$$$$\\ |$$ |      $$$$$$$$ |$$ |      $$$$$  /       $$ |$$$$$$$$ |$$ |      $$$$$  /  
$$  __$$\\ $$ |      $$  __$$ |$$ |      $$  $$<  $$\\   $$ |$$  __$$ |$$ |      $$  $$<   
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$\\ $$ |\\$$\\ $$ |  $$ |$$ |  $$ |$$ |  $$\\ $$ |\\$$\\  
$$$$$$$  |$$$$$$$$\\ $$ |  $$ |\\$$$$$$  |$$ | \\$$\\\\$$$$$$  |$$ |  $$ |\\$$$$$$  |$$ | \\$$\\ 
\\_______/ \\________|\\__|  \\__| \\______/ \\__|  \\__|\\______/ \\__|  \\__| \\______/ \\__|  \\__|
""")
    main()
    return


# asks the user for the amount they want to start with. Recursive if invalid input
def totalAmount():
    try:
        amount = float(input("How much money would you like to start with today??\n"))
    except:
        print("That's not a number")
        amount = totalAmount()
    if amount < 1:
        print("You cannot start with less than 1 dollar.")
        amount = totalAmount()
    return amount


# Adds money to the player's account. Recurssive if the input is invalid.
def addMoney():
    global amount
    choice = input("Would you like to add more money to your account or not? (Y/N)\n")
    if choice.lower() == "y":
        try: 
            print(f"You currently have ${amount:.2f}")
            value = float(input("How much money would you like to add to your account?\n"))
            if value < 0:
                print("That is not a valid amount")
                addMoney()
            else:
                amount += value
                print(f"The total money in your account is ${amount:.2f}")
        except:
            print("That is not a valid amount")
            addMoney()
    elif choice.lower() == "n":
        return
    else:
        print("That's not a yes or a no.")
        addMoney()
    return


# asks the user how much they want to bet. Recursive if invalid input
def bet():
    global amount
    betAmount = 0.0
    try:
        betAmount = float(input("\nHow much would you like to bet?\n"))
    except:
        print("That's not a number. Please try again")
        betAmount = bet()
    if betAmount > amount:
        print("You can't bet money you don't have.")
        addMoney()
        betAmount = bet()
    elif betAmount <= 0:
        print("You can't bet negative money!")
        betAmount = bet()
    return betAmount


# generates a random card and returns the card number and the type
def randomCard():
    kind = random.choice(["♣","♠","❤","❖"])
    number = str(random.randrange(1,14))
    if number == "1":
        number = "A"
    if number == "11":
        number = "J"
    if number == "12":
        number = "Q"
    if number == "13":
        number = "K"
    return kind, number


# creates the first four cards that are dealt. Puts the information in lists to be used when printing the cards
def create():
    global compCardNum
    global compCardType
    global compCardNum
    global compCardType
    global closedType
    global closedNum
    a,b = randomCard()
    compCardType.append(a)
    compCardNum.append(b)
    compCardType.append("?")
    compCardNum.append("?")
    closedType, closedNum = randomCard()
    for i in range (2):
        a,b = randomCard()
        playerCardType.append(a)
        playerCardNum.append(b)
    return


# Calls the methods to print the cards and to calculate the total
def printCards():
    printDealerCards()
    calcCompTotal(compCardNum)
    time.sleep(2)
    printPlayerCards()
    calcPlayerTotal(playerCardNum)
    time.sleep(2)
    return


# prints the dealer's cards using a LOT of loops (ASCII Art)
def printDealerCards():
    for i in range (30):
        print("\n")
    print("\n\nDealer's Hand:")
    time.sleep(1)
    for i in range (len(compCardType)):
        print(" ______________   ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(compCardType)):
        if compCardNum[i] == "10":
            print(f"| {compCardNum[i]}         {compCardType[i]} |  ", end = "")
        else:
            print(f"| {compCardNum[i]}          {compCardType[i]} |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print(f"|       {compCardType[i]}      |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(compCardType)):
        if compCardNum[i] == "10":
            print(f"| {compCardType[i]}         {compCardNum[i]} |  ", end = "")
        else:
            print(f"| {compCardType[i]}          {compCardNum[i]} |  ", end = "")
    print()
    for i in range (len(compCardType)):
        print("|______________|  ", end = "")    
    print()
    return


# prints the players cards using a LOT of loops (ASCII Art)
def printPlayerCards():
    print("\n\nYour Hand:")
    time.sleep(1)
    for i in range (len(playerCardType)):
        print(" ______________   ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        if playerCardNum[i] == "10":
            print(f"| {playerCardNum[i]}         {playerCardType[i]} |  ", end = "")
        else:
            print(f"| {playerCardNum[i]}          {playerCardType[i]} |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print(f"|       {playerCardType[i]}      |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|              |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        if playerCardNum[i] == "10":
            print(f"| {playerCardType[i]}         {playerCardNum[i]} |  ", end = "")
        else:
            print(f"| {playerCardType[i]}          {playerCardNum[i]} |  ", end = "")
    print()
    for i in range (len(playerCardType)):
        print("|______________|  ", end = "")    
    print()
    return


# calculates the total for the dealers cards and prints it out. Prints out both the totals if there is an ace (both totals are below 21).
# the total is calculated everytime because aces can be 1 or 11 based on the rest of the cards
# the 'tempTotal' variable saves the lowest possible total (used in deciding whether to hit or hold). 
def calcCompTotal(a):
    global compTotal
    global tempTotal
    total1 = 0
    total2 = 0
    aceCount = 0
    for i in range(len(a)):
        if a[i] == "A":
            aceCount +=1
    for i in range(len(a)):
        try:
            total1 += int(a[i])
            total2 += int(a[i])
        except:
            if a[i] == "J" or a[i] == "Q" or a[i] == "K":
                total1 += 10
                total2 += 10
            elif a[i] == "A":
                if aceCount > 1:
                    total1 += 1
                    total2 += 1
                    aceCount -= 1
                else:
                    total1 += 1
                    total2 += 11
    for i in range (len(a)):
        if a[i] == "A":
            if total2 > 0 and total2 < 22:
                print(f"\nTotal = {total1} OR {total2} ")
                tempTotal = total1
                compTotal = total2
                return
    print(f"\nTotal = {total1}")
    tempTotal = total1
    compTotal = total1
    return


# calculates the total for the player's cards and prints it out. Prints out both the totals is there is and ace (both totals are below 21).
# the total is calculated everytime because aces can be 1 or 11 based on the rest of the cards
def calcPlayerTotal(a):
    global playerTotal
    total1 = 0
    total2 = 0
    aceCount = 0
    for i in range(len(a)):
        if a[i] == "A":
            aceCount +=1
    for i in range(len(a)):
        try:
            total1 += int(a[i])
            total2 += int(a[i])
        except:
            if a[i] == "J" or a[i] == "Q" or a[i] == "K":
                total1 += 10
                total2 += 10
            elif a[i] == "A":
                if aceCount > 1:
                    total1 += 1
                    total2 += 1
                    aceCount -= 1
                else:
                    total1 += 1
                    total2 += 11
    for i in range (len(a)):
        if a[i] == "A":
            if total2 > 0 and total2 < 22:
                print(f"\nTotal = {total1} OR {total2} ")
                playerTotal = total2
                return
    print(f"\nTotal = {total1}")
    playerTotal = total1
    return


# runs right after the first four cards are printed 
# checks the dealer's closed card if the open card is an ace. Also checks if the player has a blackjack or if there's a draw
def check():
    global compCardNum
    global compCardType
    if compCardNum[0] == "A":
        print("The dealer has an ace so he is going to look at his other card...")
        time.sleep(3)
        if closedNum == "10" or closedNum == "J" or closedNum == "Q" or closedNum == "K":
            compCardType.pop(1)
            compCardNum.pop(1)
            compCardType.append(closedType)
            compCardNum.append(closedNum)
            printCards()
            if playerTotal != 21:
                print("\nThe dealer's total is 21! YOU LOSE!!")
                winORLose(False)
            else: 
                print("\nIt's a DRAW")
                draw()
        else:
            print("The dealer's cards don't add up to 21 so the game will continue as normal.")
    if playerTotal == 21:
        print("\nThat's lucky! YOU WIN!!")
        winORLose(True)
    else:
        choose()
    return


# asks the user to pick hit or hold. Recursive if the input is invalid
def choose():
    choice = input("Hit (1) or Hold/Stand (2)?\n")
    if choice == "1" or choice.lower() == "hit":
        hit(True)
    elif choice == "2" or choice.lower() == "hold" or choice.lower() == "stand":
        hold()
    else:
        print("Please type either '1' or '2'")
        choose()
    return


# generates a new random card and adds it to the appropriate lists is the player or the dealer decides to hit
# paramter to seperate between the dealer and player cards.
def hit(x):
    a,b = randomCard()
    if x:
        playerCardType.append(a)
        playerCardNum.append(b)
        printCards()
        playerWinCheck()
    else:
        compCardType.append(a)
        compCardNum.append(b)
        printCards()
    return


# Called when the  players holds. Opens the dealer's closde card and calls the hit function if it's already open but the games hasn't ended yet.
def hold():
    global compCardNum
    global compCardType
    if compCardType[1] == "?":
        compCardType.pop(1)
        compCardNum.pop(1)
        compCardType.append(closedType)
        compCardNum.append(closedNum)
        printCards()
        time.sleep(1)
        compWinCheck()
    else:
        print("\nThe dealer will open a card...")
        time.sleep(2)
        hit(False)
        time.sleep(1)
        compWinCheck()
    return


# checks if the player won or not. Called when theh player uses 'hit'
def playerWinCheck():
    if playerTotal == 21:
        print("\nThat's lucky! YOU WIN!!")
        winORLose(True)
    elif playerTotal > 21:
        print("\nYou LOSE!")
        winORLose(False)
    else:
        choose()
    return


# checks if the Dealer won or not. Called when the dealer opens the closed card or adds more cards to his pile
# decides whether the dealer should hit or not. The 'hold()' call actually means hit for the dealer
def compWinCheck():
    global tempTotal
    if compTotal > 21:
        print("\nYou WIN!")
        winORLose(True)
    elif compTotal == 21:
        print("\nYou LOSE!")
        winORLose(False)
    elif compTotal > playerTotal:
        print("\nYou LOSE!")
        winORLose(False)
    elif compTotal < 17:
        hold()
    elif compTotal <= playerTotal and tempTotal < 17:
            hold()
    elif compTotal == playerTotal:
        print("\nIt's a DRAW!")
        draw()
    else:
        print("\nYou WIN!")
        winORLose(True)
    return


# changes the balance if the player won and checks if the player had a blackjack
# player wins only if the parameter is True
def winORLose(a):
    global amount
    global betAmount
    if a:
        if playerTotal == 21:
            amount += betAmount*2
        else:
            amount += betAmount*1.5
    print(f"\nThe total money in your account is ${amount:.2f}")
    addMoney()
    again()
    return


# called if the match is a draw. Adds the amount betted back into the total balance
def draw():
    global amount
    global betAmount
    amount += betAmount
    print(f"\nThe total money in your account is ${amount:.2f}")
    addMoney()
    again()
    return


# asks the user if they want to play again. Recursive if the input is invalid
def again():
    a = input("\n\nWould you like to play again? (Y/N)\n")
    if a.lower() == "y":
        reset()
    elif a.lower() == "n":
        print("\nThanks a lot for playing with us. Please come again soon to lose all your money!")
        sys.exit()
    else:
        print("That's not a yes or a no")
        again()
    return


# resets all the global variables, except 'amount', if the player wants to play again.
def reset():
    global betAmount
    global compCardNum
    global compCardType
    global playerCardType
    global playerCardNum
    global closedType
    global closedNum
    global compTotal
    global playerTotal
    betAmount = 0.0
    compCardNum = []
    compCardType = []
    playerCardNum = []
    playerCardType = []
    closedType = ""
    closedNum = ""
    compTotal = 0
    playerTotal = 0
    main()
    return


# This is the main method that calls everything else at the start and is called again if the player wants to play again
def main():
    global betAmount
    global amount
    betAmount = bet()
    amount -= betAmount
    create()
    time.sleep(0.5)
    printCards()
    check()
    return


start()