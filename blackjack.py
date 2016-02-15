# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 10:55:59 2016

@author: Geetha Yedida
"""

import random
import re
import sys

class deckofcards(object):
    suits = ['club', 'diamond', 'heart', 'spade']
    cards = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
    
    def deck(self):
        deck = []
        for suit in self.suits:
            for card in self.cards:
                deck.append(suit+"-" +str(card))
        return deck

class cards(deckofcards):   
    usercards = []
    dealercards = []
    def playercards(self,deck,usercards):
        for i in range(2):
            card = random.choice(deck)
            usercards.append(card)
    def drawsinglecarddealer(self,deck,dealercards):
        for i in range(1):
            card = random.choice(deck)
            dealercards.append(card)
    
    def drawsinglecarduser(self,deck,usercards):
        for i in range(1):
            card = random.choice(deck)
            usercards.append(card)
 
def main():
    cds = deckofcards()
    car = cards()
    dk = cds.deck()
    usercards = []
    dealercards = []
    usercardvalues = []     
    dealercardvalues = []
    
      
    def getuseramount():
        try:
            total_amount = int(raw_input("Enter your total amount: "))
            return total_amount
        except:
            print "Enter amount in integers"
            sys.exit()
        
    def getbetamount():
        try:
            bet_amount = int(raw_input("Enter your bet amount: "))
            return bet_amount
        except:
            print "Enter amount in integers"
    
    def printusercards():
        for card in usercards:
                print card
    
    def printdealercards():
        for card in dealercards:
                print card
       
    def playgame(total_amount, bet_amount):
        d_sum = 0
        us_sum = 0
        try:
            if bet_amount > 0 and bet_amount <= total_amount and total_amount >= 5 and total_amount <= 500:
                print "Your Cards: "
                car.playercards(dk,usercards)
                printusercards()
                user_sum = determineusersum(usercards,us_sum)
                print "The sum of your cards is: %d" %user_sum
                print "Dealer Card is: "
                car.drawsinglecarddealer(dk,dealercards)    
                printdealercards()
                dealer_sum = determinedealersum(dealercards,d_sum)
                getuseroption(user_sum,dealer_sum,total_amount,bet_amount)
            else:
                print "Please enter amount greater than zero and less than total amount and total amount must be greater than 5"
                bet = getbetamount()
                playgame(total,bet)
        except:
            sys.exit()
            
        
            
    def getuseroption(user_sum,dealer_sum,total,bet):
        option = raw_input("Enter one option: \"Stand\" or \"Hit\": ")
        if option.lower() == "stand":
            print "Dealer cards are: "
            car.drawsinglecarddealer(dk,dealercards)
            printdealercards()
            dealer_sum = determinedealersum(dealercards,dealer_sum)
            print "The sum of Dealer's cards is: %d" %dealer_sum
            if user_sum > dealer_sum:
                print "You Won!!"
                total = total + bet
                print "Your current balance is %d" %total
                nextgame(total)                
                
            elif dealer_sum > user_sum:
                print "you lose :("
                total = total - bet
                print "Your current balance is %d" %total
                nextgame(total)
            
            elif dealer_sum == user_sum:
                print "Nobody Wins!!!"
                nextgame(total)
        
        elif option.lower() == "hit":
            print "With your new card, you have: "
            car.drawsinglecarduser(dk,usercards)
            printusercards()
            user_sum = determineusersum(usercards,user_sum)
            print "The sum of your cards is: %d" %user_sum
            
            if user_sum > 21:
                print "Sory. You lose. that's a bust! :("
                total = total - bet
                print "Your current balance is %d" %total
                nextgame(total)
            
            elif user_sum == 21:
                print "You won!!!"
                total = total + bet
                print "Your current balance is %d" %total
                nextgame(total)
                
            else:
                getuseroption(user_sum,dealer_sum,total,bet)
        else:
            print "Invalid Choice"
            
    def determineusersum(usercards,user_sum):
        sum_user = 0        
            # initial addition
        for card in usercards:
            r = re.findall('\w+-(\w+)',card)
#            print r
            try:
                #check for integer
                r = map(int,r)
                for i in r:
                    usercardvalues.append(i)
            except:
                if r[0] == "ace":
                    ace_value = int(raw_input("Do you want ace as 1 or 11? Enter the number: "))
                    if ace_value == 1:
                        usercardvalues.append(1)
                    elif ace_value == 11:
                        usercardvalues.append(11)
                    else:
                        print "Incorrect value. Enter again"
                        continue
                else:
                    usercardvalues.append(10)
        for i in usercardvalues:
            sum_user = sum_user + i
        del usercardvalues[:]
        
        return sum_user
                
        
    def determinedealersum(deal_cards,deal_sum):
        sum_dealer = 0
        for card in deal_cards:
            r = re.findall('\w+-(\w+)',card)
            try:
                #check for integer
                r = map(int,r)
                for i in r:
                    dealercardvalues.append(i)
            except:
                if r[0] == "ace":
                    dealercardvalues.append(11)
                else:
                    dealercardvalues.append(10)
        for i in dealercardvalues:
            sum_dealer = sum_dealer + i
        del dealercardvalues[:]
        return sum_dealer
        
        
    def nextgame(total):
        if total > 5:
            decision = raw_input("Do you want to play another game? Type YES or NO: ")
            if decision.lower() == "yes":
                del dealercards[:]
                del usercards[:]
                bet = getbetamount()
                playgame(total,bet)
            elif decision.lower() == "no":
                print "Thank you for playing Blackjack!"
            else:
                print "Invalid Choice"
        else:
            print "Thank you for playing today."
         
    def initialuseramount(total_amount):
        print "Your initial amount was: %d" %total_amount
   
    total = getuseramount()
    bet = getbetamount()
    playgame(total,bet)   
    
    
if __name__ == '__main__':
    main()