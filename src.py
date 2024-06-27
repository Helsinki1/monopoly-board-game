import random as r
import pandas as pd
import matplotlib.pyplot as plt

numPlayers = int(input("How many players are there? "))
if numPlayers < 2 or numPlayers > 6:
  print("error, this game only accepts 2 to 6 players. Please re-run the program and enter an acceptable number of players")
  numPlayers = ''
players = []
player = ''
for i in range(numPlayers):
  player = str(input("Please enter the name of a player "))
  players.append(player)

money = []
for i in players:
  money.append(1500)

spots = []
for i in players:    
  spots.append(0)

inJail = []
for i in players:
  inJail.append("no")

playerDict = {
  'players' : players,
  'money' : money,
  'place on board': spots,
  'in jail?' : inJail
  }

def showDataFrame():
  playerDict = {
      'players' : players,
      'money' : money,
      'place on board': spots,
      'in jail?' : inJail
      }
  display(pd.DataFrame(playerDict))

def plot():
  fig, ax = plt.subplots()  # board
  ax.plot([0,11,11,0,0], [0,0,22,22,0], color = 'black')
  ax.plot([1,10,10,1,1], [2,2,20,20,2], color = 'black')
  for i in range(1,11):
    ax.plot([i,i], [0,2], color = 'black')
  for i in range(1,11):
    ax.plot([i,i], [22,20], color = 'black')
  for i in range(2,23,2):
    ax.plot([0,1], [i,i], color = 'black')
  for i in range(2,23,2):
    ax.plot([10,11], [i,i], color = 'black')

  for i in range(len(spots)):
    if inJail[i] == 'yes':
      spots[i] = 10
    if spots[i] >= 0 and spots[i] < 10:
      if i < 3:
        plt.scatter(0.2 + i/4, 0.5 + 2*spots[i], label = players[i])
      if i >= 3:
        plt.scatter(0.2 + i/4 - 3/4, 1.5 + 2*spots[i], label = players[i])
    elif spots[i] >= 10 and spots[i] < 20:
      if i < 3:
        plt.scatter(0.2 + spots[i] - 10 + i/4, 20.5, label = players[i])
      if i >= 3:
        plt.scatter(0.2 + spots[i] - 11 + i/4 - 3/4, 21.5, label = players[i])
    elif spots[i] >= 20 and spots[i] < 31:
      if i < 3:
        plt.scatter(10.2 + i/4, 20.5 - 2*(spots[i] - 20), label = players[i])
      if i >= 3:
        plt.scatter(10.2 + i/4 - 3/4, 21.5 - 2*(spots[i] - 20), label = players[i])
    elif spots[i] >= 31 and spots[i] <= 39:
      if i < 3:
        plt.scatter(10.2 + i/4 - (spots[i] - 30), 0.5, label = players[i])
      if i >= 3:
        plt.scatter(10.2 + i/4 - 3/4 - (spots[i] - 30), 1.5, label = players[i])
  ax.legend()
  plt.show()
  ax.clear()

#starting plot
plot()

potMoney = 0                                                               


def payPlayer(amount, playerfrom, playerto):
  x = players.index(playerfrom)
  y = players.index(playerto)
  money[x] -= amount
  money[y] += amount
  print(f"{playerfrom} has paid {playerto} {amount} dollars")

def bankPaysDividend(playerName):
  x = players.index(playerName)
  if money[x] > 0:
    money[x] += 50
    print(f"{playerName} has received 50$ dividend from the bank! (Chance Card)")
    showDataFrame()

def goToJail(playerName):
  x = players.index(playerName)
  if money[x] > 0:
    inJail[x] = 'yes'
    print(f"{playerName} has been sent to jail. (Chance Card)")
    showDataFrame()
    plot()

def getOutOfJail(playerName):
  x = players.index(playerName)
  if inJail[x] == 'yes':
    inJail[x] = 'no'
    print(f"{playerName} gotten out of jail for free. (Chance Card)")
    showDataFrame()
    plot()
  else:
    print(f"{playerName} has received a -get out of jail free card- but they are not in jail. (Chance Card)")

def poorTax(playerName):
  x = players.index(playerName)
  if money[x] > 0:
    money[x] -= 15
    print(f"{playerName} has been taxed 15$. (Chance Card)")
    potMoney += 15
    showDataFrame()

def loansMature(playerName):
  x = players.index(playerName)
  if money[x] > 0:
    money[x] += 150
    print(f"{playerName}'s loans have matured and {playerName} received 150$. (Chance Card)")
    showDataFrame()

def advanceGo(playerName):
  x = players.index(playerName)
  if money[x] > 0:
    spots = 0
    showDataFrame()
    plot()
    print(f"{playerName} advanced to go! (Chance Card)")

def goBack3Places(playerName):
  x = players.index(playerName)
  if money[x] > 0:
    print(f"{playerName} has to go back 3 tiles. (Chance Card)")
    spotvalue = spots[players.index(playerName)]
    spotvalue -= 3
    spots[players.index(playerName)] = spotvalue
    showDataFrame()

def electedChairman(playerName):
  x = players.index(playerName)
  if money[x] > 0:
    for i in range(len(money)):
      money[i] += 50
    print(f"{playerName} has been elected as the Chairman of the Board. Everybody receives 50$. (Chance Card)")
    showDataFrame()

