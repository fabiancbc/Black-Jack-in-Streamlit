# Black Jack in Streamlit
BlackJack simulator using python and streamlit.
# Overview
Users have freedom to choose the number of decks, number of simulations, position of cutting card, and use their own strategy in order to get results such as percentage of wins, and amount of money earned or lost after a number of simulations. This simulator will also use techniques such as card counting and an automated system where after a certain amount of card counter the bet can increase or decrease in order to find the most optimum strategy and guarantee wins.

This simulators uses real world probability in order to give the most accurate results. For instance, the probability of getting a card will always change if the card was already withdrawn from the deck.

# Why Blackjack?

Blackjack has a special behaviour that makes it different from other gambling games and is that the probability of getting a card changes every times a card is pulled. Other games like roulette, poker, or dice related has a different statistical behaviour as the chances of getting any result is always the same over time (i.e for most poker tables cards are re-shuffled every game) making Blackjack a little bit more manipulative than other games.

In addion, Blackjack has another interesting feature and it is that the dealer behaves as a machine as they do not have decision in somebody's game. This makes de simulation easier to be programmed and also more predictable and accurate for a real life game.

# Installation

This code was done using Python version 3.8.10. In order for the code to work you have to make sure you have the latest version of streamlit (https://docs.streamlit.io/library/get-started/installation) and Pandas for chart generation. Once both libraries are downloaded and added to your environment, make sure that the pages folder is included in the directory where the main page is located (otherwise these pages will not show up when you launch the code). Once the pages folder is in your directory, open the main code, run it, and then open the command prompt from the directory and write "Streamlit run BlackJack.py". If you change the name of the main code just change BlackJack.py with the name of the folder.

After following these steps. copy and paste the URL of the local host that Streamlit assigned you and enjoy the program.
