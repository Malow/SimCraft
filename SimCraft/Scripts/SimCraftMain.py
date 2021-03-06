﻿# -*- coding: utf-8 -*-
#Static Variables
#Compare lists
#Call by reference
#
from Vector3 import Vector3
import Python # Ladda in vår c++ modul Python
# -*- coding: utf-8 -*-
from Person import Person
from FoodBush import FoodBush
from Tree import Tree
from Wolf import Wolf

#v1 = Vector3(0,0,0)
#v2 = Vector3(2,2,2)
#v3 = Vector3(1,1,1)
#v4 = v3 - v3
totaltime = 0
entId = int(0)
entities = []


#Load from map
def LoadMap(filename):
	global entId
	global entities

	f = open(filename)
	nrOfEntries = int(f.readline().replace('\n', ''))
	f.readline()

	for i in range(0, nrOfEntries):
		line = f.readline().replace('\n', '')
		if line == "Human":
			male = int(f.readline().replace('\n', ''))
			age = int(f.readline().replace('\n', ''))
			x = float(f.readline().replace('\n', ''))
			y = float(f.readline().replace('\n', ''))
			z = float(f.readline().replace('\n', ''))
			if male == 0:
				newPerson = Person(entId, age, "male", Vector3(x, y, z))
				entities.append(newPerson)
				entId += 1
			else:
				newPerson = Person(entId, age, "female", Vector3(x, y, z))
				entities.append(newPerson)
				entId += 1
		elif line == "Tree":
			age = int(f.readline().replace('\n', ''))
			wood = int(f.readline().replace('\n', ''))
			x = float(f.readline().replace('\n', ''))
			y = float(f.readline().replace('\n', ''))
			z = float(f.readline().replace('\n', ''))
			newTree = Tree(entId, age, wood, Vector3(x, y, z))
			entities.append(newTree)
			entId += 1
		elif line == "Food Bush":
			food = int(f.readline().replace('\n', ''))
			x = float(f.readline().replace('\n', ''))
			y = float(f.readline().replace('\n', ''))
			z = float(f.readline().replace('\n', ''))
			newBush = FoodBush(entId, food, Vector3(x, y, z))
			entities.append(newBush)
			entId += 1
		elif line == "Wolf":
			male = int(f.readline().replace('\n', ''))
			age = int(f.readline().replace('\n', ''))
			x = float(f.readline().replace('\n', ''))
			y = float(f.readline().replace('\n', ''))
			z = float(f.readline().replace('\n', ''))
			if male == 0:
				newWolf = Wolf(entId, age, "male", Vector3(x, y, z))
				entities.append(newWolf)
				entId += 1
			else:
				newWolf = Wolf(entId, age, "female", Vector3(x, y, z))
				entities.append(newWolf)
				entId += 1

		asd = f.readline()

	return 1 == 1


def Update(time):
	time /= 1000
	#Python.Debug("" + str(time))
	##if v1 == v3:
	##	Python.Debug("Wrong")
	##else:
	##	Python.Debug("Correct")
	##if v1 == v1:
	##	Python.Debug("Correct1")
	##else:
	##	Python.Debug("Wrong1")
	##if v4 == v4:
	##	Python.Debug("Correct2")
	##else:
	##	Python.Debug("Wrong2")
	##if v2.Length()/2 == v3.Length():
	##	Python.Debug("Correct3")
	##else:
	##	Python.Debug("Wrong3")
	##if v2 == v3*2:
	##	Python.Debug("Correct4")
	##else:
	##	Python.Debug("Wrong4")

	global totaltime
	global entId
	global entities
	for onePerson in entities:
		entId = onePerson.Update(time, entities, entId)

	'''
	totaltime += time
	if totaltime < 0:
		tempPerson = Person(entId, 10, "male", Vector3((entId * 2 + 150), 0, (entId * 2 + 150)))
		entities.append(tempPerson)
		for entity in entities:
			if entity.GetID() == entId:
				pos = entity.GetPosition()
		Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , pos.x, pos.y, pos.z)
		entId += 1
		totaltime = 0

	if entId > 500:
		for tempPerson in entities:
			if isinstance(tempPerson, Person):
				if tempPerson.GetID() == 1:
					Python.DeleteEntity(tempPerson.GetID())
					entities.remove(tempPerson)
				if tempPerson.GetID() == 2:
					Python.DeleteEntity(tempPerson.GetID())
					entities.remove(tempPerson)
				if tempPerson.GetID() == 4:
					Python.DeleteEntity(tempPerson.GetID())
					entities.remove(tempPerson)
	'''
	return 1 == 1