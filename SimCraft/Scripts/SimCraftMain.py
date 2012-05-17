# -*- coding: utf-8 -*-
#Static Variables
#Compare lists
#Call by reference
#
from Vector3 import Vector3
import Python # Ladda in vår c++ modul Python
# -*- coding: utf-8 -*-
from Person import Person
from FoodBush import FoodBush

#v1 = Vector3(0,0,0)
#v2 = Vector3(2,2,2)
#v3 = Vector3(1,1,1)
#v4 = v3 - v3
totaltime = 0
entId = int(0)
entities = []

tempPerson = Person(entId, 40, "female", Vector3(112, 0, 112))
entities.append(tempPerson)
pos = entities[entId].GetPosition()
Python.CreateEntity("Media/Human.obj", tempPerson.GetID(), pos.x, pos.y, pos.z)
entId += 1

foodBush = FoodBush(entId, Vector3(20, 0, 40))
entities.append(foodBush)
pos = entities[entId].GetPosition()
Python.CreateEntity("Media/FoodBush.obj", foodBush.GetID(), pos.x, pos.y, pos.z)
entId += 1

foodBush = FoodBush(entId, Vector3(40, 0, 40))
entities.append(foodBush)
pos = entities[entId].GetPosition()
Python.CreateEntity("Media/FoodBush.obj", foodBush.GetID(), pos.x, pos.y, pos.z)
entId += 1

#tempPerson = Person(entId, 42, "male", Vector3(108, 0, 108))
#entities.append(tempPerson)
#pos = entities[entId].GetPosition()
#Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID(), pos.x, pos.y, pos.z)
#entId += 1

#tempPerson = Person(entId, 15, "male", Vector3(110, 0, 110))
#entities.append(tempPerson)
#pos = entities[entId].GetPosition()
#Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID(), pos.x, pos.y, pos.z)
#entId += 1

def Update(time):
	time /= 1000
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
			
	return 1 == 1