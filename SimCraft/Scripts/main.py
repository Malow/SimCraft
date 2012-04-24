# -*- coding: utf-8 -*-

import Python # Ladda in vår c++ modul GameEngine

print("Entering our own python script") # Standard python print funktion

# PythonWrapper.SetValue("Test", "2")

# print("")
# PythonWrapper.Print("Value of Test is: " + PythonWrapper.GetValue("Test") + "\n")

def pyFunction(a, b, c):
	print("Rearranging args")
	print("Data: " + a + ", " + b + ", " + c)
	return c, b, a

def MyFunction(a, b):
	if a < b:
		return a
	else:
		return b

		
		
		
		
class Person:
	posx = 0
	posy = 0
	TimeToStatusChange = 0
	status = ""
	
	def __init__(self, x, y, time, stat):
		self.posx = x
		self.posy = y
		self.TimeToStatusChange = time
		self.status = stat
		
Person1 = Person(1, 1, 5000, "Working")
Person2 = Person(3, 3, 7000, "Working")
Person3 = Person(2, 5, 9000, "Working")
		
i = 0
def tick(time):
	global i # Detta måste göras för att kunna manipulera en global variabel
	global Person1
	global Person2
	global Person3
	i = i + time
	Person1.TimeToStatusChange = Person1.TimeToStatusChange - time
	Person2.TimeToStatusChange = Person2.TimeToStatusChange - time
	Person3.TimeToStatusChange = Person3.TimeToStatusChange - time
	
	#PERSON1
	#Testing change status
	if Person1.TimeToStatusChange < 0:
		if Person1.status == "Working":
			Person1.TimeToStatusChange = 10000
			Person1.status = "Getting Coffee"
			#GameEngine.SetLastPrintedString("Person1 going to get Coffee")
		else:
			Person1.TimeToStatusChange = 20000
			Person1.status = "Working"
			#GameEngine.SetLastPrintedString("Person1 going back to work")
	
	#Script
	if Person1.status == "Working":
		if Person1.posx > 1:
			Person1.posx  = Person1.posx - (time / 1000)
		else:
			Person1.posx = 1
			
	else:
		if Person1.posx < 10:
			Person1.posx  = Person1.posx + (time / 1000)
		else:
			Person1.posx = 10
			
	
	
	
	
	
	#PERSON2
	#Testing change status
	if Person2.TimeToStatusChange < 0:
		if Person2.status == "Working":
			Person2.TimeToStatusChange = 5000
			Person2.status = "Taking a break"
			#GameEngine.SetLastPrintedString("Person2 is taking a break")
		else:
			Person2.TimeToStatusChange = 15000
			Person2.status = "Working"
			#GameEngine.SetLastPrintedString("Person2 going back to work")
		
	#Script
	if Person2.status == "Working":
		Person2.posx = 3
	else:
		Person2.posx = 4
	
	
	
	
	
	
	#PERSON3
	#Testing change status
	if Person3.TimeToStatusChange < 0:
		if Person3.status == "Working":
			Person3.TimeToStatusChange = 5000
			Person3.status = "Taking a break"
			#GameEngine.SetLastPrintedString("Person3 is taking a break and goes to watch his colleagues.")
		else:
			Person3.TimeToStatusChange = 30000
			Person3.status = "Working"
			#GameEngine.SetLastPrintedString("Person3 going back to work")
	
	#Script
	if Person3.status == "Working":
		if Person3.posy < 5:
			Person3.posy  = Person3.posy + (time / 1000)
		else:
			Person3.posy = 5
			
	else:
		if Person3.posy > 1:
			Person3.posy  = Person3.posy - (time / 1000)
		else:
			Person3.posy = 1
			
	
	
	#GameEngine.SetPerson(0, int(Person1.posx), int(Person1.posy))
	#GameEngine.SetPerson(1, int(Person2.posx), int(Person2.posy))
	#GameEngine.SetPerson(2, int(Person3.posx), int(Person3.posy))
	
	return (i < 20000) #20 secs
	
	
settings = {
	"Name" : "BTH Example",
	"debug" : "true",
	"lookup" : 1
	}

print("MyFunction returned: " + str(MyFunction(1,2)))

print "Are we in debug mode?: " + str(settings["debug"]) # Vi kan använda print utan paranteser, men är det nödvändigt?