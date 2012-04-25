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

tempPerson = Person.Person(id, 40, "female", 2, 0, 0)
persons.append(tempPerson)
Python.CreateEntity("Media/bth.obj", tempPerson.GetID() , (2), (0), (0))
id += 1
tempPerson = Person.Person(id, 42, "male", -2, 0, 0)
persons.append(tempPerson)
Python.CreateEntity("Media/bth.obj", tempPerson.GetID() , (-2), (0), (0))
id += 1
tempPerson = Person.Person(id, 15, "male", 0, 0, 0)
persons.append(tempPerson)
Python.CreateEntity("Media/bth.obj", tempPerson.GetID() , (0), (0), (0))
id += 1

def Update(time):
	global totaltime
	global id
	
	totaltime += time
	if totaltime > 5000:
		tempPerson = Person.Person(id, 10, "male", 0, 0, 0)
		persons.append(tempPerson)
		Python.CreateEntity("Media/bth.obj", tempPerson.GetID() , (id * 5), (0), (0))
		id += 1
		totaltime = 0
		
	if id > 3:
		for id in persons:
			if id.GetID == 0:
				persons.remove(id)
				Python.DeleteEntity(id.GetID)
			if id.GetID == 1:
				persons.remove(id)
				Python.DeleteEntity(id.GetID)
			if id.GetID == 2:
				persons.remove(id)
				Python.DeleteEntity(id.GetID)
	return 1 == 1