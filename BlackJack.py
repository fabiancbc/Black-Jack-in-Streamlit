

#BlackJack Beta Version in Streamlit
import random
import streamlit as st




st.set_page_config(page_title="BlackJack Beta Version",page_icon=":game_die:", layout="centered")
# "st.session_state object:", st.session_state

st.title(":blue[Welcome to The BlackJack Simulator]")
st.text("""This blackJack is inspired in Las Vegas BlackJack 
As this program measures the probability of winning single hands, there in no 
    option to double or split
This is a single player simulator
    Rules: 
        1. If dealer's first 2 cards add up to 21 and user's first 2 cards add up
            to 21, it's a push (tie).
        2. If dealer's first 2 cards add up to 21 and user's first 2 cards don't
            add up to 21, dealer automatically wins.
        3. If user gets more than 21, it a bust and dealer automatically wins.
        4. If user's cards add up to 21 or less then dealer has to hit until
            reaches at least 17.
        5. If dealer has 17 or more, must stand.
    
    User's Instructions:
        1. Enter the number of decks you want to play with.
        2. Enter number of simulations (the more simulation, the more accurate).
        3. Enter position of cutting card in form of fractional percentage 
            (Cutting card is where the dealer will stop and re-shuffle the 
             decks so no counting cards happens in casinos)
        4. Enter for each possible scenario where you want to stop the simulator
            to hit. (Deffault values are provided and is the most recommended 
            strategy regarding to 
            https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/b/Blackjack.htm)
        """)

def shuffle_cards(sets):
    shoe = []
    for i in range(14):
        for j in range(sets*4):
            if i != 0:
                shoe.append(i+1)
    return shoe



def int_to_card(lis):
    # Replace each None with the correct values

    card1 = random.choice(lis)
    lis.remove(card1)
    # print(lis)
    if card1 == 10:
        value1 = 10
        card1 = "10"
    elif card1 == 11:
        value1 = 10
        card1 = "J"
    elif card1 == 12:
        value1 = 10
        card1 = "Q"
    elif card1 == 13:
        value1 = 10
        card1 = "K"
    elif card1 == 14:
        value1 = 11
        card1 = "A"
    else:
        value1 = card1
        card1 = f"{card1}"

    return card1, value1




def deal_hand_player(player_name,lis):
    funct = int_to_card(lis)
    card1 = funct[0]
    total1 = funct[1]
    funct2 = int_to_card(lis)
    card2 = funct2[0]
    total2 = funct2[1]
    total = total1 + total2
    if total == 22:
        total1 = 1
        total = 12

    # print(f"{player_name} was dealt ({card1},{card2}): a value of {total}!")
    return [total, card1, card2,total1,total2]



def one_hand_blackjack_simulator():
    dealer = deal_hand_player("Dealer",lis)
    dealer_deck = [dealer[3],dealer[4]]
    player = deal_hand_player("Player",lis)
    player_deck = [player[3],player[4]]
    player_total = player[0]
    if dealer[0] == 21 and player_total != 21:

        return "Dealer"
    elif dealer[0] == 21 and player_total == 21:

        return "Push"
    elif dealer[0] != 21 and player_total == 21:

        return "Player"

    while player_total < 21:
        if dealer[3] == 2:
            if player_total < if_2:
                pass
            else:
                break
        elif dealer[3] == 3:
            if player_total < if_3:
                pass
            else:
                break
        elif dealer[3] == 4:
            if player_total < if_4:
                pass
            else:
                break
        elif dealer[3] == 5:
            if player_total < if_5:
                pass
            else:
                break
        elif dealer[3] == 6:
            if player_total < if_6:
                pass
            else:
                break
        elif dealer[3] == 7:
            if player_total < if_7:
                pass
            else:
                break
        elif dealer[3] == 8:
            if player_total < if_8:
                pass
            else:
                break
        elif dealer[3] == 9:
            if player_total < if_9:
                pass
            else:
                break
        elif dealer[3] == 10:
            if player_total < if_10:
                pass
            else:
                break
        elif dealer[1] == "A":
            if player_total < if_A:
                pass
            else:
                break

        player_hit = int_to_card(lis)
        player_deck.append(player_hit[1])
        player_total += player_hit[1]

        if player_total > 21:
            for i in range(len(player_deck)):
                if player_deck[i] == 11:
                    player_total -= 10
                    player_deck[i] = 1
                if player_total < 22:
                    break



    partial = dealer[0]
    while partial < 17 and player_total < 21:
        functd = int_to_card(lis)
        dealer_deck.append(functd[1])
        partial += functd[1]
        if partial > 21:

            for i in range(len(dealer_deck)):
                if dealer_deck[i] == 11:
                    partial -= 10
                    dealer_deck[i] = 1
                if partial < 22:
                    break

    if partial > player_total:
        if partial > 21:
            return "Player"
        else:
            return "Dealer"
    elif player_total > partial:
        if player_total > 21:
            return "Dealer"
        else:
            return "Player"
    else:
        return "Push"

st.write("---")
decks = st.number_input("Enter number of decks: ", min_value = 1, step = 1, value = 6)
number_of_games = st.number_input("Enter number of simulations: ", min_value = 1, step = 1, value = 100000)
card_cut = st.number_input("Enter where in the shoe the cut card is positioned (enter number between greater than 0.2 and less than 1): ", min_value = 0.2, max_value = 0.99, step = 0.01, value = 0.5)
# If dealer get the followings, hit until get which number
if_2 = st.number_input("If dealer gets 2 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 13)
if_3 = st.number_input("If dealer gets 3 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 13)
if_4 = st.number_input("If dealer gets 4 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 12)
if_5 = st.number_input("If dealer gets 5 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 12)
if_6 = st.number_input("If dealer gets 6 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 12)
if_7 = st.number_input("If dealer gets 7 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 17)
if_8 = st.number_input("If dealer gets 8 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 17)
if_9 = st.number_input("If dealer gets 9 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 17)
if_10 = st.number_input("If dealer gets 10 hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 17)
if_A = st.number_input("If dealer gets A hit until you reach: ", min_value = 2, max_value = 21, step = 1, value = 17)
count_player = 0
count_dealer = 0
count_push = 0
for i in range(number_of_games):
    if i == 0:
        lis = shuffle_cards(decks)
    elif len(lis) <= decks*52*card_cut:
        lis = shuffle_cards(decks)
    result = (one_hand_blackjack_simulator())
    if result == "Player":
        count_player += 1
    elif result == "Dealer":
        count_dealer += 1
    else:
        count_push += 1
st.write(f"Player won {count_player}, lost {count_dealer} and pushed {count_push} hands. Just won {count_player*100/number_of_games}% of the games")

    


