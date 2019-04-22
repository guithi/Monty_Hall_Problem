# Monty Hall paradox - 22/4/2019
# problem statement : We have 3 doors : behind 2 doors, there is a goat and behind one door there is car
# 1 - The player choose one door
# 2 - The presenter knows where the car is. He opens a door whith a goat behind
# 3 - The presenter offers the player to change his choice

# To garantee a correct result, program iterates one million
# at each iteration, we count if the good choice is the first door or the other door
# and we can check the results as a percentage : Should the player change his mind or not ?

#!/usr/bin/python
# -*-coding:utf-8 -*
from random import randrange
from math import ceil

def main():
	cpt  = 0
	winsFirstChoice = 0
	winsChange = 0
	listNoPorte = [0, 0, 0] # le n° à la postiton 0 est la porte de la voiture, les deux autres postions 1 et 2 sont les portes des chèvres
	while cpt<1000000:
		listNoPorte[0] = randrange(1,4) # randomize behind which door is the car between 0, 1 or 2
		if listNoPorte[0] == 1:
			listNoPorte[1] = randrange(2,4)
			listNoPorte[2] = 5 - listNoPorte[1]
		elif listNoPorte[0] == 2:
			listNoPorte[1] = randrange(1,3)
			if listNoPorte[1] == 2:
				listNoPorte[1] = 3
			listNoPorte[2] = 4 - listNoPorte[1]
		else:
			listNoPorte[1] = randrange(1,3)
			listNoPorte[2] = 3 - listNoPorte[1]

		wantedDoor = randrange(1,4) #randomize the door the player choose between 1, 2 or 3

		if wantedDoor == listNoPorte[0]:
			openDoor = listNoPorte[randrange(1,3)]
		elif wantedDoor == listNoPorte[1]:
			openDoor = listNoPorte[2]
		else:
			openDoor = listNoPorte[1]

		if wantedDoor == listNoPorte[0]:
			winsFirstChoice +=1
		if (listNoPorte[0]!=wantedDoor) & (listNoPorte[0]!=openDoor):
			winsChange += 1
		cpt += 1

	print("win first choice ="+str(round(winsFirstChoice*100/cpt, 2))+ " %")
	print("win with change ="+str(round(winsChange*100/cpt, 2))+" %")

if __name__ == "__main__":
    main()