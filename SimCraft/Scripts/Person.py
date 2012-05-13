import Python
import SimCraftMain
from Vector3 import Vector3

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
	__foodReq = 5
	__foodCollected = 0
	__goingToDo = "unknown"
	__goingToPos = Vector3(0, 0, 0)
	__timeUntillSleep = 60 * 60 * 8 # sec * min * tim
	__walkSpeed = 100
	__home = Vector3(0,0,0)
	
	def __init__(self, ID, age, sex, pos):
		ScriptedEntity.__init__(self, ID, pos)
		self.__age = age
		self.__sex = sex
		self.__home = Vector3(10 * ID + 50, 0 , 10 * ID + 50)
		
	def Update(self, deltaTime, entities, entId):
		self.__timeUntillSleep = self.__timeUntillSleep - deltaTime
		
		#if entId == 4:
		#	tempPerson = Person(entId, 10, "male", Vector3(2, 0, 2))
		#	entities.append(tempPerson)
		#	pos = entities[entId].GetPosition()
		#	Python.CreateEntity("Media/Human.obj", tempPerson.GetID(), pos.x, pos.y, pos.z)
		#	entId += 1
		
		if self.__goingToDo == "CollectFood":
		
			if self.GetPosition() == self.__goingToPos:
			
				if self.__foodCollected < self.__foodReq:
					self.__foodCollected = self.__foodCollected + (1 * deltaTime)
				else:
					self.__goingToDo == "Sleep"
					
			else:
				self.WalkTo(self.__goingToPos, deltaTime)
				
		elif self.__goingToDo == "Sleep":
		
			if self.GetPosition() == self.__home:
				i = 0
			else:
				self.WalkTo(self.__home, deltaTime)
			
		if self.__foodCollected < self.__foodReq:
			self.__goingToDo = "CollectFood"
		else:
			self.__goingToDo = "Sleep"
		
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