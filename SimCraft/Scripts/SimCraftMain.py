# -*- coding: utf-8 -*-
# Koden ovan låter oss använda svenska tecken i python, den måste ligga först

# Created by: Ermin Hrkalovic (ERH)
# Email: ermin.hrkalovic@bth.se

import Python # Ladda in vår c++ modul GameEngine
# -*- coding: utf-8 -*-
import Person

totaltime = 0
id = 0
persons = []

tempPerson = Person.Person(id, 40, "female", 112, 0, 112)
persons.append(tempPerson)
Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (112), (0), (112))
id += 1
tempPerson = Person.Person(id, 42, "male", 108, 0, 108)
persons.append(tempPerson)
Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (108), (0), (108))
id += 1
tempPerson = Person.Person(id, 15, "male", 110, 0, 110)
persons.append(tempPerson)
Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (110), (0), (110))
id += 1

def Update(time):
	global totaltime
	global id
	global persons
	
	for onePerson in persons:
		temp = onePerson.Update(time)
		if temp == 1:
			Python.SetCameraPosition(0,0,0)
		elif temp == 2:
			Python.SetCameraPosition(100,40,100)
	totaltime += time
	if totaltime > 5000:
		tempPerson = Person.Person(id, 10, "male", (id * 2 + 150), 0, (id * 2 + 150))
		persons.append(tempPerson)
		Python.CreateEntity("Media/FoodBush.obj", tempPerson.GetID() , (id * 2 + 150), (0), (id * 2 + 150))
		id += 1
		totaltime = 0
	
	for tempPerson in persons:
		if tempPerson.GetID() == 0:
			Python.DeleteEntity(tempPerson.GetID())
			persons.remove(tempPerson)
		if tempPerson.GetID() == 1:
			Python.DeleteEntity(tempPerson.GetID())
			persons.remove(tempPerson)
		if tempPerson.GetID() == 2:
			Python.DeleteEntity(tempPerson.GetID())
			persons.remove(tempPerson)
			
	return 1 == 1