tiles = ['Go', 'Old Kent Road', 'Community Chest', 'White Chapel Road', 'Income Tax', 'Kings Cross Station', 'The Angel Islington', 'Chance', 'Euston Road', 'PentonVille Road', 'Jail', 'Pall Mall', 'Electric Company', 'White Hall', 'North Humrld Avenue', 'Marylebone Station', 'Bow Street', 'Community Chest', 'Marlborough Street', 'Vine Street', 'Free Parking', 'Strand', 'Chance', 'Fleet Street', 'Trafalger Square', 'Fenchurch St. Station', 'Leicester Square', 'Coventry Street', 'Water Works', 'Piccadilly', 'Go To Jail', 'Regent Street', 'Oxford Street', 'Community Chest', 'Bond Street', 'Liverpool St. Station', 'Chance', 'Park Lane', 'SUPER TAX', 'May Fair']
chanceCards = [bankPaysDividend, goToJail, getOutOfJail, poorTax, loansMature, advanceGo, goBack3Places, electedChairman]

def turn():
  print(f"{i} has rolled a {total}")
  spots[players.index(i)] += total 
  if spots[players.index(i)] > 39:
    spots[players.index(i)] -= 40
    print(f"{i} has landed on {tiles[spots[players.index(i)]]}")
    if spots[players.index(i)] == 0:
      print(f"{i} has landed on 'Go.' They receive 400$")
      money[players.index(i)] += 400
      plot()
      showDataFrame()
    else:
      print(f"{i} has passed 'Go.' They receive 200$")
      money[players.index(i)] += 200
      plot()
      showDataFrame()
  else:
    print(f"{i} has landed on {tiles[spots[players.index(i)]]}")
    if spots[players.index(i)] == 20:
      print(f"{i} gets all the money in the pot after landing on Free Parking!")
      money[players.index(i)] += potMoney
      potMoney = 0
      showDataFrame()
    elif spots[players.index(i)] == 30:
      print(f"{i} has landed on GO TO JAIL. They are now in jail")
      inJail[players.index(i)] = 'yes'
      spots[players.index(i)] = 10
    plot()
  if tiles[spots[players.index(i)]] == "Chance":
    print(f"{i} has landed on a Chance tile.")
    a = r.randint(0,7)
    chanceCards[a](i)

gameOn = True
doublesCount = 0
jailTurnCount = 0

while gameOn:           

  for i in players:

    while 0 in money:
      print(f"{players[money.index(0)]} has gone bankrupt")
      inJail.remove(inJail[money.index(0)])
      spots.remove(spots[money.index(0)])
      players.remove(players[money.index(0)])
      money.remove(money[money.index(0)])
    if len(money) == 1:
      gameOn = False
      print(f"{players[0]} has won the game!")
      showDataFrame()
      break
  
    print(f"it is {i}'s turn")
    showDataFrame()
    if inJail[players.index(i)] == 'yes':
      x = str(input(f"{i}, would you like to pay 50$ to get out of jail? (yes/no) "))
      if x == 'yes':
        money[players.index(i)] -= 50
        potMoney += 50
        inJail[players.index(i)] = 'no'
        showDataFrame()

    x = str(input("roll your dice? (input 'ok') "))
    diceroll1 = r.randint(1,6)
    diceroll2 = r.randint(1,6)
    total = diceroll1 + diceroll2

    if diceroll1 == diceroll2 and inJail[players.index(i)] == 'yes':
      inJail[players.index(i)] == 'no'
      print(f"{i} has gotten out of jail after rolling doubles!")
      turn()
      continue

    elif diceroll1 == diceroll2 and inJail[players.index(i)] == 'no':
      while diceroll1 == diceroll2:
        if inJail[players.index(i)] == 'yes':
          inJail[players.index(i)] == 'no'
          print(f"{i} has gotten out of jail after rolling doubles!")
          turn()
          doublesCount = 0
          continue
          
        doublesCount += 1
        if doublesCount >= 3:
          inJail[players.index(i)] = "yes"
          print(f"{i} has rolled doubles three times in a row. They are now in jail")
          continue
        turn()
        print(f"{i} has rolled doubles! They can roll their dice again!")
        x = str(input("roll your dice again? (input 'ok') "))
        diceroll1 = r.randint(1,6)
        diceroll2 = r.randint(1,6)
        total = diceroll1 + diceroll2
      else:
        doublesCount = 0
        turn()
    elif inJail[players.index(i)] == 'no':
      turn()
    if inJail[players.index(i)] == 'yes':
      jailTurnCount += 1
      if jailTurnCount >= 3:
        print(f"{i}, you have been in jail for three turns! You must pay 50$ NOW and get out of jail!")
        money[players.index(i)] -= 50
        potMoney += 50
        inJail[players.index(i)] == 'no'
        turn()

    while x != '3':
      x = str(input(f"{i}, would you like to pay someone (if yes, enter 1), buy something/pay the bank? (if yes, enter 2), or end turn (if yes, enter 3)" ))      
      if x == '1':
        y = str(input("who would you like to pay? "))
        z = int(input("how much are you paying them? "))
        if z < money[players.index(i)]:
          payPlayer(z, i, y)
        else:
          print("error. If you were to pay that much, you would go bankrupt!")
      elif x == '2':
        y = int(input("how much are you paying the bank? "))
        if y < money[players.index(i)]:
          money[players.index(i)] -= y
          z = str(input("is this a property payment? (yes/no) "))
          if z == 'no':
            potMoney += y
        else:
          print("error. If you were to pay that much, you would go bankrupt!")
