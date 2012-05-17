import Python
from Vector3 import Vector3
import math
from FoodBush import FoodBush


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
	__foodReq = 27000
	__foodCollected = 10000
	__goingToDo = "Nothing"
	__goingToPos = Vector3(0, 0, 0)
	__maxSleepTime = 60 * 60 * 8  #sec * min * tim
	__timeUntillSleep =  60 * 60 * 8 #sec * min * tim
	__walkSpeed = 100
	__home = Vector3(0,0,0)
	__foodCollecingSpeed = 6
	__eatingSpeed = 4
	__SleepingMultiplier = 1
	
	def __init__(self, ID, age, sex, pos):
		ScriptedEntity.__init__(self, ID, pos)
		Python.CreateEntity("Media/Human.obj", ID, pos.x, pos.y, pos.z)
		self.__age = age
		self.__sex = sex
		self.__home = Vector3(10 * ID + 50, 0 , 10 * ID + 50)
		
	def Update(self, deltaTime, entities, entId):
		self.UpdateValues(deltaTime)
		
		if self.__goingToDo == "Sleep":
			self.Sleeping(deltaTime)
		elif self.__goingToDo == "CollectFood":
			self.CollectFood(deltaTime, entities)
		elif self.__goingToDo == "Nothing":
			self.Nothing(deltaTime)
		#if entId == 4:
		#	tempPerson = Person(entId, 10, "male", Vector3(2, 0, 2))
		#	entities.append(tempPerson)
		#	pos = entities[entId].GetPosition()
		#	Python.CreateEntity("Media/Human.obj", tempPerson.GetID(), pos.x, pos.y, pos.z)
		#	entId += 1
		return entId
		
	def WalkTo(self, to, deltaTime):
		#walkingVec = to - self.GetPosition()
		#if walkingVec.Length() > 1:
		#	walkingVec.Normalize()
		#	newPos = self.GetPosition() + (walkingVec * (self.__walkSpeed * deltaTime))
		#else:
		newPos = to
			
		ScriptedEntity.SetPosition(self, newPos.x, newPos.y, newPos.z)
		Python.SetPosition(self.GetID(), newPos.x, newPos.y, newPos.z)
		Python.SetCameraPosition(newPos.x, 40, newPos.z)
		
	def UpdateValues(self, deltaTime):
		if self.__goingToDo == "CollectFood":
			self.__timeUntillSleep -= deltaTime*self.__SleepingMultiplier
			self.__foodCollected -= (self.__eatingSpeed * deltaTime)
		elif self.__goingToDo == "Sleep":
			self.__foodCollected -= ((self.__eatingSpeed / 2) * deltaTime)
		elif self.__goingToDo == "Nothing":
			self.__timeUntillSleep -= deltaTime*self.__SleepingMultiplier
			self.__foodCollected -= (self.__eatingSpeed * deltaTime)
			
	def Sleeping(self, deltaTime):
		self.__goingToPos = self.__home
	
		if self.GetPosition() == self.__goingToPos:
			self.__timeUntillSleep += deltaTime * self.__SleepingMultiplier * 2
			if self.__timeUntillSleep > self.__maxSleepTime:
				self.__goingToDo = "Nothing"
				if self.__foodCollected > 9000:
					self.__foodCollected -= (10 * deltaTime)
		else:
			self.WalkTo(self.__goingToPos, deltaTime)
					
	def CollectFood(self, deltaTime, entities):
		Python.Debug("Food: " + str(self.__foodCollected))
		
		if self.__foodCollected > self.__foodReq:
				self.__goingToDo = "Nothing"
				return
		sleepValue = 1 - (math.pow(self.__timeUntillSleep / self.__maxSleepTime, 2))
		if sleepValue > 0.95:
			self.__goingToDo = "Sleep"
				
		######Calculate the closest foodBush
		distToClosest = 99999
		closest = self
		for entity in entities:
			if isinstance(entity, FoodBush):
				dist = (entity.GetPosition() - self.GetPosition()).Length()
				if dist < distToClosest:
					if entity.GetFood() > 0:
						distToClosest = dist
						closest = entity
					
		self.__goingToPos = closest.GetPosition()
		###### END
		if self.GetPosition() == self.__goingToPos:
			self.__foodCollected += (self.__foodCollecingSpeed * deltaTime)
			if isinstance(closest, FoodBush):
				closest.RemoveFood(self.__foodCollecingSpeed * deltaTime)
		else:
			self.WalkTo(self.__goingToPos, deltaTime)
			
	def Nothing(self, deltaTime):
		if self.GetPosition() != Vector3(100, 0 ,100): #temp to see when its here
				self.WalkTo(Vector3(100, 0 ,100), deltaTime)
	
		sleepValue = 1 - (math.pow(self.__timeUntillSleep / self.__maxSleepTime, 2))
		if self.__foodCollected != 0:
			gatherFoodValue = 1 - (self.__foodCollected / self.__foodReq)
		else:
			gatherFoodValue = 1
		
		Python.Debug("Sleep Value: " + str(sleepValue))
		Python.Debug("Gather Value: " + str(gatherFoodValue))
		
		if sleepValue > 0.8:
			self.__goingToDo = "Sleep"
		elif gatherFoodValue > 0.8:
			self.__goingToDo = "CollectFood"
		else:
			self.__goingToDo = "Nothing"
			
	def GetAge(self):
		return self.__age
		
	def SetAge(self, age):
		self.__age = age
		
	def GetSex(self):
		return self.__sex
		
	def SetSex(self, sex):
		self.__sex = sex