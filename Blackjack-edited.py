# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 10:55:59 2016

@author: Geetha Yedida
"""

import sys
import random
import re


class DeckOfCards(object):
    suits = ['club', 'diamond', 'heart', 'spade']
    cards = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']

    def deck(self):
        deck = []
        for suit in self.suits:
            for card in self.cards:
                deck.append(suit+"-" + str(card))
        return deck

class Hand(DeckOfCards):

    def printfirstcards(self, user_type=None):
        if user_type is None:
            user_cards = []
            cards_deck = DeckOfCards().deck()
            print "Your Card: "
            for i in range(2):
                card = random.choice(cards_deck)
                user_cards.append(card)
            for card in user_cards:
                print card
            return user_cards
        elif user_type == "dealer":
            dealer_cards = []
            cards_deck = DeckOfCards().deck()
            print "Dealers Card: "
            for i in range(1):
                card = random.choice(cards_deck)
                dealer_cards.append(card)
            for card in dealer_cards:
                print card
            return dealer_cards

    def printincrementcards(self, cards):
        cards_deck = DeckOfCards().deck()
        rcard = random.choice(cards_deck)
        cards.append(rcard)
        for card in cards:
            print card
        return cards


class DetermineSum(Hand):

    def getcardsum(self,given_cards):
        cards_sum = 0
        ace_count = 0
        for card in given_cards:
            r = re.findall('\w+-(\w+)',card)
            try:
                value = map(int, r)
                cards_sum += value[0]
            except:
                if r[0] == "ace":
                    ace_count += 1
                    cards_sum += 11
                else:
                    cards_sum += 10

        if cards_sum > 21:
            for i in range(ace_count):
                cards_sum -= 11
                cards_sum += 1
                if cards_sum <= 21:
                    break
            return cards_sum
        else:
            return cards_sum

class Pack():

    def getuseramount(self):
        try:
            tot_amount = int(raw_input("Enter your total amount: "))
            return tot_amount
        except:
            print "Enter amount in integers"
            sys.exit()

    def getbetamount(self):
        try:
            bet_amnt = int(raw_input("Enter your bet amount: "))
            return bet_amnt

        except:
            print "Enter amount in integers"

    def validatebetamount(self,total, bet):
        try:
            if bet > 0 & bet <= total & total >= 5 & total <= 500:
                han = Hand()
                user_cards = han.printfirstcards()
                user_sum = DetermineSum().getcardsum(user_cards)
                print "Your sum is: ", user_sum
                Pack().dealercard(user_cards,user_sum,total,bet)
            else:
                print "Enter greater than zero, <= total amount and total amount must be greater than or equal to 5"
                bet_amount = Pack().getbetamount()
        except:
            sys.exit()

    def dealercard(self,user_cards,user_sum,total,bet):
        dealer_cards = Hand().printfirstcards("dealer")
        Pack().getuseroption(dealer_cards,user_cards,user_sum,total,bet)

    def getuseroption(self,dealer_cards,user_cards,user_sum,total,bet):
        option = raw_input("Enter one option: \"Stand\" or \"Hit\": ")
        if option.lower() == "stand":
            print "Dealer cards are: "
            dealer_cards = Hand().printincrementcards(dealer_cards)
            dealer_sum = DetermineSum().getcardsum(dealer_cards)
            print "Your sum is: ",user_sum
            print "Dealer sum is: ", dealer_sum
            if user_sum > dealer_sum:
                print "You Won!!"
                total = total + bet
                print "Your current balance is $%d" % total
                Pack().nextgame(total)
            elif dealer_sum > user_sum:
                print "You lost :("
                total = total - bet
                print "Your current balance is $%d" %total
                Pack().nextgame(total)
            elif dealer_sum == user_sum:
                print "Nobody Wins!!!"
                Pack().nextgame(total)
        elif option.lower() == "hit":
            print "Your cards are now: "
            user_cards = Hand().printincrementcards(user_cards)
            user_sum = DetermineSum().getcardsum(user_cards)
            print "User Sum is: ",user_sum
            if user_sum > 21:
                print "Sorry. You lost. that's a bust! :("
                total = total - bet
                print "Your current balance is $%d" %total
                Pack().nextgame(total)
            else:
                self.getuseroption(dealer_cards, user_cards, user_sum, total, bet)
                print user_sum
        else:
            print "Invalid Choice Please try again"
            Pack.getuseroption(dealer_cards,user_cards)

    def nextgame(self,total):
        if total > 5:
            print "total",total
            decision = raw_input("Do you want to play another game? Type YES or NO: ")
            if decision.lower() == "yes":
                bet = Pack().getbetamount()
                print bet
                Pack.validatebetamount(self,total, bet)
            elif decision.lower() == "no":
                print "Thank you for playing Blackjack!"
            else:
                print "Invalid Choice"
        else:
            print "Thank you for playing today."


def main():
    pack_cards = Pack()
    total_amount = pack_cards.getuseramount()
    bet_amount = pack_cards.getbetamount()
    pack_cards.validatebetamount(total_amount, bet_amount)


if __name__ == '__main__':
    main()