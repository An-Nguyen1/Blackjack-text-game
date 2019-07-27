#blackjack game
#it is a random number and not a actual card
#it hand the A for your
import random
player_cards_in_hand = []
dealer_cards_in_hand = []
score = [0, 0]
game_over = False
winning = None


def check(cards_in_hand, p):
	#check if the card are Busted or a Blackjack
	global game_over
	global winning
	global score
	if score[p] == 21:
		print('Blackjack!!!')
		game_over = True
	elif score[p] > 21:
		if 'A' == cards_in_hand[-1]:
			score[p] -= 9
			print(score[p])
			if score[p] > 21:
				print('Busted!!')
				game_over = True
		else:
			print('Busted!!')
			game_over = True
			winning = False


def random_card(cards_in_hand, p):
	#pick a random number and add it to the player or dealer hand
	global score
	card = random.randint(1, 13)
	if card == 11:
		cards_in_hand.append('J')
		card -= 1
	elif card == 12:
		cards_in_hand.append('Q')
		card -= 2
	elif card == 13:
		cards_in_hand.append('K')
		card -= 3
	elif card == 1:
		cards_in_hand.append('A')
		if score[p] <= 10:
			score[p] += 10
	else:
		cards_in_hand.append(card)
	score[p] += card


def print_score(name, cards_in_hand, p):
	#print the hands and the score of the player or the dealer
	print(name + ':')
	print('card: {}		score: {}'.format(cards_in_hand, score[p]))


for i in range(2):
	#pick random number 2 time
	random_card(player_cards_in_hand, 0)
	random_card(dealer_cards_in_hand, 1)
print_score('player', player_cards_in_hand, 0)
print('dealer:')
print(dealer_cards_in_hand[0])
check(player_cards_in_hand, 0)

while game_over is False:
	h_s = input('do you want to hit or stand? ')
	if h_s == 'hit':
		random_card(player_cards_in_hand, 0)
		print_score('player', player_cards_in_hand, 0)
		check(player_cards_in_hand, 0)

	elif h_s == 'stand':
		game_over = True
	else:
		print('pls type hit or stand')
while score[1] < 17 and score[0] != 21:
	random_card(dealer_cards_in_hand, 1)
print_score('dealer', dealer_cards_in_hand, 1)
if (score[0] > score[1] or score[1] > 21) and score[0] <= 21:
	print('you win!!!!')
elif score[0] == score[1]:
	print('tie')
else:
	print('you lose')
