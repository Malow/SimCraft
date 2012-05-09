# -*- coding: utf-8 -*-
#Static Variables
#Compare lists
#Call by reference
#

import Python # Ladda in vår c++ modul Python
# -*- coding: utf-8 -*-
from Person import Person

totaltime = 0
entId = int(0)
entities = []

tempPerson = Person(entId, 40, "female", 112, 0, 112)
entities.append(tempPerson)
Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (112), (0), (112))
entId += 1
tempPerson = Person(entId, 42, "male", 108, 0, 108)
entities.append(tempPerson)
Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (108), (0), (108))
entId += 1
tempPerson = Person(entId, 15, "male", 110, 0, 110)
entities.append(tempPerson)
Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (110), (0), (110))
entId += 1

def Update(time):
	global totaltime
	global entId
	global entities
	for onePerson in entities:
		entId = onePerson.Update(time, entities, entId)
		
	totaltime += time
	if totaltime > 5000:
		tempPerson = Person(entId, 10, "male", (entId * 2 + 150), 0, (entId * 2 + 150))
		entities.append(tempPerson)
		Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (entId * 2 + 150), (0), (entId * 2 + 150))
		entId += 1
		totaltime = 0
	if entId > 5:
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
			
	return 1 == 1