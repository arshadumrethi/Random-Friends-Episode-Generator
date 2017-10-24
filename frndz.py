import pandas as pd
import numpy as np
import random

data = pd.read_csv('frnds4.csv')

Generator = data.iloc[[random.randint(1, 236)], [1, 2, 3, 4]]

print Generator

#"Your random episode is %s" % Generator

#def shuffle(data):
	#win = data.pop()
	#print "You get %s" % win

#print shuffle(data1)
