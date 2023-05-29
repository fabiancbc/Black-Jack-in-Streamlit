
import streamlit as st
import random 
import pandas as pd
count = 0



def shuffle_cards(sets):
    shoe = []
    for i in range(14):
        for j in range(sets*4):
            if i != 0:
                shoe.append(i+1)
    return shoe



def int_to_card(lis,hi_lo_count,grifin_ultimate_count):
    # Replace each None with the correct values

    card1 = random.choice(lis)
    lis.remove(card1)

    if card1 == 2:
        hi_lo_count.append(1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(37+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 3:
        hi_lo_count.append(1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(45+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 4:
        hi_lo_count.append(1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(52+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 5:
        hi_lo_count.append(1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(70+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 6:
        hi_lo_count.append(1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(46+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 7:
        hi_lo_count.append(0+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(27+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 8:
        hi_lo_count.append(0+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(0+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 9:
        hi_lo_count.append(0+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(-17+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
        
    if card1 == 10:
        value1 = 10
        card1 = "10"
        hi_lo_count.append(-1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(-50+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
        
    elif card1 == 11:
        value1 = 10
        card1 = "J"
        hi_lo_count.append(-1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(-50+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 12:
        value1 = 10
        card1 = "Q"
        hi_lo_count.append(-1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(-50+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 13:
        value1 = 10
        card1 = "K"
        hi_lo_count.append(-1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(-50+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    elif card1 == 14:
        value1 = 11
        card1 = "A"
        hi_lo_count.append(-1+hi_lo_count[-1])
        hi_lo_true.append(hi_lo_count[-1]/decks_remaining)
        griffin_ultimate_count.append(-60+griffin_ultimate_count[-1])
        griffin_ultimate_true.append(griffin_ultimate_count[-1]/decks_remaining)
    else:
        value1 = card1
        card1 = f"{card1}"

    return card1, value1




def deal_hand_player(player_name,lis):

    funct = int_to_card(lis,hi_lo_count,griffin_ultimate_count)
    card1 = funct[0]
    total1 = funct[1]
    funct2 = int_to_card(lis,hi_lo_count,griffin_ultimate_count)
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

        player_hit = int_to_card(lis,hi_lo_count,griffin_ultimate_count)
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
        functd = int_to_card(lis,hi_lo_count,griffin_ultimate_count)
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
    
st.title(":orange[Ultimate Strategy]")  
st.write("""The ultimate strategy combines the basic streategy (When to hit or stand)
with the Hi-Lo counting card system which basically tell the users
how to bet when they have a favorable or unfavorable true count.
When true count of -1 or less, the bet will be 0. When true 
count is 1, bet is 1.5 times original bet. When 2, 2 times original
bet. when true count 3, 2.5 times original bet. This will continue
until true count of 6 or more where be is bet times 4.
         """)   
decks = st.number_input("Enter number of decks: ", min_value = 1, step = 1, value = 6)
number_of_games = st.number_input("Enter number of simulations: ", min_value = 1, step = 1, value = 100)
card_cut = st.number_input("Enter where in the shoe the cut card is positioned (enter number between greater than 0.2 and less than 1): ", min_value = 0.2, max_value = 0.99, step = 0.01, value = 0.3)
# If dealer get the followings, hit until get which number
if_2 = 13
if_3 = 13
if_4 = 12
if_5 = 12
if_6 = 12
if_7 = 17
if_8 = 17
if_9 = 17
if_10 = 17
if_A = 17
count_player = 0
count_dealer = 0
count_push = 0


money = [1000]
money2 = [1000]

wins = [0]
losses = [0]
ties = [0]
bet = 10
bet2 = 10

if st.button("Click to start"):
    hi_lo_count = [0]
    griffin_ultimate_count = [0]
    hi_lo_true = [0]
    griffin_ultimate_true = [0]
    decks_remaining = decks
    for i in range(number_of_games):

        bet = 10
        if round(hi_lo_true[-1]) == 1:
            bet = bet*1.5
        elif round(hi_lo_true[-1]) == 2:
            bet = bet*2
        elif round(hi_lo_true[-1]) == 3:
            bet = bet * 2.5
        elif round(hi_lo_true[-1]) == 4:
            bet = bet * 3
        elif round(hi_lo_true[-1]) == 5:
            bet = bet*3.5
        elif round(hi_lo_true[-1]) >=6:
            bet = bet*4
        elif round(hi_lo_true[-1]) <= -1:
            bet = bet*0
        else:
            pass
        if i == 0:
            lis = shuffle_cards(decks)
        elif len(lis) <= decks*52*card_cut:
            lis = shuffle_cards(decks)
            griffin_ultimate_count.append(0)
            griffin_ultimate_true.append(0)
            hi_lo_true.append(0)
            hi_lo_count.append(0)
            
        decks_remaining = int((len(lis)-1)/52)+1
        result = (one_hand_blackjack_simulator())
        if result == "Player":
            count_player += 1
            wins.append(wins[-1]+1)
            losses.append(losses[-1])
            ties.append(ties[-1])
            money.append(money[-1]+bet)
            money2.append(money2[-1]+bet2)
        elif result == "Dealer":
            count_dealer += 1
            losses.append(losses[-1]+1)
            wins.append(wins[-1])
            ties.append(ties[-1])
            money.append(money[-1]-bet)
            money2.append(money2[-1]-bet2)
        else:
            count_push += 1
            ties.append(ties[-1]+1)
            wins.append(wins[-1])
            losses.append(losses[-1])
            money.append(money[-1])
            money2.append(money2[-1])



            

    dicc_keys = {"wins": wins,
               "losses": losses,
               "ties": ties}
    dicc_keys2 = {"Hi-Lo Count System": hi_lo_count,
                  "Hi-Lo True Count": hi_lo_true}
    
    dicc_keys3 = {"Griffin Ultimate Count System": griffin_ultimate_count,
                  "Griffin Ultimate True Count": griffin_ultimate_true}
    dicc_keys4 = {"Money Following Strategy" : money,
                  "Money no Strategy": money2}
    dataframe = pd.DataFrame(dicc_keys)
    counting_dataframe = pd.DataFrame(dicc_keys2)
    money_dataframe = pd.DataFrame(dicc_keys4)
    st.write(f"Player won {count_player}, lost {count_dealer} and pushed {count_push} hands. Just won {count_player*100/number_of_games}% of the games")
    st.line_chart(dataframe, width=0, height=0, use_container_width=True)
    st.line_chart(counting_dataframe, width=0, height=0, use_container_width=True)
    st.line_chart(money_dataframe, width=0, height=0, use_container_width=True)
