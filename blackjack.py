import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# start = input("if you want to play the game type 'y' or 'n'\n")
# user = []
# comp = []
# userscore = -1
# compscore = -1
# if start == "y":
#     u1 =list(random.sample(cards, 2))
#     c1 =list(random.sample(cards, 2))
#     user.append(u1)
#     comp.append(c1)
# u = user[0][0] + user[0][1]
# c = comp[0][0] + comp[0][1]
# print(f"your cards = {user}, your current score  = {u}")
# print(f"computer first card  = {comp[0][0]}")
# if u >c:
#     print("you win")
# else:
#     print("you lose ")


def select():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def scorecal(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(uscore, cscore):
    if uscore == cscore or cscore == uscore:
        print ("match is drawn")
    elif cscore == 0:
        return "computer wins it has a black jack"
    elif uscore == 0:
        return "you wins you have a blackjack"
    elif uscore > 21:
        return "your sore is over 21 you had lost the game"
    elif cscore > 21:
        return "you win computer's score os over then 21"
    elif uscore > cscore:
        return "you win "
    elif cscore > uscore:
        return "you lose"

def playgame():
    user_card = []
    comp_card = []
    usr_scr = 0
    com_scr = 0
    gameisover = False
    for i in range(2):
        user_card.append(select)
        comp_card.append(select)
    while not gameisover:
        usr_scr = scorecal(user_card)
        com_scr = scorecal(comp_card)