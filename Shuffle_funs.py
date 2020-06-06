import numpy as np
from Utility_funs import *

# np.random.seed(12)




# TODO
'''
- Make Riffle shuffle function
- ...
'''


# IN PROGRESS

def RiffleShuffle(deck):
	start = time.time()
	half1, half2 = CutDeck(deck)
	print('# cards in left: ', len(half1))
	print(half1)
	print('# Cards in right: ', len(half2))
	print(half2)
	# probability of crossing over to other half = nCards in other deck left/ nCards in self left
	if np.random.binomial(1,0.5):
		# Set current and other
		current = half1
		other = half2
	else:
		# Set current and other
		current = half2
		other = half1

	newDeck = [current[0]]  # Add first card to newDeck
	current = current[1:]  # Remove that card from the half1
	placementOrder = [0]
	while current.size != 0 or other.size != 0:  # While at least one of the decks still has cards in it
		prob = len(other) / (len(other)+len(current))  # Probability of switching to othr deck
		if prob == 0: # No cards left in other deck
			placementOrder.append(0)
			newDeck.append(current[0])
			current = current[1:]
		elif np.random.binomial(1 , prob): # Use card from other deck
			placementOrder.append(1)

			newDeck.append(other[0])
			other = other[1:]

			# switch other and current
			temp = current
			current = other
			other = temp
		else: # Use card from current
			placementOrder.append(0)
			newDeck.append(current[0])
			current = current[1:]
	print('Time in RiffleShuffle: ',time.time()-start)
	return np.asarray(newDeck), np.asarray(placementOrder)





def RiffleShuffl2(deck):
	start = time.time()
	left, right = CutDeck(deck)
	print('# cards in left: ', len(left))
	print(left)
	print('# Cards in right: ', len(right))
	print(right)
	# probability of crossing over to other half = nCards in other deck left/ nCards in self left
	if np.random.binomial(1,0.5):
		# Start with left side
		newDeck = [left[0]]
		left = left[1:]
		placementOrder = [0]
		last = 'l'
	else:
		# Start with right side
		newDeck = [right[0]]
		right = right[1:]
		placementOrder = [1]
		last = 'r'

	while left.size != 0 or right.size != 0:  # While at least one side still has cards in it
		if last == 'l':  # just put down a card from the left side
			prob = len(right) / (len(right) + len(left))  # Probability of switching to othr deck
			if prob == 0:  # No cards remaining in right deck, add card from left deck
				newDeck.append(left[0])
				left = left[1:]
				placementOrder.append(0)
		elif last == 'r':  # just put down a card from the right side
			prob = len(left) / (len(left) + len(right))
			if prob == 0:  # No cards remaining in left deck, add card from right deck
				newDeck.append(right[0])
				


		if prob == 0:  # No cards left in other deck
			placementOrder.append(0)
			newDeck.append(current[0])
			current = current[1:]
		elif np.random.binomial(1 , prob): # Use card from other deck
			placementOrder.append(1)

			newDeck.append(other[0])
			other = other[1:]

			# switch other and current
			temp = current
			current = other
			other = temp
		else: # Use card from current
			placementOrder.append(0)
			newDeck.append(current[0])
			current = current[1:]
	print('Time in RiffleShuffle: ',time.time()-start)
	return np.asarray(newDeck), np.asarray(placementOrder)

# DONE
	''' Easy --> Hard
	+ Random permutation of the deck
	- Repeat many small swaps (switch 2/3/4 cards at a time and repeat 40-50 times)
	- Ant movement (cards move randomly, but move somewhat in the direction of their neightbors)
	'''


def CorgiShuffle(deck):
	start = time.time()
	deck = np.random.permutation(deck)
	print('Time in CorgiShuffle: ',time.time()-start)
	return deck
