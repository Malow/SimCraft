import Python
import SimCraftMain
from Vector3 import Vector3
import math


class ScriptedEntity():
    __ID = 0
    __Pos = Vector3(0,0,0)
	
    def __init__(self, ID, pos):
        self.__ID = ID
        self.__Pos = pos
        
    def GetID(self):
        return self.__ID
    
    def GetPosition(self):
        return self.__Pos
    
    def SetPosition(self, x, y, z):
        self.__Pos = Vector3(x, y, z)
		
class Person(ScriptedEntity):
	__age = 0
	__sex = "unknown"
	__foodReq = 50
	__foodCollected = 0
	__goingToDo = "unknown"
	__goingToPos = Vector3(0, 0, 0)
	__maxAwakeTime = 60 * 60 * 8  #sec * min * tim
	__timeUntillSleep = 60 * 60 * 8  #sec * min * tim
	__walkSpeed = 100
	__home = Vector3(0,0,0)
	
	def __init__(self, ID, age, sex, pos):
		ScriptedEntity.__init__(self, ID, pos)
		self.__age = age
		self.__sex = sex
		self.__home = Vector3(10 * ID + 50, 0 , 10 * ID + 50)
		
	def Update(self, deltaTime, entities, entId):		
	##################
	#Calc the value to understand what to do
		sleepValue = 1 - (math.pow(self.__timeUntillSleep / self.__maxAwakeTime, 2))
		if self.__foodCollected != 0:
			gatherFoodValue = 1 - (self.__foodCollected / self.__foodReq)
		else:
			gatherFoodValue = 1
		
		if gatherFoodValue > sleepValue:
			self.__goingToDo = "CollectFood"
		else:
			self.__goingToDo = "Sleep"
	##################
	
		if self.__goingToDo != "Sleep":
			self.__timeUntillSleep = self.__timeUntillSleep - deltaTime*100
			if self.__foodCollected > 0:
				self.__foodCollected -= (1 * deltaTime)
			
		
		if self.__goingToDo == "CollectFood":
			if self.GetPosition() == self.__goingToPos:
				self.__foodCollected = self.__foodCollected + (10 * deltaTime)
			else:
				self.WalkTo(self.__goingToPos, deltaTime)
		elif self.__goingToDo == "Sleep":
			if self.GetPosition() == self.__home:
				self.__timeUntillSleep += deltaTime * 10
				if self.__timeUntillSleep > self.__maxAwakeTime:
					self.__goingToDo = "Nothing"
			else:
				self.WalkTo(self.__home, deltaTime)
		
		#if entId == 4:
		#	tempPerson = Person(entId, 10, "male", Vector3(2, 0, 2))
		#	entities.append(tempPerson)
		#	pos = entities[entId].GetPosition()
		#	Python.CreateEntity("Media/Human.obj", tempPerson.GetID(), pos.x, pos.y, pos.z)
		#	entId += 1
		
		return entId
		
	def WalkTo(self, to, deltaTime):
		walkingVec = to - self.GetPosition()
		if walkingVec.Length() > 1:
			walkingVec.Normalize()
			newPos = self.GetPosition() + (walkingVec * (self.__walkSpeed * deltaTime))
		else:
			newPos = to
			
		ScriptedEntity.SetPosition(self, newPos.x, newPos.y, newPos.z)
		Python.SetPosition(self.GetID(), newPos.x, newPos.y, newPos.z)
		
	def GetAge(self):
		return self.__age
		
	def SetAge(self, age):
		self.__age = age
		
	def GetSex(self):
		return self.__sex
		
	def SetSex(self, sex):
		self.__sex = sex