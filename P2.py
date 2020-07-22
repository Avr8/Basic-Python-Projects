import random
suits=['clubs','spades','hearts','diamonds']
num=[]
for i in range(1,14):
    num.append(i)
#creating_deck_of_cards
deck=[]
def deck_cards():
    for i in num:
        for j in suits:
            card=[i,j]
            deck.append(card)
deck_cards()
#distribution_to_player
p1=[]
p2=[]
def divide_cards():    
    while len(deck) != 0: 
        random.shuffle(deck)
        p1.append(deck.pop())
        random.shuffle(deck)
        p2.append(deck.pop())
divide_cards()
print("Welcome! Let's start the game..")
print("Your Deck has been divided!")
#game_start
def game_on():
    x=0
    flag=0
    random.shuffle(p1)
    random.shuffle(p2)
    while flag==0:
        x+=1
        print("Round {}".format(x)) 
        save_p1=[]
        save_p2=[]
        a1=0     
        a1=input("Player 1 press '1' to pick  card" )        
        card1=[]
        card1.append(p1.pop(0))
        a2=0
        a2=input("Player 2 press '2' to pick  card" )
        card2=[]
        card2.append(p2.pop(0))
        print(card1)
        print(card2)
        if card1[0][0]==1 and card2[0][0] != 1:
            print("Player 1 wins Round {}".format(x))
            p2.append(card1[0])
            if len(save_p1) != 0:
                p2.append(save_p1)
                save_p1.clear()
        elif card2[0][0]==1 and card1[0][0] != 1:
            print("Player 2 wins Round {}".format(x))
            p1.append(card2[0])
            if len(save_p2) != 0:
                p1.append(save_p2)
                save_p2.clear()
        elif card2[0][0]>card1[0][0]:
            print("Player 2 wins Round {}".format(x))
            p1.append(card2[0])
            if len(save_p2) != 0:
                p1.append(save_p2)
                save_p2.clear()
        elif card1[0][0]>card2[0][0]:
            print("Player 1 wins Round {}".format(x))
            p2.append(card1[0])
            if len(save_p1) != 0:
                p2.append(save_p1)
                save_p1.clear()
        else:
            print("Both Player have same value cards..")
            save_p1.append(card1[0])
            save_p2.append(card2[0])            
        if len(p1)==0 or len(p2)==0:
            flag=1    
    print("Game End!")
    if len(p1)==0:
        print("Player 1 Won!")
    else:
        print("Player 2 Won!")
game_on()
                





    

