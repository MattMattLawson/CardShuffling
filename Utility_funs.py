import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time


# np.random.seed(12)



cardDict = {
0:  'A♠', 1:  '2♠', 2:  '3♠', 3:  '4♠', 4:  '5♠', 5:  '6♠', 6:  '7♠', 7:  '8♠', 8:  '9♠', 9:  '10♠', 10: 'J♠', 11: 'Q♠', 12: 'K♠',
13: 'A♦', 14: '2♦', 15: '3♦', 16: '4♦', 17: '5♦', 18: '6♦', 19: '7♦', 20: '8♦', 21: '9♦', 22: '10♦', 23: 'J♦', 24: 'Q♦', 25: 'K♦',
26: 'A♣', 27: '2♣', 28: '3♣', 29: '4♣', 30: '5♣', 31: '6♣', 32: '7♣', 33: '8♣', 34: '9♣', 35: '10♣', 36: 'J♣', 37: 'Q♣', 38: 'K♣',
39: 'A♥', 40: '2♥', 41: '3♥', 42: '4♥', 43: '5♥', 44: '6♥', 45: '7♥', 46: '8♥', 47: '9♥', 48: '10♥', 49: 'J♥', 50: 'Q♥', 51: 'K♥'
			}



# DONE

def CutDeck(deck):
	start = time.time()
	cutLoc = int(np.random.normal(loc=25.5,scale=2))  # mean = 25.2, std = 2
	half1 = deck[:cutLoc]
	half2 = deck[cutLoc:]
	print('Time in CutDeck: ',time.time()-start)
	return (half1, half2)


def PrintActualDeck(deck):
	start = time.time()
	# Given the list of numbers, print the order of cards
	cardSequence = ''
	for index in deck:
		cardSequence += cardDict[index] + ', '
	print(cardSequence + '\n')
	print('Time in PrintActualDeck: ',time.time()-start)
	return


def GenerateRandomDeck():
	start = time.time()
	# Generate a randomly ordered deck
	deck = np.arange(52)
	deck = np.random.permutation(deck)
	print('Time in GenerateRandomDeck: ',time.time()-start)
	return deck


def GenerateNewDeck():
	start = time.time()
	# Generate an ordered deck
	print('Time in GenerateNewDeck: ',time.time()-start)
	return np.arange(52)
