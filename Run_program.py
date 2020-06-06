from Utility_funs import *
from Shuffle_funs import *
from Shuffle_vis import *
import numpy as np
import matplotlib.pyplot as plt


deck = GenerateNewDeck()
# PrintActualDeck(deck)
newDeck, placementOrder = RiffleShuffle(deck)

Show_Riffle_Order(placementOrder)
