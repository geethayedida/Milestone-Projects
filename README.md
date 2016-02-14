# Milestone-Projects

 This is the first milestone project in python. This project is about implementing blackjack in python.

About Blackjack: 
 In this project I am only implementing the one player version. The player plays with the dealer. 
 The dealer says who won the game. The dealer also says if there is a bust.
 The game is won if the sum of the cards is close to 21 and the dealer cards has a sum less than the player card sum
 The player goes bust if the sum of his cards is more than 21 and he loses the game.
 The card values are taken as they are for number cards. For an ace, the program asks the user for suggestion: 
 if an ace must be considered as one or as zero. For other cards, the value is 10.

This is acheived in the following steps.
1. The deck of cards is implemented using python lists.
2. The programs prompts for total money available with user
3. The program aslo prompts for the bet amount he want to play in this game.
4. Using random keyword, the cards are selected at random and shown to users. 2 user cards and one dealer card is shown.
5. The user is asked for the next step. Does he wants to Hit or Stand?
6. a. If stand is chosen, the program shows the other dealer card and says who the winner is
   b. If Hit is chosen, the program displays the next user card
     a. If the sum is greater than 21, program is terminated, as a result of bust.
     b. continues asking for user input otherwise.
7. Keeps track of the user amount and displays after each game.
